---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'RCCL (pronounced "Rickle") is a stand-alone library of standard collective
    communication

    routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, reduce-scatter,
    gather, scatter,

    and all-to-all. There is also initial support for direct GPU-to-GPU send and receive
    operations. It has been

    optimized to achieve high bandwidth on platforms using PCIe, xGMI as well as networking
    using InfiniBand Verbs

    or TCP/IP sockets. RCCL supports an arbitrary number of GPUs installed in a single
    node or multiple nodes, and

    can be used in either single- or multi-process (e.g., MPI) applications.'
  license: Not confirmed
  name: RCCL
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
  softwareVersion: '[''2.22.3'']'
  url: https://github.com/ROCm/RCCL
---
# RCCL


RCCL (pronounced "Rickle") is a stand-alone library of standard collective communication
routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, reduce-scatter, gather, scatter,
and all-to-all. There is also initial support for direct GPU-to-GPU send and receive operations. It has been
optimized to achieve high bandwidth on platforms using PCIe, xGMI as well as networking using InfiniBand Verbs
or TCP/IP sockets. RCCL supports an arbitrary number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI) applications.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/RCCL](https://github.com/ROCm/RCCL)</span>

## Available installations


|RCCL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.22.3|`generic`: `x86_64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-amd">AMD</span>: `gfx1030`, `gfx1100`, `gfx1101`, `gfx1200`, `gfx1201`, `gfx908`, `gfx90a`, `gfx942`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`RCCL/2.22.3-rocm-compilers-19.0.0-ROCm-6.4.1`|