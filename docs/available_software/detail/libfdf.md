---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: LibFDF is the official implementation of the FDF specifications for
    use in client codes.
  license: Not confirmed
  name: libfdf
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
  softwareVersion: '[''0.5.1'']'
  url: https://gitlab.com/siesta-project/libraries/libfdf
---
# libfdf


LibFDF is the official implementation of the FDF specifications for use in client codes.

<small>homepage: </small><span class="software-link">[https://gitlab.com/siesta-project/libraries/libfdf](https://gitlab.com/siesta-project/libraries/libfdf)</span>

## Available installations


|libfdf version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libfdf/0.5.1-GCC-12.3.0`|