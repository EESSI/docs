---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: SLEPc (Scalable Library for Eigenvalue Problem Computations) is a software
    library for the solution of large scale sparse eigenvalue problems on parallel
    computers. It is an extension of PETSc and can be used for either standard or
    generalized eigenproblems, with real or complex arithmetic. It can also be used
    for computing a partial SVD of a large, sparse, rectangular matrix, and to solve
    quadratic eigenvalue problems.
  license: Not confirmed
  name: SLEPc
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
  softwareVersion: '[''SLEPc/3.20.1-foss-2023a'']'
  url: https://slepc.upv.es
---

SLEPc
=====


SLEPc (Scalable Library for Eigenvalue Problem Computations) is a software library for the solution of large scale sparse eigenvalue problems on parallel computers. It is an extension of PETSc and can be used for either standard or generalized eigenproblems, with real or complex arithmetic. It can also be used for computing a partial SVD of a large, sparse, rectangular matrix, and to solve quadratic eigenvalue problems.

https://slepc.upv.es
# Available modules


The overview below shows which SLEPc installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using SLEPc, load one of these modules using a `module load` command like:

```shell
module load SLEPc/3.20.1-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|SLEPc/3.20.1-foss-2023a|x|x|x|x|x|x|x|x|x|x|
