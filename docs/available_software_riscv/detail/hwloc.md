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
    \ hardware so as to exploit it accordingly and efficiently.\n"
  license: Not confirmed
  name: hwloc
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
# hwloc



 The Portable Hardware Locality (hwloc) software package provides a portable
 abstraction (across OS, versions, architectures, ...) of the hierarchical
 topology of modern architectures, including NUMA memory nodes, sockets, shared
 caches, cores and simultaneous multithreading. It also gathers various system
 attributes such as cache and memory information as well as the locality of I/O
 devices such as network interfaces, InfiniBand HCAs or GPUs. It primarily
 aims at helping applications with gathering information about modern computing
 hardware so as to exploit it accordingly and efficiently.


<small>homepage: </small><span class="software-link">[https://www.open-mpi.org/projects/hwloc/](https://www.open-mpi.org/projects/hwloc/)</span>

## Available installations


|hwloc version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.12.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`hwloc/2.12.1-GCCcore-14.3.0`|
|2.11.2|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`hwloc/2.11.2-GCCcore-14.2.0`|