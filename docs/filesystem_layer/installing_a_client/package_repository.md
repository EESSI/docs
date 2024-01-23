# Option 2: Package repository


We have a yum repository where you can install the configuration package from. If you opt for this
solution you will get automatic updates. To configure your client using this option, run the
following commands:

```
sudo yum -y install http://repo.eessi-infra.org/eessi/rhel/8/noarch/eessi-release-0-1.noarch.rpm
sudo yum check-update
sudo yum -y install cvmfs-config-eessi
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

