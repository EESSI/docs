---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The GLPK (GNU Linear Programming Kit) package is intended for solving
    large-scale linear programming (LP), mixed integer programming (MIP), and other
    related problems. It is a set of routines written in ANSI C and organized in the
    form of a callable library.
  license: Not confirmed
  name: GLPK
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
  softwareVersion: '[''GLPK/5.0-GCCcore-12.2.0'', ''GLPK/5.0-GCCcore-12.3.0'', ''GLPK/5.0-GCCcore-13.2.0'']'
  url: https://www.gnu.org/software/glpk/
---

GLPK
====


The GLPK (GNU Linear Programming Kit) package is intended for solving large-scale linear programming (LP), mixed integer programming (MIP), and other related problems. It is a set of routines written in ANSI C and organized in the form of a callable library.

https://www.gnu.org/software/glpk/
# Available modules


The overview below shows which GLPK installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GLPK, load one of these modules using a `module load` command like:

```shell
module load GLPK/5.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GLPK/5.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|GLPK/5.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|GLPK/5.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
