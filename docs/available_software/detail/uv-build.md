---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    This package is a slimmed down version of uv containing only the build backend.

    See:

    https://pypi.org/project/uv/

    and

    https://docs.astral.sh/uv/

    for the main project package and documentation.

    '
  license: Not confirmed
  name: uv-build
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
  softwareVersion: '[''0.10.9'']'
  url: https://pypi.org/project/uv-build
---
# uv-build



This package is a slimmed down version of uv containing only the build backend.
See:
https://pypi.org/project/uv/
and
https://docs.astral.sh/uv/
for the main project package and documentation.


<small>homepage: </small><span class="software-link">[https://pypi.org/project/uv-build](https://pypi.org/project/uv-build)</span>

## Available installations


|uv-build version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.10.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`uv-build/0.10.9-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in uv-build installations


### uv-build


|`uv-build` version|uv-build modules that include it|
| --- | --- |
|0.10.9|`uv-build/0.10.9-GCCcore-14.3.0`|