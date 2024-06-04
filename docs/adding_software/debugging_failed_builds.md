# Debugging failed builds

*(for contributors + maintainers)*

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
./eessi_container.sh --access rw
```
!!! Note
    You may have to press enter to clearly see the prompt as some messages
    beginning with `CernVM-FS: ` have been printed after the first prompt
    `Apptainer> ` was shown.

If you want to debug an issue for which a lot of dependencies need to be build first, you may want to start the container with the `--save DIR/TGZ` and flag (check `./eessi_container.sh --help`). This saves the temporary directory (which we will use as working and installation directory later in this instruction) in order to be able to resume later with the same temporary directory. E.g.

```
./eessi_container.sh --access rw --save ${HOME}/pr370
```
The tarball will be saved when you exit the container. Note that the first `exit` command will first make you exit the Gentoo prefix environment. Only the second will take you out of the container, and print where the tarball will be stored:
```
[EESSI 2023.06] $ exit
logout
Leaving Gentoo Prefix with exit status 1
Apptainer> exit
exit
Saved contents of tmp directory '/tmp/eessi-debug.VgLf1v9gf0' to tarball '${HOME}/pr370/EESSI-1698056784.tgz' (to resume session add '--resume ${HOME}/pr370/EESSI-1698056784.tgz')
```

Note that the tarballs can be quite sizeable, so make sure to pick a filesystem where you have a large enough quotum.


Next time you want to continue investigating this issue, you can start the container with `--resume DIR/TGZ` and continue where you left off, having all dependencies already built and available.
```
./eessi_container.sh --access rw --resume ${HOME}/pr370/EESSI-1698056784.tgz
```

For a detailed description on using the script `eessi_container.sh`, see [here](../getting_access/eessi_container.md).

### Start the Gentoo Prefix environment
The next step is to start the Gentoo Prefix environment. 

Before we start, check the current values of `${EESSI_CVMFS_REPO}` and `${EESSI_VERSION}` so that you can reset them later:
```
echo ${EESSI_CVMFS_REPO}
echo ${EESSI_VERSION}
```

Then, we set `EESSI_OS_TYPE` and `EESSI_CPU_FAMILY` and run the `startprefix` command to start the Gentoo Prefix environment:
```
export EESSI_OS_TYPE=linux  # We only support Linux for now
export EESSI_CPU_FAMILY=$(uname -m)
${EESSI_CVMFS_REPO}/versions/${EESSI_VERSION}/compat/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/startprefix
```

Now, reset the `${EESSI_CVMFS_REPO}` and `${EESSI_VERSION}` in your prefix environment with the initial values (printed in the echo statements above)
```
export EESSI_CVMFS_REPO=...
export EESSI_VERSION=...
```

!!! Note
    By activating the Gentoo Prefix environment, the system tools (e.g. `ls`) you would normally use are now provided by Gentoo Prefix, instead of the container OS. E.g. running `which ls` after starting the prefix environment as above will return `/cvmfs/software.eessi.io/versions/2023.06/compat/linux/x86_64/bin/ls`. This makes the builds completely independent from the container OS.

### Starting the EESSI software environment
!!! Note
    If you want to replicate a build with `generic` optimization (i.e. in `$EESSI_CVMFS_REPO/versions/${EESSI_VERSION}/software/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/generic`) you will need to set `export EESSI_SOFTWARE_SUBDIR_OVERRIDE=${EESSI_CPU_FAMILY}/generic` before starting the EESSI environment.

To activate the software environment, run
```
source ${EESSI_CVMFS_REPO}/versions/${EESSI_VERSION}/init/bash
```

!!! Note
    If you get an error `bash: /versions//init/bash: No such file or directory`, you forgot to reset the `${EESSI_CVFMS_REPO}` and `${EESSI_VERSION}` environment variables at the end of the previous step.

!!! Note
    If you want to build with generic optimization, you should run `export EESSI_CPU_FAMILY=$(uname -m) && export EESSI_SOFTWARE_SUBDIR_OVERRIDE=${EESSI_CPU_FAMILY}/generic` before sourcing.


For more info on starting the EESSI software environment, see [here](../using_eessi/setting_up_environment.md)

### Configure EasyBuild
It is important that we configure EasyBuild in the same way as the bot uses it, with one small exceptions: our working directory will be different. Typically, that doesn't matter, but it's good to be aware of this one difference, in case you fail to replicate the build failure.

In this example, we create a unique temporary directory inside `/tmp` to serve both as our workdir. Finally, we will source the `configure_easybuild` script, which will configure EasyBuild by setting environment variables.

```
export WORKDIR=$(mktemp --directory --tmpdir=/tmp  -t eessi-debug.XXXXXXXXXX)
source configure_easybuild
```
Among other things, the `configure_easybuild` script sets the install path for EasyBuild to point to the correct installation directory in (to `${EESSI_CVMFS_REPO}/versions/${EESSI_VERSION}/software/${EESSI_OS_TYPE}/${EESSI_SOFTWARE_SUBDIR}`). This is the exact same path the `bot` uses to build, and uses a writeable overlay filesystem in the container to write to a path in `/cvmfs` (which normally is read-only). This is identical to what the `bot` does.

!!! Note
    If you started the container using --resume, you may want WORKDIR to point to the workdir you created previously (instead of creating a new, temporary directory with `mktemp`).

