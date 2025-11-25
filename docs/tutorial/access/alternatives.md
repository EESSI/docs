!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Alternative ways to access CernVM-FS repositories

While a [native installation of CernVM-FS on the client system](client.md),
along with a [proxy server](proxy.md) and/or [Stratum 1 replica server](stratum1.md) for large-scale production setups,
is recommended, there are other alternatives available for getting access to CernVM-FS repositories.

We briefly cover some of these here, mostly to clarify that there are alternatives available,
including some that do not require system administrator permissions.

## `cvmfsexec`

Using [`cvmfsexec`](https://github.com/cvmfs/cvmfsexec), mounting of CernVM-FS repositories as
an unprivileged user is possible, without having CernVM-FS installed system-wide.

`cvmfsexec` supports multiple ways of doing this depending on the OS version and system configuration,
more specifically whether or not particular features are enabled, like:

* [FUSE mounting](https://www.kernel.org/doc/html/latest/filesystems/fuse.html) with `fusermount`;
* unprivileged user namespaces;
* unprivileged namespace fuse mounts;
* a `setuid` installation of Singularity 3.4+ (via `singcvmfs` which uses the `--fusemount` feature),
  or an unprivileged installation of Singularity 3.6+;

Start by cloning the `cvmfsexec` repository from GitHub, and change to the `cvmfsexec` directory:

```
git clone https://github.com/cvmfs/cvmfsexec.git
cd cvmfsexec
```

Before using `cvmfsexec`, you first need to make a `dist` directory that includes CernVM-FS, configuration files,
and scripts. For this, you can run the `makedist` script that comes with `cvmfsexec`:

```
./makedist default
```

With the `dist` directory in place, you can use `cvmfsexec` to run commands in an environment
where a CernVM-FS repository is mounted.

For example, we can run a script named `test_eessi.sh` that contains:

```shell
#!/bin/bash

source /cvmfs/software.eessi.io/versions/2023.06/init/bash

module load TensorFlow/2.13.0-foss-2023a

python -V
python3 -c 'import tensorflow as tf; print(tf.__version__)'
```

which gives:
```
$ ./cvmfsexec software.eessi.io -- ./test_eessi.sh

CernVM-FS: loading Fuse module... done
CernVM-FS: mounted cvmfs on /home/rocky/cvmfsexec/dist/cvmfs/cvmfs-config.cern.ch
CernVM-FS: loading Fuse module... done
CernVM-FS: mounted cvmfs on /home/rocky/cvmfsexec/dist/cvmfs/software.eessi.io

Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
archdetect says x86_64/amd/zen2
Using x86_64/amd/zen2 as software subdirectory.
Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Environment set up to use EESSI (2023.06), have fun!

Python 3.11.3
2.13.0
```

By default, the CernVM-FS client cache directory will be located in `dist/var/lib/cvmfs`.

For more information on `cvmfsexec`, see <https://github.com/cvmfs/cvmfsexec>.


## Apptainer with `--fusemount`

If [Apptainer](https://apptainer.org) is available, you can get access to a CernVM-FS repository
by using a container image that includes the CernVM-FS client component (see for example the Docker recipe
for the client container used in EESSI, which is available [here](https://github.com/EESSI/filesystem-layer/blob/main/containers/Dockerfile.EESSI-client-centos7)).

Using the `--fusemount` option you can specify that a CernVM-FS repository should be mounted
when starting the container. For example for [EESSI](../eessi/high-level-design.md#filesystem_layer),
you should use:

```bash
apptainer ... --fusemount "container:cvmfs2 software.eessi.io /cvmfs/software.eessi.io" ...
```

There are a couple of caveats here:

* If the configuration for the CernVM-FS repository is provided via the `cvmfs-config` repository,
  you need to instruct Apptainer to also mount that, by using the `--fusemount` option twice: once for
  the `cvmfs-config` repository, and once for the target repository itself:
  ```bash
  FUSEMOUNT_CVMFS_CONFIG="container:cvmfs2 cvmfs-config.cern.ch /cvmfs/cvmfs-config.cern.ch"
  FUSEMOUNT_EESSI="container:cvmfs2 software.eessi.io /cvmfs/software.eessi.io"
  apptainer ... --fusemount "${FUSEMOUNT_CVMFS_CONFIG}" --fusemount "${FUSEMOUNT_EESSI}" ...
  ```

* Next to mounting CernVM-FS repositories, you also need to *bind mount* local writable directories
  to `/var/run/cvmfs`, since CernVM-FS needs write access in those locations (for the CernVM-FS client cache):
  ```bash
  mkdir -p /tmp/$USER/{var-lib-cvmfs,var-run-cvmfs}
  export APPTAINER_BIND="/tmp/$USER/var-run-cvmfs:/var/run/cvmfs,/tmp/$USER/var-lib-cvmfs:/var/lib/cvmfs"
  apptainer ... --fusemount ...
  ```

To try this, you can use the EESSI client container that is available in Docker Hub,
to start an interactive shell in which EESSI is available, as follows:

```{ .bash .copy }
mkdir -p /tmp/$USER/{var-lib-cvmfs,var-run-cvmfs}
export APPTAINER_BIND="/tmp/$USER/var-run-cvmfs:/var/run/cvmfs,/tmp/$USER/var-lib-cvmfs:/var/lib/cvmfs"
FUSEMOUNT_CVMFS_CONFIG="container:cvmfs2 cvmfs-config.cern.ch /cvmfs/cvmfs-config.cern.ch"
FUSEMOUNT_EESSI="container:cvmfs2 software.eessi.io /cvmfs/software.eessi.io"
apptainer shell --fusemount "${FUSEMOUNT_CVMFS_CONFIG}" --fusemount "${FUSEMOUNT_EESSI}" docker://ghcr.io/eessi/client:rocky8
```

## Alien cache

An alien cache can be used, optionally in combination with preloading, as another alternative,
typically in combination with using a container image or unprivileged user namespaces.

For more information, see the [Alien cache subsection](../configuration_hpc.md#alien-cache-diskless) in the next part of the
tutorial.

---

*(next: [Configuration on HPC systems](../configuration_hpc.md))*
