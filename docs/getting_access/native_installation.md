# Native installation

## Installation for single clients

Setting up native access to EESSI, that is a system-wide deployment that does not require workarounds like
[using a container](eessi_container.md), requires the installation and configuration of [CernVM-FS](https://cernvm.cern.ch/fs).

This requires **admin privileges**, since you need to install CernVM-FS as an OS package.

The following actions must be taken for a (basic) native installation of EESSI:

* Installing CernVM-FS itself, ideally using the OS packages provided by the CernVM-FS project
  (although installing from source is also possible);
* Installing the EESSI configuration for CernVM-FS, which can be done by installing the ``cvmfs-config-eessi``
  package that we provide for the most popular Linux distributions
  (more information available [here](https://github.com/EESSI/filesystem-layer/));
* Creating a small client configuration file for CernVM-FS (``/etc/cvmfs/default.local``);
  see also the [CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html#create-default-local).

The good news is that all of this only requires a handful commands :astonished: :

=== "RHEL-based Linux distributions"

    ``` { .bash .copy }
    # Installation commands for RHEL-based distros like CentOS, Rocky Linux, Almalinux, Fedora, ...

    # install CernVM-FS
    sudo yum install -y https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest.noarch.rpm
    sudo yum install -y cvmfs

    # create client configuration file for CernVM-FS (no squid proxy, 10GB local CernVM-FS client cache)
    sudo bash -c "echo 'CVMFS_CLIENT_PROFILE="single"' > /etc/cvmfs/default.local"
    sudo bash -c "echo 'CVMFS_QUOTA_LIMIT=10000' >> /etc/cvmfs/default.local"

    # make sure that EESSI CernVM-FS repository is accessible
    sudo cvmfs_config setup
    ```

=== "Debian-based Linux distributions"

    ``` { .bash .copy }
    # Installation commands for Debian-based distros like Ubuntu, ...

    # install CernVM-FS
    sudo apt-get install lsb-release
    wget https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest_all.deb
    sudo dpkg -i cvmfs-release-latest_all.deb
    rm -f cvmfs-release-latest_all.deb
    sudo apt-get update
    sudo apt-get install -y cvmfs

    # create client configuration file for CernVM-FS (no squid proxy, 10GB local CernVM-FS client cache)
    sudo bash -c "echo 'CVMFS_CLIENT_PROFILE="single"' > /etc/cvmfs/default.local"
    sudo bash -c "echo 'CVMFS_QUOTA_LIMIT=10000' >> /etc/cvmfs/default.local"

    # make sure that EESSI CernVM-FS repository is accessible
    sudo cvmfs_config setup
    ```

!!! Note
    The default location for the cache directory is `/var/lib/cvmfs`. Please,
    check that the partition on which this directory is stored is big enough to
    store the cache (and other data). You may override this by adding
    `CVMFS_CACHE_BASE=<some other directory for the cache>` to your
    `default.local`, e.g., running
    ``` { .bash .copy }
    sudo bash -c "echo 'CVMFS_CACHE_BASE=<some other directory for the cache>' >> /etc/cvmfs/default.local"
    ```

## Installation for larger systems (e.g. clusters)

When using CernVM-FS on a larger number of local clients, e.g. on a HPC cluster or set of workstations,
it is very strongly recommended to at least set up some Squid proxies close to your clients.
These Squid proxies will be used to cache content that was recently accessed by your clients,
which reduces the load on the Stratum 1 servers and reduces the latency for your clients.
As a rule of thumb, you should use about one proxy per 500 clients, and have a minimum of two.
Instructions for setting up a Squid proxy can be found in the [CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-squid.html) and
in the [CernVM-FS tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/03_stratum1_proxies/#32-setting-up-a-proxy).

Additionally, setting up a private Stratum 1, which will make a full copy of the repository,
 can be beneficial to improve the latency and bandwidth even further, and to be better protected against network outages.
Instructions for setting up your own EESSI Stratum 1 can be found in [setting up your own CernVM-FS Stratum 1 mirror server](../filesystem_layer/stratum1.md).

### Configuring your client to use a Squid proxy

If you have set up one or more Squid proxies, you will have to add them to your CernVM-FS client configuration.
This can be done by removing `CVMFS_CLIENT_PROFILE="single"` from `/etc/cvmfs/default.local`, and add the following line:

```
CVMFS_HTTP_PROXY="http://ip-of-your-1st-proxy:port|http://ip-of-your-2nd-proxy:port"
```

In this case, both proxies are equally preferable.
More advanced use cases can be found in [the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#proxy-list-examples).

### Configuring your client to use a private Stratum 1 mirror server

If you have set up your own Stratum 1 mirror server that replicates the EESSI CernVM-FS repositories,
you can instruct your CernVM-FS client(s) to use it by prepending your newly created Stratum 1 to the existing list of EESSI Stratum 1 servers by creating a local CVMFS configuration file for the EESSI domain:

```bash
echo 'CVMFS_SERVER_URL="http://<url-or-ip-to-your-stratum1>/cvmfs/@fqrn@;$CVMFS_SERVER_URL"' | sudo tee -a /etc/cvmfs/domain.d/eessi.io.local
```

!!! note
    By prepending your new Stratum 1 to the list of existing Stratum 1 servers, your clients should by default use the private Stratum 1.
    In case of downtime of your private Stratum 1, they will also still be able to make use of the public EESSI Stratum 1 servers.


### Applying changes in the CernVM-FS client configuration files

After you have made any changes to the CernVM-FS client configuration, you will have to apply them.
If this is the first time you set up the client, you can simply run:

```bash
sudo cvmfs_config setup
```

If you already had configured the client before, you can reload the configuration for the EESSI repository (or, similarly, for any other repository) using:

```bash
sudo cvmfs_config reload -c software.eessi.io
```

