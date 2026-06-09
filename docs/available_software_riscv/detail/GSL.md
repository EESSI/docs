---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The GNU Scientific Library (GSL) is a numerical library for C and\
    \ C++ programmers.\n The library provides a wide range of mathematical routines\
    \ such as random number generators, special functions\n and least-squares fitting."
  license: Not confirmed
  name: GSL
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
  softwareVersion: '[''2.8'']'
  url: https://www.gnu.org/software/gsl/
---
# GSL


The GNU Scientific Library (GSL) is a numerical library for C and C++ programmers.
 The library provides a wide range of mathematical routines such as random number generators, special functions
 and least-squares fitting.

<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/gsl/](https://www.gnu.org/software/gsl/)</span>

## Available installations


|GSL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.8|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`GSL/2.8-GCC-14.3.0`|