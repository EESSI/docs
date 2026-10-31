---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'ParaView Catalyst provides a small, easy-to-use, API that any simulation
    developed in C++, C, Fortran

    or Python can use to do in situ analysis without developing its own custom data
    analysis code.

    '
  license: Not confirmed
  name: ParaView-Catalyst
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
  softwareVersion: '[''2.0.0'']'
  url: https://docs.paraview.org/en/latest/Catalyst/
---
# ParaView-Catalyst


ParaView Catalyst provides a small, easy-to-use, API that any simulation developed in C++, C, Fortran
or Python can use to do in situ analysis without developing its own custom data analysis code.


<small>homepage: </small><span class="software-link">[https://docs.paraview.org/en/latest/Catalyst/](https://docs.paraview.org/en/latest/Catalyst/)</span>

## Available installations


|ParaView-Catalyst version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ParaView-Catalyst/2.0.0-foss-2025b`|