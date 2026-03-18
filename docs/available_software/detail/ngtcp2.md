---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    ''Call it TCP/2. One More Time.''


    ngtcp2 project is an effort to implement RFC9000 QUIC protocol.'
  license: Not confirmed
  name: ngtcp2
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
  softwareVersion: '[''1.2.0'']'
  url: https://github.com/ngtcp2/ngtcp2
---
# ngtcp2



'Call it TCP/2. One More Time.'

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

<small>homepage: </small><span class="software-link">[https://github.com/ngtcp2/ngtcp2](https://github.com/ngtcp2/ngtcp2)</span>

## Available installations


|ngtcp2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ngtcp2/1.2.0-GCC-12.3.0`|