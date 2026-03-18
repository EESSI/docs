---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    PyVO lets you find and retrieve astronomical data available from archives that
    support standard IVOA virtual

    observatory service protocols.

    '
  license: Not confirmed
  name: PyVO
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
  softwareVersion: '[''1.7'']'
  url: https://pyvo.readthedocs.io/
---
# PyVO



PyVO lets you find and retrieve astronomical data available from archives that support standard IVOA virtual
observatory service protocols.


<small>homepage: </small><span class="software-link">[https://pyvo.readthedocs.io/](https://pyvo.readthedocs.io/)</span>

## Available installations


|PyVO version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`PyVO/1.7-foss-2023b`|

## Extensions

Overview of extensions included in PyVO installations


### pyvo


|`pyvo` version|PyVO modules that include it|
| --- | --- |
|1.7|`PyVO/1.7-foss-2023b`|