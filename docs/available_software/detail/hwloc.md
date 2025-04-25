---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Portable Hardware Locality (hwloc) software package provides a
    portable abstraction (across OS, versions, architectures, ...) of the hierarchical
    topology of modern architectures, including NUMA memory nodes, sockets, shared
    caches, cores and simultaneous multithreading. It also gathers various system
    attributes such as cache and memory information as well as the locality of I/O
    devices such as network interfaces, InfiniBand HCAs or GPUs. It primarily aims
    at helping applications with gathering information about modern computing hardware
    so as to exploit it accordingly and efficiently.
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
  softwareVersion: '[''hwloc/2.8.0-GCCcore-12.2.0'', ''hwloc/2.9.1-GCCcore-12.3.0'',
    ''hwloc/2.9.2-GCCcore-13.2.0'']'
  url: https://www.open-mpi.org/projects/hwloc/
---

hwloc
=====


The Portable Hardware Locality (hwloc) software package provides a portable abstraction (across OS, versions, architectures, ...) of the hierarchical topology of modern architectures, including NUMA memory nodes, sockets, shared caches, cores and simultaneous multithreading. It also gathers various system attributes such as cache and memory information as well as the locality of I/O devices such as network interfaces, InfiniBand HCAs or GPUs. It primarily aims at helping applications with gathering information about modern computing hardware so as to exploit it accordingly and efficiently.

https://www.open-mpi.org/projects/hwloc/
# Available modules


The overview below shows which hwloc installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using hwloc, load one of these modules using a `module load` command like:

```shell
module load hwloc/2.9.2-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|hwloc/2.9.2-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
|hwloc/2.9.1-GCCcore-12.3.0|x|x|x|-|x|x|x|x|x|x|x|x|
|hwloc/2.8.0-GCCcore-12.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
