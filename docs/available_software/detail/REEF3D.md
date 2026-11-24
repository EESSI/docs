---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    REEF3D and its dependency DIVEMesh are hydrodynamics frameworks that offers

    open-source CFD and wave models.  The software is efficiently parallelized,

    designed to run on a large number of processors. High-order spatial and

    temporal discretization schemes result in accurate and stable numerical

    behavior. The modular programming approach allows the framework to incorporate

    a range of different flow solvers which together represent all relevant length

    scales. With a focus on coastal, marine and hydraulic engineering flows,

    tailor-made multiphysics solvers are available for a range of relevant

    problems (e.g. sediment transport or floating body dynamics).

    '
  license: Not confirmed
  name: REEF3D
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
  softwareVersion: '[''26.05'']'
  url: https://reef3d.wordpress.com/
---
# REEF3D



REEF3D and its dependency DIVEMesh are hydrodynamics frameworks that offers
open-source CFD and wave models.  The software is efficiently parallelized,
designed to run on a large number of processors. High-order spatial and
temporal discretization schemes result in accurate and stable numerical
behavior. The modular programming approach allows the framework to incorporate
a range of different flow solvers which together represent all relevant length
scales. With a focus on coastal, marine and hydraulic engineering flows,
tailor-made multiphysics solvers are available for a range of relevant
problems (e.g. sediment transport or floating body dynamics).


<small>homepage: </small><span class="software-link">[https://reef3d.wordpress.com/](https://reef3d.wordpress.com/)</span>

## Available installations


|REEF3D version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|26.05|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`REEF3D/26.05-foss-2025b`|