---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GNU Compiler Collection (GCC) based compiler toolchain, including OpenMPI
    for MPI support.
  license: Not confirmed
  name: gompi
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
  softwareVersion: '[''gompi/2022b'', ''gompi/2023a'', ''gompi/2023b'']'
  url: (none)
---

gompi
=====


GNU Compiler Collection (GCC) based compiler toolchain, including OpenMPI for MPI support.

(none)
# Available modules


The overview below shows which gompi installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using gompi, load one of these modules using a `module load` command like:

```shell
module load gompi/2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|gompi/2023b|x|x|x|x|x|x|x|x|x|x|x|
|gompi/2023a|x|x|x|x|x|x|x|x|x|x|x|
|gompi/2022b|x|x|x|x|x|x|x|x|x|x|x|