!!! Note
    If you want to replicate a build with `generic` optimization (i.e. in `$EESSI_CVMFS_REPO/versions/${EESSI_VERSION}/software/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/generic`) you will need to set `export EASYBUILD_OPTARCH=GENERIC` after sourcing `configure_easybuild`.


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
robot-paths          (D) = /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/neoverse_n1/software/EasyBuild/4.8.1/easybuild/easyconfigs
rpath                (E) = True
sourcepath           (E) = /tmp/easybuild/easybuild/sources:
sysroot              (E) = /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64
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

!!! Note
    While this might be faster than the EasyStack-based approach, this is _not_ how the bot builds. So why it _may_ reproduce the failure the bot encounters, it may not reproduce the bug _at all_ (no failure) or run into _different_ bugs. If you want to be sure, use the EasyStack-based approach.

## Running the test step
If you are still in the prefix layer (i.e. after previously building something), exit it first:
```
$ exit
logout
Leaving Gentoo Prefix with exit status 0
```
Then, source the EESSI init script (again):
```
Apptainer> source ${EESSI_CVMFS_REPO}/versions/${EESSI_VERSION}/init/bash
Environment set up to use EESSI (2023.06), have fun!
{EESSI 2023.06} Apptainer>
```

!!! Note
    If you are in a SLURM environment, make sure to run `for i in $(env | grep SLURM); do unset "${i%=*}"; done` to unset any SLURM environment variables. Failing to do so will cause `mpirun` to pick up on these and e.g. infer how many slots are available. If you run into errors of the form "There are not enough slots available in the system to satisfy the X slots that were requested by the application:", you probably forgot this step.

Then, execute the `run_tests.sh` script. We are assuming you are still in the root of the `software-layer` repository that you cloned earlier:
```
./run_tests.sh
```
if all goes well, you should see (part of) the EESSI test suite being run by ReFrame, finishing with something like

```
[  PASSED  ] Ran X/Y test case(s) from Z check(s) (0 failure(s), 0 skipped, 0 aborted)
```

!!! Note
    If you are running on a system with hyperthreading enabled, you may still run into the "There are not enough slots available in the system to satisfy the X slots that were requested by the application:" error from `mpirun`, because hardware threads are not considered to be slots by default by OpenMPIs `mpirun`. In this case, run with `OMPI_MCA_hwloc_base_use_hwthreads_as_cpus=1 ./run_tests.sh` (for OpenMPI 4.X) or `PRTE_MCA_rmaps_default_mapping_policy=:hwtcpus ./run_tests.sh` (for OpenMPI 5.X).

## Known causes of issues in EESSI

### The custom system prefix of the compatibility layer
Some installations might expect the system root (sysroot, for short) to be in `/`. However, in case of EESSI, we are building against the OS in the [compatibility layer](../compatibility_layer.md). Thus, our sysroot is something like `${EESSI_CVMFS_REPO}/versions/${EESSI_VERSION}/compat/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}`. This _can_ cause issues if installation procedures _assume_ the sysroot is in `/`.

One example of a sysroot [issue](https://github.com/EESSI/software-layer/pull/370#issuecomment-1774744151) was in installing `wget`. The EasyConfig for `wget` defined
```
# make sure pkg-config picks up system packages (OpenSSL & co)
preconfigopts = "export PKG_CONFIG_PATH=/usr/lib64/pkgconfig:/usr/lib/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig && "
configopts = '--with-ssl=openssl '
```
This will not work in EESSI, since the OpenSSL should be picked up from the compatibility layer. This was fixed by changing the EasyConfig to read
```
preconfigopts = "export PKG_CONFIG_PATH=%(sysroot)s/usr/lib64/pkgconfig:%(sysroot)s/usr/lib/pkgconfig:%(sysroot)s/usr/lib/x86_64-linux-gnu/pkgconfig && "
configopts = '--with-ssl=openssl
```
The `%(sysroot)s` is a template value which EasyBuild will resolve to the value that has been configured in EasyBuild for `sysroot` (it is one of the fields printed by `eb --show-config` if a non-standard sysroot is configured).

If you encounter issues where the installation can not find something that is _normally_ provided by the OS (i.e. _not_ one of the dependencies in your module environment), you may need to resort to a similar approach.

### The writeable overlay
The writeable overlay in the container is known to be a bit slow sometimes. Thus, we have seen tests failing because they exceed some timeout (e.g. [this issue](https://github.com/EESSI/software-layer/pull/332#issuecomment-1775374260)).

To investigate if the writeable overlay is somehow the issue, you can make sure the installation gets done somewhere else, e.g. in the temporary directory in `/tmp` that you created as workdir. To do this, set

```
export EASYBUILD_INSTALLPATH=${WORKDIR}
```

_after_ the step in which you have sourced the `configure_easybuild` script. Note that in order to find (with `module av`) any modules that get installed here, you will need to add this path to the `MODULEPATH`:

```
module use ${EASYBUILD_INSTALLPATH}/modules/all
```

Then, retry building the software (as described above). If the build now succeeds, you know that indeed the writeable overlay caused the issue. We _have_ to build in this writeable overlay when we do real deployments. Thus, if you hit such a timeout, try to see if you can (temporarily) modify the timeout value in the test so that it passes.
