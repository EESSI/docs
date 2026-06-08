# Leverage EESSI's build procedure for site builds
In this approach, you use the EESSI build bot (`EESSI/eessi-bot-software-layer`), together with the EESSI build scripts (`EESSI/software-layer-scripts`) to build and deploy software into a CernVM-FS repository of your own. Essentially, this means you'll build in a way that is essentially identical to how it is done for upstream EESSI - with the only major difference being the target CernVM-FS repository.

## Setup steps
What we need:
- Infrastructure for a site-specific CVMFS repository (Stratum 0, Stratum 1, proxies, client configuration)
- An instance of the EESSI build bot
- A bucket in an AWS S3-compatible object store (though you could work around this)
- A GitHub organization on which you can install GitHub Apps
- A GitHub repository within that organization which will be used to list the software you want to build
- Optionally: an automated procedure to ingest tarballs

This documentation will go through the steps to set each of these up, in order. Since many of these individual steps are documented elsewhere, we will often reference that (and only list a very short summary here).

### A site-specific CVMFS infrastructure
The recommended CVMFS setup for a site-specific CVMFS repository is:
- A Stratum 0 servers
- Two (or more) Stratum 1 servers
- Two (or more) proxies

Main reason here is:
- Having two Stratum 1's provides redundancy: if one dies, proxies seamlessly failover to the other one.
- Having two proxies provides both redundancy _and_ load balancing. If one proxy dies, clients failover to the other one. If clients are configured to use the proxies in a [proxy group](https://cvmfs.readthedocs.io/en/2.8/cpt-configure.html#proxy-lists), each client selects a proxy randomly, thus providing load balancing.

!!! note

    The recommended CVMFS setup requires a fair amount of machines. If this is more than you can afford, there are some tricks you can pull. First, you can combine each proxy with a Stratum 1 on the same machine, only use the proxies for proxy-ing upstream EESSI, and simply have your clients contact your site-specific Stratum 1's directly (without proxy). In this scenario, you can achieve load-balancing by configuring half your clients with `CVMFS_SERVER_URL="<instance_1>;<instance_2>"` and half with `CVMFS_SERVER_URL="<instance_2>;<instance_1>"`, where `instance_1` and `instance_2` are the IPs of your Stratum 1's. Finally, you can even use the Stratum 0 instead of a second Stratum 1. Note that this has security implications, as it means your Stratum 0 needs to be directly accessible to your clients. This is a potential concern: if there are vulnarebilities in the Stratum 0 software, end-users may be able to push (malicious) software in there.

An extensive [tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/) is available that teaches how to setup each of these machines, and how to configure the clients to use the relevant Stratum 1's and proxies. Below, we will summarize some of the key steps, and point out things that are specifically relevant for this setup.

#### Setting up the CVMFS Stratum 0

For extensive instructions, see [the CVMFS tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/02_stratum0_client/#21-setting-up-the-stratum-0) or the [upstream documentation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html).

They key steps are:

1. Define a repository name, typically something like `software.<name_of_the_site>.tld`

```bash
repo_name=name.sitename.tld
```
Note that while this looks like a URL, it is not: it is simply a name for the CVMFS repository. If you set up any DNS though, it is conventional to use the same domain structure, to avoid confusion.

2. Install the `cvmfs` and `cvmfs-server` packages. Typically:
```bash
wget https://cvmrepo.s3.cern.ch/cvmrepo/apt/cvmfs-release-latest_all.deb
sudo dpkg -i cvmfs-release-latest_all.deb
rm -f cvmfs-release-latest_all.deb
sudo apt-get -y update
sudo apt-get -y install cvmfs cvmfs-server
```

3. To facilitate ingestion later on, we make sure that the `software.eessi.io` repository is available on our Stratum 0 machine as well. Because the `cvmfs-server` cannot perform certain actions when `autofs` is enabled (which is usually how CVMFS repositories are mounted), we have to mount it manually. We also mount the `cvmfs-config.cern.ch` repository, as that provides the configuration for `software.eessi.io`

```bash
sudo mkdir -p /cvmfs/{cvmfs-config.cern.ch,software.eessi.io}
sudo bash -c "echo 'cvmfs-config.cern.ch /cvmfs/cvmfs-config.cern.ch cvmfs defaults 0 0' >> /etc/fstab"
sudo bash -c "echo 'software.eessi.io /cvmfs/software.eessi.io cvmfs defaults 0 0' >> /etc/fstab"
sudo systemctl daemon-reload
sudo mount -a
```

You should now be able to see the `cvmfs-config.cern.ch` and `software.eessi.io` repositories:
```bash
ls -al /cvmfs/cvmfs-config.cern.ch
ls -al /cvmfs/software.eessi.io
```

4. By default, CVMFS will store data for repositories in `/srv/cvmfs`. If you want to store this elsewhere, create a link `/srv/cvmfs` that points to where you want to store the repository data.
```bash
sudo ln -s /my/desired/data/prefix /srv/cvmfs
```

5. Create the repository owned by `root`:
```bash
sudo cvmfs_server mkfs -o root $repo_name
```

!!! note

    The reason we configure `root` to be the owner of the CVMFS repository is that EasyBuild, when configured through `EESSI-extend`, by default creates read-only installations. This causes issues if CVMFS has to put catalog files (`.cvmfscatalog`) files in these directories, which are metadata files that CVMFS uses to list the files/directories present in the repository. While it is technically possible to use a regular user, this would require making all directories in which CVMFS would create a `.cvmfscatalog` file writeable in a transaction, then create the catalog files, then remove the write permissions again. The same approach would need to be taken to reinstall software that was already installed. We consider this unnecessarily complex, and instead prefer to have the repository owned by root.


Then, we create a `.cvmfsdirtab` file, that will tell CVMFS in at which directory levels to create [catalog files](https://cvmfs.readthedocs.io/en/stable/cpt-details.html#nested-catalogs). We advise that you simply use the latest `.cvmfsdirtab` that is used for the upstream EESSI repository as well. You can get it from [the `EESSI/filesystem-layer` repository](https://github.com/EESSI/filesystem-layer/blob/main/roles/create_cvmfs_content_structure/files/.cvmfsdirtab) or simply copy it from `/cvmfs/software.eessi.io/.cvmfsdirtab` on a system where `EESSI` is available. Alternatively, you can configure your CVMFS server to do [automatic catalog creation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#automatic-management-of-nested-catalogs) by setting `CVMFS_AUTOCATALOGS=true` in the server configuration file (`/etc/cvmfs/repositories.d/$repo_name/server.conf`).

To get the `.cvmfsdirtab` in our repository, we have to open a transaction, move the file into the repository, and publish the transaction. In the same transaction, we can remove the `new_repository` file that is present by default in any newly created repository

```bash
wget https://raw.githubusercontent.com/EESSI/filesystem-layer/refs/heads/main/roles/create_cvmfs_content_structure/files/.cvmfsdirtab
sudo cvmfs_server transaction $repo_name
mv .cvmfsdirtab /cvmfs/$repo_name/
rm /cvmfs/$repo_name/new_repository
sudo cvmfs_server publish -m "Add .cvfmsdirtab file and remove new_repository file"
```

As we already have a `.cvmfsdirtab` file in place, you should see CVMFS going through the logic of creating catalogs. None will be created at this point, as none of the directory structures listed in the `.cvmfsdirtab` file match existing directories in your repository (since it is still empty). CVMFS will warn you about the patterns that don't have any match (these are harmless).

For convenience, we list all the commands here together:

```bash
# Define CVMFS repository name
repo_name=name.sitename.tld
echo "Defined CVMFS repository name as $repo_name"

# Install cvmfs client and cvmfs-server packages
echo "Installing cvmfs and cvmfs-server packages"
wget https://cvmrepo.s3.cern.ch/cvmrepo/apt/cvmfs-release-latest_all.deb
sudo dpkg -i cvmfs-release-latest_all.deb
rm -f cvmfs-release-latest_all.deb
sudo apt-get -y update
sudo apt-get -y install cvmfs cvmfs-server

# Manually mount cvmfs-config.cern.ch and software.eessi.io repositories
echo "Manually mounting cvmfs-config.cern.ch and software.eessi.io repositories"
sudo mkdir -p /cvmfs/{cvmfs-config.cern.ch,software.eessi.io}
sudo bash -c "echo 'cvmfs-config.cern.ch /cvmfs/cvmfs-config.cern.ch cvmfs defaults 0 0' >> /etc/fstab"
sudo bash -c "echo 'software.eessi.io /cvmfs/software.eessi.io cvmfs defaults 0 0' >> /etc/fstab"
sudo systemctl daemon-reload
sudo mount -a

# Check that manually mounted repositories are available
echo "Check that we can access manually mounted cvmfs-config.cern.ch"
ls -al /cvmfs/cvmfs-config.cern.ch/
echo "Check that we can access manually mounted software.eessi.io"
ls -al /cvmfs/software.eessi.io/

# Create the cvmfs repository, owned by root
echo "Creating new CVMFS repository $repo_name"
sudo cvmfs_server mkfs -o root $repo_name

# Create the .cvmfsdirtab file in the root of the repository
echo "Opening transaction, adding .cvmfsdirtab file to the root of $repo_name, and then publish the transaction"
sudo cvmfs_server transaction $repo_name
cp /cvmfs/software.eessi.io/.cvmfsdirtab /cvmfs/$repo_name/
rm /cvmfs/$repo_name/new_repository
sudo cvmfs_server publish -m "Add .cvfmsdirtab file and remove new_repository file"
```

#### Sanity checking your Stratum 0 setup

On the machine where you've set up your CVMFS stratum 0, you can perform some checks to see if things where set up correctly:

1. Check that the repository was created correctly:

```bash
cvmfs_server list
```

lists all the Stratum servers installed on this machine and should report something like `$repo_name (stratum0 / local)`.

2. Check that two mount points are now present related to your repository:

```bash
mount
```

Should print something like

```
$repo_name on /var/spool/cvmfs/$repo_name/rdonly type fuse (...)
overlay_$repo_name on /cvmfs/$repo_name type overlay (...)
```

The first is a read-only mount of the current state of your repository. The second is an overlay filesystem that shows the current state of your repositories (as `lowerdir`) with any changes done in a currently open transaction (if any) overlayed on top (as `upperdir`, for which it uses `/var/spool/cvmfs/$repo_name/scratch/current`). I.e. it displays the state of your repository under `/cvmfs/$repo_name` as it will be once you publish any open transactions.

3. The directory

```bash
ls /srv/cvmfs/$repo_name
```

should now contain some hidden `.cvmfs<...>` files and a `data` directory. The latter is where the data in your repository will actually be stored.

4. The directory

```bash
ls -al /cvmfs/$repo_name
```

should now show you the `.cvmfsdirtab` file we added in our transaction.

#### Setting up a CVMFS Stratum 1

#### Setting up proxies

#### Configuring your CVMFS clients

### Setting up an object store to stage build tarballs

#### Creating a bucket
- create bucket
- set policies

#### Create tokens to access bucket
- consider creating seperate IAM identities with separate permissions for your build bot and Stratum 0

### Setting up the EESSI build bot

#### Creating a SMEE channel

#### Registering a GitHub App for the bot

#### Installing the GitHub App onto a repository
- create new repo to hold easystacks
- install GH app on new repo

#### Install EESSI build bot on a machine
- app.cfg
- set up an environment for the bot to run in
- run the necessary scripts

### Set up automatic ingestion on CVMFS Stratum 0 (optional)
- list steps this needs to do

### Add your first software
- add easystack
- create PR
- bot:show_config first!
- bot:build
- Add deploy label
- See deployment happening in real-time :)
