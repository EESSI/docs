!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Configuring CernVM-FS on HPC infrastructure

In the [previous section](access/index.md) we have outlined how to set up a robust CernVM-FS infrastructure, by having a private Stratum 1 replica server and/or dedicated Squid proxy servers. While this approach will work for many HPC systems, some may have slightly more esoteric setups that require specific solutions, which we will discuss in this section.


## Diskless worker nodes

Some HPC systems may have worker nodes without any type of local disk, which is problematic for CernVM-FS since it uses a local cache on the worker nodes. Without this local cache, CernVM-FS can not store the repository content that is being accessed by users.

A couple of workarounds are possible in this case:

* [In-memory client cache](#in-memory-cache)
* [Loopback filesystem on a shared filesystem](#loopback-filesystem)
* [Alien cache](#alien-cache-diskless)

### In-memory client cache {: #in-memory-cache }

An easy way to set up a client cache on diskless systems is to use a RAM disk like `/dev/shm`.

It suffices to use a path like `/dev/shm/cvmfs-cache` (or equivalent) as the value for the `CVMFS_CACHE_BASE`
configuration setting in `/etc/cvmfs/default.local`, along with setting `CVMFS_QUOTA_LIMIT` to
the amount of memory that you would like to dedicate to the CernVM-FS client cache.

For example:

```{ .ini .copy }
# use max. 4GB of memory for CernVM-FS client cache
CVMFS_CACHE_BASE=/dev/shm/cvmfs-cache
CVMFS_QUOTA_LIMIT=4000
```

Do not forget to apply the changes made by running:

```{ .bash .copy }
sudo cvmfs_config reload
```

An obvious significant drawback of this is that less memory will be available to workloads running on the worker nodes,
but it may be worth considering especially if enough memory is available in total.

For general information on CernVM-FS cache settings, [see the CernVM-FS
documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#cache-settings).


### Loopback on shared filesystem {: #loopback-filesystem }

The generally recommended solution for diskless worker nodes is to use a [*loopback
filesystem*](https://en.wikipedia.org/wiki/Loop_device) for the CernVM-FS client
cache, which can be stored on the cluster's shared filesystem of the HPC cluster.
Every worker node will need its own file in this case.

This ensures that the parallelism of the shared file system can be exploited, while metadata accesses are performed
within the loopback filesystems, and hence not overloading the shared filesystem's metadata server(s).

The loopback filesystem files can be created using `dd` or `mkfs`. They should be formatted as an `ext3`, `ext4`,
or `xfs` file system, and should be 15% larger than the cache size configured on the nodes (with `CVMFS_QUOTA_LIMIT`).

On the worker nodes the loopback filesystem can be mounted from the shared file system, and they should be made
available at the location specified in the `CVMFS_CACHE_BASE` configuration setting (or `/var/lib/cvmfs`, by default).

### Alien cache {: #alien-cache-diskless }

An *alien cache* is a cache that is outside of the (full) control of CernVM-FS.

In this scenario you store the cache on a shared filesystem, and have the CernVM-FS processes on all worker nodes
use and fill it simultaneously. These processes can pull in the required files that are being accessed by users/jobs,
or you can even manually [*preload* the cache](https://cvmfs.readthedocs.io/en/stable/cpt-hpc.html#preloading-the-cernvm-fs-cache).

Using the alien cache still requires a very small local cache on the worker nodes for storing some control files.
Given its size, you can store this local cache on a shared filesystem, or [in memory](#in-memory-cache).

Compared to using a loopback filesystem described in the previous subsection, the drawback of storing the alien cache
on your shared filesystem is that all metadata operations are now performed on the shared filesystem.
Typically, this will result in a large number of metadata operations, and on many shared filesystems will be a significant bottleneck.

For more information about an alien cache and configuring it, see the [Alien Cache
section](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#alien-cache) in the CernVM-FS documentation.


## Offline worker nodes

Another typical scenario for HPC systems is that worker nodes do not have (direct) access to the internet.

In the context of CernVM-FS, this means that the clients running on the worker nodes are not be able to pull in files
from (external) Stratum 1 replica servers.

For this scenario, several solutions are available as well:

* [Squid proxy in local network](#squid-local)
* [Private Stratum 1 replica server](#private-stratum1)
* [Alien cache](#alien-cache-offline)

### Squid proxy in local network {: #squid-local }

Setting up a [Squid proxy server](access/proxy.md) in the internal network of the cluster, which is highly recommended regardless of whether
the worker nodes are offline or not, will circumvent this issue since the worker nodes can be configured to only connect
to Stratum 1 servers via the Squid proxy.

This means that only the Squid proxy server requires internet access in order to fetch files from the Stratum 1 servers,
while the clients will fetch the files from the proxy using the internal network.

### Private Stratum 1 replica server {: #private-stratum1 }

Similar to having a Squid proxy in the internal network of the cluster, one could also opt for setting up a [private
Stratum 1 replica server](access/stratum1.md) that is accessible by the worker nodes, or even do both.

Again, only the private Stratum 1 server needs to connect to the internet, as it will need to regularly synchronize
with a [synchronisation server](http://127.0.0.1:8000/access/stratum1/#synchronisation-server).


### Alien cache {: #alien-cache-offline }

As a last resort, you can consider use an [alien cache](#alien-cache-diskless) that is being prepopulated
on a dedicated system outside of the HPC, which does have internet access.

This alien cache can then be made available on the worker nodes, for instance by having it stored on the shared filesystem of the cluster.

This is (again) not recommended however, for the same reason as before: this kind of setup will put significant load
on the metadata server(s) of the shared filesystem.



## Worker nodes without CernVM-FS

The last scenario that we cover here is for HPC systems that do not have the CernVM-FS client component
installed on the worker nodes, for example because the system administrators are not willing to install,
configure, and maintain a CernVM-FS installation.

Though less ideal than a native installation of CernVM-FS, solutions to make CernVM-FS repositories accessible
even in this case exist:

* [Syncing a to another filesystem](#sync-other-filesystem)
* [Alternative access mechanisms](#alternatives)

### Syncing a to another filesystem {: #sync-other-filesystem }

A seemingly straightforward solution may be to synchronize (a part of) the contents of a CernVM-FS repository to
another filesystem, and make that available on worker nodes.

CernVM-FS provides the [`cvmfs_shrinkwrap` utility](https://cvmfs.readthedocs.io/en/stable/cpt-shrinkwrap.html)
exactly for this purpose.

However, though the solution may sound easy, it has some severe disadvantages: `cvmfs_shrinkwrap` utility puts a
heavy load on the server that is being used to pull in the contents, as it has to fetch all the contents
(which may be a large amount of data) in one large bulk operation.

In addition, the repository contents will have to be synchronized in some way, which involves rerunning this process
regularly.

Finally, this approach somewhat defeats the purpose of CernVM-FS, as you will be replacing a filesystem that is optimized for distributing software by one that most likely is not.

### Alternative access mechanisms {: #alternatives }

Alternative mechanisms to access CernVM-FS repositories exist that do not require system administrator privileges,
so they can be leveraged by end users of HPC infrastructure.

Examples include using a container runtime like [Apptainer](https://apptainer.org),
or using [`cvmfsexec`](https://github.com/cvmfs/cvmfsexec).

For more details on these alternatives, see [Alternative ways to access CernVM-FS repositories](access/alternatives.md).

!!! note "Parrot connector to CernVM-FS"

    While [Parrot](https://ccl.cse.nd.edu/software/parrot) is still mentioned in the CernVM-FS documentation
    (see [here](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#parrot-connector-to-cernvm-fs)),
    it is no longer recommended to use it, since better alternatives (like `cvmfsexec`) are available now.

---

*(next: [Troubleshooting for CernVM-FS repositories](troubleshooting.md))*
