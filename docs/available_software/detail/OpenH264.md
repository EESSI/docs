---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Open Source H.264 Codec
  license: Not confirmed
  name: OpenH264
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
  softwareVersion: '[''2.6.0'']'
  url: https://github.com/cisco/openh264
---
# OpenH264


Open Source H.264 Codec

<small>homepage: </small><span class="software-link">[https://github.com/cisco/openh264](https://github.com/cisco/openh264)</span>

## Available installations


|OpenH264 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`OpenH264/2.6.0-GCCcore-15.2.0`|