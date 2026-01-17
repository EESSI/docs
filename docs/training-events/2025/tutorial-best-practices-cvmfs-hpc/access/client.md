# CernVM-FS client system

The recommended way to gain access to CernVM-FS repositories is to set up
a *system-wide native installation* of CernVM-FS on the [client system(s)](../appendix/terminology.md#client),
which comes down to:

* Installing the client component of CernVM-FS;
* Creating a minimal client configuration file (`/etc/cvmfs/default.local`);
* Completing the client setup by:
    * Creating a`cvmfs` user account and group;
    * Creating the `/cvmfs` and `/var/lib/cvmfs` directories;
    * Configuring `autofs` to enable auto-mounting of repositories *(recommended)*.

For repositories that are not included in the default
CernVM-FS configuration you also need to provide some additional information
specific to those repositories in order to access them.

!!! danger "This is not a production-ready setup (yet)!"

    While these basic steps are enough to *gain access* to CernVM-FS repositories,
    this is not sufficient to obtain a production-ready setup.

    This is especially true on HPC infrastructure that typically consists of a
    large number of worker nodes on which software provided by one or more
    CernVM-FS repositories will be used.

    After covering the basic client setup in this section, we will outline
    how to make accessing of CernVM-FS repositories more reliable and performant,
    by also setting up a [proxy server](proxy.md) and [CernVM-FS Stratum 1
    replica server](stratum1.md).


## Installing CernVM-FS client

Start with installing the `cvmfs` package which provides the CernVM-FS client component:

=== "For RHEL-based Linux distros (incl. CentOS, Rocky, Fedora, ...)"

    ``` { .bash .copy }
    # install cvmfs-release package to add yum repository
    sudo yum install -y https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest.noarch.rpm

    # install CernVM-FS client package
    sudo yum install -y cvmfs
    ```

=== "For Debian-based Linux distros (incl. Ubuntu)"

    ``` { .bash .copy }
    # install cvmfs-release package to add apt repository
    sudo apt install lsb-release
    curl -OL https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest_all.deb
    sudo dpkg -i cvmfs-release-latest_all.deb
    sudo apt update

    # install CernVM-FS client package
    sudo apt install -y cvmfs
    ```

If none of the available `cvmfs` packages are compatible with your system,
you can also [build CernVM-FS from
source](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html#building-from-source).


## Minimal client configuration {: #minimal_configuration }

Next to installing the CernVM-FS client, you should also create a minimal configuration file for it.

This is typically done in `/etc/cvmfs/default.local`,
which should contain something like:

``` { .ini .copy }
CVMFS_CLIENT_PROFILE="single" # a single node setup, not a cluster
CVMFS_QUOTA_LIMIT=10000
```

More information on the structure of `/etc/cvmfs` and supported configuration settings is available
[in the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html).


??? note "Client profile setting *(click to expand)*"

    With `CVMFS_CLIENT_PROFILE="single"` we specify that this CernVM-FS client should:

    * Use the [proxy server](../appendix/terminology.md#proxy) specified via `CVMFS_HTTP_PROXY`, if that configuration setting is defined;
    * Directly connect to a [Stratum-1 replica server](../appendix/terminology.md#stratum1) that provides the repository being used if no proxy server
      is specified via `CVMFS_HTTP_PROXY`.

    As an alternative to defining `CVMFS_CLIENT_PROFILE`, you can also set `CVMFS_HTTP_PROXY` to `DIRECT` to specify
    that no proxy server should be used by CernVM-FS:

    ``` { .ini .copy }
    CVMFS_HTTP_PROXY="DIRECT"
    ```

    We will get back to `CVMFS_HTTP_PROXY` later when [setting up a proxy server](proxy.md).

??? note "Maximum size of client cache *(click to expand)*"

    The `CVMFS_QUOTA_LIMIT` configuration setting specifies the maximum size of the CernVM-FS client cache (in MBs).

    In the example above, we specify that no more than ~10GB should be used for the client cache.

    When the specified quota limit is reached, CernVM-FS will automatically remove files from the cache according
    to the [Least Recently Used (LRU) policy](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU),
    until half of the maximum cache size has been freed.

    The location of the cache directory can be controlled by `CVMFS_CACHE_BASE` if needed (default: `/var/lib/cvmfs`),
    but **must** be a on a *local* file system of the client, not a network file system that can be modified by multiple
    hosts.

    Using a directory in a RAM disk (like `/dev/shm`) for the CernVM-FS client cache
    can be considered if enough memory is available in the client system, which would
    help reduce latency and start-up performance of software.

    For more information on cache-related configuration settings,
    [see the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#cache-settings).

### Hierarchy of configuration files {: #configuration_hierarchy }

CernVM-FS can be configured through a *hierarchy* of configuration files (sometimes also referred to as
parameter files), which can be located under either `/etc/cvmfs`, or the [CernVM-FS configuration repository](
https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#the-config-repository)
that is being used (there can be only one), which lives under `/cvmfs` and is determined by the
`CVMFS_CONFIG_REPOSITORY` configuration setting.

There are 3 levels of configuration files: [general](#cfg_general), [domain-specific](#cfg_domain), and [repository-specific](#cfg_repository).

Each CernVM-FS configuration file has either `.conf` or `.local` as file extension.

#### Order of configuration files

A CernVM-FS configuration file is *sourced* to set the configuration settings (a.k.a. parameters)
it specifies, in the order outlined below:

* By level: first general, then domain-specific, finally repository-specific;
* Within each level:
    * `.conf` before `.local`;
    * CernVM-FS configuration repository before `/etc/cvmfs` (except for general level);

As a result, a configuration file that is picked up later can override configuration settings
that were specified in an earlier consider configuration file.

Concrete example: the settings in the general `/etc/cvmfs/default.local` configuration file
are overridden by those specified in the domain-specific configuration file
`/cvmfs/cvmfs-config.cern.ch/etc/cvmfs/domain.d/eessi.io.conf` (which is located in
the default CernVM-FS configuration repository `cvmfs-config.cern.ch`).

#### General level {: #cfg_general }

At the general level, the following configuration files are considered (in order):
  
* `/etc/cvmfs/default.conf`
* `/etc/cvmfs/default.d/*.conf` (in alphabetical order)
* `$CVMFS_CONFIG_REPOSITORY/etc/cvmfs/default.conf`
* `/etc/cvmfs/default.local`

#### Domain-specific level {: #cfg_domain }

At the domain-specific level, the following configuration files are considered (in order):

* `$CVMFS_CONFIG_REPOSITORY/etc/cvmfs/domain.d/DOMAIN.conf`
* `/etc/cvmfs/domain.d/DOMAIN.conf`
* `/etc/cvmfs/domain.d/DOMAIN.local`

where "`DOMAIN`" is replaced by the domain of the CernVM-FS repository being considered,
like `eessi.io` for `software.eessi.io`.

#### Repository-specific level {: #cfg_repository }

At the repository-specific level, the following configuration files are considered (in order):

* `$CVMFS_CONFIG_REPOSITORY/etc/cvmfs/config.d/<your_repository>.conf`
* `/etc/cvmfs/config.d/<your_repository>.conf`
* `/etc/cvmfs/config.d/<your_repository>.local`

### Show configuration

To show all configuration settings in alphabetical order, including by which configuration file it got set,
use `cvmfs_config showconfig`, for example:

```{ .bash .copy }
cvmfs_config showconfig software.eessi.io
```

For `CVMFS_QUOTA_LIMIT`, you should see this in the output:

```
CVMFS_QUOTA_LIMIT=10000    # from /etc/cvmfs/default.local
```

See also [Inspecting repository configuration](#inspecting_configuration).

## Completing the client setup

To complete the setup of the CernVM-FS client component,
we need to make sure that a `cvmfs` service account and group are present on the system,
and the `/cvmfs` and `/var/lib/cvmfs` directories exist with the correct ownership and permissions.

This should be taken care of by the post-install script that is run when installing the `cvmfs` package,
so you will only need to take action on these aspects if you were installing the CernVM-FS client from source.

In addition, it is recommended to update the `autofs` configuration
to enable auto-mounting of CernVM-FS repositories, and to make sure the `autofs` service is running.

All these actions can be performed in one go by running the following command:

``` { .bash .copy }
sudo cvmfs_config setup
```

Additional options can be passed to the `cvmfs_config setup` command to disable some of the actions,
like `nouser` to not create the `cvmfs` user and group, or `noautofs` to not
update the `autofs` configuration.

### Recommendations for `autofs` {: #autofs }

It is recommended to configure `autofs` to *never unmount* repositories due to inactivity,
since that [can cause problems in specific situations](https://github.com/cvmfs/cvmfs/issues/3402).

This can be done by setting additional options in `/etc/sysconfig/autofs` (on RHEL-based Linux distributions)
or `/etc/default/autofs` (on Debian-based distributions):

```{ .ini .copy }
OPTIONS="--timeout 0"
```

The default `autofs` timeout is typically 5 minutes (300 seconds), which is usually specified in `/etc/autofs.conf`.

??? warning "Warning when using Slurm's `job_container/tmpfs` plugin with `autofs` *(click to expand)*"

    Slurm versions up to 23.02 had issues when the [`job_container/tmpfs` plugin](https://slurm.schedmd.com/job_container_tmpfs.html) was being used in combination with `autofs`.
    More information can be found at the [Slurm bug tracker](https://bugs.schedmd.com/show_bug.cgi?id=12567) and the [CernVM-FS forum](https://cernvm-forum.cern.ch/t/intermittent-client-failures-too-many-levels-of-symbolic-links/156).

    Slurm version 23.02 includes a fix by providing a `Shared` option for the `job_container/tmpfs` plugin, which allows it to work with `autofs`.


### Using static mounts

If you prefer not to use `autofs`, you will need to use static mounting, by either:

* Manually mounting the CernVM-FS repositories you want to use, for example:
  ``` { .bash .copy }
  sudo mkdir -p /cvmfs/software.eessi.io
  sudo mount -t cvmfs software.eessi.io /cvmfs/software.eessi.io
  ```

* Updating `/etc/fstab` to ensure that the CernVM-FS repositories are mounted at boot time.

[Configuring `autofs`](#autofs) to never unmount due to inactivity is preferable to using static mounts,
because the latter requires that every repository is mounted individually,
even if is already known in your CernVM-FS configuration.
When using `autofs` you can access all repositories that are known to CernVM-FS through its active configuration.

For more information on mounting repositories,
[see the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#mounting).

## Checking client setup

To ensure that the setup of the CernVM-FS client component is valid, you can run:

``` { .bash .copy }
sudo cvmfs_config chksetup
```

You should see `OK` as output of this command.

## Default repositories

The default configuration of CernVM-FS, provided by the `cvmfs-config-default`
package, provides the public keys and configuration for a number of
commonly used CernVM-FS repositories.

One particular repository included in the default CernVM-FS configuration is
`cvmfs-config.cern.ch`, which is a [CernVM-FS *config repository*](
https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#the-config-repository)
that provides public keys and configuration for additional [flagship
CernVM-FS repositories](../cvmfs/flagship-repositories.md),
like [`software.eessi.io`](../eessi/high-level-design.md#filesystem_layer):

```bash
$ ls /cvmfs/cvmfs-config.cern.ch/etc/cvmfs
common.conf  config.d  default.conf  domain.d  keys

$ find /cvmfs/cvmfs-config.cern.ch/etc/cvmfs -type f -name '*eessi*'
/cvmfs/cvmfs-config.cern.ch/etc/cvmfs/domain.d/eessi.io.conf
/cvmfs/cvmfs-config.cern.ch/etc/cvmfs/keys/eessi.io/eessi.io.pub
```

That means we now already have access to the EESSI CernVM-FS repository:

```
$ ls /cvmfs/software.eessi.io
README.eessi  host_injections  versions
```

## Inspecting repository configuration {: #inspecting_configuration }

To check whether a specific CernVM-FS repository is accessible, we can *probe* it:

```
$ cvmfs_config probe software.eessi.io
Probing /cvmfs/software.eessi.io... OK
```

To view the configuration for a specific repository, use `cvmfs_config showconfig`:
``` { .bash .copy }
cvmfs_config showconfig software.eessi.io
```

To check the *active* configuration for a specific repository used
by the running CernVM-FS instance,
use `cvmfs_talk -i <repo> parameters` (which requires admin privileges):

``` { .bash .copy }
sudo cvmfs_talk -i software.eessi.io parameters
```

`cvmfs_talk` requires that the repository is currently mounted.
If not, you will see an error like this:

```bash
$ sudo cvmfs_talk -i software.eessi.io parameters
Seems like CernVM-FS is not running in /var/lib/cvmfs/shared (not found: /var/lib/cvmfs/shared/cvmfs_io.software.eessi.io)
```

## Accessing a repository

To access the contents of the repository, just use the corresponding subdirectory as if it were a local filesystem.

While the contents of the files you are accessing are not actually available on the client system the first time
they are being accessed, CernVM-FS will automatically downloaded them in the background, providing the illusion
that the whole repository is already there.

We like to refer to this as "streaming" of software installations, much like streaming music or video services.

To start using EESSI just [source the initialisation script](../eessi/using-eessi.md#init) included in the repository:

```{ .bash .copy }
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
```


You may notice some "lag" when files are being accessed, or not, depending on the network latency.

## Additional repositories

To access additional CernVM-FS repositories beyond those that are available by default, you will need to:

* Add the public keys for those repositories into a domain-specific subdirectory of `/etc/cvmfs/keys/`;
* Add the configuration for those repositories into `/etc/cvmfs/domain.d` (domain-specific) or `/etc/cvmfs/config.d` (repository-specific).

Examples are available in the `etc/cvmfs` subdirectory of the [config-repo GitHub repository](https://github.com/cvmfs-contrib/config-repo).

---

*(next: [Squid proxy server](../access/proxy.md))*
