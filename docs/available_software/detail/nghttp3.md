---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ' nghttp3 is an implementation of RFC 9114 HTTP/3

    mapping over QUIC and RFC 9204 QPACK in C.

    It does not depend on any particular QUIC transport implementation.'
  license: Not confirmed
  name: nghttp3
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
  softwareVersion: '[''1.3.0'']'
  url: https://github.com/ngtcp2/nghttp3
---
# nghttp3


 nghttp3 is an implementation of RFC 9114 HTTP/3
mapping over QUIC and RFC 9204 QPACK in C.
It does not depend on any particular QUIC transport implementation.

<small>homepage: </small><span class="software-link">[https://github.com/ngtcp2/nghttp3](https://github.com/ngtcp2/nghttp3)</span>

## Available installations


|nghttp3 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`nghttp3/1.3.0-GCCcore-12.3.0`|