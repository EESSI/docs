---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: petsc4py are Python bindings for PETSc, the Portable, Extensible Toolchain
    for Scientific Computation.
  license: Not confirmed
  name: petsc4py
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
  softwareVersion: '[''3.22.5'']'
  url: https://gitlab.com/petsc/petsc
---
# petsc4py


petsc4py are Python bindings for PETSc, the Portable, Extensible Toolchain for Scientific Computation.

<small>homepage: </small><span class="software-link">[https://gitlab.com/petsc/petsc](https://gitlab.com/petsc/petsc)</span>

## Available installations


|petsc4py version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.22.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`petsc4py/3.22.5-foss-2023b`|