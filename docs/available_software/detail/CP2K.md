---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "CP2K is a freely available (GPL) program, written in Fortran 95, to\
    \ perform atomistic and molecular\n simulations of solid state, liquid, molecular\
    \ and biological systems. It provides a general framework for different\n methods\
    \ such as e.g. density functional theory (DFT) using a mixed Gaussian and plane\
    \ waves approach (GPW), and\n classical pair and many-body potentials. "
  license: Not confirmed
  name: CP2K
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
  softwareVersion: '[''2023.1'']'
  url: https://www.cp2k.org/
---
# CP2K


CP2K is a freely available (GPL) program, written in Fortran 95, to perform atomistic and molecular
 simulations of solid state, liquid, molecular and biological systems. It provides a general framework for different
 methods such as e.g. density functional theory (DFT) using a mixed Gaussian and plane waves approach (GPW), and
 classical pair and many-body potentials. 

<small>homepage: </small><span class="software-link">[https://www.cp2k.org/](https://www.cp2k.org/)</span>

## Available installations


|CP2K version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2023.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`CP2K/2023.1-foss-2023a`|