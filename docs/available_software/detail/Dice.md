---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Dice contains code for performing SHCI, VMC, GFMC, DMC, FCIQMC, stochastic
    MRCI

    and SC-NEVPT2, and AFQMC calculations with a focus on ab initio systems.'
  license: Not confirmed
  name: Dice
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
  softwareVersion: '[''20250615'']'
  url: https://github.com/sanshar/Dice
---
# Dice


Dice contains code for performing SHCI, VMC, GFMC, DMC, FCIQMC, stochastic MRCI
and SC-NEVPT2, and AFQMC calculations with a focus on ab initio systems.

<small>homepage: </small><span class="software-link">[https://github.com/sanshar/Dice](https://github.com/sanshar/Dice)</span>

## Available installations


|Dice version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|20250615|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Dice/20250615-foss-2025a`|