---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'rocBLAS is the ROCm Basic Linear Algebra Subprograms (BLAS) library.

    rocBLAS is implemented in the HIP programming language and optimized for AMD GPUs.'
  license: Not confirmed
  name: rocBLAS
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
  softwareVersion: '[''4.4.0'']'
  url: https://github.com/ROCm/rocBLAS
---
# rocBLAS


rocBLAS is the ROCm Basic Linear Algebra Subprograms (BLAS) library.
rocBLAS is implemented in the HIP programming language and optimized for AMD GPUs.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/rocBLAS](https://github.com/ROCm/rocBLAS)</span>

## Available installations


|rocBLAS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.4.0|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`rocBLAS/4.4.0-rocm-compilers-19.0.0-ROCm-6.4.1`|