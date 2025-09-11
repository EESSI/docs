---
author: [Richard]
date: 2025-09-10 
slug: EESSI-on-Cray-Slingshot
---

# MPI at Warp Speed: EESSI Meets Slingshot-11

High-performance computing environments are constantly evolving, and keeping pace with the latest interconnect technologies is crucial for maximizing application performance. HPE Cray Slingshot 11 with CXI (Cassini eXascale Interconnect) promises to offer a significant advancement in HPC networking, offering improved bandwidth, lower latency, and better scalability for exascale computing workloads.

In this blog post, we present the requirements for building OpenMPI 5.x with Slingshot 11 CXI support on Cray systems and its integration with EESSI using `host_injections`. This approach enables overriding EESSI’s default MPI library with an ABI-compatible, Slingshot-optimized version. The post concludes with test results validating this setup.

<!-- more -->

## The Challenge

EESSI provides a comprehensive software stack, but specialized interconnect support like Slingshot 11 CXI requires custom-built libraries that aren't yet available in the standard EESSI distribution. Our goal is to:

1. Build OpenMPI 5.x with native Slingshot 11 CXI support
2. Create ABI-compatible replacements for EESSI's MPI libraries
3. Support both x86_64 AMD CPU partitions and NVIDIA Grace CPU partitions with Hopper accelerators
4. Avoid dependency on system packages where possible

The main technical challenge is building the complete dependency chain on top of EESSI, as many of the required libraries for CXI support don't exist in the current EESSI stack.

## System Architecture

