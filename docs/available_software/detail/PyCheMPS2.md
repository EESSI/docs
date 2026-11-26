---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'PyCheMPS2 is a python interface to CheMPS2, for compilation without

    MPI. CheMPS2 is a scientific library which contains a spin-adapted

    implementation of the density matrix renormalization group (DMRG)

    for ab initio quantum chemistry.'
  license: Not confirmed
  name: PyCheMPS2
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
  softwareVersion: '[''1.8.12'']'
  url: https://sebwouters.github.io/CheMPS2
---
# PyCheMPS2


PyCheMPS2 is a python interface to CheMPS2, for compilation without
MPI. CheMPS2 is a scientific library which contains a spin-adapted
implementation of the density matrix renormalization group (DMRG)
for ab initio quantum chemistry.

<small>homepage: </small><span class="software-link">[https://sebwouters.github.io/CheMPS2](https://sebwouters.github.io/CheMPS2)</span>

## Available installations


|PyCheMPS2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.8.12|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PyCheMPS2/1.8.12-foss-2025a`|

## Extensions

Overview of extensions included in PyCheMPS2 installations


### PyCheMPS2


|`PyCheMPS2` version|PyCheMPS2 modules that include it|
| --- | --- |
|1.8.12|`PyCheMPS2/1.8.12-foss-2025a`|