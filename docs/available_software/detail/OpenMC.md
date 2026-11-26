---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "OpenMC is a community-developed Monte Carlo neutron and photon transport\
    \ simulation code.\n It is capable of performing fixed source, k-eigenvalue, and\
    \ subcritical multiplication calculations on\n models built using either a constructive\
    \ solid geometry or CAD representation. OpenMC supports both\n continuous-energy\
    \ and multigroup transport."
  license: Not confirmed
  name: OpenMC
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
  softwareVersion: '[''0.15.3'']'
  url: https://openmc.org
---
# OpenMC


OpenMC is a community-developed Monte Carlo neutron and photon transport simulation code.
 It is capable of performing fixed source, k-eigenvalue, and subcritical multiplication calculations on
 models built using either a constructive solid geometry or CAD representation. OpenMC supports both
 continuous-energy and multigroup transport.

<small>homepage: </small><span class="software-link">[https://openmc.org](https://openmc.org)</span>

## Available installations


|OpenMC version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.15.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OpenMC/0.15.3-foss-2025b`|

## Extensions

Overview of extensions included in OpenMC installations


### endf


|`endf` version|OpenMC modules that include it|
| --- | --- |
|0.1.12|`OpenMC/0.15.3-foss-2025b`|

### openmc


|`openmc` version|OpenMC modules that include it|
| --- | --- |
|0.15.3|`OpenMC/0.15.3-foss-2025b`|