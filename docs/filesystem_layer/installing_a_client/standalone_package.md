# Option 1: Standalone package

On many operating systems the CVMFS client can be installed through your package manager. For
details for your OS/Distro, see the [Getting Started
page](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html) in the CVMFS documentation.

After installing the client, you will have to configure it. For this you can use the CVMFS
configuration packages that we provide for clients. These packages can be found on the
[Releases](https://github.com/eessi/filesystem-layer/releases) page. Download the package for your
operating system, and install it, e.g.:

```bash
rpm -i cvmfs-config-eessi-*.rpm
dpkg -i cvmfs-config-eessi-*.deb
```

Next, you need to make a file `/etc/cvmfs/default.local` manually; this file is used for local
settings and contains, for instance, the URL to your local proxy and the size of the local cache. As
an example, you can put the following in this file, which corresponds to not using a proxy and
setting the local quota limit to 40000MB:

```bash
CVMFS_CLIENT_PROFILE=single
CVMFS_QUOTA_LIMIT=40000
```

If you do want to use your own proxy, replace the first line by:

```bash
CVMFS_HTTP_PROXY=<hostname of your proxy>:<port>
```

For more details about configuring your client, see the CVMFS documentation on [`client
configuration`](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html).

Finally, run `cvmfs_config setup` to set up CVMFS.

