---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Installs of the jupyter kernel provided by Cling.
  license: Not confirmed
  name: cling-kernel
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
  softwareVersion: '[''1.2'']'
  url: https://root.cern/cling/
---
# cling-kernel


Installs of the jupyter kernel provided by Cling.

<small>homepage: </small><span class="software-link">[https://root.cern/cling/](https://root.cern/cling/)</span>

## Available installations


|cling-kernel version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`cling-kernel/1.2-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in cling-kernel installations


### clingkernel


|`clingkernel` version|cling-kernel modules that include it|
| --- | --- |
|0.0.2|`cling-kernel/1.2-GCCcore-14.3.0`|