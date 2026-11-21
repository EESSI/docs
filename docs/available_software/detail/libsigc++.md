---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The libsigc++ package implements a typesafe callback system

    for standard C++.'
  license: Not confirmed
  name: libsigc++
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
  softwareVersion: '[''3.8.1'']'
  url: https://libsigcplusplus.github.io/libsigcplusplus/
---
# libsigc++


The libsigc++ package implements a typesafe callback system
for standard C++.

<small>homepage: </small><span class="software-link">[https://libsigcplusplus.github.io/libsigcplusplus/](https://libsigcplusplus.github.io/libsigcplusplus/)</span>

## Available installations


|libsigc++ version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.8.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`libsigc++/3.8.1-GCCcore-15.2.0`|