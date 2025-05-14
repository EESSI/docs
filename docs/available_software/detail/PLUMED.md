---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: PLUMED is an open source library for free energy calculations in molecular
    systems which works together with some of the most popular molecular dynamics
    engines. Free energy calculations can be performed as a function of many order
    parameters with a particular  focus on biological problems, using state of the
    art methods such as metadynamics, umbrella sampling and Jarzynski-equation based
    steered MD. The software, written in C++, can be easily interfaced with both fortran
    and C/C++ codes.
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
  softwareVersion: '[''PLUMED/2.9.0-foss-2023a'', ''PLUMED/2.9.2-foss-2023b'']'
  url: https://www.plumed.org
---

PLUMED
======


PLUMED is an open source library for free energy calculations in molecular systems which works together with some of the most popular molecular dynamics engines. Free energy calculations can be performed as a function of many order parameters with a particular  focus on biological problems, using state of the art methods such as metadynamics, umbrella sampling and Jarzynski-equation based steered MD. The software, written in C++, can be easily interfaced with both fortran and C/C++ codes.

https://www.plumed.org
# Available modules


The overview below shows which PLUMED installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PLUMED, load one of these modules using a `module load` command like:

```shell
module load PLUMED/2.9.2-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PLUMED/2.9.2-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|
|PLUMED/2.9.0-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|
