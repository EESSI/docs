---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The primary goal of libunwind is to define a portable and efficient\
    \ C programming interface\n (API) to determine the call-chain of a program. The\
    \ API additionally provides the means to manipulate the\n preserved (callee-saved)\
    \ state of each call-frame and to resume execution at any point in the call-chain\n\
    \ (non-local goto). The API supports both local (same-process) and remote (across-process)\
    \ operation.\n As such, the API is useful in a number of applications"
  license: Not confirmed
  name: libunwind
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
  softwareVersion: '[''1.8.2'']'
  url: https://www.nongnu.org/libunwind/
---
# libunwind


The primary goal of libunwind is to define a portable and efficient C programming interface
 (API) to determine the call-chain of a program. The API additionally provides the means to manipulate the
 preserved (callee-saved) state of each call-frame and to resume execution at any point in the call-chain
 (non-local goto). The API supports both local (same-process) and remote (across-process) operation.
 As such, the API is useful in a number of applications

<small>homepage: </small><span class="software-link">[https://www.nongnu.org/libunwind/](https://www.nongnu.org/libunwind/)</span>

## Available installations


|libunwind version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.8.2|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libunwind/1.8.2-GCCcore-14.3.0`|