---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'html5lib is a pure-python library for parsing HTML.

    It is designed to conform to the WHATWG HTML specification, as is implemented
    by all major web browsers.'
  license: Not confirmed
  name: html5lib
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
  softwareVersion: '[''1.1'']'
  url: https://github.com/html5lib/html5lib-python
---
# html5lib


html5lib is a pure-python library for parsing HTML.
It is designed to conform to the WHATWG HTML specification, as is implemented by all major web browsers.

<small>homepage: </small><span class="software-link">[https://github.com/html5lib/html5lib-python](https://github.com/html5lib/html5lib-python)</span>

## Available installations


|html5lib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`html5lib/1.1-GCCcore-15.2.0`|

## Extensions

Overview of extensions included in html5lib installations


### html5lib


|`html5lib` version|html5lib modules that include it|
| --- | --- |
|1.1|`html5lib/1.1-GCCcore-15.2.0`|

### webencodings


|`webencodings` version|html5lib modules that include it|
| --- | --- |
|0.6.1|`html5lib/1.1-GCCcore-15.2.0`|