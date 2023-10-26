# Debugging failed builds (contributors/maintainers)

Unfortunately, software does not always build successfully. Since EESSI targets novel CPU architectures as well, build failures on such platforms are quite common, as the software and/or the software build systems have not always been adjusted to support these architectures yet.

In EESSI, all software packages are built by a bot. This is great for builds that complete successfully as we can build many software packages for a wide range of hardware with little human intervention. However, it does mean that you, as contributor, can not easily access the build directory and build logs to figure out build issues.

This page describes how you can interactively reproduce failed builds, so that you can more easily debug the issue.

Throughout this page, we will use [this PR](https://github.com/EESSI/software-layer/pull/360) as an example. It intends to add LAMMPS to EESSI. Among other issues, it failed on a [building Plumed](https://github.com/EESSI/software-layer/pull/360#issuecomment-1765913105).

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
!!! Note
    You may have to press enter to clearly see the prompt as some messages
    beginning with `CernVM-FS: ` have been printed after the first prompt
    `Apptainer> ` was shown.

If you want to debug an issue for which a lot of dependencies need to be build first, you may want to start the container with the `--save DIR/TGZ` and flag (check `./eessi_container.sh --help`). This saves the temporary directory (which we will use as working and installation directory later in this instruction) in order to be able to resume later with the same temporary directory. E.g.

```
./eessi_container.sh --save ${HOME}/pr370
```
The tarball will be saved when you exit the container. Note that the first `exit` command will first make you exit the Gentoo prefix environment. Only the second will take you out of the container, and print where the tarball will be stored:
```
[EESSI pilot 2023.06] $ exit
logout
Leaving Gentoo Prefix with exit status 1
Apptainer> exit
exit
Saved contents of tmp directory '/tmp/eessi.VgLf1v9gf0' to tarball '${HOME}/pr370/EESSI-pilot-1698056784.tgz' (to resume session add '--resume ${HOME}/pr370/EESSI-pilot-1698056784.tgz')
```

Note that the tarballs can be quite sizeable, so make sure to pick a filesystem where you have a large enough quotum.


Next time you want to continue investigating this issue, you can start the container with `--resume DIR/TGZ` and continue where you left off, having all dependencies already built and available.
```
./eessi_container.sh --resume ${HOME}/pr370/EESSI-pilot-1698056784.tgz
```

For a detailed description on using the script `eessi_container.sh`, see [here](../getting_access/eessi_container.md).

### Start the Gentoo Prefix environment
The next step is to start the Gentoo Prefix environment. 

Before we start, check the current values of `${EESSI_CVMFS_REPO}` and `${EESSI_PILOT_VERSION}` so that you can reset them later:
```
echo ${EESSI_CVMFS_REPO}
echo ${EESSI_PILOT_VERSION}
```

Then, we set `EESSI_OS_TYPE` and `EESSI_CPU_FAMILY` and run the `startprefix` command to start the Gentoo Prefix environment:
```
export EESSI_OS_TYPE=linux  # We only support Linux for now
export EESSI_CPU_FAMILY=$(uname -m)
${EESSI_CVMFS_REPO}/versions/${EESSI_PILOT_VERSION}/compat/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/startprefix
```

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

For both, any writeable path will do. In this example, we create a unique temporary directory inside `/tmp` to serve both as our workdir and installpath. Finally, we will source the `configure_easybuild` script, which will configure EasyBuild by setting environment variables.

```
export WORKDIR=$(mktemp --directory --tmpdir=/tmp  -t eessi.XXXXXXXXXX)
source configure_easybuild
export EASYBUILD_INSTALLPATH=${WORKDIR}
```
!!! Note
    If you started the container using --resume, you probably want WORKDIR to point to the workdir you created previously, instead of create a new, temporary directory.

!!! Note
    If you want to replicate a build with `generic` optimization (i.e. in `$EESSI_CVMFS_REPO/versions/${EESSI_PILOT_VERSION}/software/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/generic`) you will need to set `export EASYBUILD_OPTARCH=GENERIC`.

Next, add the path where the modules are installed to your `MODULEPATH`, so that you can easily find these with `module av` after installation has completed:
```
module use ${EASYBUILD_INSTALLPATH}/modules/all
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
hooks                (E) = ${HOME}/software-layer/eb_hooks.py
ignore-osdeps        (E) = True
installpath          (E) = /tmp/easybuild/software/linux/aarch64/neoverse_n1
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

## Building the software
When the bot builds software, it loops over all EasyStack files that have been changed, and builds them using EasyBuild. However, a single PR may add multiple items to a single EasyStack file, and the issue you are trying to debug is probably in _one_ of them. Getting EasyBuild to build the full EasyStack file will create the most similar situation to what the bot does. However, you _may_ just want to build the individual software that has changed. Below, we describe both approaches.

### Building everything in the EasyStack file
In our [example PR](https://github.com/EESSI/software-layer/pull/360), the EasyStack file that was changed was `eessi-2023.06-eb-4.8.1-2021b.yml`. To build this, we run (in the directory that contains the checkout of this feature branch):
```
eb --easystack eessi-2023.06-eb-4.8.1-2021b.yml --robot
```
After some time, this build fails while trying to build `Plumed`, and we can access the build log to look for clues on why it failed.

### Building an individual package
In our [example PR](https://github.com/EESSI/software-layer/pull/360), the individual package that was added to `eessi-2023.06-eb-4.8.1-2021b.yml` was `LAMMPS-23Jun2022-foss-2021b-kokkos.eb`. We'll also have to (re)use any options that are listed in the EasyStack file for `LAMMPS-23Jun2022-foss-2021b-kokkos.eb`, in this case the option `--from-pr 19000`. Thus, to build, we run:
```
eb LAMMPS-23Jun2022-foss-2021b-kokkos.eb --robot --from-pr 19000
```
After some time, this build fails while trying to build `Plumed`, and we can access the build log to look for clues on why it failed.