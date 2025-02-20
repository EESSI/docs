# Non-standard ways to use EESSI

In case that an EESSI installation is not possible or desirable, there are a couple of "non-standard" ways to access EESSI.

## Using cvmfsexec

This option relies on the [cvmfsexec package](https://github.com/cvmfs/cvmfsexec) provided by CernVM-FS team. It will allow you to mount cvmfs as an unprivileged user, so no need to have a native cvmfs installation.

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

In order to get multi-node runs of software working without having EESSI available system-wide, we also had to create a small wrapper script for the `orted` command that is used by Open MPI to start processes on remote nodes. This is necessary because `mpirun` launches `orted`, which must be run in an environment in which the EESSI repository is mounted. If not, MPI startup will fail with an error like

```bash
"error: execve(): orted: No such file or directory".
```

This wrapper script must be named `orted`, and must be located in a path that is listed in `$PATH`.

We placed it in `~/bin/orted`, and you can add `export PATH=$HOME/bin:$PATH` to your `~/.bashrc` login script.

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

The `cvmfsexec_eessi.sh` can be used insided a Slurm job script inside your HPC system to initialize the EESSI environment in a subshell which the EESSI CernVM-FS repository is mounted. Thus, you will be able to load any module from EESSI you might need.

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
You can see the original blog post on how they used this solution in Deucalion [here](https://www.eessi.io/docs/blog/2024/06/28/espresso-portable-test-run-eurohpc/#running-espresso-on-deucalion-via-eessi-cvmfsexec). 