Our target system [Olivia](https://documentation.sigma2.no/olivia_pilot_period_docs/olivia_pilot_main.html) is based on HPE Cray EX platforms for compute and accelerator nodes, and HPE ClusterStor for global storage, all connected via HPE Slingshot high-speed interconnect.
It consists of two main distinct partitions:

- **Partition 1**: x86_64 AMD CPUs without accelerators
- **Partition 2**: NVIDIA Grace CPUs with Hopper accelerators

For the Grace/Hopper partition we needed to enable CUDA support in libfabric.

## Building the Dependency Chain

### Building Strategy

Rather than relying on Cray-provided system packages, we opted to build all dependencies from source on top of EESSI. This approach provides several advantages:

- **Consistency**: All libraries built with the same compiler toolchain
- **Compatibility**: Ensures ABI compatibility with EESSI libraries
- **Control**: Full control over build configurations and optimizations

### Required Dependencies

To build OpenMPI 5.x with CXI support, we needed the following missing dependencies:

1. **libuv** - Asynchronous I/O library
2. **libnl** - Netlink library for network configuration
3. **libconfig** - Library designed for processing structured configuration files
4. **libfuse** - Filesystem in Userspace library  
5. **libpdap** - Performance Data Access Protocol library
6. **shs-libcxi** - Slingshot CXI library
7. **lm-sensors** - Monitoring tools and drivers
8. **libfabric 2.x** - OpenFabrics Interfaces library with CXI provider
9. **OpenMPI 5.x** - The final MPI implementation

## EESSI Integration via `host_injections`

EESSI's [host_injections](../../../../site_specific_config/host_injections.md) mechanism allows us to override EESSI's MPI library with an ABI compatible host MPI while maintaining compatibility with the rest of the software stack.

**Validating the `libmpi.so.40` in `host_injections` from OpenMPI/5.0.7 on ARM nodes built with:** 
```
./configure --prefix=/cluster/installations/eessi/default/aarch64/software/OpenMPI/5.0.7-GCC-12.3.0 --with-cuda=${EBROOTCUDA} --with-cuda-libdir=${EBROOTCUDA}/lib64 --with-slurm --enable-mpi-ext=cuda --with-libfabric=${EBROOTLIBFABRIC} --with-ucx=${EBROOTUCX} --enable-mpirun-prefix-by-default  --enable-shared --with-hwloc=/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/hwloc/2.9.1-GCCcore-12.3.0  --with-libevent=/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/libevent/2.1.12-GCCcore-12.3.0  --with-pmix=/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/PMIx/4.2.4-GCCcore-12.3.0  --with-ucc=/cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/UCC/1.2.0-GCCcore-12.3.0  --with-prrte=internal
```
```
ldd /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/aarch64/nvidia/grace/rpath_overrides/OpenMPI/system/lib/libmpi.so.40

        linux-vdso.so.1 (0x0000fffcfd1d0000)
        libucc.so.1 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/UCC/1.2.0-GCCcore-12.3.0/lib64/libucc.so.1 (0x0000fffcfce50000)
        libucs.so.0 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/UCX/1.14.1-GCCcore-12.3.0/lib64/libucs.so.0 (0x0000fffcfcde0000)
        libnuma.so.1 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/numactl/2.0.16-GCCcore-12.3.0/lib64/libnuma.so.1 (0x0000fffcfcdb0000)
        libucm.so.0 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/UCX/1.14.1-GCCcore-12.3.0/lib64/libucm.so.0 (0x0000fffcfcd70000)
        libopen-pal.so.80 => /cluster/installations/eessi/default/aarch64/software/OpenMPI/5.0.7-GCC-12.3.0/lib/libopen-pal.so.80 (0x0000fffcfcc40000)
        libfabric.so.1 => /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/aarch64/nvidia/grace/rpath_overrides/OpenMPI/system/lib/libfabric.so.1 (0x0000fffcfca50000)
        librdmacm.so.1 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/librdmacm.so.1 (0x0000fffcfca10000)
        libefa.so.1 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/libefa.so.1 (0x0000fffcfc9e0000)
        libibverbs.so.1 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/libibverbs.so.1 (0x0000fffcfc9a0000)
        libcxi.so.1 => /cluster/installations/eessi/default/aarch64/software/shs-libcxi/1.7.0-GCCcore-12.3.0/lib64/libcxi.so.1 (0x0000fffcfc960000)
        libcurl.so.4 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/libcurl.so.4 (0x0000fffcfc8a0000)
        libjson-c.so.5 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/json-c/0.16-GCCcore-12.3.0/lib64/libjson-c.so.5 (0x0000fffcfc870000)
        libatomic.so.1 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/GCCcore/12.3.0/lib64/libatomic.so.1 (0x0000fffcfc840000)
        libcudart.so.12 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/accel/nvidia/cc90/software/CUDA/12.1.1/lib64/libcudart.so.12 (0x0000fffcfc780000)
        libcuda.so.1 => /usr/lib64/libcuda.so.1 (0x0000fffcf97d0000)
        libnvidia-ml.so.1 => /usr/lib64/libnvidia-ml.so.1 (0x0000fffcf8980000)
        libnl-route-3.so.200 => /cluster/installations/eessi/default/aarch64/software/libnl/3.11.0-GCCcore-12.3.0/lib64/libnl-route-3.so.200 (0x0000fffcf88d0000)
        libnl-3.so.200 => /cluster/installations/eessi/default/aarch64/software/libnl/3.11.0-GCCcore-12.3.0/lib64/libnl-3.so.200 (0x0000fffcf8890000)
        libpmix.so.2 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/PMIx/4.2.4-GCCcore-12.3.0/lib64/libpmix.so.2 (0x0000fffcf8690000)
        libevent_core-2.1.so.7 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/libevent/2.1.12-GCCcore-12.3.0/lib64/libevent_core-2.1.so.7 (0x0000fffcf8630000)
        libevent_pthreads-2.1.so.7 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/libevent/2.1.12-GCCcore-12.3.0/lib64/libevent_pthreads-2.1.so.7 (0x0000fffcf8600000)
        libhwloc.so.15 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/hwloc/2.9.1-GCCcore-12.3.0/lib64/libhwloc.so.15 (0x0000fffcf8580000)
        libpciaccess.so.0 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/libpciaccess/0.17-GCCcore-12.3.0/lib64/libpciaccess.so.0 (0x0000fffcf8550000)
        libxml2.so.2 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/libxml2/2.11.4-GCCcore-12.3.0/lib64/libxml2.so.2 (0x0000fffcf83e0000)
        libz.so.1 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/libz.so.1 (0x0000fffcf83a0000)
        liblzma.so.5 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/liblzma.so.5 (0x0000fffcf8330000)
        libm.so.6 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/lib/../lib64/libm.so.6 (0x0000fffcf8280000)
        libc.so.6 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/lib/../lib64/libc.so.6 (0x0000fffcf80e0000)
        /lib/ld-linux-aarch64.so.1 (0x0000fffcfd1e0000)
        libcares.so.2 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/libcares.so.2 (0x0000fffcf80a0000)
        libnghttp2.so.14 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/usr/lib/../lib64/libnghttp2.so.14 (0x0000fffcf8050000)
        libssl.so.1.1 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/OpenSSL/1.1/lib64/libssl.so.1.1 (0x0000fffcf7fb0000)
        libcrypto.so.1.1 => /cvmfs/software.eessi.io/versions/2023.06/software/linux/aarch64/nvidia/grace/software/OpenSSL/1.1/lib64/libcrypto.so.1.1 (0x0000fffcf7d10000)
        libdl.so.2 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/lib/../lib64/libdl.so.2 (0x0000fffcf7ce0000)
        libpthread.so.0 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/lib/../lib64/libpthread.so.0 (0x0000fffcf7cb0000)
        librt.so.1 => /cvmfs/software.eessi.io/versions/2023.06/compat/linux/aarch64/lib/../lib64/librt.so.1 (0x0000fffcf7c80000)
```

### Testing

**1- Test using OSU-Micro-Benchmarks on 2-nodes (x86_64 AMD-CPUs)**:
```
Environment set up to use EESSI (2023.06), have fun!
hostname:
x1001c6s2b0n1
x1001c6s3b0n0

CPU info:
Vendor ID:                            AuthenticAMD
Model name:                           AMD EPYC 9745 128-Core Processor
Virtualization:                       AMD-V

Currently Loaded Modules:
  1) GCCcore/12.3.0
  2) GCC/12.3.0
  3) numactl/2.0.16-GCCcore-12.3.0
  4) libxml2/2.11.4-GCCcore-12.3.0
  5) libpciaccess/0.17-GCCcore-12.3.0
  6) hwloc/2.9.1-GCCcore-12.3.0
  7) OpenSSL/1.1
  8) libevent/2.1.12-GCCcore-12.3.0
  9) UCX/1.14.1-GCCcore-12.3.0
 10) libfabric/1.18.0-GCCcore-12.3.0
 11) PMIx/4.2.4-GCCcore-12.3.0
 12) UCC/1.2.0-GCCcore-12.3.0
 13) OpenMPI/4.1.5-GCC-12.3.0
 14) gompi/2023a
 15) OSU-Micro-Benchmarks/7.1-1-gompi-2023a

# OSU MPI Bi-Directional Bandwidth Test v7.1
# Size      Bandwidth (MB/s)
# Datatype: MPI_CHAR.
1                       2.87
2                       5.77
4                      11.55
8                      23.18
16                     46.27
32                     92.64
64                    185.21
128                   369.03
256                   743.08
512                  1487.21
1024                 2975.75
2048                 5928.14
4096                11809.66
8192                23097.44
16384               31009.54
32768               36493.20
65536               40164.63
131072              43150.62
262144              45075.57
524288              45918.07
1048576             46313.37
2097152             46507.25
4194304             46609.10


# OSU MPI Latency Test v7.1
# Size          Latency (us)
# Datatype: MPI_CHAR.
1                       1.66
2                       1.65
4                       1.65
8                       1.65
16                      1.65
32                      1.65
64                      1.65
128                     2.13
256                     2.20
512                     2.23
1024                    2.31
2048                    2.46
4096                    2.61
8192                    2.87
16384                   3.24
32768                   5.24
65536                   6.60
131072                  9.29
262144                 14.69
524288                 26.21
1048576                47.32
2097152                90.79
```

**2- Test using OSU-Micro-Benchmarks/7.5-gompi-2023b-CUDA-12.4.0 on 2-nodes (Grace/Hopper GPUs)**:
```
Environment set up to use EESSI (2023.06), have fun!

hostname:
x1000c4s4b1n0
x1000c5s3b0n0

CPU info:
Vendor ID:                            ARM

Currently Loaded Modules:
  1) GCCcore/13.2.0
  2) GCC/13.2.0
  3) numactl/2.0.16-GCCcore-13.2.0
  4) libxml2/2.11.5-GCCcore-13.2.0
  5) libpciaccess/0.17-GCCcore-13.2.0
  6) hwloc/2.9.2-GCCcore-13.2.0
  7) OpenSSL/1.1
  8) libevent/2.1.12-GCCcore-13.2.0
  9) UCX/1.15.0-GCCcore-13.2.0
 10) libfabric/1.19.0-GCCcore-13.2.0
 11) PMIx/4.2.6-GCCcore-13.2.0
 12) UCC/1.2.0-GCCcore-13.2.0
 13) OpenMPI/4.1.6-GCC-13.2.0
 14) gompi/2023b
 15) GDRCopy/2.4-GCCcore-13.2.0
 16) UCX-CUDA/1.15.0-GCCcore-13.2.0-CUDA-12.4.0       (g)
 17) NCCL/2.20.5-GCCcore-13.2.0-CUDA-12.4.0           (g)
 18) UCC-CUDA/1.2.0-GCCcore-13.2.0-CUDA-12.4.0        (g)
 19) OSU-Micro-Benchmarks/7.5-gompi-2023b-CUDA-12.4.0 (g)

  Where:
   g:  built for GPU

# OSU MPI-CUDA Bi-Directional Bandwidth Test v7.5
# Datatype: MPI_CHAR.
# Size      Bandwidth (MB/s)
1                       0.18
2                       0.37
4                       0.75
8                       1.49
16                      2.99
32                      5.93
64                     11.88
128                    23.76
256                    72.78
512                   145.45
1024                  282.03
2048                  535.46
4096                 1020.24
8192                16477.70
16384               25982.96
32768               30728.30
65536               37637.46
131072              41808.92
262144              44316.19
524288              43693.89
1048576             43759.66
2097152             43593.38
4194304             43436.60


# OSU MPI-CUDA Latency Test v7.5
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                      11.71
2                      11.66
4                      11.66
8                      11.71
16                     11.67
32                     11.68
64                     11.66
128                    12.45
256                     3.76
512                     3.82
1024                    3.91
2048                    4.08
4096                    4.25
8192                    4.49
16384                   5.09
32768                   8.02
65536                   9.56
131072                 13.52
262144                 17.96
524288                 28.94
1048576                50.50
2097152                93.98
4194304               180.14
```
## Conclusion

The approach demonstrates EESSI's flexibility in accommodating specialized hardware requirements while preserving the benefits of a standardized software stack!


