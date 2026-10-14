---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'MessagePack is an efficient binary serialization format, which lets
    you exchange

    data among multiple languages like JSON, except that it''s faster and smaller.

    Small integers are encoded into a single byte while typical short strings

    require only one extra byte in addition to the strings themselves.'
  license: Not confirmed
  name: msgpack-cxx
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
  softwareVersion: '[''7.0.0'']'
  url: http://msgpack.org/
---
# msgpack-cxx


MessagePack is an efficient binary serialization format, which lets you exchange
data among multiple languages like JSON, except that it's faster and smaller.
Small integers are encoded into a single byte while typical short strings
require only one extra byte in addition to the strings themselves.

<small>homepage: </small><span class="software-link">[http://msgpack.org/](http://msgpack.org/)</span>

## Available installations


|msgpack-cxx version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.0.0|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`msgpack-cxx/7.0.0-rocm-compilers-19.0.0-ROCm-6.4.1`|