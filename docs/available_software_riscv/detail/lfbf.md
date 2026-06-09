---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "LLVM based compiler toolchain, including\n FlexiBLAS (BLAS and LAPACK\
    \ support) and (serial) FFTW."
  license: Not confirmed
  name: lfbf
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
  softwareVersion: '[''2025b'']'
  url: (none)
---
# lfbf


LLVM based compiler toolchain, including
 FlexiBLAS (BLAS and LAPACK support) and (serial) FFTW.

<small>homepage: </small><span class="software-link">[(none)]((none))</span>

## Available installations


|lfbf version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2025b|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`lfbf/2025b`|