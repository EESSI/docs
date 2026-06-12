---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Kokkos Core implements a programming model in C++ for writing performance portable
    applications

    targeting all major HPC platforms. For that purpose it provides abstractions for
    both parallel

    execution of code and data management. Kokkos is designed to target complex node
    architectures

    with N-level memory hierarchies and multiple types of execution resources. It
    currently can use

    CUDA, HIP, SYCL, HPX, OpenMP and C++ threads as backend programming models with
    several other

    backends in development.

    '
  license: Not confirmed
  name: Kokkos
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
  softwareVersion: '[''5.0.2'']'
  url: https://kokkos.org/
---
# Kokkos



Kokkos Core implements a programming model in C++ for writing performance portable applications
targeting all major HPC platforms. For that purpose it provides abstractions for both parallel
execution of code and data management. Kokkos is designed to target complex node architectures
with N-level memory hierarchies and multiple types of execution resources. It currently can use
CUDA, HIP, SYCL, HPX, OpenMP and C++ threads as backend programming models with several other
backends in development.


<small>homepage: </small><span class="software-link">[https://kokkos.org/](https://kokkos.org/)</span>

## Available installations


|Kokkos version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.0.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Kokkos/5.0.2-GCC-14.2.0`|