---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Libint library is used to evaluate the traditional (electron repulsion)\
    \ and certain novel two-body\n matrix elements (integrals) over Cartesian Gaussian\
    \ functions used in modern atomic and molecular theory."
  license: Not confirmed
  name: Libint
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
  softwareVersion: '[''2.7.2'']'
  url: https://github.com/evaleev/libint
---
# Libint


Libint library is used to evaluate the traditional (electron repulsion) and certain novel two-body
 matrix elements (integrals) over Cartesian Gaussian functions used in modern atomic and molecular theory.

<small>homepage: </small><span class="software-link">[https://github.com/evaleev/libint](https://github.com/evaleev/libint)</span>

## Available installations


|Libint version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.7.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Libint/2.7.2-GCC-12.3.0-lmax-6-cp2k`|