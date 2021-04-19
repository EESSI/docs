## Pilot software stack (2021.03)

### Caveats

The current EESSI pilot software stack (version 2021.03) is the 5th iteration,
and there are some known issues and limitations, please take these into account:

* First of all: the EESSI pilot software stack is **NOT READY FOR PRODUCTION!**

  Do not use it for production work, and be careful when testing it on production systems!


### Reporting problems

If you notice any problems, please report them via https://github.com/EESSI/software-layer/issues.


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
  singularity shell --fusemount "$EESSI_CONFIG" --fusemount "$EESSI_PILOT" docker://eessi/client-pilot:centos7-$(uname -m)
  ```

 * This should give you a shell in the container, where the EESSI config and pilot repositories are mounted:
   ```
   $ singularity shell --fusemount "$EESSI_CONFIG" --fusemount "$EESSI_PILOT" docker://eessi/client-pilot:centos7-$(uname -m)
   INFO:    Using cached SIF image
   CernVM-FS: pre-mounted on file descriptor 3
   CernVM-FS: pre-mounted on file descriptor 3
   CernVM-FS: loading Fuse module... done
   CernVM-FS: loading Fuse module... done
   Singularity>
   ```
 * It is possible that you see some scary looking warnings, but those can be ignored for now.

   To verify that things are working, check the contents of the `/cvmfs/pilot.eessi-hpc.org/2021.03` directory:
   ```shell
   Singularity> ls /cvmfs/pilot.eessi-hpc.org/2021.03
   compat  init  software
   ```
#### Standard installation

For those with privileges on their system, there are a number of example installation scripts for different architectures
and operating systems available in the [EESSI demo repository](https://github.com/EESSI/eessi-demo/tree/main/scripts).

Here we prefer the Singularity approach as we can guarantee that the docker image is up to date.

### Setting up the EESSI environment

Once you have the EESSI pilot repository mounted, you can set up the environment by sourcing the provided init script:

```shell
source /cvmfs/pilot.eessi-hpc.org/2021.03/init/bash
```

If all goes well, you should see output like this:

```shell
Singularity> source /cvmfs/pilot.eessi-hpc.org/2021.03/init/bash
Found EESSI pilot repo @ /cvmfs/pilot.eessi-hpc.org/2021.03!
Using x86_64/intel/haswell as software subdirectory.
Using /cvmfs/pilot.eessi-hpc.org/2021.03/software/linux/x86_64/intel/haswell/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/pilot.eessi-hpc.org/2021.03/software/linux/x86_64/intel/haswell/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/pilot.eessi-hpc.org/2021.03/software/linux/x86_64/intel/haswell/modules/all to $MODULEPATH...
Environment set up to use EESSI pilot software stack, have fun!
[EESSI pilot 2021.03] $ 
```

Now you're all set up! Go ahead and explore the software stack using "`module avail`", and go wild with testing the available software installations!

### Testing the EESSI pilot software stack

Please test the EESSI pilot software stack as you see fit: running simple commands, performing small calculations or running small benchmarks, etc.

Test scripts that have been verified to work correctly using the pilot software stack are available at [https://github.com/EESSI/software-layer/tree/main/tests](https://github.com/EESSI/software-layer/tree/main/tests) .

### Giving feedback or reporting problems

Any feedback is welcome, and questions or problems reports are welcome as well, through one of the EESSI communication channels:

* (**preferred!**) EESSI `software-layer` GitHub repository: [https://github.com/EESSI/software-layer/issues](https://github.com/EESSI/software-layer/issues)
* EESSI mailing list (`eessi@list.rug.nl`)
* EESSI Slack: [https://eessi-hpc.slack.com](https://eessi-hpc.slack.com) (get an invite via [https://www.eessi-hpc.org/join](https://www.eessi-hpc.org/join))
* monthly EESSI meetings (first Thursday of the month at 2pm CEST)

### Available software

*(last update: Apr 19th 2021)*

EESSI currently supports the following HPC applications as well as all their dependencies:

- GROMACS (2020.1)
- OpenFOAM (v2006 and 8)
- R (4.0.0) + R-bundle-Bioconductor (3.11) + RStudio Server (1.3.1093)
- TensorFlow (2.3.1) *(currently not available on `ppc64le`)*
- OSU-Micro-Benchmarks (5.6.3)
- ReFrame (3.5.1)
- Spark (3.1.1)
- IPython (7.15.0)

```
[EESSI pilot 2020.13] $ module --nx avail

