---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "PLUMED is an open source library for free energy calculations in molecular\
    \ systems which\n works together with some of the most popular molecular dynamics\
    \ engines. Free energy calculations can be\n performed as a function of many order\
    \ parameters with a particular  focus on biological problems, using\n state of\
    \ the art methods such as metadynamics, umbrella sampling and Jarzynski-equation\
    \ based steered MD.\n The software, written in C++, can be easily interfaced with\
    \ both fortran and C/C++ codes.\n"
  license: Not confirmed
  name: PLUMED
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
  softwareVersion: '[''2.9.4'']'
  url: https://www.plumed.org
---
# PLUMED


PLUMED is an open source library for free energy calculations in molecular systems which
 works together with some of the most popular molecular dynamics engines. Free energy calculations can be
 performed as a function of many order parameters with a particular  focus on biological problems, using
 state of the art methods such as metadynamics, umbrella sampling and Jarzynski-equation based steered MD.
 The software, written in C++, can be easily interfaced with both fortran and C/C++ codes.


<small>homepage: </small><span class="software-link">[https://www.plumed.org](https://www.plumed.org)</span>

## Available installations


|PLUMED version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.9.4|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PLUMED/2.9.4-foss-2025b`|