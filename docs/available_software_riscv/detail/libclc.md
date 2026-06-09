---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    libclc is an open source, BSD/MIT dual licensed implementation of the library
    requirements of the OpenCL

    C programming language, as specified by the OpenCL 1.1 Specification.

    '
  license: Not confirmed
  name: libclc
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
  softwareVersion: '[''20.1.8'']'
  url: https://libclc.llvm.org/
---
# libclc



libclc is an open source, BSD/MIT dual licensed implementation of the library requirements of the OpenCL
C programming language, as specified by the OpenCL 1.1 Specification.


<small>homepage: </small><span class="software-link">[https://libclc.llvm.org/](https://libclc.llvm.org/)</span>

## Available installations


|libclc version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|20.1.8|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libclc/20.1.8-GCCcore-14.3.0`|