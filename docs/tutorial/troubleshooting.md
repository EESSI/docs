!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Troubleshooting for CernVM-FS

When you experience problems with getting access to a CernVM-FS repository,
it can be tricky to figure out what the actual underlying cause is,
given the complexity of a typical CernVM-FS setup.

In this section we provide some guidelines on how to troubleshoot some potential problems
you may run into with CernVM-FS.
We focus on client-side issues: problems that may arise on a CernVM-FS client system itself,
or with the connection to external servers like a [Squid proxy](appendix/terminology.md#proxy)
or a [Stratum 1 replica server](appendix/terminology.md#stratum1).

While some commands suggested below that can help to determine the actual problem at hand
require system administrator privileges (indicated with the use of `sudo`),
several can also be run as an unprivileged user.

<p align="center">
<img src="../img/off_and_on.png" alt="Have you tried turning it off and on again?" width="60%"/></br>
</p>

!!! note

    In this section, we will continue to use the [EESSI CernVM-FS repository `software.eessi.io`](
    eessi/high-level-design.md#filesystem_layer) as a running example, but the troubleshooting guidelines
    are by no means specific to EESSI.

    Make sure you adjust the example commands to the CernVM-FS repository you are using, if needed.


## Typical problems

### Error messages

The error messages that you may encounter when accessing a CernVM-FS repository
are often quite cryptic, especially if you are not very familiar with CernVM-FS, or with
file systems and networking on Linux systems in general.

Here are a couple of examples:

* The CernVM-FS repository may not be known (yet) on your system, which will result
  in a (clear) error message like this when you try to access it:
  ```
  $ ls /cvmfs/software.eessi.io
  ls: cannot access '/cvmfs/software.eessi.io': No such file or directory
  ```
  
* You may see errors messages that suggest network connectivity problems, like:
  ```
  Failed to discover HTTP proxy servers (23 - proxy auto-discovery failed)
  ```

* Other problems may be quite specific to the internals of CernVM-FS,
  rather than being configuration or networking issues. Examples include:
  ```
  Failed to initialize root file catalog (16 - file catalog failure)
  ```
  ```
  Failed to transfer ownership of /var/lib/cvmfs/shared to cvmfs
  ```
  ```
  ls: cannot open directory '/cvmfs/config-repo.cern.ch': Too many levels of symbolic links
  ```
  ```
  Transport endpoint is not connected
  ```
  The last error message indicates that [FUSE](https://www.kernel.org/doc/html/latest/filesystems/fuse.html) has failed.

  We will give some advice below on how you might figure out what is wrong when seeing error messages like this.

### Lag and/or hangs

When you notice lag of even (perceived) hanging when accessing a CernVM-FS repository,
you should consider revising the [connectivity](#connectivity)- and [cache](#caching)-related configuration settings.


## General approach

In general, it is recommended to take a step-by-step approach to troubleshooting:

* Start with verifying the CernVM-FS (client) [installation](#installation);
* Review the CernVM-FS [configuration](#configuration);
* Consider potential [network connectivity](#connectivity) issues;
* Keep an eye out for [mounting](#mounting) problems;
* Make sure you have sufficient available [resources](#resources) like memory and local disk space;
* Rule out any [cache](#caching)-related shenanigans;

Always keep in mind to [check the logs](#logs), and also consider to employ the [other tools](#other-tools)
that we put forward.


## Common problems

### CernVM-FS installation {: #installation }

Make sure that CernVM-FS is actually installed (correctly).

Check whether both the `/cvmfs` directory and the `cvmfs` service account exists on the system:
```{ .bash .copy }
ls /cvmfs
id cvmfs
```

Either of these errors would be a clear indication that CernVM-FS is not installed,
or that the [installation was not completed](access/client.md#completing-the-client-setup):
```
ls: cannot access '/cvmfs': No such file or directory
```
```
id: ‘cvmfs’: no such user
```

You can also check whether the `cvmfs2` command is available, and working:

``` { .bash .copy }
cvmfs2 --help
```

which should produce output that starts with:

```
The CernVM File System
Version 2.11.2
```

In case of problems, revise the section on
[installing the CernVM-FS client](access/client.md#installing-cernvm-fs-client).


### CernVM-FS configuration {: #configuration }

A common issue is incorrectly configuring CernVM-FS, either by making a silly mistake in a configuration file,
or by not taking into account the [hierarchy of configuration files](access/client.md#configuration_hierarchy)
that CernVM-FS considers.

#### Reloading

Don't forget to reload the CernVM-FS configuration after you've made changes to it:

``` { .bash .copy }
sudo cvmfs_config reload
```

Note that changes to specific configuration settings, in particular those related to FUSE,
will not be reloaded with this command, since they require remounting the repository.

#### Show configuration

Verify the configuration via `cvmfs_config showconfig`:

``` { .bash .copy }
cvmfs_config showconfig software.eessi.io
```

Using the `-s` option, you can trim the output to only show non-empty configuration settings:
``` { .bash .copy }
cvmfs_config showconfig -s software.eessi.io
```

We strongly advise combining this command with `grep` to check for specific configuration settings, like:

```
$ cvmfs_config showconfig software.eessi.io | grep CVMFS_SERVER_URL
CVMFS_SERVER_URL='http://aws-eu-central-s1.eessi.science/cvmfs/software.eessi.io;http://azure-us-east-s1.eessi.science/cvmfs/software.eessi.io'    # from /cvmfs/cvmfs-config.cern.ch/etc/cvmfs/domain.d/eessi.io.conf
```

Be aware that `cvmfs_config showconfig` will read the configuration files as they are currently,
but that does not necessarily mean that those configuration settings are currently active;
see also [reloading](#reloading).

#### Non-existing repositories

Keep in mind that `cvmfs_config` does *not* check whether the specified
repository is actually known at all. Try for example querying the configuration
for the fictional `vim.or.emacs.io` repository:

``` { .bash .copy }
cvmfs_config showconfig vim.or.emacs.io
```

#### Inspect *active* configuration {: #active_configuration }

Inspect the *active* configuration that is currently used by *talking* to the running CernVM-FS service
via `cvmfs_talk`.

!!! note
    This requires that the specified CernVM-FS repository is currently mounted.

``` { .bash .copy }
ls /cvmfs/software.eessi.io > /dev/null  # to trigger mount if not mounted yet
sudo cvmfs_talk -i software.eessi.io parameters
```

`cvmfs_talk` can also be used to query other live aspects of a particular repository,
see the output of `cvmfs_talk --help`. For example:

* The current revision of repository contents (via `revision`);
* Information on the Stratum 1 replica server being used (via `host ...`);
* Information on the proxy server being used (via `proxy ...`);
* Information on the CernVM-FS client cache (via `cache ...`);

#### Non-mounted repositories

If running `cvmfs_talk` fails with an error like "`Seems like CernVM-FS is not running`",
try triggering a mount of the repository first by accessing it (with `ls`), or by running:

``` { .bash .copy }
cvmfs_config probe software.eessi.io
```

If the latter succeeds but accessing the repository does not,
there may be an issue with the (active) configuration,
or there may be a [connectivity problem](#connectivity).

#### Repository public key

In order for CernVM-FS to access a repository the corresponding *public key* must be available,
in a domain-specific subdirectory of `/etc/cvmfs/keys`, like:
```
$ ls /etc/cvmfs/keys/cern.ch
cern-it1.cern.ch.pub  cern-it4.cern.ch.pub  cern-it5.cern.ch.pub
```

or in the active CernVM-FS config repository, like for EESSI:

```
$ ls /cvmfs/cvmfs-config.cern.ch/etc/cvmfs/keys/eessi.io
eessi.io.pub
```

### Connectivity issues {: #connectivity }

There could be various issues related to network connectivity,
for example a [*firewall*](https://en.wikipedia.org/wiki/Firewall_(computing)) blocking connections.

CernVM-FS uses plain `HTTP` as data transfer protocol, so basic tools can be used to investigate
connectivity issues.

You should make sure that the client system can connect to the Squid proxy and/or Stratum-1 replica server(s)
via the required ports.

#### Determine proxy server {: #determine_proxy }

First figure out if a [proxy server](appendix/terminology.md#proxy) is being used via:
``` { .bash .copy }
sudo cvmfs_talk -i software.eessi.io proxy info
```

This should produce output that looks like:

```
Load-balance groups:
[0] http://PROXY_IP:3128 (PROXY_IP, +6h)
[1] DIRECT
Active proxy: [0] http://PROXY_IP:3128
```

(to protect the innocent, the actual proxy IP was replaced with "`PROXY_IP`" in the output above)

The last line indicates that a proxy server is indeed being used currently.

`DIRECT` would mean that *no* proxy server is being used.

#### Access to proxy server

If a proxy server is used, you should check whether it can be accessed at port `3128` (default Squid port).

For this, you can use standard networking tools (if available):

* `nc`, [ncat](https://nmap.org/ncat), a reimplementation of [netcat](https://sectools.org/tool/netcat):
  ```{ .bash .copy }
  nc -vz PROXY_IP 3128
  ```
* `telnet`:
  ```{ .bash .copy }
  telnet PROXY_IP 3128
  ```
* [`tcptraceroute`](https://linux.die.net/man/1/tcptraceroute):
  ```{ .bash .copy }
  sudo tcptraceroute PROXY_IP 3128
  ```

You will need to replace "`PROXY_IP`" in the commands above with the actual IP (or hostname) of the proxy
server being used.

#### Determine Stratum 1

Check which Stratum 1 servers are currently configured:

```{ .bash .copy }
cvmfs_config showconfig software.eessi.io | grep CVMFS_SERVER_URL
```

Determine which Stratum 1 is currently being *used* by CernVM-FS:

```
$ sudo cvmfs_talk -i software.eessi.io host info
  [0] http://aws-eu-central-s1.eessi.science/cvmfs/software.eessi.io (unprobed)
  [1] http://azure-us-east-s1.eessi.science/cvmfs/software.eessi.io (unprobed)
Active host 0: http://aws-eu-central-s1.eessi.science/cvmfs/software.eessi.io
```

In this case, the public Stratum 1 for EESSI in AWS `eu-central` is being used: `aws-eu-central-s1.eessi.science`.

#### Access to Stratum 1

If no proxy is being used (`CVMFS_HTTP_PROXY` is set to `DIRECT`, see also [above](#determine_proxy)),
you should check whether the active Stratum 1 is directly accessible at port `80`.

Again, you can use standard networking tools for this:

```{ .bash .copy }
nc -vz aws-eu-central-s1.eessi.science 80
```
```{ .bash .copy }
telnet aws-eu-central-s1.eessi.science 80
```
```{ .bash .copy }
sudo tcptraceroute aws-eu-central-s1.eessi.science 80
```

#### Download from Stratum 1

To see whether a Stratum 1 replica server can be used to download repository contents from,
you can use `curl` to check whether the `.cvmfspublished` file is accessible ( this file must exist in every repository ):

``` { .bash .copy }
S1_URL="http://aws-eu-central-s1.eessi.science"
curl --head ${S1_URL}/cvmfs/software.eessi.io/.cvmfspublished
```

If CernVM-FS is configured to use a proxy server, you should let `curl` use it too:
``` { .bash .copy }
P_URL="http://PROXY_IP:3128"
S1_URL="http://aws-eu-central-s1.eessi.science"
curl --proxy ${P_URL} --head ${S1_URL}/cvmfs/software.eessi.io/.cvmfspublished
```
or equivalently via the standard `http_proxy` environment variable that `curl` picks up on:
``` { .bash .copy }
S1_URL="http://aws-eu-central-s1.eessi.science"
http_proxy="PROXY_IP:3128" curl --head ${S1_URL}/cvmfs/software.eessi.io/.cvmfspublished
```

Make sure you replace "`PROXY_IP`" in the commands above with the actual IP (or hostname) of the proxy server.

If you see a `200` HTTP return code in the first line of output produced by `curl`, access is working as it should:

```
HTTP/1.1 200 OK
```

If you see `403` as return code, then something is blocking the connection:

```
HTTP/1.1 403 Forbidden
```

In this case, you should check whether a firewall is being used,
or whether an ACL in the [Squid proxy configuration](access/proxy.md#configuration) is the culprit.

If you see `404` as return code, you made a typo in the `curl` command :wink::
```
HTTP/1.1 404 Not Found
```
Maybe you forgot the '`.`' in `.cvmfspublished`?

!!! note

    A Stratum 1 server does not provide access to *all* possible CernVM-FS repositories.

    It has to be configured to serve particular repositories, as shown in [Private Stratum 1 replica server - Creating repository replica](access/stratum1.md#creating-repository-replica).

#### Network latency & bandwidth

To check the network latency and bandwidth, you can use [`iperf3`](https://iperf.fr/) and [`tcptraceroute`](https://linux.die.net/man/1/tcptraceroute),
see also [*Network details* in *System configurations* of the Performance section](
performance.md#system_configurations) of this tutorial.

### Mounting problems {: #mounting }

#### `autofs`

Keep in mind that (by default) CernVM-FS repositories are mounted [via `autofs`](access/client.md#autofs).

Hence, you should not rely on the output of `ls /cvmfs` to determine which repositories
can be accessed with your current configuration, since they may not be mounted currently.

You can check whether a specific repository is available by trying to access it directly:

```{ .bash .copy }
ls /cvmfs/software.eessi.io
```

#### Currently mounted repositories

To check which CernVM-FS repositories are currently mounted, run:
``` { .bash .copy }
cvmfs_config stat
```

#### Probing

To check whether a repository can be mounted, you can try to probe it:

```
$ cvmfs_config probe software.eessi.io
Probing /cvmfs/software.eessi.io... OK
```

#### Manual mounting

If you can not get access to a repository via auto-mounting by `autofs`,
you can try to manually mount it, since that may reveal specific error messages:

``` { .bash .copy }
mkdir -p /tmp/cvmfs/eessi
sudo mount -t cvmfs software.eessi.io /tmp/cvmfs/eessi
```

You can even try using the `cvmfs2` command directly to mount a repository:
``` { .bash .copy }
mkdir -p /tmp/cvmfs/eessi
sudo /usr/bin/cvmfs2 -d -f \
    -o rw,system_mount,fsname=cvmfs2,allow_other,grab_mountpoint,uid=$(id -u cvmfs),gid=$(id -g cvmfs),libfuse=3 \
    software.eessi.io /tmp/cvmfs/eessi
```
which prints lots of information for debugging (option `-d`).

### Insufficient resources {: #resources }

Keep in mind that the problems you observe may be the result of a shortage in resources,
for example:

* Lack of sufficient memory, for example for the kernel file system cache, which will typically
  lead to degrated (start-up) performance;
* Lack of sufficient disk space, for the CernVM-FS client cache, for the proxy server,
  or for the private Stratum 1 replica server;
* Network latency issues, either within the local network (to the proxy server or Stratum 1 replica server),
  or to the outside world (public Stratum 1 replica servers) &ndash; see also the [Connectivity](#connectivity)
  section;


### Caching woes {: #caching }

CernVM-FS assumes that the local cache directory is trustworthy.

Although unlikely, problems you are observing could be caused by some form
of corruption in the CernVM-FS client cache, for example due to problems
outside of the control of CernVM-FS (like a disk partition running full).

Even in the absence of problems it may still be interesting to inspect the contents
of the client cache, for example when trying to understand performance-related problems.

#### Checking cache usage

To check the current usage of the client cache across all repositories, you can use:

```{ .bash .copy }
cvmfs_config stat -v
```

You can get machine-readable output by *not* using the `-v` option (which is for getting human-readable output).

To only get information on cache usage for a particular repository, pass it as an extra argument:

```{ .bash .copy }
cvmfs_config stat -v software.eessi.io
```

To check overall cache size, use `du` on the cache directory (determined by `CVMFS_CACHE_BASE`):

```
$ sudo du -sh /var/lib/cvmfs
1.1G	/var/lib/cvmfs
```

#### Inspecting cache contents

To inspect which files are currently included in the client cache, run the following command:

``` { .bash .copy }
sudo cvmfs_talk -i software.eessi.io cache list
```

#### Checking cache consistency

To check the consistency of the CernVM-FS cache, use [`cvmfs_fsck`](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#cvmfs-fsck):
```{ .bash .copy }
sudo time cvmfs_fsck -j 8 /var/lib/cvmfs/shared
```

This will take a while, depending on the current size of the cache, and how many cores to use are specified (via the `-j` option).

#### Clearing client cache

To start afresh, you can clear the CernVM-FS client cache:
``` { .bash .copy }
sudo cvmfs_config wipecache
```

## Logs {: #logs }

By default CernVM-FS logs to [syslog](https://en.wikipedia.org/wiki/Syslog),
which usually corresponds to either `/var/log/messages` or `/var/log/syslog`.

Scanning these logs for messages produced by `cvmfs2` may help to determine the root cause of a problem.

### Debug log

For obtaining more detailed information, CernVM-FS provides the `CVMFS_DEBUGLOG` configuration setting:
``` { .bash .copy }
CVMFS_DEBUGLOG=/tmp/cvmfs-debug.log
```

CernVM-FS will log more information to the specified debug log file after [reloading the CernVM-FS
configuration](#reloading) (supported since CernVM-FS 2.11.0).

!!! warning "Debug logging is a bit like a firehose - use with care!"

    Note that with debug logging enabled *every* operation performed by CernVM-FS will be logged,
    which quickly generates large files and introduces a significant overhead,
    so it **should only be enabled temporarily** when trying to obtain more information on a particular problem.

!!! warning "Make sure that the debug log file is writable!"

    Make sure that the `cvmfs` user has write permission to the path specified in `CVMFS_DEBUGLOG`.

    If not, you will not only get no debug logging information, but it will also lead to *client failures*!

For more information on debug logging, [see the CernVM-FS documentation](
https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#debug-logs).

### Logs via extended attributes

An interesting source of information for mounted CernVM-FS repositories is the
[extended attributes](https://en.wikipedia.org/wiki/Extended_file_attributes)
that CernVM-FS uses, which can accessed via the `attr` command (see also [the CernVM-FS
documentation](https://cvmfs.readthedocs.io/en/stable/cpt-details.html#getxattr)).

In particular the `logbuffer` attribute, which contains the last log messages for that particular
repository, which **can be accessed without special privileges** that are required to access log messages
emitted to `/var/log/*`.

For example:
```
$ attr -g logbuffer /cvmfs/software.eessi.io
Attribute "logbuffer" had a 283 byte value for /cvmfs/software.eessi.io:
[3 Dec 2023 21:01:33 UTC] switching proxy from (none) to http://PROXY_IP:3128 (set proxies)
[3 Dec 2023 21:01:33 UTC] switching proxy from (none) to http://PROXY_IP:3128 (cloned)
[3 Dec 2023 21:01:33 UTC] switching proxy from http://PROXY_IP:3128 to DIRECT (set proxies)
```


## Other tools {: #other-tools }

### General check

To verify whether the basic setup is sound, run:
``` { .bash .copy }
sudo cvmfs_config chksetup
```
which should print "`OK`".

If something is wrong, it may report a problem like:

```
Warning: autofs service is not running
```

You can also use `cvmfs_config` to perform a status check, and verify that the
command has exit code zero:

```
$ sudo cvmfs_config status
$ echo $?
0
```


---

*(next: [Performance aspects of CernVM-FS](performance.md))*
