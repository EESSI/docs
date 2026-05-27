---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'absl-py is a collection of Python library code for building Python

    applications. The code is collected from Google''s own Python code base, and has

    been extensively tested and used in production.'
  license: Not confirmed
  name: absl-py
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
  softwareVersion: '[''2.1.0'']'
  url: https://github.com/abseil/abseil-py
---
# absl-py


absl-py is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.

<small>homepage: </small><span class="software-link">[https://github.com/abseil/abseil-py](https://github.com/abseil/abseil-py)</span>

## Available installations


|absl-py version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`absl-py/2.1.0-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in absl-py installations


### absl-py


|`absl-py` version|absl-py modules that include it|
| --- | --- |
|2.1.0|`absl-py/2.1.0-GCCcore-13.3.0`|