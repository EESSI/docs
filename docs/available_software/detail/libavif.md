---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This library aims to be a friendly, portable C implementation of the
    AV1 Image File Format,

    as described here: https://aomediacodec.github.io/av1-avif/

    '
  license: Not confirmed
  name: libavif
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
  softwareVersion: '[''1.0.4'']'
  url: https://github.com/AOMediaCodec/libavif
---
# libavif


This library aims to be a friendly, portable C implementation of the AV1 Image File Format,
as described here: https://aomediacodec.github.io/av1-avif/


<small>homepage: </small><span class="software-link">[https://github.com/AOMediaCodec/libavif](https://github.com/AOMediaCodec/libavif)</span>

## Available installations


|libavif version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libavif/1.0.4-GCCcore-12.3.0`|