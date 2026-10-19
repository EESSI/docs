---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'CheMPS2 is a scientific library which contains a spin-adapted implementation
    of the

    density matrix renormalization group (DMRG) for ab initio quantum chemistry.'
  license: Not confirmed
  name: CheMPS2
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
  url: https://github.com/SebWouters/CheMPS2
---
# CheMPS2


CheMPS2 is a scientific library which contains a spin-adapted implementation of the
density matrix renormalization group (DMRG) for ab initio quantum chemistry.

<small>homepage: </small><span class="software-link">[https://github.com/SebWouters/CheMPS2](https://github.com/SebWouters/CheMPS2)</span>

## Available installations


|CheMPS2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.8.12|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`CheMPS2/1.8.12-foss-2025a`|