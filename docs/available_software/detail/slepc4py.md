---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Python bindings for SLEPc, the Scalable Library for Eigenvalue Problem
    Computations.
  license: Not confirmed
  name: slepc4py
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
  softwareVersion: '[''3.22.2'']'
  url: https://bitbucket.org/slepc/slepc4py
---
# slepc4py


Python bindings for SLEPc, the Scalable Library for Eigenvalue Problem Computations.

<small>homepage: </small><span class="software-link">[https://bitbucket.org/slepc/slepc4py](https://bitbucket.org/slepc/slepc4py)</span>

## Available installations


|slepc4py version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.22.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`slepc4py/3.22.2-foss-2023b`|