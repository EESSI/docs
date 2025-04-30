!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Squid proxy server

As a first step towards a production-ready CernVM-FS setup
we can install a [Squid forward proxy server](http://www.squid-cache.org),
which is strongly recommended in the context of HPC systems.

The proxy server will (often dramatically) **reduce the latency** for client systems for accessing CernVM-FS repositories,
and hence **significantly improve start-up performance** of software provided via CernVM-FS.
In addition, it reduces the load on the Stratum 1 replica servers that
support the repositories being used.

This is particularly important when running large-scale [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface)
software, since the software binary and all the libraries it requires must be available on *all* worker nodes being
employed before the software can start running.

## General recommendations

The proxy server should have a 10Gbit link to the client systems,
a sufficiently powerful CPU, a decent amount of memory for the kernel cache (tens of GBs),
and fast local storage (SSD or NVMe).

It is strongly recommended to have **at least two proxy servers** available,
to have some redundancy available in case of unexpected problems, or during a maintenance window.

As a rule of thumb, it is recommended to have (at least) *one proxy server for every couple
of hundred worker nodes* (100-500).

Note that the load on the proxy servers used by CernVM-FS is highly dependent on the workload mix on the client systems.

## Proxy server setup

### Installation

First, install the `squid` package using your OS package manager:

=== "For RHEL-based Linux distros (incl. CentOS, Rocky, Fedora, ...)"

    ``` { .bash .copy }
    sudo yum install -y squid
    ```

=== "For Debian-based Linux distros (incl. Ubuntu)"

    ``` { .bash .copy }
    sudo apt install -y squid
    ```

### Configuration

Create a configuration file for the Squid proxy in `/etc/squid/squid.conf`.

You can use the following template for this:

```{ .apache .copy }
# List of local IP addresses (separate IPs and/or CIDR notation) allowed to access your local proxy
acl local_nodes src YOUR_CLIENT_IPS

# Destination domains that are allowed
acl stratum_ones dstdomain .YOURDOMAIN.ORG

# Squid port
http_port 3128

# Deny access to anything which is not part of our stratum_ones ACL.
http_access deny !stratum_ones

# Only allow access from our local machines
http_access allow local_nodes
http_access allow localhost

# Finally, deny all other access to this proxy
http_access deny all

minimum_expiry_time 0
maximum_object_size 1024 MB

# proxy memory cache of 1GB
cache_mem 1024 MB
maximum_object_size_in_memory 128 KB
# 50 GB disk cache
cache_dir ufs /var/spool/squid 50000 16 256
```

In this template, you *must* change two things in the Access Control List (ACL) settings:

1) Specify which client systems can access your proxy by replacing "`YOUR_CLIENT_IPS`" with the corresponding IP range, using [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation);

2) Make sure that the proxy server allows access to the Stratum 1 replica servers that are relevant for the CernVM-FS repositories
   you are using, by replacing "`.YOURDOMAIN.ORG`" with domain name for the Stratum 1 replica servers
   (see also the [Squid ACL documentation](http://www.squid-cache.org/Doc/config/acl/)).

For example, to allow connecting to the EESSI Stratum 1 replica servers, use:

```{ .apache .copy }
acl stratum_ones dstdomain .eessi.science
```

Note that this configuration assumes that port 3128 is accessible on the proxy server.

To check your Squid configuration, use:

```{ .bash .copy }
sudo squid -k parse
```

If no warnings or errors are printed by this command, you should be all set (assuming that the ACLs are set correctly).

For more information on configuring a Squid proxy, [see the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-squid.html),

### Starting the service

To start the Squid and enable it on booting the proxy server, run:

```{ .bash .copy }
sudo systemctl start squid
sudo systemctl enable squid
```

To check the status of the Squid, you can use:

```{ .bash .copy }
sudo systemctl status squid
```

## Client system configuration

To make a CernVM-FS client system use the proxy server,
the `/etc/cvmfs/default.local` configuration file *on the client system* should be updated to include:

```{ .ini .copy }
# replace PROXY_IP with the IP address of the proxy server
CVMFS_HTTP_PROXY="http://PROXY_IP:3128"
```

To apply the change we need to reload the CernVM-FS configuration on the client system:

```{ .bash .copy }
sudo cvmfs_config reload
```

You can test the new configuration and verify whether the proxy is indeed being used
by the client system via `cvmfs_config stat`:

```{ .bash .copy }
ls /cvmfs/software.eessi.io
cvmfs_config stat -v software.eessi.io
```

We first inspect the contents of the repository using `ls` to make sure that the repository is mounted,
which is assumed by `cvmfs_config stat`.

The output of the `stat` command should look something like this:

Note the `Connection` line, which clearly shows that the proxy server is used (and is working):

```
Connection: .../software.eessi.io through proxy http://PROXY_IP:3128 (online)
```

To check whether the proxy is working as intended you can use `curl` to try to access
the `.cvmfspublished` file in the root of the repository on a Stratum 1, for example:

```{ .bash .copy }
# replace PROXY_IP with the IP address of the proxy server
http_proxy=http://PROXY_IP:3128 curl --head http://aws-eu-central-s1.eessi.science/cvmfs/software.eessi.io/.cvmfspublished
```

The first output line of this command should be:

```
HTTP/1.1 200 OK
```

## Cleanup to prepare for Stratum 1 {: #cleanup_proxy }

To prepare for the next tutorial section on [setting up a private Stratum 1 replica server](stratum1.md),
comment out the `CVMFS_HTTP_PROXY` line in `/etc/cvmfs/default.local` by prefixing it with a hash (`#`):

``` { .ini .copy }
#CVMFS_HTTP_PROXY="http://PROXY_IP:3128"
```

The full contents of `/etc/cvmfs/default.local` on the client system should again be as shown below, like it was initially created when
[configuring the client](client.md##minimal_configuration):

``` { .ini .copy }
CVMFS_CLIENT_PROFILE="single"
CVMFS_QUOTA_LIMIT=10000
```

Do not forget to also reload the CernVM-FS client configuration:
```{ .bash .copy }
sudo cvmfs_config reload
```

We will later reconfigure the proxy server so it can be used together with our private Stratum 1.

---

*(next: [Setting up a Stratum 1 replica server](stratum1.md))*
