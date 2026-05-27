---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    LoopTools is a package for evaluation of scalar and tensor one-loop integrals.


    It is based on the FF package by G.J. van Oldenborgh.

    '
  license: Not confirmed
  name: LoopTools
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
  softwareVersion: '[''2.15'']'
  url: https://feynarts.de/looptools/
---
# LoopTools



LoopTools is a package for evaluation of scalar and tensor one-loop integrals.

It is based on the FF package by G.J. van Oldenborgh.


<small>homepage: </small><span class="software-link">[https://feynarts.de/looptools/](https://feynarts.de/looptools/)</span>

## Available installations


|LoopTools version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.15|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`LoopTools/2.15-GCC-12.3.0`|