---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Provides a Python interface to GPU management and monitoring functions.

    This is a wrapper around the NVML library.'
  license: Not confirmed
  name: pyNVML
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
  softwareVersion: '[''13.590.48'']'
  url: https://pypi.org/project/nvidia-ml-py
---
# pyNVML


Provides a Python interface to GPU management and monitoring functions.
This is a wrapper around the NVML library.

<small>homepage: </small><span class="software-link">[https://pypi.org/project/nvidia-ml-py](https://pypi.org/project/nvidia-ml-py)</span>

## Available installations


|pyNVML version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|13.590.48|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`pyNVML/13.590.48-GCCcore-14.2.0`|

## Extensions

Overview of extensions included in pyNVML installations


### nvidia-ml-py


|`nvidia-ml-py` version|pyNVML modules that include it|
| --- | --- |
|13.590.48|`pyNVML/13.590.48-GCCcore-14.2.0`|