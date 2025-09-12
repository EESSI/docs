---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Osi (Open Solver Interface) provides an abstract base class to a generic
    linearprogramming (LP) solver, along with derived classes for specific solvers.
    Manyapplications may be able to use the Osi to insulate themselves from a specificLP
    solver. That is, programs written to the OSI standard may be linked to anysolver
    with an OSI interface and should produce correct results. The OSI hasbeen significantly
    extended compared to its first incarnation. Currently, theOSI supports linear
    programming solvers and has rudimentary support for integerprogramming.
  license: Not confirmed
  name: Osi
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
  softwareVersion: '[''Osi/0.108.9-GCC-12.3.0'']'
  url: https://github.com/coin-or/Osi
---

Osi
===


Osi (Open Solver Interface) provides an abstract base class to a generic linearprogramming (LP) solver, along with derived classes for specific solvers. Manyapplications may be able to use the Osi to insulate themselves from a specificLP solver. That is, programs written to the OSI standard may be linked to anysolver with an OSI interface and should produce correct results. The OSI hasbeen significantly extended compared to its first incarnation. Currently, theOSI supports linear programming solvers and has rudimentary support for integerprogramming.

https://github.com/coin-or/Osi
# Available modules


The overview below shows which Osi installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Osi, load one of these modules using a `module load` command like:

```shell
module load Osi/0.108.9-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Osi/0.108.9-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
