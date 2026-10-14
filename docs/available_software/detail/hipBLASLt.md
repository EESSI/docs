---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'hipBLASLt is a library that provides general matrix-matrix operations.

    It has a flexible API that extends functionalities beyond a traditional BLAS library,

    such as adding flexibility to matrix data layouts, input types, compute types,
    and

    algorithmic implementations and heuristics.'
  license: Not confirmed
  name: hipBLASLt
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
  softwareVersion: '[''0.12.1'']'
  url: https://github.com/ROCm/hipBLASLt
---
# hipBLASLt


hipBLASLt is a library that provides general matrix-matrix operations.
It has a flexible API that extends functionalities beyond a traditional BLAS library,
such as adding flexibility to matrix data layouts, input types, compute types, and
algorithmic implementations and heuristics.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/hipBLASLt](https://github.com/ROCm/hipBLASLt)</span>

## Available installations


|hipBLASLt version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.12.1|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`hipBLASLt/0.12.1-rocm-compilers-19.0.0-ROCm-6.4.1`|