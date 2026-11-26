---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Python wrappers to the C++ library SymEngine, a fast C++ symbolic manipulation
    library.
  license: Not confirmed
  name: SymEngine-python
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
  softwareVersion: '[''0.14.0'']'
  url: https://github.com/symengine/symengine.py
---
# SymEngine-python


Python wrappers to the C++ library SymEngine, a fast C++ symbolic manipulation library.

<small>homepage: </small><span class="software-link">[https://github.com/symengine/symengine.py](https://github.com/symengine/symengine.py)</span>

## Available installations


|SymEngine-python version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.14.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`SymEngine-python/0.14.0-gfbf-2025b`|

## Extensions

Overview of extensions included in SymEngine-python installations


### symengine


|`symengine` version|SymEngine-python modules that include it|
| --- | --- |
|0.14.0|`SymEngine-python/0.14.0-gfbf-2025b`|