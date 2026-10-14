---
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
|1.3.0|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`nghttp3/1.3.0-GCCcore-12.3.0`|