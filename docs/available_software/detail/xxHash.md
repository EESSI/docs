---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: xxHash is an extremely fast non-cryptographic hash algorithm, working
    at RAM speed limit.
  license: Not confirmed
  name: xxHash
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
  softwareVersion: '[''0.8.2'']'
  url: https://cyan4973.github.io/xxHash
---
# xxHash


xxHash is an extremely fast non-cryptographic hash algorithm, working at RAM speed limit.

<small>homepage: </small><span class="software-link">[https://cyan4973.github.io/xxHash](https://cyan4973.github.io/xxHash)</span>

## Available installations


|xxHash version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.8.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`xxHash/0.8.2-GCCcore-12.3.0`|