---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A few simple math functions for other Oxford Nanopore processing scripts
  license: Not confirmed
  name: nanomath
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
  softwareVersion: '[''1.4.0'']'
  url: https://github.com/wdecoster/nanomath
---
# nanomath


A few simple math functions for other Oxford Nanopore processing scripts

<small>homepage: </small><span class="software-link">[https://github.com/wdecoster/nanomath](https://github.com/wdecoster/nanomath)</span>

## Available installations


|nanomath version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.4.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`nanomath/1.4.0-gfbf-2025b`|

## Extensions

Overview of extensions included in nanomath installations


### nanomath


|`nanomath` version|nanomath modules that include it|
| --- | --- |
|1.4.0|`nanomath/1.4.0-gfbf-2025b`|

### Python-Deprecated


|`Python-Deprecated` version|nanomath modules that include it|
| --- | --- |
|1.1.0|`nanomath/1.4.0-gfbf-2025b`|