------------------------ /cvmfs/pilot.eessi-hpc.org/2021.03/software/linux/x86_64/intel/haswell/modules/all -------------------------
   ant/1.10.8-Java-11                                              MariaDB-connector-c/3.1.7-GCCcore-9.3.0
   Arrow/0.17.1-foss-2020a-Python-3.8.2                            matplotlib/3.2.1-foss-2020a-Python-3.8.2
   Bazel/3.6.0-GCCcore-9.3.0                                       Mesa/20.0.2-GCCcore-9.3.0
   Bison/3.5.3-GCCcore-9.3.0                                       Meson/0.55.1-GCCcore-9.3.0-Python-3.8.2
   Boost/1.72.0-gompi-2020a                                        METIS/5.1.0-GCCcore-9.3.0
   cairo/1.16.0-GCCcore-9.3.0                                      MPFR/4.0.2-GCCcore-9.3.0
   CGAL/4.14.3-gompi-2020a-Python-3.8.2                            NASM/2.14.02-GCCcore-9.3.0
   CMake/3.16.4-GCCcore-9.3.0                                      ncdf4/1.17-foss-2020a-R-4.0.0
   code-server/3.7.3                                               netCDF/4.7.4-gompi-2020a
   DB/18.1.32-GCCcore-9.3.0                                        nettle/3.6-GCCcore-9.3.0
   double-conversion/3.1.5-GCCcore-9.3.0                           networkx/2.4-foss-2020a-Python-3.8.2
   Doxygen/1.8.17-GCCcore-9.3.0                                    Ninja/1.10.0-GCCcore-9.3.0
   EasyBuild/4.3.4                                                 NLopt/2.6.1-GCCcore-9.3.0
   Eigen/3.3.7-GCCcore-9.3.0                                       NSPR/4.25-GCCcore-9.3.0
   expat/2.2.9-GCCcore-9.3.0                                       NSS/3.51-GCCcore-9.3.0
   FFmpeg/4.2.2-GCCcore-9.3.0                                      nsync/1.24.0-GCCcore-9.3.0
   FFTW/3.3.8-gompi-2020a                                          numactl/2.0.13-GCCcore-9.3.0
   flatbuffers/1.12.0-GCCcore-9.3.0                                OpenBLAS/0.3.9-GCC-9.3.0
   fontconfig/2.13.92-GCCcore-9.3.0                                OpenFOAM/v2006-foss-2020a
   foss/2020a                                                      OpenFOAM/8-foss-2020a                              (D)
   freetype/2.10.1-GCCcore-9.3.0                                   OpenMPI/4.0.3-GCC-9.3.0
   FriBidi/1.0.9-GCCcore-9.3.0                                     OpenPGM/5.2.122-GCCcore-9.3.0
   GCC/9.3.0                                                       OSU-Micro-Benchmarks/5.6.3-gompi-2020a
   GCCcore/9.3.0                                                   Pango/1.44.7-GCCcore-9.3.0
   Ghostscript/9.52-GCCcore-9.3.0                                  ParaView/5.8.0-foss-2020a-Python-3.8.2-mpi
   giflib/5.2.1-GCCcore-9.3.0                                      PCRE/8.44-GCCcore-9.3.0
   git/2.23.0-GCCcore-9.3.0-nodocs                                 PCRE2/10.34-GCCcore-9.3.0
   GLib/2.64.1-GCCcore-9.3.0                                       Perl/5.30.2-GCCcore-9.3.0
   GLPK/4.65-GCCcore-9.3.0                                         pixman/0.38.4-GCCcore-9.3.0
   GMP/6.2.0-GCCcore-9.3.0                                         pkg-config/0.29.2-GCCcore-9.3.0
   gnuplot/5.2.8-GCCcore-9.3.0                                     pkgconfig/1.5.1-GCCcore-9.3.0-Python-3.8.2
   GObject-Introspection/1.64.0-GCCcore-9.3.0-Python-3.8.2         PMIx/3.1.5-GCCcore-9.3.0
   gompi/2020a                                                     poetry/1.0.9-GCCcore-9.3.0-Python-3.8.2
   groff/1.22.4-GCCcore-9.3.0                                      protobuf-python/3.13.0-foss-2020a-Python-3.8.2
   GROMACS/2020.1-foss-2020a-Python-3.8.2                          protobuf/3.13.0-GCCcore-9.3.0
   GSL/2.6-GCC-9.3.0                                               pybind11/2.4.3-GCCcore-9.3.0-Python-3.8.2
   gzip/1.10-GCCcore-9.3.0                                         Python/2.7.18-GCCcore-9.3.0
   h5py/2.10.0-foss-2020a-Python-3.8.2                             Python/3.8.2-GCCcore-9.3.0                         (D)
   HarfBuzz/2.6.4-GCCcore-9.3.0                                    PyYAML/5.3-GCCcore-9.3.0
   HDF5/1.10.6-gompi-2020a                                         Qt5/5.14.1-GCCcore-9.3.0
   hwloc/2.2.0-GCCcore-9.3.0                                       R-bundle-Bioconductor/3.11-foss-2020a-R-4.0.0
   ICU/66.1-GCCcore-9.3.0                                          R/4.0.0-foss-2020a
   ImageMagick/7.0.10-1-GCCcore-9.3.0                              re2c/1.3-GCCcore-9.3.0
   IPython/7.15.0-foss-2020a-Python-3.8.2                          ReFrame/3.5.1
   JasPer/2.0.14-GCCcore-9.3.0                                     RStudio-Server/1.3.1093-foss-2020a-Java-11-R-4.0.0
   Java/11.0.2                                             (11)    ScaLAPACK/2.1.0-gompi-2020a
   JsonCpp/1.9.4-GCCcore-9.3.0                                     scikit-build/0.10.0-foss-2020a-Python-3.8.2
   LAME/3.100-GCCcore-9.3.0                                        SciPy-bundle/2020.03-foss-2020a-Python-3.8.2
   libcerf/1.13-GCCcore-9.3.0                                      SCOTCH/6.0.9-gompi-2020a
   libdrm/2.4.100-GCCcore-9.3.0                                    snappy/1.1.8-GCCcore-9.3.0
   libevent/2.1.11-GCCcore-9.3.0                                   Spark/3.1.1-foss-2020a-Python-3.8.2
   libfabric/1.11.0-GCCcore-9.3.0                                  SQLite/3.31.1-GCCcore-9.3.0
   libffi/3.3-GCCcore-9.3.0                                        SWIG/4.0.1-GCCcore-9.3.0
   libgd/2.3.0-GCCcore-9.3.0                                       Szip/2.1.1-GCCcore-9.3.0
   libGLU/9.0.1-GCCcore-9.3.0                                      Tcl/8.6.10-GCCcore-9.3.0
   libglvnd/1.2.0-GCCcore-9.3.0                                    TensorFlow/2.3.1-foss-2020a-Python-3.8.2
   libiconv/1.16-GCCcore-9.3.0                                     Tk/8.6.10-GCCcore-9.3.0
   libjpeg-turbo/2.0.4-GCCcore-9.3.0                               Tkinter/3.8.2-GCCcore-9.3.0
   libpciaccess/0.16-GCCcore-9.3.0                                 UCX/1.8.0-GCCcore-9.3.0
   libpng/1.6.37-GCCcore-9.3.0                                     UDUNITS/2.2.26-foss-2020a
   libsndfile/1.0.28-GCCcore-9.3.0                                 UnZip/6.0-GCCcore-9.3.0
   libsodium/1.0.18-GCCcore-9.3.0                                  X11/20200222-GCCcore-9.3.0
   LibTIFF/4.1.0-GCCcore-9.3.0                                     x264/20191217-GCCcore-9.3.0
   libunwind/1.3.1-GCCcore-9.3.0                                   x265/3.3-GCCcore-9.3.0
   libxml2/2.9.10-GCCcore-9.3.0                                    xorg-macros/1.19.2-GCCcore-9.3.0
   libyaml/0.2.2-GCCcore-9.3.0                                     Xvfb/1.20.9-GCCcore-9.3.0
   LittleCMS/2.9-GCCcore-9.3.0                                     Yasm/1.3.0-GCCcore-9.3.0
   LLVM/9.0.1-GCCcore-9.3.0                                        ZeroMQ/4.3.2-GCCcore-9.3.0
   LMDB/0.9.24-GCCcore-9.3.0                                       Zip/3.0-GCCcore-9.3.0
   lz4/1.9.2-GCCcore-9.3.0                                         zstd/1.4.4-GCCcore-9.3.0
   Mako/1.1.2-GCCcore-9.3.0
