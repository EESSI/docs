---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n The Portable Hardware Locality (hwloc) software package provides\
    \ a portable\n abstraction (across OS, versions, architectures, ...) of the hierarchical\n\
    \ topology of modern architectures, including NUMA memory nodes, sockets, shared\n\
    \ caches, cores and simultaneous multithreading. It also gathers various system\n\
    \ attributes such as cache and memory information as well as the locality of I/O\n\
    \ devices such as network interfaces, InfiniBand HCAs or GPUs. It primarily\n\
    \ aims at helping applications with gathering information about modern computing\n\
    \ hardware so as to exploit it accordingly and efficiently.\n\n This provides\
    \ the CUDA and NVML plugins for hwloc\n"
  license: Not confirmed
  name: hwloc-CUDA
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''2.12.1'', ''2.11.2'']'
  url: https://www.open-mpi.org/projects/hwloc/
---
# hwloc-CUDA



 The Portable Hardware Locality (hwloc) software package provides a portable
 abstraction (across OS, versions, architectures, ...) of the hierarchical
 topology of modern architectures, including NUMA memory nodes, sockets, shared
 caches, cores and simultaneous multithreading. It also gathers various system
 attributes such as cache and memory information as well as the locality of I/O
 devices such as network interfaces, InfiniBand HCAs or GPUs. It primarily
 aims at helping applications with gathering information about modern computing
 hardware so as to exploit it accordingly and efficiently.

 This provides the CUDA and NVML plugins for hwloc


<small>homepage: </small><span class="software-link">[https://www.open-mpi.org/projects/hwloc/](https://www.open-mpi.org/projects/hwloc/)</span>

## Available installations


|hwloc-CUDA version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.12.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-nvidia">NVIDIA</span>: `cc100`, `cc120`, `cc70`, `cc80`, `cc90`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`hwloc-CUDA/2.12.1-GCCcore-14.3.0-CUDA-12.9.1`|
|2.11.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-nvidia">NVIDIA</span>: `cc100`, `cc120`, `cc70`, `cc80`, `cc90`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`hwloc-CUDA/2.11.2-GCCcore-14.2.0-CUDA-12.8.0`|