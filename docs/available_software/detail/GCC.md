---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The GNU Compiler Collection includes front ends for C, C++, Objective-C,
    Fortran, Java, and Ada, as well as libraries for these languages (libstdc++, libgcj,...).
  license: Not confirmed
  name: GCC
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
  softwareVersion: '[''GCC/12.2.0'', ''GCC/12.3.0'', ''GCC/13.2.0'']'
  url: https://gcc.gnu.org/
---

GCC
===


The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, and Ada, as well as libraries for these languages (libstdc++, libgcj,...).

https://gcc.gnu.org/
# Available modules


The overview below shows which GCC installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GCC, load one of these modules using a `module load` command like:

```shell
module load GCC/13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GCC/13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|GCC/12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|GCC/12.2.0|x|x|x|x|x|x|x|x|x|x|x|
