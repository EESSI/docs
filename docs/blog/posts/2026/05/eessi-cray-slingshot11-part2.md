---
author: [Richard]
date: 2026-05-08 
slug: EESSI-on-Cray-Slingshot-part2
---

# MPI at Warp Speed: EESSI Meets Slingshot-11<sub><sup>(part2)</sup></sub>

Building on our initial HPE/Cray Slingshot‑11 results, we further refined MPI tuning and validated the setup using EESSI/2025.06. The outcome is a significant performance improvement, bringing EESSI MPI behavior much closer to vendor tuned Cray MPI environments.
In our previous blog post, [MPI at Warp Speed: EESSI Meets Slingshot‑11](https://www.eessi.io/docs/blog/2025/11/14/EESSI-on-Cray-Slingshot/), we demonstrated that EESSI could successfully leverage the HPE Cray Slingshot‑11 interconnect via the [host_injections](https://www.eessi.io/docs/site_specific_config/host_injections/) mechanism. Even as a proof‑of‑concept, the results were promising especially for GPU aware MPI communication on NVIDIA Grace Hopper systems.
We have continued to tune and refine MPI communication while using EESSI/2025.06 software stack. Through updates to several core components and improvements to library configuration, we significantly reduced latency overheads and improved bandwidth utilization across Slingshot‑11.
In this follow‑up post, we present the results using OSU-Micro-Benchmarks/7.5 and discuss show how close EESSI can now get to native, vendor‑optimized MPI performance on Slingshot‑11 systems. 

### System Architecture

Our target system is [Olivia](https://documentation.sigma2.no/hpc_machines/olivia.html#olivia) which is based on HPE Cray EX platforms for compute and accelerator nodes, and HPE Cray ClusterStor for global storage, all
connected via HPE Slingshot high-speed interconnect.
It consists of two main distinct partitions:

- **Partition 1**: x86_64 AMD CPUs without accelerators
- **Partition 2**: NVIDIA Grace CPUs with Hopper accelerators

### Testing

The following tests were conducted on Olivia accel partition (Grace nodes with Hopper GPUs), using two-node, two-GPU configuration with one MPI task per node. 

We evaluated two OSU Micro-Benchmark builds:

1- OSU-Micro-Benchmarks/7.5-gompi-2024a-CUDA-12.6.0 from EESSI

2- OSU-Micro-Benchmarks/7.5 compiled with PrgEnv-cray.

The following commands were used to run the benchmarks:

`mpirun -np 2 osu_bibw D D`

`mpirun -np 2 osu_latency D D`

<details>
<summary>See details</summary>

<b>Test using OSU-Micro-Benchmarks/7.5-gompi-2024a-CUDA-12.6.0 from EESSI</b>:
```
Environment set up to use EESSI (2025.06), have fun!

hostname:
gpu-1-111
gpu-1-102

CPU info:
Vendor ID:                            ARM

Currently Loaded Modules:
  1) EESSI/2025.06                           12) PMIx/5.0.2-GCCcore-13.3.0
  2) GCCcore/13.3.0                          13) PRRTE/3.0.5-GCCcore-13.3.0
  3) GCC/13.3.0                              14) UCC/1.3.0-GCCcore-13.3.0
  4) numactl/2.0.18-GCCcore-13.3.0           15) OpenMPI/5.0.3-GCC-13.3.0
  5) libxml2/2.12.7-GCCcore-13.3.0           16) gompi/2024a
  6) libpciaccess/0.18.1-GCCcore-13.3.0      17) GDRCopy/2.4.1-GCCcore-13.3.0
  7) hwloc/2.10.0-GCCcore-13.3.0             18) UCX-CUDA/1.16.0-GCCcore-13.3.0-CUDA-12.6.0       (g)
  8) OpenSSL/3                               19) NCCL/2.22.3-GCCcore-13.3.0-CUDA-12.6.0           (g)
  9) libevent/2.1.12-GCCcore-13.3.0          20) UCC-CUDA/1.3.0-GCCcore-13.3.0-CUDA-12.6.0        (g)
 10) UCX/1.16.0-GCCcore-13.3.0               21) OSU-Micro-Benchmarks/7.5-gompi-2024a-CUDA-12.6.0 (g)
  Where:
   g:  built for GPU

# OSU MPI-CUDA Bi-Directional Bandwidth Test v7.5
# Datatype: MPI_CHAR.
# Size      Bandwidth (MB/s)
1                       1.24
2                       2.53
4                       5.09
8                      10.21
16                     20.56
32                     41.06
64                     82.56
128                   164.61
256                   328.11
512                   652.27
1024                 1295.71
2048                 2568.34
4096                 3161.87
8192                10383.73
16384               19679.28
32768               26194.74
65536               34068.25
131072              38747.45
262144              38515.90
524288              37048.28
1048576             44631.12
2097152             44871.95
4194304             45065.66

# OSU MPI-CUDA Latency Test v7.5
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                       2.79
2                       2.82
4                       2.91
8                       2.76
16                      2.82
32                      2.89
64                      2.80
128                     3.71
256                     4.14
512                     4.21
1024                    4.31
2048                    4.44
4096                    4.85
8192                    8.40
16384                   9.31
32768                  15.94
65536                  12.02
131072                 13.51
262144                 18.55
524288                 29.56
1048576                51.48
2097152                94.93
4194304               180.92
```

<b>Test using OSU-Micro-Benchmarks/7.5 with PrgEnv-cray</b>:
```

hostname:
gpu-1-111
gpu-1-102

CPU info:
Vendor ID:                            ARM

Currently Loaded Modules:
  1) craype-arm-grace                      8) craype/2.7.34
  2) libfabric/1.22.0                      9) cray-dsmml/0.3.1
  3) craype-network-ofi                   10) cray-mpich/8.1.32
  4) perftools-base/25.03.0               11) cray-libsci/25.03.0
  5) xpmem/2.11.3-1.3_gdbda01a1eb3d       12) PrgEnv-cray/8.6.0
  6) cce/19.0.0                           13) cudatoolkit/24.11_12.6

# OSU MPI-CUDA Bi-Directional Bandwidth Test v7.5
# Datatype: MPI_CHAR.
# Size      Bandwidth (MB/s)
1                       1.06
2                       2.17
4                       4.40
8                       8.80
16                     17.64
32                     35.17
64                     70.55
128                   140.91
256                   281.22
512                   559.04
1024                 1114.45
2048                 2081.25
4096                 4068.64
8192                 1852.11
16384               18564.47
32768               22647.40
65536               33108.03
131072              39553.95
262144              43140.01
524288              44853.40
1048576             45761.69
2097152             46228.10
4194304             46470.29

# OSU MPI-CUDA Latency Test v7.5
# Datatype: MPI_CHAR.
# Size       Avg Latency(us)
1                       2.76
2                       2.72
4                       2.90
8                       2.86
16                      2.85
32                      2.73
64                      2.60
128                     3.41
256                     4.17
512                     4.19
1024                    4.29
2048                    4.44
4096                    4.66
8192                    7.59
16384                   8.17
32768                   8.44
65536                   9.92
131072                 12.59
262144                 18.07
524288                 29.00
1048576                50.64
2097152                94.06
4194304               180.44
```
</details>
