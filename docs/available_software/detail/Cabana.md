---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Cabana is a performance portable library for particle-based simulations. Applications
    include,

    but are not limited to, molecular dynamics (MD) with short- and/or long-range
    atomic

    interactions; various flavors of particle-in-cell (PIC) methods, including use
    within

    fluid/solid mechanics and plasma physics; N-body cosmology simulations; and peridynamics

    for fracture mechanics.


    Cabana provides particle data structures, algorithms, and communication, as well
    as

    structured grids, grid algorithms, and particle-grid interpolation to enable simulations

    on a variety of platforms including many-core CPU and GPU architectures. Cabana
    is built

    on Kokkos, with many additional optional library dependencies, including MPI for
    multi-node

    simulation.

    '
  license: Not confirmed
  name: Cabana
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
  softwareVersion: '[''0.7.0'']'
  url: https://github.com/ECP-copa/Cabana
---
# Cabana



Cabana is a performance portable library for particle-based simulations. Applications include,
but are not limited to, molecular dynamics (MD) with short- and/or long-range atomic
interactions; various flavors of particle-in-cell (PIC) methods, including use within
fluid/solid mechanics and plasma physics; N-body cosmology simulations; and peridynamics
for fracture mechanics.

Cabana provides particle data structures, algorithms, and communication, as well as
structured grids, grid algorithms, and particle-grid interpolation to enable simulations
on a variety of platforms including many-core CPU and GPU architectures. Cabana is built
on Kokkos, with many additional optional library dependencies, including MPI for multi-node
simulation.


<small>homepage: </small><span class="software-link">[https://github.com/ECP-copa/Cabana](https://github.com/ECP-copa/Cabana)</span>

## Available installations


|Cabana version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.7.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Cabana/0.7.0-foss-2025a`|
|0.7.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Cabana/0.7.0-foss-2023b`|