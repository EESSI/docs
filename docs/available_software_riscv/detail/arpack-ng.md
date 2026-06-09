---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ARPACK is a collection of Fortran77 subroutines designed to solve large
    scale eigenvalue problems.
  license: Not confirmed
  name: arpack-ng
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
  softwareVersion: '[''3.9.1'']'
  url: https://github.com/opencollab/arpack-ng
---
# arpack-ng


ARPACK is a collection of Fortran77 subroutines designed to solve large scale eigenvalue problems.

<small>homepage: </small><span class="software-link">[https://github.com/opencollab/arpack-ng](https://github.com/opencollab/arpack-ng)</span>

## Available installations


|arpack-ng version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.9.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`arpack-ng/3.9.1-foss-2025b`|