```

### Architecture and micro-architecture support

#### x86_64

  - generic (currently implies `march=x86-64` and `-mtune=generic`)
  - AMD
      - zen2 (Rome)
  - Intel
      - haswell
      - skylake_avx512

#### aarch64/arm64

  - generic (currently implies `-march=armv8-a` and `-mtune=generic`)
  - AWS Graviton2

### EasyBuild configuration

EasyBuild v4.3.4 was used to install the software in the `2021.03` version of the pilot repository.
For some installations pull requests with changes that will be included in later EasyBuild versions were leveraged,
see the [build script](https://github.com/EESSI/software-layer/blob/main/EESSI-pilot-install-software.sh) that was used.

An example configuration of the build environment based on https://github.com/EESSI/software-layer can be seen here:
```
$ eb --show-config
#
# Current EasyBuild configuration
# (C: command line argument, D: default value, E: environment variable, F: configuration file)
#
buildpath         (E) = /tmp/eessi-build/easybuild/build
containerpath     (E) = /tmp/eessi-build/easybuild/containers
debug             (E) = True
filter-deps       (E) = Autoconf, Automake, Autotools, binutils, bzip2, cURL, DBus, flex, gettext, gperf, help2man, intltool, libreadline, libtool, Lua, M4, makeinfo, ncurses, util-linux, XZ, zlib
filter-env-vars   (E) = LD_LIBRARY_PATH
hooks             (E) = /home/eessi-build/software-layer/eb_hooks.py
ignore-osdeps     (E) = True
installpath       (E) = /cvmfs/pilot.eessi-hpc.org/2021.03/software/linux/x86_64/intel/haswell
module-extensions (E) = True
packagepath       (E) = /tmp/eessi-build/easybuild/packages
prefix            (E) = /tmp/eessi-build/easybuild
repositorypath    (E) = /tmp/eessi-build/easybuild/ebfiles_repo
robot-paths       (D) = /cvmfs/pilot.eessi-hpc.org/2021.03/software/linux/x86_64/intel/haswell/software/EasyBuild/4.3.4/easybuild/easyconfigs
rpath             (E) = True
sourcepath        (E) = /tmp/eessi-build/easybuild/sources:
sysroot           (E) = /cvmfs/pilot.eessi-hpc.org/2021.03/compat/linux/x86_64
trace             (E) = True
zip-logs          (E) = bzip2
```
