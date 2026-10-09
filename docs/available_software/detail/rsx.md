---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Streaming toolkit for RAD-seq sex-determination analysis.
  license: Not confirmed
  name: rsx
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
  softwareVersion: '[''0.2.10'']'
  url: https://github.com/HaoZeke/rsx-rs
---
# rsx


Streaming toolkit for RAD-seq sex-determination analysis.

<small>homepage: </small><span class="software-link">[https://github.com/HaoZeke/rsx-rs](https://github.com/HaoZeke/rsx-rs)</span>

## Available installations


|rsx version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.2.10|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`rsx/0.2.10-GCCcore-15.2.0`|