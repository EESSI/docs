# Production EESSI repository (`software.eessi.io`)

### Reporting problems

If you notice any problems, please report them via https://gitlab.com/eessi/support or send it in via email, `support (at) eessi.io`.


### Accessing the EESSI repository

#### Via a container

To access the EESSI repository you only need a minimal operating system and the necessary packages to access the EESSI repository through CernVM-FS, and it is suitable for `aarch64`, `ppc64le`, and `x86_64`.

The easiest way to access the EESSI repository is by using Singularity. You can find the instructions for using EESSI on a container, [here](../getting_access/eessi_container.md).

#### Standard installation

For those with privileges on their system, and would like to install CernVM-FS natively. You can follow the instructions, [here](../getting_access/native_installation.md). 

On Mon 4 Dec 2023 the tutorial, Best Practices for CernVM-FS in HPC, was orginased. You can find a recording for the tutorial, [here](https://www.youtube.com/watch?v=L0Mmy7NBXDU).

There are a number of example installation scripts for different architectures
and operating systems available in the [EESSI demo repository](https://github.com/EESSI/eessi-demo/tree/main/scripts).

Here we prefer the Singularity approach as we can guarantee that the container image is up to date.

### Setting up the EESSI environment

Once you have the EESSI pilot repository mounted, you can set up the environment by sourcing the provided init script:

```shell
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
```

If all goes well, you should see output like this:

```shell
Found EESSI pilot repo @ /cvmfs/software.eessi.io/versions/2023.06!
archdetect says x86_64/amd/zen2
Using x86_64/amd/zen2 as software subdirectory.
Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Environment set up to use EESSI (2023.06), have fun!
```

Now you're all set up! Go ahead and explore the software stack using "`module avail`", and go wild with testing the available software installations!

### Testing the EESSI pilot software stack

Please test the EESSI pilot software stack as you see fit: running simple commands, performing small calculations or running small benchmarks, etc.

Test scripts that have been verified to work correctly using the pilot software stack are available at [https://github.com/EESSI/software-layer/tree/main/tests](https://github.com/EESSI/software-layer/tree/main/tests) .

### Giving feedback or reporting problems

Any feedback is welcome, and questions or problems reports are welcome as well, through one of the EESSI communication channels:

* (**preferred!**) EESSI support portal: [https://gitlab.com/eessi/support](https://gitlab.com/eessi/support) OR `support (at) eessi.io`
* EESSI `software-layer` GitHub repository: [https://github.com/EESSI/software-layer/issues](https://github.com/EESSI/software-layer/issues)
* EESSI mailing list (`eessi@list.rug.nl`)
* EESSI Slack: [https://eessi-hpc.slack.com](https://eessi-hpc.slack.com) (get an invite via [https://www.eessi-hpc.org/join](https://www.eessi-hpc.org/join))
* monthly EESSI meetings (first Thursday of the month at 2pm CEST)

### Available software

*(last update: 3 Jan 2024)*

EESSI currently supports the following HPC applications as well as all their dependencies:

- R (4.3.2) 
- TensorFlow (2.13.0)
- OSU-Micro-Benchmarks (7.1.1)

```
[EESSI 2023.06] $ module --nx avail

--------------------------- /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/modules/all ----------------------------
Abseil/20230125.3-GCCcore-12.3.0          (D)    gfbf/2023a                                          libpciaccess/0.17-GCCcore-12.3.0              pkgconfig/1.5.5-GCCcore-12.3.0-python     (D)
   ALL/0.9.2-foss-2023a                             giflib/5.2.1-GCCcore-12.3.0                 (D)     libpng/1.6.38-GCCcore-12.2.0                  PMIx/4.2.2-GCCcore-12.2.0
   Bazel/6.3.1-GCCcore-12.3.0                (D)    git/2.38.1-GCCcore-12.2.0-nodocs                    libpng/1.6.39-GCCcore-12.3.0           (D)    PMIx/4.2.4-GCCcore-12.3.0
   Bison/3.8.2-GCCcore-12.2.0                       git/2.41.0-GCCcore-12.3.0-nodocs                    LibTIFF/4.5.0-GCCcore-12.3.0           (D)    poetry/1.5.1-GCCcore-12.3.0
   Bison/3.8.2-GCCcore-12.3.0                       GLib/2.75.0-GCCcore-12.2.0                          libunwind/1.6.2-GCCcore-12.2.0                protobuf-python/4.24.0-GCCcore-12.3.0     (D)
   BLIS/0.9.0-GCC-12.2.0                            GLib/2.77.1-GCCcore-12.3.0                  (D)     libunwind/1.6.2-GCCcore-12.3.0         (D)    protobuf/24.0-GCCcore-12.3.0              (D)
   BLIS/0.9.0-GCC-12.3.0                            GMP/6.2.1-GCCcore-12.2.0                            libxml2/2.10.3-GCCcore-12.2.0                 pybind11/2.11.1-GCCcore-12.3.0
   Boost/1.82.0-GCC-12.3.0                   (D)    GObject-Introspection/1.74.0-GCCcore-12.2.0         libxml2/2.11.4-GCCcore-12.3.0                 Python-bundle-PyPI/2023.06-GCCcore-12.3.0
   Brotli/1.0.9-GCCcore-12.2.0                      GObject-Introspection/1.76.1-GCCcore-12.3.0 (D)     LLVM/15.0.5-GCCcore-12.2.0                    Python/2.7.18-GCCcore-12.2.0-bare
   Brotli/1.0.9-GCCcore-12.3.0               (D)    gompi/2022b                                         LLVM/16.0.6-GCCcore-12.3.0             (D)    Python/3.10.8-GCCcore-12.2.0-bare
   cairo/1.17.4-GCCcore-12.2.0                      gompi/2023a                                         LoopTools/2.15-GCC-12.3.0                     Python/3.10.8-GCCcore-12.2.0
   cairo/1.17.8-GCCcore-12.3.0               (D)    graphite2/1.3.14-GCCcore-12.2.0                     lz4/1.9.4-GCCcore-12.2.0                      Python/3.11.3-GCCcore-12.3.0
   Catch2/2.13.9-GCCcore-12.3.0                     graphite2/1.3.14-GCCcore-12.3.0             (D)     lz4/1.9.4-GCCcore-12.3.0               (D)    Qt5/5.15.7-GCCcore-12.2.0
   cffi/1.15.1-GCCcore-12.3.0                       groff/1.22.4-GCCcore-12.2.0                         make/4.3-GCCcore-12.2.0                       Qt5/5.15.10-GCCcore-12.3.0                (D)
   CMake/3.24.3-GCCcore-12.2.0                      gzip/1.12-GCCcore-12.2.0                            make/4.4.1-GCCcore-12.3.0                     R/4.3.2-gfbf-2023a                        (D)
   CMake/3.26.3-GCCcore-12.3.0                      gzip/1.12-GCCcore-12.3.0                    (D)     Mako/1.2.4-GCCcore-12.2.0                     RE2/2023-08-01-GCCcore-12.3.0             (D)
   cryptography/41.0.1-GCCcore-12.3.0               h5py/3.9.0-foss-2023a                       (D)     Mako/1.2.4-GCCcore-12.3.0              (D)    re2c/3.0-GCCcore-12.2.0
   CUDA-Samples/12.1-GCC-12.3.0-CUDA-12.1.1  (g)    HarfBuzz/5.3.1-GCCcore-12.2.0                       Mesa/22.2.4-GCCcore-12.2.0                    re2c/3.1-GCCcore-12.3.0                   (D)
   CUDA/12.1.1                               (D)    HarfBuzz/5.3.1-GCCcore-12.3.0               (D)     Mesa/23.1.4-GCCcore-12.3.0             (D)    Rust/1.65.0-GCCcore-12.2.0
   cURL/7.86.0-GCCcore-12.2.0                       hatchling/1.18.0-GCCcore-12.3.0                     Meson/0.64.0-GCCcore-12.2.0                   Rust/1.70.0-GCCcore-12.3.0
   cURL/8.0.1-GCCcore-12.3.0                        HDF5/1.14.0-gompi-2023a                     (D)     Meson/1.1.1-GCCcore-12.3.0                    ScaLAPACK/2.2.0-gompi-2022b-fb
   DB/18.1.40-GCCcore-12.2.0                 (D)    hwloc/2.8.0-GCCcore-12.2.0                          mpi4py/3.1.4-gompi-2023a               (D)    ScaLAPACK/2.2.0-gompi-2023a-fb
   dill/0.3.7-GCCcore-12.3.0                 (D)    hwloc/2.9.1-GCCcore-12.3.0                          NASM/2.15.05-GCCcore-12.2.0                   scikit-build/0.17.6-GCCcore-12.3.0
   double-conversion/3.2.1-GCCcore-12.2.0           hypothesis/6.82.0-GCCcore-12.3.0                    NASM/2.16.01-GCCcore-12.3.0            (D)    SciPy-bundle/2023.07-gfbf-2023a           (D)
   double-conversion/3.3.0-GCCcore-12.3.0    (D)    ICU/72.1-GCCcore-12.2.0                             netCDF/4.9.2-gompi-2023a               (D)    SDL2/2.28.2-GCCcore-12.3.0                (D)
   Doxygen/1.9.5-GCCcore-12.2.0                     ICU/73.2-GCCcore-12.3.0                     (D)     Nextflow/23.10.0                       (D)    setuptools-rust/1.6.0-GCCcore-12.3.0
   Doxygen/1.9.7-GCCcore-12.3.0              (D)    JasPer/4.0.0-GCCcore-12.2.0                         Ninja/1.11.1-GCCcore-12.2.0                   snappy/1.1.9-GCCcore-12.2.0
   EasyBuild/4.8.2                                  JasPer/4.0.0-GCCcore-12.3.0                 (D)     Ninja/1.11.1-GCCcore-12.3.0                   snappy/1.1.10-GCCcore-12.3.0              (D)
   EasyBuild/4.9.0                           (D)    Java/11.0.20                                (11)    nodejs/18.12.1-GCCcore-12.2.0                 SQLite/3.39.4-GCCcore-12.2.0
   Eigen/3.4.0-GCCcore-12.3.0                       jbigkit/2.1-GCCcore-12.3.0                  (D)     nodejs/18.17.1-GCCcore-12.3.0          (D)    SQLite/3.42.0-GCCcore-12.3.0
   expat/2.4.9-GCCcore-12.2.0                       JsonCpp/1.9.5-GCCcore-12.3.0                (D)     NSPR/4.35-GCCcore-12.2.0                      Szip/2.1.1-GCCcore-12.3.0                 (D)
   expat/2.5.0-GCCcore-12.3.0                       LAME/3.100-GCCcore-12.3.0                   (D)     NSPR/4.35-GCCcore-12.3.0               (D)    Tcl/8.6.12-GCCcore-12.2.0
   FFmpeg/6.0-GCCcore-12.3.0                 (D)    LHAPDF/6.5.4-GCC-12.3.0                             NSS/3.85-GCCcore-12.2.0                       Tcl/8.6.13-GCCcore-12.3.0
   ffnvcodec/12.0.16.0                       (D)    libarchive/3.6.1-GCCcore-12.2.0                     NSS/3.89.1-GCCcore-12.3.0              (D)    TensorFlow/2.13.0-foss-2023a              (D)
   FFTW.MPI/3.3.10-gompi-2022b                      libarchive/3.6.2-GCCcore-12.3.0                     nsync/1.26.0-GCCcore-12.3.0            (D)    Tk/8.6.13-GCCcore-12.3.0                  (D)
   FFTW.MPI/3.3.10-gompi-2023a                      libdeflate/1.18-GCCcore-12.3.0              (D)     numactl/2.0.16-GCCcore-12.2.0                 UCC/1.1.0-GCCcore-12.2.0
   FFTW/3.3.10-GCC-12.2.0                           libdrm/2.4.114-GCCcore-12.2.0                       numactl/2.0.16-GCCcore-12.3.0                 UCC/1.2.0-GCCcore-12.3.0
   FFTW/3.3.10-GCC-12.3.0                           libdrm/2.4.115-GCCcore-12.3.0               (D)     OpenBLAS/0.3.21-GCC-12.2.0                    UCX/1.13.1-GCCcore-12.2.0
   flatbuffers-python/23.5.26-GCCcore-12.3.0 (D)    libevent/2.1.12-GCCcore-12.2.0                      OpenBLAS/0.3.23-GCC-12.3.0                    UCX/1.14.1-GCCcore-12.3.0
   flatbuffers/23.5.26-GCCcore-12.3.0        (D)    libevent/2.1.12-GCCcore-12.3.0                      OpenMPI/4.1.4-GCC-12.2.0                      UnZip/6.0-GCCcore-12.2.0
   FlexiBLAS/3.2.1-GCC-12.2.0                       libfabric/1.16.1-GCCcore-12.2.0                     OpenMPI/4.1.5-GCC-12.3.0                      UnZip/6.0-GCCcore-12.3.0
   FlexiBLAS/3.3.1-GCC-12.3.0                       libfabric/1.18.0-GCCcore-12.3.0                     OpenSSL/1.1                            (D)    virtualenv/20.23.1-GCCcore-12.3.0
   flit/3.9.0-GCCcore-12.3.0                        libffi/3.4.4-GCCcore-12.2.0                         OSU-Micro-Benchmarks/7.1-1-gompi-2023a        VTK/9.3.0-foss-2023a                      (D)
```

### Architecture and micro-architecture support

#### x86_64

  - generic (currently implies `march=x86-64` and `-mtune=generic`)
  - AMD
      - zen2 (Rome)
      - zen3 (Milan)
  - Intel
      - haswell
      - skylake_avx512

#### aarch64/arm64

  - generic (currently implies `-march=armv8-a` and `-mtune=generic`)
  - neoverse_n1
  - neoverse_v1

### EasyBuild configuration

!!warning
  **What Should we mention about the EasyBuild configuration or can this be removed?**

EasyBuild v4.5.1 was used to install the software in the `2021.12` version of the pilot repository.
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
installpath       (E) = /cvmfs/pilot.eessi-hpc.org/2021.06/software/linux/x86_64/intel/haswell
module-extensions (E) = True
packagepath       (E) = /tmp/eessi-build/easybuild/packages
prefix            (E) = /tmp/eessi-build/easybuild
repositorypath    (E) = /tmp/eessi-build/easybuild/ebfiles_repo
robot-paths       (D) = /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/haswell/software/EasyBuild/4.5.1/easybuild/easyconfigs
rpath             (E) = True
sourcepath        (E) = /tmp/eessi-build/easybuild/sources:
sysroot           (E) = /cvmfs/pilot.eessi-hpc.org/versions/2021.12/compat/linux/x86_64
trace             (E) = True
zip-logs          (E) = bzip2
```
