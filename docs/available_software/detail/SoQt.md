---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "SoQt is a library which provides the glue between Systems in\n Motion's\
    \ Coin high-level 3D visualization library and the Qt 2D user interface\n library."
  license: Not confirmed
  name: SoQt
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
  softwareVersion: '[''1.6.4'']'
  url: https://coin3d.github.io/SoQt/html/
---
# SoQt


SoQt is a library which provides the glue between Systems in
 Motion's Coin high-level 3D visualization library and the Qt 2D user interface
 library.

<small>homepage: </small><span class="software-link">[https://coin3d.github.io/SoQt/html/](https://coin3d.github.io/SoQt/html/)</span>

## Available installations


|SoQt version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.6.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`SoQt/1.6.4-GCC-14.3.0`|