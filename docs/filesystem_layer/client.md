# Configuring a client

In order to mount the EESSI repository on a client machine,
you will have to install a CernVM-FS client and configure it to use the EESSI repository.

This can be done in several ways.
On this page we describe the following three methods:

- manual installation using your distribution's package manager;
- automated installation using a Ansible playbook;
- fully prepared Singularity container.


## Option 1: manual installation

The installation procedure of the CVMFS client is very well described on the
[Getting Started page of the CVMFS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html).

You can simply follow the steps on that page up to the
[Verify the file system](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html#verify-the-file-system) section.

!!! info
    In the section that instructs you to create `defaults.local` file, use `CVMFS_REPOSITORIES=pilot.eessi-hpc.org`.

    The default limit for the cache directory that CVMFS will be using on the client machine is set to 4GB.
    If you want to override this, add `CVMFS_QUOTA_LIMIT=<value in megabytes>` to your `defaults.local`.

!!! warning
    Do **not** set `CVMFS_CLIENT_PROFILE=single` in your `defaults.local` if you are setting up multiple clients, e.g. on a cluster.
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

