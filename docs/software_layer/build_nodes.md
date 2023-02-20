# Build nodes

Any system can be used as a build node to create additional software installations that should be
added to the EESSI CernVM-FS repository.

## Requirements

OS and software:

* GNU/Linux (any distribution) as operating system;
* a recent version of [Singularity](https://sylabs.io/singularity/) (>= 3.6 is recommended);
    * check with ``singularity --version``
* ``screen`` or ``tmux`` is highly recommended;

Admin privileges are ***not*** required, as long as Singularity is installed.

Resources:

* 8 or more cores is recommended (though not strictly required);
* at least 50GB of free space on a local filesystem (like `/tmp`);
* at least 16GB of memory (2GB/core or higher recommended);

Instructions to install Singularity and screen (click to show commands):

??? note "CentOS 8 (`x86_64` or `aarch64` or `ppc64le`)"
    ```
    sudo dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    sudo dnf update -y
    sudo dnf install -y screen singularity
    ```

## Setting up the container

!!! warning
    **It is highly recommended to start a `screen` or `tmux` session first!**

A container image is provided that includes everything that is required to set up a writable overlay
on top of the EESSI CernVM-FS repository.

First, pick a location on a local filesystem for the temporary directory:

Requirements:

* **Do not use a shared filesystem** like NFS, Lustre or GPFS.
* There should be **at least 50GB of free disk space** in this local filesystem (more is better).
* There should be **no automatic cleanup of old files** via a cron job on this local filesystem.
* Try to make sure the directory is unique (not used by anything else).

NB.
If you are going to install on a separate drive (due to lack of space on /), then you need to set some variables to 
point to that location. You will also need to bind mount it in the `singularity` command. Let's say that you drive is 
mounted in /srt. Then you change the relevant commands below to this:
```shell
export EESSI_TMPDIR=/srt/$USER/EESSI
mkdir -p $EESSI_TMPDIR
mkdir /srt/tmp
export SINGULARITY_BIND="$EESSI_TMPDIR/var-run-cvmfs:/var/run/cvmfs,$EESSI_TMPDIR/var-lib-cvmfs:/var/lib/cvmfs,/srt/tmp:/tmp"
singularity shell -B /srt --fusemount "$EESSI_PILOT_READONLY" --fusemount "$EESSI_PILOT_WRITABLE_OVERLAY" docker://ghcr.io/eessi/build-node:debian10
```

We will assume that `/tmp/$USER/EESSI` meets these requirements:

```shell
export EESSI_TMPDIR=/tmp/$USER/EESSI
mkdir -p $EESSI_TMPDIR
```

Create some subdirectories in this temporary directory:

```shell
mkdir -p $EESSI_TMPDIR/{home,overlay-upper,overlay-work}
mkdir -p $EESSI_TMPDIR/{var-lib-cvmfs,var-run-cvmfs}
```

Configure Singularity cache directory, bind mounts, and (fake) home directory:

```shell
export SINGULARITY_CACHEDIR=$EESSI_TMPDIR/singularity_cache
export SINGULARITY_BIND="$EESSI_TMPDIR/var-run-cvmfs:/var/run/cvmfs,$EESSI_TMPDIR/var-lib-cvmfs:/var/lib/cvmfs"
export SINGULARITY_HOME="$EESSI_TMPDIR/home:/home/$USER"
```

Define values to pass to ``--fusemount` in ``singularity`` command:

```shell
export EESSI_PILOT_READONLY="container:cvmfs2 pilot.eessi-hpc.org /cvmfs_ro/pilot.eessi-hpc.org"
export EESSI_PILOT_WRITABLE_OVERLAY="container:fuse-overlayfs -o lowerdir=/cvmfs_ro/pilot.eessi-hpc.org -o upperdir=$EESSI_TMPDIR/overlay-upper -o workdir=$EESSI_TMPDIR/overlay-work /cvmfs/pilot.eessi-hpc.org"
```

Start the container (which includes Debian 10, [CernVM-FS](https://cernvm.cern.ch/fs/) and
[fuse-overlayfs](https://github.com/containers/fuse-overlayfs)):

```shell
singularity shell --fusemount "$EESSI_PILOT_READONLY" --fusemount "$EESSI_PILOT_WRITABLE_OVERLAY" docker://ghcr.io/eessi/build-node:debian10
```

Once the container image has been downloaded and converted to a Singularity image (SIF format),
you should get a prompt like this:

```
...
CernVM-FS: loading Fuse module... done

Singularity>
```

and the EESSI CernVM-FS repository should be mounted:

```
Singularity> ls /cvmfs/pilot.eessi-hpc.org
2020.12  2021.03  latest
```

## Setting up the environment

Set up the environment by starting a Gentoo Prefix session using the ``startprefix`` command.

**Make sure you use the correct version of the EESSI pilot repository!**

```shell
export EESSI_PILOT_VERSION='2021.03'
/cvmfs/pilot.eessi-hpc.org/${EESSI_PILOT_VERSION}/compat/linux/$(uname -m)/startprefix
```

## Installing software

Clone the [software-layer](https://github.com/EESSI/software-layer) repository:

```shell
git clone https://github.com/EESSI/software-layer.git
```

Run the software installation script in `software-layer`:

```shell
cd software-layer
./EESSI-pilot-install-software.sh
```

This script will figure out the CPU microarchitecture of the host automatically (like `x86_64/intel/haswell`).

To build generic software installations (like `x86_64/generic`), use the ``--generic`` option:

```shell
./EESSI-pilot-install-software.sh --generic
```

Once all missing software has been installed, you should see a message like this:

```
No missing modules!
```

## Creating tarball to ingest

Before tearing down the build node, you should create tarball to ingest into the EESSI CernVM-FS repository.

To create a tarball of *all* installations, assuming your build host is ``x86_64/intel/haswell``:

```shell
export EESSI_PILOT_VERSION='2021.03'
cd /cvmfs/pilot.eessi-hpc.org/${EESSI_PILOT_VERSION}/software/linux
eessi_tar_gz="$HOME/eessi-${EESSI_PILOT_VERSION}-haswell.tar.gz"
tar cvfz ${eessi_tar_gz} x86_64/intel/haswell
```

To create a tarball for specific installations, make sure you pick up both
the software installation directories and the corresponding module files:

```shell
eessi_tar_gz="$HOME/eessi-${EESSI_PILOT_VERSION}-haswell-OpenFOAM.tar.gz"
tar cvfz ${eessi_tar_gz} x86_64/intel/haswell/software/OpenFOAM modules/all//OpenFOAM
```

This tarball should be uploaded to the Stratum 0 server for ingestion.
If needed, you can ask for help in the
[EESSI `#software-layer` Slack channel](https://eessi-hpc.slack.com/archives/CNMM6G2RG)
