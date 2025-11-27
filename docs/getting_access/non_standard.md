# Non-standard ways to use EESSI

In case that an EESSI installation is not possible or desirable, there are a couple of "non-standard" ways to access EESSI.

## Using cvmfsexec

This option only works for [RHEL-like systems](https://github.com/cvmfs/cvmfsexec?tab=readme-ov-file#supported-operating-systems) and relies on the [cvmfsexec package](https://github.com/cvmfs/cvmfsexec) provided by CernVM-FS team. It will allow you to mount cvmfs as an unprivileged user, so no need to have a native cvmfs installation.

### `cvmfsexec_eessi.sh`  wrapper script


This wrapper script, `cvmfsexec_eessi.sh`, can be used to run a command in a subshell in which the EESSI CernVM-FS repository (`software.eessi.io`) is mounted via cvmfsexec`.

```bash
#!/bin/bash
if [ -d /cvmfs/software.eessi.io ]; then
    # run command directly, EESSI CernVM-FS repository is already mounted
    "$@"
else
    # run command via in subshell where EESSI CernVM-FS repository is mounted,
    # via cvmfsexec which is set up in a unique temporary directory
    orig_workdir=$(pwd)
    mkdir -p /tmp/$USER
    tmpdir=$(mktemp -p /tmp/$USER -d)
    cd $tmpdir
    git clone https://github.com/cvmfs/cvmfsexec.git > $tmpdir/git_clone.out 2>&1
    cd cvmfsexec
    ./makedist default > $tmpdir/cvmfsexec_makedist.out 2>&1
    cd $orig_workdir
    $tmpdir/cvmfsexec/cvmfsexec software.eessi.io -- "$@"
    # cleanup
    rm -rf $tmpdir
fi

```

Do make sure that this script is executable:

```bash
    chmod u+x ~/bin/cvmfsexec_eessi.sh
```

A simple way to test this script is to use it to inspect the contents of the EESSI repository:

```bash
    ~/bin/cvmfsexec_eessi.sh ls /cvmfs/software.eessi.io
```

or to start an interactive shell in which the EESSI repository is mounted:

```bash
    # Expected output from a machine without a cvmfs installation
    $ ls /cvmfs
    ls: cannot access '/cvmfs': No such file or directory

    # Starting interactive shell
    $ ~/bin/cvmfsexec_eessi.sh /bin/bash -l
    CernVM-FS: loading Fuse module... done
    CernVM-FS: mounted cvmfs on /tmp/hvela/tmp.iH6e993Adw/cvmfsexec/dist/cvmfs/cvmfs-config.cern.ch
    CernVM-FS: loading Fuse module... done
    CernVM-FS: mounted cvmfs on /tmp/hvela/tmp.iH6e993Adw/cvmfsexec/dist/cvmfs/software.eessi.io

    # Now it's mounted!
    $ ls /cvmfs/
    cvmfs-config.cern.ch  software.eessi.io

```

Notice how now that EESSI is mounted, you will need to [set up the environment](https://www.eessi.io/docs/using_eessi/setting_up_environment/) in order to access the software itself.

### `orted`  wrapper script

In order to get multi-node runs of software working without having EESSI available system-wide, you also need to create a small wrapper script for the `orted` command that is used by Open MPI to start processes on remote nodes. This is necessary because `mpirun` launches `orted`, which must be run in an environment in which the EESSI repository is mounted. If not, MPI startup may fail with an error like

```bash
"error: execve(): orted: No such file or directory".
```

This wrapper script must be named `orted`, and must be located in a path that is listed in `$PATH`.

For example, it can be placed in `~/bin/orted`, and you can add `export PATH=$HOME/bin:$PATH` to your `~/.bashrc` login script.

Contents of ~/bin/orted:

```bash
#!/bin/bash

# first remove path to this orted wrapper from $PATH, to avoid infinite loop
orted_wrapper_dir=$(dirname $0)
export PATH=$(echo $PATH | tr ':' '\n' | grep -v $orted_wrapper_dir | tr '\n' ':')

~/bin/cvmfsexec_eessi.sh orted "$@"
```

Again, do make sure that also this `orted` wrapper script is executable:

```bash
chmod u+x ~/bin/orted
```

If not, you will likely run into an error that starts with:


```bash
An ORTE daemon has unexpectedly failed after launch ...
```

### Slurm job script

The `cvmfsexec_eessi.sh` can be used inside a Slurm job script inside your HPC system to initialize the EESSI environment in a subshell which the EESSI CernVM-FS repository is mounted. Thus, you will be able to load any module from EESSI you might need.

Example job script:

```bash
#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --time=5:0:0
#SBATCH --export=None
#SBATCH --mem=30000M
~/bin/cvmfsexec_eessi.sh << EOF
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load TensorFlow/2.13.0-foss-2023a
export SLURM_EXPORT_ENV=HOME,PATH,LD_LIBRARY_PATH,PYTHONPATH
mpirun -np 4 python test.py
EOF

```
You can see the original blog post on how this solution was used on the Deucalion EuroHPC system [here](https://www.eessi.io/docs/blog/2024/06/28/espresso-portable-test-run-eurohpc/#running-espresso-on-deucalion-via-eessi-cvmfsexec). 

## Via `squashfs` +  cvmfs's `shrinkwrap` utility

CernVM-FS provides the [Shrinkwrap utility](https://cvmfs.readthedocs.io/en/stable/cpt-shrinkwrap.html), allowing users to create a portable snapshot of a CVMFS repository. This can be exported and distributed without the need of a CVMFS client or network access. A big advantage of `Shrinkwrap` over e.g. simply `rsync`-ing the repository to a local directory `/cvmfs/software.eessi.io` is that `Shrinkwrap` preserves the deduplication that CernVM-FS offers.

To create an export of EESSI in user space, you will first need to create the config file `software.eessi.io.config`:

```bash
CVMFS_REPOSITORIES=software.eessi.io
CVMFS_REPOSITORY_NAME=software.eessi.io
CVMFS_CONFIG_REPOSITORY=cvmfs-config.cern.ch
CVMFS_SERVER_URL='http://aws-eu-west-s1-sync.eessi.science/cvmfs/software.eessi.io'
CVMFS_HTTP_PROXY=DIRECT # Avoid filling up any local squid's cache
CVMFS_CACHE_BASE=/tmp/shrinkwrap
CVMFS_KEYS_DIR=/etc/cvmfs/keys/eessi.io # Need to be provided for shrinkwrap
CVMFS_SHARED_CACHE=no # Important as libcvmfs does not support shared caches
CVMFS_USER=cvmfs
CVMFS_UID_MAP=uid.map
CVMFS_GID_MAP=gid.map

```
You will need to create the files `uid.map` and `gid.map` with the respective value you will use preceded by a `*`. You will probably want to use the UID and GID of the current user, so, to set the two files:

```bash
    $ echo '*' $(id -u $USER) > uid.map
    $ cat uid.map
    * 1001

    $ echo '*' $(id -g $USER) > gid.map
    $ cat gid.map
    * 1001
```
In addition, you need to create a spec file `software.eessi.io.spec` with the files you want to include and/or exclude in the shrinkwrap. Please note that specifying the compatibility layer is a must to ensure a proper functioning of the export as it initializes the environment. The most basic setup would be:

```bash
/versions/2023.06/compat/linux/x86_64/*
/versions/2023.06/init/*
/versions/2023.06/scripts/*
# Exclude the Gentoo ebuild repo and cache files
!/versions/2023.06/compat/linux/x86_64/var/db/repos/gentoo
!/versions/2023.06/compat/linux/x86_64/var/cache

``` 
From here, you can tune this file to your needs, you can change the release version, the architecture and/or micro-architectures, or even if you just need one particular software. For example, if you wanted to have all the software for Intel's AVX512, you would need to export:  


```bash
/versions/2023.06/compat/linux/x86_64/*
/versions/2023.06/init/*
/versions/2023.06/scripts/*
/versions/2023.06/software/linux/x86_64/intel/skylake_avx512/.lmod/*
/versions/2023.06/software/linux/x86_64/intel/skylake_avx512/modules/*
/versions/2023.06/software/linux/x86_64/intel/skylake_avx512/software/*
# Exclude the Gentoo ebuild repo and cache files
!/versions/2023.06/compat/linux/x86_64/var/db/repos/gentoo
!/versions/2023.06/compat/linux/x86_64/var/cache

```

If instead you wanted the whole tree for a handful of another micro-architecture: 

```bash
/versions/2023.06/compat/linux/x86_64/*
/versions/2023.06/init/*
/versions/2023.06/scripts/*
/versions/2023.06/software/linux/aarch64/neoverse_n1/*
/versions/2023.06/software/linux/aarch64/a64fx/*
/versions/2023.06/software/linux/aarch64/nvidia/*
# Exclude the Gentoo ebuild repo and cache files
!/versions/2023.06/compat/linux/x86_64/var/db/repos/gentoo
!/versions/2023.06/compat/linux/x86_64/var/cache

```
But be careful as exporting the whole tree takes huge amounts of memory. 

If you want a cleaner approach, you can store the compat layer in a separate file called `software.eessi.io_compat.spec` with the minimal contents stated before. And in the  `software.eessi.io.spec ` only the software files you are interested in. Per example, if you were only interested in GROMACS, you could use the environment inside an existing EESSI installation to generate the spec file from the loaded modules: 

``` bash
# Init EESSI and load the target software
source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
module load GROMACS

# Create the spec file for software
ls /cvmfs/software.eessi.io/versions/$EESSI_VERSION/software/linux/$EESSI_SOFTWARE_SUBDIR/modules -d | sed s#/cvmfs/software.eessi.io##g > software.eessi.io.spec
ls /cvmfs/software.eessi.io/versions/$EESSI_VERSION/software/linux/$EESSI_SOFTWARE_SUBDIR/.lmod -d | sed s#/cvmfs/software.eessi.io##g >> software.eessi.io.spec
env | grep EBROOT | sed s/=/\ /g | awk '{print $2}' | sed s#/cvmfs/software.eessi.io##g | xargs -i echo "{}/*" >> software.eessi.io.spec
``` 

The `software.eessi.io.spec` file will look this way: 

```bash 
/versions/2023.06/software/linux/x86_64/intel/haswell/modules
/versions/2023.06/software/linux/x86_64/intel/haswell/.lmod
/versions/2023.06/software/linux/x86_64/intel/haswell/software/Python-bundle-PyPI/2023.10-GCCcore-13.2.0/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/pybind11/2.11.1-GCCcore-13.2.0/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/gfbf/2023b/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/PMIx/4.2.6-GCCcore-13.2.0/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/OpenSSL/1.1/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/foss/2023b/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/OpenMPI/4.1.6-GCC-13.2.0/*
[...]
/versions/2023.06/software/linux/x86_64/intel/haswell/software/GROMACS/2024.4-foss-2023b/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/gompi/2023b/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/GCCcore/13.2.0/*
/versions/2023.06/software/linux/x86_64/intel/haswell/software/SQLite/3.43.1-GCCcore-13.2.0/*

```

Then, execute `cvmfs_shrinkwrap`to create the export:

```bash
$ cvmfs_shrinkwrap -r software.eessi.io -f software.eessi.io.config -t software.eessi.io.spec --dest-base /tmp/cvmfs -j 4

LibCvmfs version 2.12, revision 31
(libcvmfs) (manager 'standard') switching proxy from (none) to DIRECT. Reason: set random start proxy from the first proxy group [Current host: http://aws-eu-west-s1-sync.eessi.science/cvmfs/software.eessi.io]
(libcvmfs) (manager 'external') switching proxy from (none) to DIRECT. Reason: cloned [Current host: http://aws-eu-west-s1-sync.eessi.science/cvmfs/software.eessi.io]
(libcvmfs) Starting 4 workers
(libcvmfs) cntByte|0|Byte count of projected repository
cntDir|1|Number of directories from source repository
cntFile|0|Number of files from source repository
cntSymlink|0|Number of symlinks from source repository
dataBytes|0|Bytes transferred from source to destination
dataBytesDeduped|0|Number of bytes not copied due to deduplication
dataFiles|0|Number of data files transferred from source to destination
dataFilesDeduped|0|Number of files not copied due to deduplication
entriesDest|1|Number of file system entries processed in the destination
entriesSrc|1|Number of file system entries processed in the source

....

# This takes a long time, memory and storage space depending on how much you want to export
```

If you have done the compat layer and software specs separetly, you will also need to make the export of the compat layer apart: 

```bash
cvmfs_shrinkwrap -r software.eessi.io -f software.eessi.io.config -t software.eessi.io_compat.spec --dest-base /tmp/compat -j 4
```

Once completed, the contents will be available in /tmp/cvmfs. You can create an squashfs image from it:

```bash
mksquashfs /tmp/cvmfs software.eessi.io.sqsh
# And if you squashed the compat layer separetly: 
mksquashfs /tmp/compat software.eessi.io_compat.sqsh

```
Note how `mksquashfs` compresses by default all generated images using `gzip`. If you want a faster approach at compression, you can use the `-comp` option and specify your preferred option among the available ones (you can check them with the `--help` argument). We recommend `zstd` because it's multithreaded and typically achieves better compression:

```
mksquashfs /tmp/cvmfs software.eessi.io.sqsh -comp zstd  
```

This squashfs image can be mounted in any container:

```bash
apptainer shell -B software.eessi.io.sqsh:/cvmfs:image-src=/ docker://ubuntu

```

Right now, this may seem like quite a manual process, but there is work in progress towards creating a script to automate this process.




















