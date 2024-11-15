# Setting up a Stratum 1

The EESSI project provides a number of geographically distributed public Stratum 1 servers that you can use to make EESSI available on your machine(s).
It is always recommended to have a local caching layer consisting of a few Squid proxies. 
If you want to be even better protected against network outages and increase the bandwidth between your cluster nodes and the Stratum 1 servers,
you could also consider setting up a local (private) Stratum 1 server that replicates the EESSI CVMFS repository.
This guarantees that you always have a full and up-to-date copy of the entire stack available in your local network. 

## Requirements for a Stratum 1

The main requirements for a Stratum 1 server are a good network connection to the clients it is going to serve,
and sufficient disk space. As the EESSI repository is constantly growing, make sure that the disk space can easily be extended if necessary. 
Currently, we recommend to have at least 1 TB available.

In terms of cores and memory, a machine with just a few (~4) cores and 4-8 GB of memory should suffice.

Various Linux distributions are supported, but we recommend one based on RHEL 8 or 9.

Finally, make sure that ports 80 and 8000 are open to clients.


## Configure the Stratum 1

Stratum 1 servers have to synchronize the contents of their CVMFS repositories regularly, and usually they replicate from a CVMFS Stratum 0 server. 
In order to ensure the stability and security of the EESSI Stratum 0 server, it has a strict firewall, and only the EESSI-maintained public Stratum 1 servers are allowed to replicate from it.
However, EESSI provides a synchronisation server that can be used for setting up private Stratum 1 replica servers, and this is available at `http://aws-eu-west-s1-sync.eessi.science`.

!!! warn Potential issues with intrusion prevention systems
    In the past we have seen a few occurrences of data transfer issues when files were being pulled in by or from a Stratum 1 server.
    In such cases the `cvmfs_server snapshot` command, used for synchronizing the Stratum 1, may break with errors like `failed to download <URL to file>`.
    Trying to manually download the mentioned file with `curl` will also not work, and result in errors like:
    ```
    curl: (56) Recv failure: Connection reset by peer
    ```
    In all cases this was due to an intrusion prevention system scanning the associated network, and hence scanning all files going in or out of the Stratum 1.
    Though it was a false-positive in all cases, this breaks the synchronization procedure of your Stratum 1.
    If this is the case, you can try switching to HTTPS by using `https://aws-eu-west-s1-sync.eessi.science` for synchronizing your Stratum 1.
    Even though there is no advantage for CVMFS itself in using HTTPS (it has built-in mechanisms for ensuring the integrity of the data),
    this will prevent the described issues, as the intrusion prevention system will not be able to inspect the encrypted data.
    However, not only does HTTPS introduce some overhead due to the encryption/decryption, it also makes caching in forward proxies impossible.
    Therefore, it is strongly discouraged to use HTTPS as default.

### Manual configuration

In order to set up a Stratum 1 manually, you can make use of the instructions in the [Private Stratum 1 replica server](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/access/stratum1/)
section of the MultiXscale tutorial ["Best Practices for CernVM-FS in HPC"](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/).

### Configuration using Ansible

The recommended way for setting up an EESSI Stratum 1 is by running the Ansible playbook `stratum1.yml`
from the [filesystem-layer repository on GitHub](https://github.com/EESSI/filesystem-layer).
For the commands in this section, we are assuming that you cloned this repository, and your working directory is `filesystem-layer`.

!!! note GEO API
    Installing a Stratum 1 usually requires a GEO API license key, which will be used to find the (geographically) closest Stratum 1 server for your client and proxies.
    However, for a private Stratum 1 this can be skipped, and you can disable the use of the GEO API in the configuration of your clients by setting `CVMFS_USE_GEOAPI=no`.
    In this case, they will just connect to your local Stratum 1 by default.
    
    If you do want to set up the GEO API, you can find more information on how to (freely) obtain this key in the CVMFS documentation: https://cvmfs.readthedocs.io/en/stable/cpt-replica.html#geo-api-setup.
    
    You can put your license key in the local configuration file `inventory/local_site_specific_vars.yml` with the variables `cvmfs_geo_license_key` and `cvmfs_geo_account_id`.

Start by installing Ansible, e.g.:

```bash
sudo yum install -y ansible
```

Then install Ansible roles for EESSI:

```bash
ansible-galaxy role install -r ./requirements.yml --force
```

Make sure you have enough space in `/srv` on the Stratum 1, since the snapshots of the repositories
will end up there by default. To alter the directory where the snapshots get stored you can manually
create a symlink before running the playbook:
```bash
sudo ln -s /lots/of/space/cvmfs /srv/cvmfs
```

Also make sure that:
  - you are able to log in to the server from the machine that is going to run the playbook (preferably using an SSH key);
  - you can use `sudo` on this machine;
  - you add the hostname or IP address of your server to a `cvmfsstratum1servers` section in the `inventory/hosts` file, e.g.:
```
[cvmfsstratum1servers]
12.34.56.789 ansible_ssh_user=yourusername
```

Finally, install the Stratum 1 using:

``` bash
# -b to run as root, optionally use -K if a sudo password is required, and optionally include your site-specific variables
ansible-playbook -b [-K] [-e @inventory/local_site_specific_vars.yml] stratum1.yml
```
Running the playbook will automatically make replicas of all the repositories defined in `group_vars/all.yml`.
If you only want to replicate the `software.eessi.io` repository, you can remove the other ones from this file.


### Verification of the Stratum 1 using `curl`

When the playbook has finished, your Stratum 1 should be ready. In order to test your Stratum 1,
even without a client installed, you can use `curl`:

```bash
curl --head http://<url-or-ip-to-your-stratum1>/cvmfs/software.eessi.io/.cvmfspublished
```
This should return something like:

```bash
HTTP/1.1 200 OK
...
Content-Type: application/x-cvmfs
```

Example with the EESSI Stratum 1 running in AWS:

```bash
curl --head http://aws-eu-central-s1.eessi.science/cvmfs/software.eessi.io/.cvmfspublished
```

### Verification of the Stratum 1 using a CVMFS client

You can, of course, also test access to your Stratum 1 from a client.
This requires you to install a CernVM-FS client and add the Stratum 1 to the client configuration;
this is explained in more detail on the [native installation page](../getting_access/native_installation.md).

Then verify that the client connects to your new Stratum 1 by running:

```bash
cvmfs_config stat -v software.eessi.io
```

Assuming that your new Stratum 1 is working properly, this should return something like:

```bash
Connection: http://<url-or-ip-to-your-stratum1>/cvmfs/software.eessi.io through proxy DIRECT (online)
```
