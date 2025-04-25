---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GNU Compiler Collection (GCC) based compiler toolchain, including OpenMPI
    for MPI support, OpenBLAS (BLAS and LAPACK support), FFTW and ScaLAPACK.
  license: Not confirmed
  name: foss
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
  softwareVersion: '[''foss/2022b'', ''foss/2023a'', ''foss/2023b'']'
  url: https://easybuild.readthedocs.io/en/master/Common-toolchains.html#foss-toolchain
---

foss
====


GNU Compiler Collection (GCC) based compiler toolchain, including OpenMPI for MPI support, OpenBLAS (BLAS and LAPACK support), FFTW and ScaLAPACK.

https://easybuild.readthedocs.io/en/master/Common-toolchains.html#foss-toolchain
# Available modules


The overview below shows which foss installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using foss, load one of these modules using a `module load` command like:

```shell
module load foss/2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|foss/2023b|x|x|x|x|x|x|x|x|x|x|x|
|foss/2023a|x|x|x|x|x|x|x|x|x|x|x|
|foss/2022b|x|x|x|x|x|x|x|x|x|x|x|
