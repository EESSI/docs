---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A simple but powerful Python library for creating, interpreting and
    manipulating binary data.
  license: Not confirmed
  name: watchfiles
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
  softwareVersion: '[''1.1.1'']'
  url: https://github.com/scott-griffiths/tibs
---
# watchfiles


A simple but powerful Python library for creating, interpreting and manipulating binary data.

<small>homepage: </small><span class="software-link">[https://github.com/scott-griffiths/tibs](https://github.com/scott-griffiths/tibs)</span>

## Available installations


|watchfiles version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`watchfiles/1.1.1-GCCcore-15.2.0`|

## Extensions

Overview of extensions included in watchfiles installations


### anyio


|`anyio` version|watchfiles modules that include it|
| --- | --- |
|4.13.0|`watchfiles/1.1.1-GCCcore-15.2.0`|

### idna


|`idna` version|watchfiles modules that include it|
| --- | --- |
|3.11|`watchfiles/1.1.1-GCCcore-15.2.0`|

### watchfiles


|`watchfiles` version|watchfiles modules that include it|
| --- | --- |
|1.1.1|`watchfiles/1.1.1-GCCcore-15.2.0`|