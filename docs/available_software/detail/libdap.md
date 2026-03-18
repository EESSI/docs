---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "A C++ SDK which contains an implementation of DAP 2.0 and\n DAP4.0.\
    \ This includes both Client- and Server-side support classes."
  license: Not confirmed
  name: libdap
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
  softwareVersion: '[''3.20.11'']'
  url: https://www.opendap.org/software/libdap
---
# libdap


A C++ SDK which contains an implementation of DAP 2.0 and
 DAP4.0. This includes both Client- and Server-side support classes.

<small>homepage: </small><span class="software-link">[https://www.opendap.org/software/libdap](https://www.opendap.org/software/libdap)</span>

## Available installations


|libdap version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.20.11|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libdap/3.20.11-GCCcore-12.3.0`|