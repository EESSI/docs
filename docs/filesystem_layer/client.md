# Configuring a client

The EESSI repository is made available through the CernVM-FS client.
We support three methods for installing, running and configuring the CernVM-FS client
on a computer:

1. manual installation using your distribution's package manager;
2. automated installation using a Ansible playbook;
3. running a fully prepared Singularity container.

## Option 1: manual installation

The installation procedure of the CVMFS client is very well described on the
[Getting Started page of the CVMFS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html).

You can simply follow the steps on that page up to the
[Verify the file system](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html#verify-the-file-system) section.

!!! info
    In the section that instructs you to create `default.local` file, use `CVMFS_REPOSITORIES=pilot.eessi-hpc.org`.

    The default limit for the cache directory that CVMFS will be using on the client machine is set to 4GB.
    If you want to override this, add `CVMFS_QUOTA_LIMIT=<value in megabytes>` to your `default.local`.

    The default location for the cache directory is `/var/lib/cvmfs`. Please, check that the partition on which this
    directory is stored is big enough to store the cache (and other data). You may override this by adding
    `CVMFS_CACHE_BASE=<some other directory for the cache>` to your `default.local`.

!!! warning
    Do **not** set `CVMFS_CLIENT_PROFILE=single` in your `default.local` if you are setting up multiple clients, e.g. on a cluster.
    In this case you should first set up one or more proxies, and then use `CVMFS_HTTP_PROXY` as described.

Before you can run the `probe` command from the
[Verify the file system](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html#verify-the-file-system) section,
you will first have to install the EESSI-specific CVMFS configuration.
You can find packages that are suitable for different operating systems and Linux distributions on the
[Filesystem Layer releases page](https://github.com/EESSI/filesystem-layer/releases/).
The latest version can always be found at [the release page of the moving `latest` tag](https://github.com/EESSI/filesystem-layer/releases/tag/latest).

After you have installed an appropriate package, you should be able to mount the repository by running:
```
cvmfs_config probe pilot.eessi-hpc.org
```


## Option 2: Ansible playbook


## Option 3: Singularity container

