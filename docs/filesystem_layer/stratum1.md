# Setting up a Stratum 1

The EESSI project provides a number of geographically distributed public Stratum 1 servers that you can use to make EESSI available on your machine(s).
If you want to be better protected against network outages and increase the bandwidth between your cluster nodes and the Stratum 1 servers,
you could consider setting up a local (private) Stratum 1 server that replicates the EESSI CVMFS repository.
This guarantees that you always have a full and up-to-date copy of the entire stack available in your local network. 

## Requirements for a Stratum 1

The main requirements for a Stratum 1 server are a good network connection to the clients it is going to serve,
and sufficient disk space. As the EESSI repository is constantly growing, make sure that the disk space can easily be extended if necessary. 
Currently, we recommend to have at least 1 TB available.

In terms of cores and memory, a machine with just a few (~4) cores and 4-8 GB of memory should suffice.

Various Linux distributions are supported, but we recommend one based on RHEL 8 or 9.

Finally, make sure that ports 80 and 8000 are open to clients.


## Configure the Stratum 1

Stratum 1 servers usually replicate from the Stratum 0 server. 
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
    Even though there is no advantage for CVMFS itself in using HTTPS (it has built-in mechasnims for ensuring the integrity of the data),
    this will prevent the described issues, as the intrusion prevention system will not be able to inspect the encrypted data.
    As HTTPS does introduce some overhead due to the encryption/decryption, it is still recommended to use HTTP as default.

### Manual configuration

In order to set up a Stratum 1 manually, you can make use of the instructions in the [Private Stratum 1 replica server](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/access/stratum1/)
section of the MultiXscale tutorial ["Best Practices for CernVM-FS in HPC"](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/).

### Configuration using Ansible

The recommended way for setting up an EESSI Stratum 1 is by running the Ansible playbook `stratum1.yml`
from the [filesystem-layer repository on GitHub](https://github.com/EESSI/filesystem-layer).
For the commands in this section, we are assuming that you cloned this repository, and your working directory is `filesystem-layer`.

!!! note GEO API
    Installing a Stratum 1 usually requires a GEO API license key, which will be used to find the (geographically) closest Stratum 1 server for your client and proxies.
    However, for a private Stratum 1 this can be skipped, as clients should just connect to your local Stratum 1 by default.
    
    If you do want to set up the GEO API, you can find more information on how to (freely) obtain this key in the CVMFS documentation: https://cvmfs.readthedocs.io/en/stable/cpt-replica.html#geo-api-setup.
    
    You can put your license key in the local configuration file `inventory/local_site_specific_vars.yml`.

!!! note Squid reverse proxy
    The Stratum 1 playbooks also installs and configures a Squid reverse proxy on the server. The template configuration file for Squid can be found at `templates/eessi_stratum1_squid.conf.j2`.
    If you want to customize it, for instance for limiting the access to the Stratum 1, you can make your own version of this template file 
    and point to it by setting `local_stratum1_cvmfs_squid_conf_src` in `inventory/local_site_specific_vars.yml`.
    See the comments in the example file for more details.

Start by installing Ansible, e.g.:

```bash
sudo yum install -y ansible
```

Then install Ansible roles for EESSI:

```bash
ansible-galaxy role install -r ./requirements.yml -p ./roles --force
```

Make sure you have enough space in `/srv` on the Stratum 1, since the snapshot of the repositories
will end up there by default. To alter the directory where the snapshots get stored you can add
the following variable in `inventory/host_vars/<url-or-ip-to-your-stratum1>`:

```bash
cvmfs_srv_mount: /lots/of/space
```

Also make sure that you have added the hostname or IP address of your server to the
`inventory/hosts` file, that you are able to log in to the server from the machine that is going to run the playbook
(preferably using an SSH key), and that you can use `sudo`. 

Finally, install the Stratum 1 using:

``` bash
# -b to run as root, optionally use -K if a sudo password is required, and optionally include your site-specific variables
ansible-playbook -b [-K] [-e @inventory/local_site_specific_vars.yml] stratum1.yml
```
Running the playbook will automatically make replicas of all the repositories defined in `group_vars/all.yml`.


## Verification of the Stratum 1

When the playbook has finished, your Stratum 1 should be ready. In order to test your Stratum 1,
even without a client installed, you can use `curl`:

```bash
curl --head http://<url-or-ip-to-your-stratum1>/cvmfs/software.eessi.io/.cvmfspublished
```
This should return:

```bash
HTTP/1.1 200 OK
...
X-Cache: MISS from <url-or-ip-to-your-stratum1>
```

The second time you run it, you should get a cache hit:

```bash
X-Cache: HIT from <url-or-ip-to-your-stratum1>
```

Example with the EESSI Stratum 1 running in AWS:

```bash
curl --head http://aws-eu-central-s1.eessi.science/cvmfs/software.eessi.io/.cvmfspublished
```

You can also test access to your Stratum 1 from a client, for which you will have to install the CVMFS
[client](https://github.com/EESSI/filesystem-layer#clients). 

Then run the following command to prepend your newly created Stratum 1 to the existing list of EESSI Stratum 1 servers by creating a local CVMFS configuration file:

```bash
echo 'CVMFS_SERVER_URL="http://<url-or-ip-to-your-stratum1>/cvmfs/@fqrn@;$CVMFS_SERVER_URL"' | sudo tee -a /etc/cvmfs/domain.d/eessi-hpc.org.local
```

!!! note
    By prepending your new Stratum 1 to the list of existing Stratum 1 servers, your clients should by default use the private Stratum 1.
    In case of downtime of your private Stratum 1, they will also still be able to make use of the public EESSI Stratum 1 servers.

If this is the first time you set up the client, you now run:

```bash
sudo cvmfs_config setup
```

If you already had configured the client before, you can simply reload the config:

```bash
sudo cvmfs_config reload -c software.eessi.io
```

Finally, verify that the client connects to your new Stratum 1 by running:

```bash
cvmfs_config stat -v software.eessi.io
```

Assuming that your new Stratum 1 is working properly, this should return something like:

```bash
Connection: http://<url-or-ip-to-your-stratum1>/cvmfs/software.eessi.io through proxy DIRECT (online)
```
