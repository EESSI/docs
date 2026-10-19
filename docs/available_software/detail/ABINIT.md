---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    ABINIT is a package whose main program allows one to find the total energy, charge
    density and electronic structure of

    systems made of electrons and nuclei (molecules and periodic solids) within Density
    Functional Theory (DFT), using

    pseudopotentials and a planewave or wavelet basis.

    '
  license: Not confirmed
  name: ABINIT
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
  softwareVersion: '[''10.4.7'']'
  url: https://www.abinit.org/
---
# ABINIT



ABINIT is a package whose main program allows one to find the total energy, charge density and electronic structure of
systems made of electrons and nuclei (molecules and periodic solids) within Density Functional Theory (DFT), using
pseudopotentials and a planewave or wavelet basis.


<small>homepage: </small><span class="software-link">[https://www.abinit.org/](https://www.abinit.org/)</span>

## Available installations


|ABINIT version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|10.4.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ABINIT/10.4.7-foss-2025b`|