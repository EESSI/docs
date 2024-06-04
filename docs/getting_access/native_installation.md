# Native installation

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

    # install EESSI configuration for CernVM-FS
    sudo yum install -y https://github.com/EESSI/filesystem-layer/releases/download/latest/cvmfs-config-eessi-latest.noarch.rpm

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

    # install EESSI configuration for CernVM-FS
    wget https://github.com/EESSI/filesystem-layer/releases/download/latest/cvmfs-config-eessi_latest_all.deb
    sudo dpkg -i cvmfs-config-eessi_latest_all.deb

    # create client configuration file for CernVM-FS (no squid proxy, 10GB local CernVM-FS client cache)
    sudo bash -c "echo 'CVMFS_CLIENT_PROFILE="single"' > /etc/cvmfs/default.local"
    sudo bash -c "echo 'CVMFS_QUOTA_LIMIT=10000' >> /etc/cvmfs/default.local"

    # make sure that EESSI CernVM-FS repository is accessible
    sudo cvmfs_config setup
    ```

!!! note

    :point_up: The commands above only cover the basic installation of EESSI.

    This is good enough for an individual client, or for testing purposes,
    but for a production-quality setup you should also set up a Squid proxy cache.

    For large-scale systems, like an HPC cluster, you should also consider [setting up your own CernVM-FS Stratum-1 mirror server](filesystem_layer/stratum1.md).

    For more details on this, please refer to the
    [*Stratum 1 and proxies section* of the CernVM-FS tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/03_stratum1_proxies/).

## Configuring your client to use a Squid proxy

If you have set up one or more Squid proxies, you will have to add them to your CernVM-FS client configuration.
This can be done by removing `CVMFS_CLIENT_PROFILE="single"` from `/etc/cvmfs/default.local`, and add the following line:

```
CVMFS_HTTP_PROXY="http://ip-of-your-1st-proxy:port|http://ip-of-your-2nd-proxy:port"
```

In this case, both proxies are equally preferable.
More advanced use cases can be found in [the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#proxy-list-examples).


