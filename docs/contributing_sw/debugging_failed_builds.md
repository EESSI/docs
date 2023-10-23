# Debugging failed builds

Unfortunately, software does not always build successfully. Since EESSI targets novel CPU architectures as well, build failures on such platforms are quite common, as the software and/or the software build systems have not always been adjusted to support these architectures yet.

In EESSI, the build are performed by a bot. This is great for builds that complete successfully as we can build a lot of software, for a wide range of hardware because of this automation. However, it does means that you, as contributor, can not easily access the build directory and build logs to figure out build issues.

This page describes how you can interactively reproduce failed builds, so that you can more easily debug the issue.

Throughout this page, we will use [this PR](https://github.com/EESSI/software-layer/pull/360) as an example. It builds LAMMPS, and failed (among other things) on a [build issue for Plumed](https://github.com/EESSI/software-layer/pull/360#issuecomment-1765913105).

## Prerequisites
You will need to have:

- Access to a machine with the hardware for which the build that you want to debug failed. 
- On that machine, meet the requirements for running the EESSI container, as described on [this page](../getting_access/eessi_container.md#prerequisites).

## Preparing the environment
A number of steps are needed to create the same environment in which the bot builds.

- Fetching the feature branch from which you want to replicate a build.
- Starting a shell in the EESSI container.
- Start the Gentoo Prefix environment.
- Start the EESSI software environment.
- Configure EasyBuild.

### Fetching the feature branch
Looking at [the example PR](https://github.com/EESSI/software-layer/pull/360), we see the PR is created from [this fork](https://github.com/laraPPr/software-layer/). First, we clone the fork, then checkout the feature branch (`LAMMPS_23Jun2022`)
```
git clone https://github.com/laraPPr/software-layer/
cd software-layer
git checkout LAMMPS_23Jun2022
```
Alternatively, if you already have a clone of the `software-layer` you can add it as a new remote
```
cd software-layer
git remote add laraPPr https://github.com/laraPPr/software-layer/
git fetch laraPPr
git checkout LAMMPS_23Jun2022
```

### Starting a shell in the EESSI container
Simply run the EESSI container (`eessi_container.sh`), which should be in the root of the `software-layer` repository
```
./eessi_container.sh
```
If you want to debug an issue for which a lot of dependencies need to be build first, you may want to start the container with the `--save DIR/TGZ` and flag (check `./eessi_container.sh --help`) in order to be able to resume later. Next time you want to continue investigating this issue, you can start the container with `--resume DIR/TGZ` and continue where you left off, having all dependencies already built and available.

!!! Note
    You may have to press enter to clearly see the prompt as some messages
        beginning with `CernVM-FS: ` have been printed after the first prompt
            `Apptainer> ` was shown.

For more info on using the EESSI container, see [here](../getting_access/eessi_container.md).

### Start the Gentoo Prefix environment
The next step is to start the Gentoo Prefix environment. 

Before we start, check the current values of `${EESSI_CVMFS_REPO}` and `${EESSI_PILOT_VERSION}` so that you can reset them later:
```
echo ${EESSI_CVMFS_REPO}
echo ${EESSI_PILOT_VERSION}
```

To do that, you need to run the `startprefix` command. However, we have several compatibility layers, and you'll need to run it for the one that matches the host node. For example, on an aarch64 (ARM) linux machine:
```
export EESSI_OS_TYPE=linux
export EESSI_CPU_FAMILY=aarch64
${EESSI_CVMFS_REPO}/versions/${EESSI_PILOT_VERSION}/compat/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/startprefix
```

if you are unsure, you can start the EESSI software environment (see next step) and check the values of `EESSI_OS_TYPE` and `EESSI_CPU_FAMILY` set by that initialization script. Note that you'll have to start over with a new shell (i.e. quit the container) and repeat the current step of starting the Gentoo Prefix environment, as the order of those two steps matters.

Now, reset the `${EESSI_CVMFS_REPO}` and `${EESSI_PILOT_VERSION}` in your prefix environment
```
export EESSI_CVMFS_REPO=...
export EESSI_PILOT_VERSION=...
```

!!! Note
    By activating the Gentoo Prefix environment, the system tools (e.g. `ls`) you would normally use are now provided by Gentoo Prefix, instead of the container OS. E.g. running `which ls` after starting the prefix environment as above will return `/cvmfs/pilot.eessi-hpc.org/versions/2023.06/compat/linux/x86_64/bin/ls`. This makes the builds completely independent from the container OS.

### Starting the EESSI software environment
!!! Note
    If you want to replicate a build with `generic` optimization (i.e. in `$EESSI_CVMFS_REPO/versions/${EESSI_PILOT_VERSION}/software/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/generic`) you will need to set `export EESSI_SOFTWARE_SUBDIR_OVERRIDE=${EESSI_CPU_FAMILY}/generic` before starting the EESSI environment.

To activate the software environment, run
```
source ${EESSI_CVMFS_REPO}/versions/${EESSI_PILOT_VERSION}/init/bash
```

!!! Note
    If you get an error `bash: /versions//init/bash: No such file or directory`, you forgot to reset the `${EESSI_CVFMS_REPO}` and `${EESSI_PILOT_VERSION}` environment variables at the end of the previous step.


For more info on starting the EESSI software environment, see [here](../using_eessi/setting_up_environment.md)

### Configure EasyBuild
It is important that we configure EasyBuild in the same way as the bot uses it, with two small exceptions:

- Our working directory will be different
- Our installpath will be different

For both, any writeable path will do. In this example, we will choose `/tmp/easybuild` as our workdir, and `$HOME/.local/easybuild` as our installpath. Finally, we will source the `configure_easybuild` script, which will configure EasyBuild by setting environment variables.

```
export WORKDIR=/tmp/easybuild
source configure_easybuild
export EASYBUILD_INSTALLPATH="${HOME}/.local/easybuild"
```
Next, we need to determine the correct version of EasyBuild to load. Since [the example PR](https://github.com/EESSI/software-layer/pull/360) changes the file `eessi-2023.06-eb-4.8.1-2021b.yml`, this tells us the bot was using version `4.8.1` of EasyBuild to build this. Thus, we load that version of the EasyBuild module and check if everything was configured correctly:
```
module load EasyBuild/4.8.1
eb --show-config
```
You should get something similar to

```
#
# Current EasyBuild configuration
# (C: command line argument, D: default value, E: environment variable, F: configuration file)
#
buildpath            (E) = /tmp/easybuild/easybuild/build
containerpath        (E) = /tmp/easybuild/easybuild/containers
debug                (E) = True
experimental         (E) = True
filter-deps          (E) = Autoconf, Automake, Autotools, binutils, bzip2, DBus, flex, gettext, gperf, help2man, intltool, libreadline, libtool, Lua, M4, makeinfo, ncurses, util-linux, XZ, zlib, Yasm
filter-env-vars      (E) = LD_LIBRARY_PATH
hooks                (E) = /home/casparvl/software-layer/eb_hooks.py
ignore-osdeps        (E) = True
installpath          (E) = /cvmfs/pilot.eessi-hpc.org/versions/2023.06/software/linux/aarch64/neoverse_n1
module-extensions    (E) = True
packagepath          (E) = /tmp/easybuild/easybuild/packages
prefix               (E) = /tmp/easybuild/easybuild
read-only-installdir (E) = True
repositorypath       (E) = /tmp/easybuild/easybuild/ebfiles_repo
robot-paths          (D) = /cvmfs/pilot.eessi-hpc.org/versions/2023.06/software/linux/aarch64/neoverse_n1/software/EasyBuild/4.8.1/easybuild/easyconfigs
rpath                (E) = True
sourcepath           (E) = /tmp/easybuild/easybuild/sources:
sysroot              (E) = /cvmfs/pilot.eessi-hpc.org/versions/2023.06/compat/linux/aarch64
trace                (E) = True
zip-logs             (E) = bzip2
```

!!! Note
    If you want to replicate a build with `generic` optimization (i.e. in `$EESSI_CVMFS_REPO/versions/${EESSI_PILOT_VERSION}/software/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/generic`) you will need to set `export EASYBUILD_OPTARCH=GENERIC`.

## Building the software
When the bot builds software, it loops over all EasyStack files that have been changed, and builds them using EasyBuild. However, a single PR may add multiple items to a single EasyStack file, and the issue you are trying to debug is probably in _one_ of them. Getting EasyBuild to build the full EasyStack file will create the most similar situation to what the bot does. However, you _may_ just want to build the individual software that has changed. Below, we describe both approaches.

### Building everything in the EasyStack file
In our [example PR](https://github.com/EESSI/software-layer/pull/360), the EasyStack file that was changed was `eessi-2023.06-eb-4.8.1-2021b.yml`. To build this, we run (in the directory that contains the checkout of this feature branch):
```
eb --easystack eessi-2023.06-eb-4.8.1-2021b.yml --robot
```
After some time, this build fails whil trying to build `Plumed`, and we can access the build log to look for clues on why it failed.

### Building an individual package
In our [example PR](https://github.com/EESSI/software-layer/pull/360), the individual package that was added to `eessi-2023.06-eb-4.8.1-2021b.yml` was `LAMMPS-23Jun2022-foss-2021b-kokkos.eb`. We'll also have to mind any options that are listed in the EasyStack file for `LAMMPS-23Jun2022-foss-2021b-kokkos.eb`, in this case the option `--from-pr 19000`. Thus, to build, we run:
```
eb LAMMPS-23Jun2022-foss-2021b-kokkos.eb --robot --from-pr 19000
```
After some time, this build fails whil trying to build `Plumed`, and we can access the build log to look for clues on why it failed.
