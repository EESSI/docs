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

## Site-specific CVMFS infrastructure
The recommended CVMFS setup for a site-specific CVMFS repository is:

- A Stratum 0 servers
- Two (or more) Stratum 1 servers
- Two (or more) proxies

Main reason here is:

- Having two Stratum 1's provides redundancy: if one dies, proxies seamlessly failover to the other one.
- Having two proxies provides both redundancy _and_ load balancing. If one proxy dies, clients failover to the other one. If clients are configured to use the proxies in a [proxy group](https://cvmfs.readthedocs.io/en/2.8/cpt-configure.html#proxy-lists), each client selects a proxy randomly, thus providing load balancing.

!!! note

    The recommended CVMFS setup requires a fair amount of machines. If this is more than you can afford, there are some tricks you can pull.

    1. Reuse the same proxies you set up to proxy upstream EESSI to also proxy your local site-specific CVMFS repository.
    2. Deploy your site-specific Stratum 1's on the same machines that proxy upstream EESSI. Don't configure the proxies to proxy your site-specific CVMFS repository, but simply have your clients contact your site-specific Stratum 1's directly (without proxy). In this scenario, you can achieve load-balancing by configuring half your clients with `CVMFS_SERVER_URL="<instance_1>;<instance_2>"` and half with `CVMFS_SERVER_URL="<instance_2>;<instance_1>"`, where `instance_1` and `instance_2` are the IPs of your Stratum 1's.
    3. You can even use the Stratum 0 instead of a second Stratum 1 (even in addition to (1) or (2)). Note that this has security implications, as it means your Stratum 0 needs to be directly accessible to your clients. This is a potential concern: if there are vulnarebilities in the Stratum 0 software, end-users may be able to push (malicious) software in there.

An extensive [tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/) is available that teaches how to setup each of these machines, and how to configure the clients to use the relevant Stratum 1's and proxies. Below, we will summarize some of the key steps, and point out things that are specifically relevant for the site-specific CVMFS setup.

### Setting up your Stratum 0

The documentation below provides you with the minimal steps required to set up a working Stratum 0 and is specifically aimed at setting up a Stratum 0 for hosting a site software stack on top of EESSI (which is why e.g. it makes the `software.eessi.io` repository available on this Stratum 0 as well). However, there is a vast amount of things you can configure for a CVMFS Stratum 0, and nothing beats the detail of the extensive [upstream documentation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html). The [CVMFS tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/02_stratum0_client/#21-setting-up-the-stratum-0) may also be helpful.

**1. Choose a repository name**

Define a repository name, typically something like `software.<name_of_the_site>.tld`

``` { .bash .copy }
repo_name=name.sitename.tld
```
Note that while this looks like a URL, it is not: it is simply a name for the CVMFS repository. If you set up any DNS though, it is conventional to use the same domain structure, to avoid confusion.

**2. Install the `cvmfs` and `cvmfs-server` packages**

Typically:
``` { .bash .copy }
wget https://cvmrepo.s3.cern.ch/cvmrepo/apt/cvmfs-release-latest_all.deb
sudo dpkg -i cvmfs-release-latest_all.deb
rm -f cvmfs-release-latest_all.deb
sudo apt-get -y update
sudo apt-get -y install cvmfs cvmfs-server
```

**3. Make `software.eessi.io` available on your Stratum 0**

To facilitate ingestion later on, we make sure that the `software.eessi.io` repository is available on our Stratum 0 machine as well. This allows us to leverage e.g. the Lmod installation from there to build the Lmod cache. Because the `cvmfs-server` cannot perform certain actions when `autofs` is enabled (which is usually how CVMFS repositories are mounted), we have to mount `software.eessi.io` manually. We also mount the `cvmfs-config.cern.ch` repository, as that provides the configuration for `software.eessi.io`

``` { .bash .copy }
sudo mkdir -p /cvmfs/{cvmfs-config.cern.ch,software.eessi.io}
sudo bash -c "echo 'CVMFS_CLIENT_PROFILE="single"' > /etc/cvmfs/default.local"
sudo bash -c "echo 'CVMFS_QUOTA_LIMIT=10000' >> /etc/cvmfs/default.local"
sudo bash -c "echo 'cvmfs-config.cern.ch /cvmfs/cvmfs-config.cern.ch cvmfs defaults 0 0' >> /etc/fstab"
sudo bash -c "echo 'software.eessi.io /cvmfs/software.eessi.io cvmfs defaults 0 0' >> /etc/fstab"
sudo systemctl daemon-reload
sudo mount -a
```

You should now be able to see the `cvmfs-config.cern.ch` and `software.eessi.io` repositories:
``` { .bash .copy }
ls -al /cvmfs/cvmfs-config.cern.ch
ls -al /cvmfs/software.eessi.io
```

**4. (Optional) Change location to store Stratum 0 data**

By default, CVMFS will store data for repositories in `/srv/cvmfs`. If you want to store this elsewhere, create a link `/srv/cvmfs` that points to where you want to store the repository data.

``` { .bash .copy }
sudo ln -s /my/desired/data/prefix /srv/cvmfs
```

**5. Create a new CVMFS repository**

To create a new CVMFS repository on the Stratum 0, run

``` { .bash .copy }
sudo cvmfs_server mkfs -o root $repo_name
```

The `-o root` tells CVMFS that this repository should be owned by root.

!!! note

    The reason we configure `root` to be the owner of the CVMFS repository is that EasyBuild, when configured through `EESSI-extend`, by default creates read-only installations. This causes issues if CVMFS has to put catalog files (`.cvmfscatalog`) files in these directories, which are metadata files that CVMFS uses to list the files/directories present in the repository. While it is technically possible to use a regular user, this would require making all directories in which CVMFS would create a `.cvmfscatalog` file writeable in a transaction, then create the catalog files, then remove the write permissions again. The same approach would need to be taken to reinstall software that was already installed. We consider this unnecessarily complex, and instead prefer to have the repository owned by root.

**6. Configure CVMFS catalog creation**

Here, we have two options. 

**Option 1:** we create a `.cvmfsdirtab` file in the root of the repository. This will tell CVMFS at which directory levels to create [catalog files](https://cvmfs.readthedocs.io/en/stable/cpt-details.html#nested-catalogs). We advise that you simply use the latest `.cvmfsdirtab` that is used for the upstream EESSI repository as well. You can get it from [the EESSI/filesystem-layer repository](https://github.com/EESSI/filesystem-layer/blob/main/roles/create_cvmfs_content_structure/files/.cvmfsdirtab) or simply copy it from `/cvmfs/software.eessi.io/.cvmfsdirtab` on a system where `EESSI` is available. The upside of Option 1 is that it creates catalogue files at the root of each EasyBuild installation prefix. This causes files that are typically accessed together (namely: that belong to the same software installation) to be indexed within the same catalog, which is typically good for performance. The downside is that if installations are extremely big, the catalog may exceed the largest size that CVMFS recommends (upto 200k files/dirs per catalog).

**Option 2:** you can configure your CVMFS server to do [automatic catalog creation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#automatic-management-of-nested-catalogs) by setting `CVMFS_AUTOCATALOGS=true` in the server configuration file (`/etc/cvmfs/repositories.d/$repo_name/server.conf`). The upside of Option 2 is that it will ensure that the number of files per catalog stays within the recommended limits. The downside is that CVMFS does not know which files are commonly accessed together (e.g. because they belong to the same software installation) and might spread them over multiple catalogues - even when that's not strictly needed in terms of catalog size.

Here, we follow **Option 1**.

To get the `.cvmfsdirtab` in your repository, you have to open a transaction, move the file into the repository, and publish the transaction. In the same transaction, we can immediately remove the `new_repository` file that is present by default in any newly created repository

``` { .bash .copy }
sudo cvmfs_server transaction $repo_name
# Essentially copy the .cvmfsdirtab from EESSI, but strip every pattern related to the compatibility layer 
sudo bash -c "cat /cvmfs/software.eessi.io/.cvmfsdirtab | grep -v '^/versions/\*/compat' > /cvmfs/$repo_name/.cvmfsdirtab"
sudo rm /cvmfs/$repo_name/new_repository
sudo cvmfs_server publish -m "Add .cvfmsdirtab file and remove new_repository file"
```

As you now have a `.cvmfsdirtab` file in place, you should see CVMFS going through the logic of creating catalogs as soon as you run the `cvmfs_server publish` command. No catalogs will be created at this point, as none of the directory structures listed in the `.cvmfsdirtab` file match existing directories in your repository (since it is still empty). CVMFS will warn you about the patterns that don't have any match ('WARNING: cannot apply pathspec') - these warnings are harmless and only serve as an indication that not all pathspecs in your `.cvmfsdirtab` file seem to actually exit (yet) in your repository.

**7. Setup automatic whitelist resigning**

Each CVMFS repository has a whitelist (`.cvmfswhitelist`) with fingerprints of certificates that are allowed to sign a repository manifest (`.cvmfspublished`) (see [signature details](https://cvmfs.readthedocs.io/en/stable/apx-security.html#signature-details)). This whitelist has to be resigned with the repository master key every 30 days (or every 7 days if using a smartcard, like a Yubikey, to store the master key) (see [master keys](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#master-keys)). You can check the current validity of the signature using

``` { .bash .copy }
sudo cvmfs_server info $repo_name
```

Which will print something like:

```
Whitelist is valid for another X days
```

We recommend that you set up automatic resigning in a daily cronjob, e.g.

``` { .bash .copy }
sudo bash -c "echo '0 11 * * * root /usr/bin/cvmfs_server resign $repo_name' > /etc/cron.d/cvmfs_resign"
```

**Scripted summary of steps**

For convenience, we list all the commands from the prior steps together:

``` { .bash .copy }
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
# Creating minimal client config
sudo bash -c "echo 'CVMFS_CLIENT_PROFILE="single"' > /etc/cvmfs/default.local"
sudo bash -c "echo 'CVMFS_QUOTA_LIMIT=10000' >> /etc/cvmfs/default.local"
# Adding the cvmfs mounts to fstab
sudo bash -c "echo 'cvmfs-config.cern.ch /cvmfs/cvmfs-config.cern.ch cvmfs defaults 0 0' >> /etc/fstab"
sudo bash -c "echo 'software.eessi.io /cvmfs/software.eessi.io cvmfs defaults 0 0' >> /etc/fstab"
# Rerun the fstab generator to create the .mount files
sudo systemctl daemon-reload
# Actually trigger mounting the cvmfs filesystems
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
# Essentially copy the .cvmfsdirtab from EESSI, but strip every pattern related to the compatibility layer 
sudo bash -c "cat /cvmfs/software.eessi.io/.cvmfsdirtab | grep -v '^/versions/\*/compat' > /cvmfs/$repo_name/.cvmfsdirtab"
sudo rm /cvmfs/$repo_name/new_repository
sudo cvmfs_server publish -m "Add .cvfmsdirtab file and remove new_repository file"

# Set up a daily cronjob to sign the .cvmfswhitelist
echo "Setting up a cronjob for daily whitelist signing"
sudo bash -c "echo '0 11 * * * root /usr/bin/cvmfs_server resign $repo_name' > /etc/cron.d/cvmfs_resign"
```

### Sanity checking your Stratum 0 setup

On the machine where you've set up your CVMFS stratum 0, you can perform some checks to see if things where set up correctly:

**1. Check that the repository was created correctly**

``` { .bash .copy }
cvmfs_server list
```

lists all the Stratum servers installed on this machine and should report something like `$repo_name (stratum0 / local)`.

**2. Check mount points for your repository**

``` { .bash .copy }
mount | grep "$repo_name"
```

Should print something like

```
$repo_name on /var/spool/cvmfs/$repo_name/rdonly type fuse (...)
overlay_$repo_name on /cvmfs/$repo_name type overlay (...)
```

The first is a read-only mount of the current state of your repository. The second is an overlay filesystem that shows the current state of your repositories (as `lowerdir`) with any changes done in a currently open transaction (if any) overlayed on top (as `upperdir`, for which it uses `/var/spool/cvmfs/$repo_name/scratch/current`). I.e. it displays the state of your repository under `/cvmfs/$repo_name` as it will be once you publish any open transactions.

**3. Check the repository storage backend**

The directory

``` { .bash .copy }
ls -al /srv/cvmfs/$repo_name
```

should now contain some hidden `.cvmfs<...>` files and a `data` directory. The latter is where the data in your repository will actually be stored.

**4. Check the repository contents**

``` { .bash .copy }
ls -al /cvmfs/$repo_name
```

should now show you the `.cvmfsdirtab` file we added in our transaction.

**5. Checking the repository info**

``` { .bash .copy }
sudo cvmfs_server info $repo_name
```

### Setting up a CVMFS Stratum 1

Again, the documentation below provides you with the minimal steps to set up a working Stratum 1 specifically aimed at hosting a site software stack on top of EESSI. There are a lot of things you can configure here, which are described in detail in the [upstream documentation](https://cvmfs.readthedocs.io/en/stable/cpt-replica.html). Also, the [CVMFS tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/03_stratum1_proxies/) may be helpful.

**1. Set up your environment**

For convencience, let's start by redefining the repository name in an environment variable on our Stratum 1 machine, as well as our Stratum 0's IP (or DNS name):

``` { .bash .copy}
site_tld=sitename.tld
repo_name="name.${site_tld}"
stratum0_ip=<IP_OR_DNS_NAME_OF_S0>
```

**2. Install the `cvmfs-server` and `mod-wsgi` package**

Note that although we will not use the `mod-wsgi` functionality (which is required for GEO-API lookups), we still need to install it.

Typically:

``` { .bash .copy}
wget https://cvmrepo.s3.cern.ch/cvmrepo/apt/cvmfs-release-latest_all.deb
sudo dpkg -i cvmfs-release-latest_all.deb
rm -f cvmfs-release-latest_all.deb
sudo apt-get -y update
sudo apt-get -y install cvmfs-server
sudo apt install -y libapache2-mod-wsgi-py3
```

Note that the client package (`cvmfs`) is not needed on Stratum 1's.

**3. Add repository master public key**

On your CVMFS **Stratum 0**, check the contents of your master key:

``` { .bash .copy}
cat "/etc/cvmfs/keys/${repo_name}.pub"
```

and copy that to `/etc/cvmfs/keys/${site_tld}/${repo_name}.pub` on your CVMFS **Stratum 1** (note that this is one level deeper than it was on the CVMFS Stratum 0).

**4. Disable use of the Geo-API**

The Geo API is an API that clients normally use to figure out which Stratum 1 is closest to them. This is useful for CVMFS repositories have Stratum 1's all over the world, but for a site repository, where all Stratum 1's are typically very close to the clients that use them anyway, it adds complexity we don't need, so we disable it. Note that if you want, you can keep it enabled and set it up [as documented upstream](https://cvmfs.readthedocs.io/en/stable/cpt-replica.html#geo-api-setup).

``` { .bash .copy }
sudo bash -c "echo 'CVMFS_GEO_DB_FILE=NONE' > /etc/cvmfs/server.local"
```

**5. Create a replica**

Now, we create a replica of the Stratum 0, owned by the current user `$USER` (no need for it to be owned by `root` here, as we will never want to overwrite anything here):

``` { .bash .copy }
sudo cvmfs_server add-replica -o $USER http://${stratum0_ip}/cvmfs/${repo_name} /etc/cvmfs/keys/${site_tld}/
```

Note that this command creates two configuration files for the replication:

```
/etc/cvmfs/repositories.d/$repo_name/server.conf
/etc/cvmfs/repositories.d/$repo_name/replica.conf
```

**6. Initiate first sychronization**

We initialize the first synchronization manually:

``` { .bash .copy }
sudo cvmfs_server snapshot ${repo_name}
```

**7. Set up a cronjob for synchronization**

We create a cronjob that synchronizes your Stratum 1 to the Stratum 0 every 5 minutes. Note that if a previous `cvmfs_server snapshot` command is still running, it'll just skip the new invocation, so a short interval should not cause trouble. You can pick a different sychronization frequency if you like - just realize that this affects the delay with which new software will be visible on your clients.

``` { .bash .copy }
sudo bash -c "echo '*/5 * * * * root output=\$(/usr/bin/cvmfs_server snapshot -a -i 2>&1) || echo \"\$output\"' > /etc/cron.d/cvmfs_stratum1_snapshot"
```

**8. Confirm the synchronization is working**

While it is not easily possible to check which files are hosted on a Stratum 1, you can check the synchronization log at `/var/log/cvmfs/snapshots.log` to see if the synchronization process finshes correctly. The report also stathes the revision the Stratum 1 is serving ('Serving revision X'). You can cross-check that this is the latest revision by running on the **Stratum 0**:

``` { .bash .copy }
sudo cvmfs_server tag "$repo_name"
```

**Scripted summary of steps**

For convenience, we list all the commands from the prior steps together. Note that you'll manually have to copy in the CVMFS Stratum 0's public key.

``` { .bash .copy }
# Define environment variables
site_tld=sitename.tld
repo_name="name.${site_tld}"
stratum0_ip=<IP_OR_DNS_NAME_OF_S0>
echo "Setting up Stratum 1 for CVMFS repository: ${repo_name}, which is hosted on ${stratum0_ip}"

# Install cvmfs-server and mod-wsgi
echo "Installing cvmfs-server and mod-wsgi"
wget https://cvmrepo.s3.cern.ch/cvmrepo/apt/cvmfs-release-latest_all.deb
sudo dpkg -i cvmfs-release-latest_all.deb
rm -f cvmfs-release-latest_all.deb
sudo apt-get -y update
sudo apt-get -y install cvmfs-server
sudo apt install -y libapache2-mod-wsgi-py3

# Add repository master public key
echo "You'll need to add the CVMFS Stratum 0 mast key before this step"
echo "Checking that it exists by printing the content of the public key file..."
cat /etc/cvmfs/keys/${site_tld}/${repo_name}.pub

# Disable geo-api
echo "Disabling Geo-API"
sudo bash -c "echo 'CVMFS_GEO_DB_FILE=NONE' > /etc/cvmfs/server.local"

# Create replica
echo "Creating replica from Stratum 0 at 'http://${stratum0_ip}/cvmfs/${repo_name}', using public key from directory '/etc/cvmfs/keys/${site_tld}/'. Replica will be owned by $USER."
sudo cvmfs_server add-replica -o $USER http://${stratum0_ip}/cvmfs/${repo_name} /etc/cvmfs/keys/${site_tld}/

# Creating first snapshot
echo "Creating first snapshot for $repo_name"
sudo cvmfs_server snapshot ${repo_name}

# Setting up synchronization cronjob
echo "Setting up cronjob for synchronization"
sudo bash -c "echo '*/5 * * * * root output=\$(/usr/bin/cvmfs_server snapshot -a -i 2>&1) || echo \"\$output\"' > /etc/cron.d/cvmfs_stratum1_snapshot"
echo "Content of cronjob:"
cat /etc/cron.d/cvmfs_stratum1_snapshot

# Checking that synchronization we are running the latest revision
echo "Checking that we are running the latest revision by checking the snapshot.log:"
tail /var/log/cvmfs/snapshots.log
```

### Setting up proxies

For more info, see [this tutorial](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/access/proxy/#proxy-server-setup) on setting up a proxy for EESSI or [this generic tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/03_stratum1_proxies/#32-setting-up-a-proxy) on setting up a proxy for CVMFS repositories.

**1. Set up your environment**

First, let's define some environment variables for later use:
``` { .bash .copy }
# IP range (in CIDR notation) of the clients that should be allowed to use to use the proxy
client_ip_range_CIDR=<some_range>
# Proxy port number you want to use
proxy_port=<PORT>
# Memory / Disk cache size (in MB) that the squid is allowed to use
memory_cache_mb=<cache_size>
disk_cache_mb=<cache_size>
# Define either
stratum1_ip1=<IP_OF_STRATUM1_INSTANCE1>
stratum1_ip2=<IP_OF_STRATUM1_INSTANCE2>
# Or define the domain of your stratum 1's, including leading dot (e.g. '.sitename.tld'
stratum1_dns_domain=<DOMAIN_OF_STRATUM_1S>
```

**2. Install squid**

``` { .bash .copy }
sudo apt-get update
sudo apt-get install -y squid
```

**3. Configure squid**

The next step is to create a configuration file for the Squid proxy in `/etc/squid/squid.conf`. The template below allows your squid to proxy both your local site's CVMFS Stratum 1's, as well as the EESSI Stratum 1's. If you only want to proxy your site Stratum 1's, simply remove the `.cern.ch`, `.opensciencegrid.org` and `.eessi.science` from the list of `dstdomain`'s in the template.

``` { .bash .copy }
# List of local IP addresses (separate IPs and/or CIDR notation) allowed to access your local proxy
acl local_nodes src $client_ip_range_CIDR

# Destination domains that are allowed
# cern.ch + opensciencegrid.org domains because of cvmfs-config.cern.ch repository,
# which are provided via Stratum-1 mirror servers hosted by CERN and OSG
acl stratum_ones dstdomain .cern.ch .opensciencegrid.org .eessi.science $stratum1_dns_domain

# Deny access to anything which is not part of our stratum_ones ACL.
http_access deny !stratum_ones

# Alternatively, you can create an ACL for a particular destination based on IP, if you don't have DNS set up for your Stratum 1s:
# acl site_stratum_ones dst $stratum1_ip1 $stratum1_ip2

# And then deny access based on either domain or IP:
# http_access deny !stratum_ones !site_stratum_ones

# Add destination IPs that are allowed for your site Stratum 1s
acl site_stratum_ones dst $stratum1_ip1 $stratum1_ip2

# Deny access to anything which is not part of our stratum_ones or site_stratum_ones ACL.
http_access deny !stratum_ones !site_stratum_ones

# Squid port
http_port $proxy_port

# Only allow access from our local machines
http_access allow local_nodes
http_access allow localhost

# Finally, deny all other access to this proxy
http_access deny all

minimum_expiry_time 0
maximum_object_size 1024 MB

# proxy memory cache of $memory_cache_mb MB
cache_mem $memory_cache_mb MB
maximum_object_size_in_memory 128 KB
# $disk_cache_mb MB disk cache
cache_dir ufs /var/spool/squid $disk_cache_mb 16 256
```

**4. Validate the squid config and reload the service**

To validate the correctness of your config file, run

```
sudo squid -k parse
```

If all looks ok, restart the squid service:

```
sudo systemctl start squid
sudo systemctl enable squid
```

**Scripted summary of steps**

WARNING: this will overwrite any existing squid config, so only execute this literally if you are on a fresh machine
``` { .bash .copy }
# IP range (in CIDR notation) of the clients that should be allowed to use to use the proxy
client_ip_range_CIDR=<some_range>
# Proxy port number you want to use
proxy_port=<PORT>
# Memory / Disk cache size (in MB) that the squid is allowed to use
memory_cache_mb=<cache_size>
disk_cache_mb=<cache_size>
# Define either
stratum1_ip1=<IP_OF_STRATUM1_INSTANCE1>
stratum1_ip2=<IP_OF_STRATUM1_INSTANCE2>
# Or define the domain of your stratum 1's, including leading dot (e.g. '.sitename.tld'
stratum1_dns_domain=<DOMAIN_OF_STRATUM_1S>

echo "Installing squid"
sudo apt-get update
sudo apt-get install -y squid

echo "Creating squid config"
``` { .bash .copy }
sudo bash -c "cat > /etc/squid/squid.conf" <<EOF
# List of local IP addresses (separate IPs and/or CIDR notation) allowed to access your local proxy
acl local_nodes src $client_ip_range_CIDR

EOF
# If you specified a DNS domain for your stratum 1's, we use that as an allowed destination domain
if [ -n "${stratum1_dns_domain}" ]; then
    sudo bash -c "cat >> /etc/squid/squid.conf" <<EOF
# Destination domains that are allowed
# cern.ch + opensciencegrid.org domains because of cvmfs-config.cern.ch repository,
# which are provided via Stratum-1 mirror servers hosted by CERN and OSG
acl stratum_ones dstdomain .cern.ch .opensciencegrid.org .eessi.science $stratum1_dns_domain

# Deny access to anything which is not part of our stratum_ones ACL.
http_access deny !stratum_ones

EOF
else  # We use the individual stratum 1 IPs as allowed destinations, in addition to the domains required for the EESSI stratum 1's
    sudo bash -c "cat >> /etc/squid/squid.conf" <<EOF
# Destination domains that are allowed
# cern.ch + opensciencegrid.org domains because of cvmfs-config.cern.ch repository,
# which are provided via Stratum-1 mirror servers hosted by CERN and OSG
acl stratum_ones dstdomain .cern.ch .opensciencegrid.org .eessi.science

# Add destination IPs that are allowed for your site Stratum 1s
acl site_stratum_ones dst $stratum1_ip1 $stratum1_ip2

# Deny access to anything which is not part of our stratum_ones or site_stratum_ones ACL.
http_access deny !stratum_ones !site_stratum_ones

EOF
fi

sudo bash -c "cat >> /etc/squid/squid.conf" <<EOF
# Squid port
http_port $proxy_port

# Only allow access from our local machines
http_access allow local_nodes
http_access allow localhost

# Finally, deny all other access to this proxy
http_access deny all

minimum_expiry_time 0
maximum_object_size 1024 MB

# proxy memory cache of $memory_cache_mb MB
cache_mem $memory_cache_mb MB
maximum_object_size_in_memory 128 KB
# $disk_cache_mb MB disk cache
cache_dir ufs /var/spool/squid $disk_cache_mb 16 256
EOF

echo "Validating squid config"
sudo squid -k parse

echo "Starting squid service"
sudo systemctl start squid
sudo systemctl enable squid
```

### (Re)configuring your CVMFS clients

**1. Set up your environment**

First, let's define some environment variables for later use
``` { .bash .copy }
site_tld=sitename.tld
repo_name="name.${site_tld}"
stratum1_ip1=<IP_OR_DNS_NAME_OF_STRATUM1_INSTANCE1>
stratum1_ip2=<IP_OR_DNS_NAME_OF_STRATUM1_INSTANCE2>
proxy_ip1=<IP_OR_DNS_NAME_OF_PROXY1>
proxy_port1=<PORT_NR_FOR_PROXY1>
proxy_ip2=<IP_OR_DNS_NAME_OF_PROXY2>
proxy_port2=<PORT_NR_FOR_PROXY2>
```

**2. Install CVMFS client**

Typically, the machines on which you want to offer your own software stack on top of EESSI already have the CVMFS client installed, otherwise you wouldn't be able to serve EESSI there. If you haven't done so, please follow the instructions [here](../../getting_access/native_installation#native-install-on-clusters).

**3. Add the repository master public key**
On your CVMFS **Stratum 0**, check the contents of your master key:
```
cat "/etc/cvmfs/keys/${repo_name}.pub"
```
and copy that to /etc/cvmfs/keys/${site_tld}/${repo_name}.pub on your client machines.

**4. Configure CVMFS client for site-repository**

Here, we will assume that you're using the same two proxies for all CVMFS repositories, so we put `CVMFS_HTTP_PROXY` within the `/etc/cvmfs/default.local`. If you still had a `CVMFS_CLIENT_PROFILE=single` in your `/etc/cvmfs/default.local` you should remove it first:

``` { .bash .copy }
sudo sed -i '/^CVMFS_CLIENT_PROFILE=single$/d' /etc/cvmfs/default.local
```

Then, we add the proxy configuration:

``` { .bash .copy }
sudo bash -c "echo 'CVMFS_HTTP_PROXY=\"http://${proxy_ip1}:${proxy_port1}|http://${proxy_ip2}:${proxy_port2}\"' >> /etc/cvmfs/default.local"
```

Then, we add your site repository to `CVMFS_REPOSITORIES` in `/etc/cvmfs/default.local`

``` { .bash .copy }
sudo bash -c "echo 'CVMFS_REPOSITORIES=\"$repo_name\"' >> /etc/cvmfs/default.local"
```

Then, we create the repository configuration file

``` { .bash .copy }
sudo bash -c "cat > /etc/cvmfs/config.d/${repo_name}.conf" <<EOF
CVMFS_SERVER_URL="http://${stratum1_ip1}/cvmfs/@fqrn@;http://${stratum1_ip2}/cvmfs/@fqrn@"
CVMFS_USE_GEOAPI="no"
CVMFS_KEYS_DIR=/etc/cvmfs/keys/${site_tld}
EOF
```

!!! note
    If you want to use different proxy servers for EESSI vs your site CVMFS repository, you can add a site-specific `CVMFS_HTTP_PROXY` configuration in this file (`/etc/cvmfs/config.d/${repo_name}.conf`) as well, with your site specific setting. For EESSI, you could add it to `/etc/cvmfs/domain.d/eessi.io.local`

!!! note
    You could have done the configuration at the domain level, i.e. in `/etc/cvmfs/domain.d/${site_tld}.conf`. This only makes a difference if you host _multiple_ repositories under a single ${site_tld} domain, in which case this configuration would apply to _all_ of those repositories. In that case, you'd have to think about which level to specify what configuration at, e.g. specifying the `CVMFS_SERVER_URL` at the `domain.d` level if all of those repositories are hosted on the same server URL.

Finally, we call `cvmfs_config setup` which will load the configuration for the newly configured repository.

``` { .bash .copy }
sudo cvmfs_config setup
```

**5. Check setup**

If all went well, you should now have both `software.eessi.io` as well as your site repository available. You can check this with:

``` { .bash .copy }
cvmfs_config probe software.eessi.io ${repo_name}
```

and/or

``` { .bash .copy }
sudo cvmfs_config chksetup
```

Another useful check is to see which proxy and which Stratum 1 the client actually connected to - and if this is indeed as you intended:

``` { .bash .copy }
sudo cvmfs_config stat -v software.eessi.io
sudo cvmfs_config stat -v ${repo_name}
```

This should report a line like

```
Connection: http://${stratum1_ipX}/cvmfs/${repo_name} through proxy http://${proxy_ipX}:${proxy_portX} (online)
```

**Scripted summary of steps**

Don't forget to add the master repository key to `/etc/cvmfs/keys/${site_tld}/${repo_name}.pub` first.

``` { .bash .copy }
site_tld=sitename.tld
repo_name="name.${site_tld}"
stratum1_ip1=<IP_OR_DNS_NAME_OF_STRATUM1_INSTANCE1>
stratum1_ip2=<IP_OR_DNS_NAME_OF_STRATUM1_INSTANCE2>
proxy_ip1=<IP_OR_DNS_NAME_OF_PROXY1>
proxy_port1=<PORT_NR_FOR_PROXY1>
proxy_ip2=<IP_OR_DNS_NAME_OF_PROXY2>
proxy_port2=<PORT_NR_FOR_PROXY2>

echo "Remove 'CVMFS_CLIENT_PROFILE=single' from /etc/cvmfs/default.local (if any)"
sudo sed -i '/^CVMFS_CLIENT_PROFILE=single$/d' /etc/cvmfs/default.local
echo "Add CVMFS_HTTP_PROXY and CVMFS_REPOSITORIES settings to /etc/cvmfs/default.local"
sudo bash -c "echo 'CVMFS_HTTP_PROXY=\"http://${proxy_ip1}:${proxy_port1}|http://${proxy_ip2}:${proxy_port2}\"' >> /etc/cvmfs/default.local"
sudo bash -c "echo 'CVMFS_REPOSITORIES=\"$repo_name\"' >> /etc/cvmfs/default.local"
echo "Contents of /etc/cvmfs/default.local:"
cat /etc/cvmfs/default.local

echo "Create repository configuration at /etc/cvmfs/config.d/${repo_name}.conf"
sudo bash -c "cat > /etc/cvmfs/config.d/${repo_name}.conf" <<EOF
CVMFS_SERVER_URL="http://${stratum1_ip1}/cvmfs/@fqrn@;http://${stratum1_ip2}/cvmfs/@fqrn@"
CVMFS_USE_GEOAPI="no"
CVMFS_KEYS_DIR=/etc/cvmfs/keys/${site_tld}
EOF
echo "Contents of /etc/cvmfs/config.d/${repo_name}.conf:"
cat /etc/cvmfs/config.d/${repo_name}.conf

echo "Checking CVMFS setup"
sudo cvmfs_config chksetup
echo "Checking setup for software.eessi.io"
cvmfs_config probe software.eessi.io
sudo cvmfs_config stat -v software.eessi.io
echo "Checking setup for ${repo_name}"
cvmfs_config probe ${repo_name}
sudo cvmfs_config stat -v ${repo_name}
```

### Debugging issues with a site CVMFS setup

If the above did _not_ give you a working repository on the client, the best way to debug things is probably to first isolate _where_ the problem is: Stratum 0, Stratum 1, proxy or client. [This troubleshooting guide](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/troubleshooting/) may also be helpful. 

**1. Connect your client directly to the Stratum 1**

To make your client connect directly to your Stratum 1, configuring it with the `CVMFS_HTTP_PROXY=DIRECT` setting. Then, run

``` { .bash .copy }
cvmfs_config probe ${repo_name}
sudo cvmfs_config stat -v ${repo_name}
```

again. The second command should now print something like

```
Connection: http://${stratum1_ipX}/cvmfs/${repo_name} through proxy DIRECT
```

If this does _not_ work, proceed to step 2.

If this _does_ work, the issue is with your proxy. Some things to check

- Is the proxy service running? (`systemctl status squid`)
- Is there a firewall blocking traffic to the proxy port?
- Is there a mistake in the squid configuration? You can try to remove restrictions (e.g. the destination or source restrictions) one by one, to see if this fixes things to find the offending restriction.

**2. Connect your client directly to the Stratum 0**

To make your client connect directly to your Stratum 0, _in addition_ to configuring it with `CVMFS_HTTP_PROXY=DIRECT`, set `CVMFS_SERVER_URL="http://${stratum0_ip}/cvmfs/@fqrn@"`. Also, make sure your Stratum 0 is accessible from your clients: you may not want this in a production environment, but you may want to open it up temporarily. Then, run

``` { .bash .copy }
cvmfs_config probe ${repo_name}
sudo cvmfs_config stat -v ${repo_name}
```

again. The second command should now print something like

```
Connection: http://${stratum0_ip}/cvmfs/${repo_name} through proxy DIRECT
```

If this _does_ work, something is wrong with your Stratum 1. Some things to check

- Is there a firewall blocking traffic?
- Do the snapshot logs on the Stratum 1 look sane, i.e. is the Stratum 1 at least succesful in mirroring the Stratum 0?

If this does _not_ work, the issue is with your Stratum 0. Go through the [sanity check](#sanity-checking-your-stratum-0-setup) steps again to be sure. Also here, think if there's a firewall that's blocking traffic to the client.

## Setting up an object store to stage build tarballs

The standard deployment method for the EESSI build bot is to stage tarballs in an S3 bucket. While the bot's functionality may be extended in the future (the [function](https://github.com/EESSI/eessi-bot-software-layer/blob/29dc5e9aa339c323a900dc1454d39246def73984/tasks/deploy.py#L689) actually uploading the tarballs could easily be altered to deploy to a central directory on a local filesystem, for example), for now this means we need an S3 bucket if we want to use the bot's deployment functionality.

There is extensive documentation on how to interact with S3 buckets available online - here we only list the few commands that you would commonly need to set up a staging bucket.

### Installing the AWS CLI commands

Today, this can be done with:

``` { .bash .copy }
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

But see the [upstream documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for up to date instructions.

### Configuring AWS CLI

Create a `.aws` folder in your homedir:

``` { .bash .copy }
mkdir -p ~/.aws
```

and create a configuration file `~/.aws/config` and `~/.aws/credentials`. The content of the configuration file are typically specific for the S3-compatible service you are using. The credentials file typically looks something like:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

To test if your setup works, run

``` { .bash .copy }
aws s3 ls
```

If you don't have any buckets, this won't actually list anything - but the command should complete succesfully.

### Creating a bucket

To create a bucket, run:

```
aws s3 mb s3://<bucket_name>
```

### Security considerations

There are many policies you can attach to a bucket to increase security. At the _very_ least, consider setting a bucket policy that restricts IP access to a whitelisted range (i.e. only the nodes where your build bot(s) run, and your Stratum 0 need access). The [AWS policy generator](https://awspolicygen.s3.amazonaws.com/policygen.html) can be a helpful tool in generating such a policy.

Another thing to consider is to create a secondary user with `aws iam create-user --user-name <name>` and attach a very limited policy to it (e.g. only read/write/list on buckets, nothing else). Then, create credentials for this user with `aws iam create-access-key --user-name <name>` and provide those credentials to the EESSI build bot and Stratum 0 machines. That way, if that token is compromized, the impact is minimized (e.g. the token can at least not be used to create new IAM idententies, etc).

## Setting up the EESSI build bot

### What is the EESSI build bot?

The [EESSI build bot](https://github.com/EESSI/eessi-bot-software-layer) is designed to start Slurm jobs and run scripts when triggered by certain GitHub events. The job script that is used can be configured, and while it goes through some fixed steps (e.g. build, check-build, test, check-test), the steps themselves are fully defined by the scripts provided in the `bot` folder of the respective repository from which it was triggered. See for example the scripts defined for the [EESSI/software-layer-scripts](https://github.com/EESSI/software-layer-scripts/tree/main/bot) repository.

The goal of the bot is to make the build process scalable: software in EESSI is build for many different architectures, and (for CPU targets) these build are done natively (i.e. the target architecture is the same as the architecture of the node one which the build was done). This means that for every software installation, the amount of build jobs that needs to be run is equal to the amount of architectures EESSI supports. For the large amount of supported architectures and software installations in EESSI, it is infeasible to start all of those build jobs manually - that's where the bot comes in.

While running build jobs manually may be sufficient for your site, sites that offer very heterogenous clusters or that plan to deploy a fair amount of software in their site-specific repository can benefit from the scalability of the bot.

The build bot has two main processes:

- [an event handler](https://github.com/EESSI/eessi-bot-software-layer/blob/develop/eessi_bot_event_handler.py) which receives events from GitHub and acts on them
- [a job manager](https://github.com/EESSI/eessi-bot-software-layer/blob/develop/eessi_bot_job_manager.py), which monitors the Slurm job queue and acts on state changes of the jobs submitted by the event handler.

### Requirements

In order to run the build bot, a few things are required:

1. An organization in GitHub. While not _strictly_ required, this means you can share management of the bot with others in your organization. For the rest of these docs, we will assume you already have a [GitHub organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch) and refer to it as GH_ORG.
2. A GitHub account, with 'Owner' rights within your organization.
3. A GitHub App, created within your organization.
4. A GitHub repository within your organization on which the GitHub App can be installed
5. A SMEE channel to relay github events to the running bot instance
6. A node that can host the bot process, and from where the bot can start jobs on a SLURM cluster
7. A shared filesystem that the bot process has access to where it can stage jobs directories

Note that the bot process itself is _relatively_ lightweight, since the builds are performed in jobs. Thus, running the bot process on a login node is probably feasible.

### Creating a SMEE channel

Go to [https://smee.io/new](https://smee.io/new) in order to create a new SMEE channel. **Write down the URL!**

### Registering a GitHub App for the bot

- Go to https://github.com/organizations/GH_ORG/settings/apps.
- Click "New GitHub App"
- Pick a descriptive name. We'll refer to it as APP_NAME
- Under "Homepage URL", we suggest you fill in the URL of the SMEE channel you just created (but unimportant for how the bot functions)
- Under "Webhook URL", fill in the URL of the SMEE channel you just created
- Generate a Webhook secret. This secret will be used by the bot's event handler to verify that the event was really sent from your GitHub app.
  - Run `python3 -c 'import secrets; print(secrets.token_hex(64))'` on any machine
  - Past the result in the 'Secret' box underneath the Webhook URL
- Under "Repository Permissions":
  - Set "Issues" to "Access: Read and Write"
  - Set "Pull requests" to "Access: Read and Write"
- Under "Subscribe to events", tick the "Issue comment" and "Pull request" boxes (note: these only appear once you've set the Repository Permissions above)
- Select "Only allow this GitHub App to be installed on the GH_ORG account
- Click "Create GitHub App"
- Scroll down to the "Private keys" section and click "Generate a private key". This key will be uesd by the bot event handler in order to be able to interact with GitHub (and e.g. post responses in your PRs).

### Create a GitHub repository

- Go to https://github.com/organizations/GH_ORG/repositories/new
- Pick a descriptive name. We'll refer to it as GH_REPO
- Add the `bot/build.sh` from [EESSI/software-layer](https://github.com/EESSI/software-layer) to your repository (under the exact same name)

Note that you may regularly want to pull in the `bot/build.sh` from the upstream `EESSI/software-layer` in case changes are made to it upstream.

### Installing the GitHub App onto a repository

- Go to https://github.com/organizations/GH_ORG/settings/apps/APP_NAME
- On the left, go to "Install App"
- Click "Install" next to your organizations' account
- Select "Only select repositories" and select the GH_REPO from the dropdown menu
- Click "Install"

### Install EESSI build bot on a machine
- app.cfg
- set up an environment for the bot to run in
- run the necessary scripts

## Set up automatic ingestion on CVMFS Stratum 0 (optional)
- list steps this needs to do

## Add your first software
- add easystack
- create PR
- bot:show_config first!
- bot:build
- Add deploy label
- See deployment happening in real-time :)
