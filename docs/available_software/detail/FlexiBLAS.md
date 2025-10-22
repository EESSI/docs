---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: FlexiBLAS is a wrapper library that enables the exchange of the BLAS
    and LAPACK implementationused by a program without recompiling or relinking it.
  license: Not confirmed
  name: FlexiBLAS
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
  softwareVersion: '[''FlexiBLAS/3.2.1-GCC-12.2.0'', ''FlexiBLAS/3.3.1-GCC-12.3.0'',
    ''FlexiBLAS/3.3.1-GCC-13.2.0'']'
  url: https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release
---

FlexiBLAS
=========


FlexiBLAS is a wrapper library that enables the exchange of the BLAS and LAPACK implementationused by a program without recompiling or relinking it.

https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release
# Available modules


The overview below shows which FlexiBLAS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using FlexiBLAS, load one of these modules using a `module load` command like:

```shell
module load FlexiBLAS/3.3.1-GCC-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|FlexiBLAS/3.3.1-GCC-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|FlexiBLAS/3.3.1-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|FlexiBLAS/3.2.1-GCC-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
