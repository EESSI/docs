---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Spglib for Python. Spglib is a library for finding and handling crystal
    symmetries written in C.
  license: Not confirmed
  name: spglib-python
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
  softwareVersion: '[''2.6.0'', ''2.1.0'', ''2.0.2'']'
  url: https://pypi.python.org/pypi/spglib
---
# spglib-python


Spglib for Python. Spglib is a library for finding and handling crystal symmetries written in C.

<small>homepage: </small><span class="software-link">[https://pypi.python.org/pypi/spglib](https://pypi.python.org/pypi/spglib)</span>

## Available installations


|spglib-python version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`spglib-python/2.0.2-gfbf-2022b`|
|2.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`spglib-python/2.1.0-gfbf-2023a`|
|2.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`spglib-python/2.6.0-gfbf-2025a`|

## Extensions

Overview of extensions included in spglib-python installations


### pyproject-metadata


|`pyproject-metadata` version|spglib-python modules that include it|
| --- | --- |
|0.7.1|`spglib-python/2.1.0-gfbf-2023a`|

### pyproject_metadata


|`pyproject_metadata` version|spglib-python modules that include it|
| --- | --- |
|0.9.1|`spglib-python/2.6.0-gfbf-2025a`|

### spglib


|`spglib` version|spglib-python modules that include it|
| --- | --- |
|2.1.0|`spglib-python/2.1.0-gfbf-2023a`|
|2.6.0|`spglib-python/2.6.0-gfbf-2025a`|