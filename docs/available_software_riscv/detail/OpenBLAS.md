---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.
  license: Not confirmed
  name: OpenBLAS
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
  softwareVersion: '[''0.3.30'', ''0.3.29'']'
  url: https://www.openblas.net/
---
# OpenBLAS


OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

<small>homepage: </small><span class="software-link">[https://www.openblas.net/](https://www.openblas.net/)</span>

## Available installations


|OpenBLAS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.3.30|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OpenBLAS/0.3.30-GCC-14.3.0`|
|0.3.30|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OpenBLAS/0.3.30-llvm-compilers-20.1.8`|
|0.3.29|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OpenBLAS/0.3.29-GCC-14.2.0`|