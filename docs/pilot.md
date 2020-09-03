## Pilot software stack (2020.08)

### Caveats

The current EESSI pilot software stack (version 2020.08) is the first iteration,
and there are some known issues and limitations, please take these into account:

* First of all: the EESSI pilot software stack is **NOT READY FOR PRODUCTION!**

  Do not use it for production work, and be careful when testing it on production systems!

* The software is currently only installed for systems compatible with Intel Haswell processors.
  Installations tuned for other CPU architectures are not available yet (but are hopefully coming soon).

* There is no Lmod (spider) cache available yet for the environment module files included in the pilot repository,
  so `module` commands may be somewhat slow.

* The provided Open MPI installation (`OpenMPI/4.0.3-GCC-9.3.0` module) is not properly configured yet to use high-speed network interconnects.


### Accessing the EESSI pilot repository through Singularity

The easiest way to access the EESSI pilot repository is by using Singularity.
If Singularity is installed already, no admin privileges are required. No other software is needed either on the host.

A container image is available in Docker Hub (see [https://hub.docker.com/r/eessi/client-pilot](https://hub.docker.com/r/eessi/client-pilot)).
It only contains a minimal operating system + the necessary packages to access the EESSI pilot repository through CernVM-FS.

The container image can be used directly by Singularity (no prior download required), as follows:

* First, create some local directories in `/tmp/$USER` which will be bind mounted in the container:
  ```shell
  mkdir -p /tmp/$USER/{var-lib-cvmfs,var-run-cvmfs,home}
  ```
  These provides space for the CernVM-FS cache, and an empty home directory to use in the container.

* Set the `$SINGULARITY_BIND` and `$SINGULARITY_HOME` environment variables to configure Singularity:
  ```shell
  export SINGULARITY_BIND="/tmp/$USER/var-run-cvmfs:/var/run/cvmfs,/tmp/$USER/var-lib-cvmfs:/var/lib/cvmfs"
  export SINGULARITY_HOME="/tmp/$USER/home:/home/$USER"
  ```

* Start the container using `singularity shell`, using `--fusemount` to mount the EESSI config and pilot repositories
  (using the `cvmfs2` command that is included in the container image):
  ```shell
  export EESSI_CONFIG="container:cvmfs2 cvmfs-config.eessi-hpc.org /cvmfs/cvmfs-config.eessi-hpc.org"
  export EESSI_PILOT="container:cvmfs2 pilot.eessi-hpc.org /cvmfs/pilot.eessi-hpc.org"
  singularity shell --fusemount "$EESSI_CONFIG" --fusemount "$EESSI_PILOT" docker://eessi/client-pilot:centos7-2020.08
  ```

 * This should give you a shell in the container, where the EESSI config and pilot repositories are mounted:
   ```
   $ singularity shell --fusemount "$EESSI_CONFIG" --fusemount "$EESSI_PILOT" docker://eessi/client-pilot:centos7-2020.08
   INFO:    Using cached SIF image
   CernVM-FS: pre-mounted on file descriptor 3
   CernVM-FS: pre-mounted on file descriptor 3
   CernVM-FS: loading Fuse module... done
   CernVM-FS: loading Fuse module... done
   Singularity>
   ```
 * It is possible that you see some scary looking warnings, but those can be ignored for now.

   To verify that things are working, check the contents of the `/cvmfs/pilot.eessi-hpc.org/2020.08` directory:
   ```shell
   Singularity> ls /cvmfs/pilot.eessi-hpc.org/2020.08
   compat  init  software
   ```
### Setting up the EESSI environment

Once you have the EESSI pilot repository mounted, you can set up the environment by sourcing the provided init script:

```shell
source /cvmfs/pilot.eessi-hpc.org/2020.08/init/bash
```

If all goes well, you should see output like this:

```shell
Singularity> source /cvmfs/pilot.eessi-hpc.org/2020.08/init/bash

Found EESSI pilot repo @ /cvmfs/pilot.eessi-hpc.org/2020.08!
Derived subdirectory for software layer: x86_64/intel/haswell
Using x86_64/intel/haswell subdirectory for software layer (HARDCODED)
Initializing Lmod...
Prepending /cvmfs/pilot.eessi-hpc.org/2020.08/software/x86_64/intel/haswell/modules/all to $MODULEPATH...
Environment set up to use EESSI pilot software stack, have fun!

[EESSI pilot 2020.08] $
```

Now you're all set up! Go ahead and explore the software stack using "`module avail`", and go wild with testing the available software installations!

### Testing the EESSI pilot software stack

Please test the EESSI pilot software stack as you see fit: running simple commands, performing small calculations or running small benchmarks, etc.

Test scripts that have been verified to work correctly using the pilot software stack are available at [https://github.com/EESSI/software-layer/tree/master/tests](https://github.com/EESSI/software-layer/tree/master/tests) .

### Giving feedback or reporting problems

Any feedback is welcome, and questions or problems reports are welcome as well, through one of the EESSI communication channels:

* (**preferred!**) EESSI `software-layer` GitHub repository: [https://github.com/EESSI/software-layer/issues](https://github.com/EESSI/software-layer/issues)
* EESSI mailing list (`eessi@list.rug.nl`)
* EESSI Slack: [https://eessi-hpc.slack.com](https://eessi-hpc.slack.com) (get an invite via [https://www.eessi-hpc.org/join](https://www.eessi-hpc.org/join))
* monthly EESSI meetings (first Thursday of the month at 2pm CEST)

### Available software

*(last update: Sept 3rd 2020)*

```
[EESSI pilot 2020.08] $ module avail

-------------------------------------- /cvmfs/pilot.eessi-hpc.org/2020.08/software/x86_64/intel/haswell/modules/all --------------------------------------
   Autoconf/2.69-GCCcore-9.3.0             (D)    OpenBLAS/0.3.9-GCC-9.3.0                     (D)    help2man/1.47.4
   Automake/1.16.1-GCCcore-9.3.0           (D)    OpenFOAM/v2006-foss-2020a                           help2man/1.47.12-GCCcore-9.3.0
   Autotools/20180311-GCCcore-9.3.0        (D)    OpenFOAM/8-foss-2020a                        (D)    hwloc/2.2.0-GCCcore-9.3.0                   (D)
   Bison/3.3.2                                    OpenMPI/4.0.3-GCC-9.3.0                             intltool/0.51.0-GCCcore-9.3.0               (D)
   Bison/3.5.3-GCCcore-9.3.0                      PCRE/8.44-GCCcore-9.3.0                      (D)    libGLU/9.0.1-GCCcore-9.3.0                  (D)
   Bison/3.5.3                                    PCRE2/10.34-GCCcore-9.3.0                    (D)    libdrm/2.4.100-GCCcore-9.3.0                (D)
   Boost/1.72.0-gompi-2020a                       ParaView/5.8.0-foss-2020a-Python-3.8.2-mpi          libevent/2.1.11-GCCcore-9.3.0               (D)
   CGAL/4.14.3-gompi-2020a-Python-3.8.2    (D)    Perl/5.30.2-GCCcore-9.3.0                           libffi/3.3-GCCcore-9.3.0                    (D)
   CMake/3.16.4-GCCcore-9.3.0              (D)    Python/2.7.18-GCCcore-9.3.0                         libglvnd/1.2.0-GCCcore-9.3.0                (D)
   DBus/1.13.12-GCCcore-9.3.0              (D)    Python/3.8.2-GCCcore-9.3.0                   (D)    libiconv/1.16-GCCcore-9.3.0                 (D)
   Doxygen/1.8.17-GCCcore-9.3.0            (D)    Qt5/5.14.1-GCCcore-9.3.0                     (D)    libjpeg-turbo/2.0.4-GCCcore-9.3.0           (D)
   EasyBuild/4.2.2                                SCOTCH/6.0.9-gompi-2020a                            libpciaccess/0.16-GCCcore-9.3.0             (D)
   EasyBuild/20200831-dev                  (D)    SQLite/3.31.1-GCCcore-9.3.0                  (D)    libpng/1.6.37-GCCcore-9.3.0                 (D)
   Eigen/3.3.7-GCCcore-9.3.0                      ScaLAPACK/2.1.0-gompi-2020a                  (D)    libreadline/8.0-GCCcore-9.3.0
   FFTW/3.3.8-gompi-2020a                         SciPy-bundle/2020.03-foss-2020a-Python-3.8.2        libtool/2.4.6-GCCcore-9.3.0                 (D)
   FFmpeg/4.2.2-GCCcore-9.3.0              (D)    Szip/2.1.1-GCCcore-9.3.0                     (D)    libunwind/1.3.1-GCCcore-9.3.0               (D)
   FriBidi/1.0.9-GCCcore-9.3.0             (D)    Tcl/8.6.10-GCCcore-9.3.0                     (D)    libxml2/2.9.10-GCCcore-9.3.0                (D)
   GCC/9.3.0                                      UCX/1.8.0-GCCcore-9.3.0                      (D)    lz4/1.9.2-GCCcore-9.3.0                     (D)
   GCCcore/9.3.0                                  X11/20200222-GCCcore-9.3.0                   (D)    ncurses/6.1
   GLib/2.64.1-GCCcore-9.3.0               (D)    XZ/5.2.5-GCCcore-9.3.0                       (D)    ncurses/6.2-GCCcore-9.3.0
   GMP/6.2.0-GCCcore-9.3.0                 (D)    Yasm/1.3.0-GCCcore-9.3.0                     (D)    netCDF/4.7.4-gompi-2020a
   GROMACS/2020.1-foss-2020a-Python-3.8.2  (D)    binutils/2.34-GCCcore-9.3.0                         networkx/2.4-foss-2020a-Python-3.8.2
   HDF5/1.10.6-gompi-2020a                        binutils/2.34                                       numactl/2.0.13-GCCcore-9.3.0                (D)
   JasPer/2.0.14-GCCcore-9.3.0             (D)    bzip2/1.0.8-GCCcore-9.3.0                    (D)    pkg-config/0.29.2-GCCcore-9.3.0             (D)
   LAME/3.100-GCCcore-9.3.0                (D)    cURL/7.69.1-GCCcore-9.3.0                    (D)    pybind11/2.4.3-GCCcore-9.3.0-Python-3.8.2   (D)
   LLVM/9.0.1-GCCcore-9.3.0                (D)    double-conversion/3.1.5-GCCcore-9.3.0        (D)    re2c/1.3-GCCcore-9.3.0                      (D)
   M4/1.4.18-GCCcore-9.3.0                        expat/2.2.9-GCCcore-9.3.0                           scikit-build/0.10.0-foss-2020a-Python-3.8.2 (D)
   M4/1.4.18                               (D)    flex/2.6.4-GCCcore-9.3.0                            snappy/1.1.8-GCCcore-9.3.0                  (D)
   METIS/5.1.0-GCCcore-9.3.0               (D)    flex/2.6.4                                   (D)    util-linux/2.35-GCCcore-9.3.0               (D)
   MPFR/4.0.2-GCCcore-9.3.0                (D)    fontconfig/2.13.92-GCCcore-9.3.0             (D)    x264/20191217-GCCcore-9.3.0                 (D)
   Mako/1.1.2-GCCcore-9.3.0                (D)    foss/2020a                                   (D)    x265/3.3-GCCcore-9.3.0                      (D)
   Mesa/20.0.2-GCCcore-9.3.0               (D)    freetype/2.10.1-GCCcore-9.3.0                (D)    xorg-macros/1.19.2-GCCcore-9.3.0            (D)
   Meson/0.55.1-GCCcore-9.3.0-Python-3.8.2 (D)    gettext/0.20.1-GCCcore-9.3.0                        zlib/1.2.11-GCCcore-9.3.0
   NASM/2.14.02-GCCcore-9.3.0              (D)    gettext/0.20.1                               (D)    zlib/1.2.11                                 (D)
   NSPR/4.25-GCCcore-9.3.0                 (D)    gompi/2020a                                  (D)    zstd/1.4.4-GCCcore-9.3.0                    (D)
   NSS/3.51-GCCcore-9.3.0                  (D)    gperf/3.1-GCCcore-9.3.0                      (D)
   Ninja/1.10.0-GCCcore-9.3.0              (D)    gzip/1.10-GCCcore-9.3.0                      (D)
```

### Build host

* CentOS 7.8.2003
* Intel Xeon CPU E5-2680 (`haswell`)
* Singularity container with CentOS 7.8.2003 + `cvmfs` 2.7.3

### EasyBuild configuration

The latest `develop` version of EasyBuild was used, all changes required to install the software in the `2020.08` version of the pilot repository will be included in the upcoming release of EasyBuild v4.3.0.

```
$ eb --show-config
#
# Current EasyBuild configuration
# (C: command line argument, D: default value, E: environment variable, F: configuration file)
#
buildpath      (E) = /tmp/easybuild/build
containerpath  (E) = /tmp/easybuild/containers
debug          (E) = True
ignore-osdeps  (E) = True
installpath    (E) = /cvmfs/pilot.eessi-hpc.org/2020.08/software/x86_64/intel/haswell
packagepath    (E) = /tmp/easybuild/packages
prefix         (E) = /tmp/easybuild
repositorypath (E) = /tmp/easybuild/ebfiles_repo
robot-paths    (D) = /home/eessi/easybuild-easyconfigs/easybuild/easyconfigs
rpath          (E) = True
sourcepath     (E) = /tmp/easybuild/sources
sysroot        (E) = /cvmfs/pilot.eessi-hpc.org/2020.08/compat/x86_64
trace          (E) = True
```
