---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Tensile is a tool for creating benchmark-driven backend libraries
    for

    GEMMs, GEMM-like problems (such as batched GEMM), and general N-dimensional tensor

    contractions on a GPU. The Tensile library is mainly used as a backend library
    for rocBLAS.

    Tensile acts as the performance backbone for a wide variety of ''compute'' applications

    running on AMD GPUs.'
  license: Not confirmed
  name: Tensile
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
  softwareVersion: '[''4.43.0'']'
  url: https://github.com/ROCm/Tensile
---
# Tensile


Tensile is a tool for creating benchmark-driven backend libraries for
GEMMs, GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as a backend library for rocBLAS.
Tensile acts as the performance backbone for a wide variety of 'compute' applications
running on AMD GPUs.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/Tensile](https://github.com/ROCm/Tensile)</span>

## Available installations


|Tensile version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.43.0|`generic`: `x86_64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-amd">AMD</span>: `gfx1030`, `gfx1100`, `gfx1101`, `gfx1200`, `gfx1201`, `gfx908`, `gfx90a`, `gfx942`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`Tensile/4.43.0-rocm-compilers-19.0.0-ROCm-6.4.1`|

## Extensions

Overview of extensions included in Tensile installations


### joblib


|`joblib` version|Tensile modules that include it|
| --- | --- |
|1.5.1|`Tensile/4.43.0-rocm-compilers-19.0.0-ROCm-6.4.1`|

### msgpack


|`msgpack` version|Tensile modules that include it|
| --- | --- |
|1.1.1|`Tensile/4.43.0-rocm-compilers-19.0.0-ROCm-6.4.1`|

### rich


|`rich` version|Tensile modules that include it|
| --- | --- |
|14.0.0|`Tensile/4.43.0-rocm-compilers-19.0.0-ROCm-6.4.1`|

### Tensile


|`Tensile` version|Tensile modules that include it|
| --- | --- |
|4.43.0|`Tensile/4.43.0-rocm-compilers-19.0.0-ROCm-6.4.1`|