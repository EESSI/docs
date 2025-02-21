---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Open MPI Project is an open source MPI-3 implementation.
  license: Not confirmed
  name: OpenMPI
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
  softwareVersion: '[''OpenMPI/4.1.4-GCC-12.2.0'', ''OpenMPI/4.1.5-GCC-12.3.0'', ''OpenMPI/4.1.6-GCC-13.2.0'']'
  url: https://www.open-mpi.org/
---

OpenMPI
=======


The Open MPI Project is an open source MPI-3 implementation.

https://www.open-mpi.org/
# Available modules


The overview below shows which OpenMPI installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using OpenMPI, load one of these modules using a `module load` command like:

```shell
module load OpenMPI/4.1.6-GCC-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|OpenMPI/4.1.6-GCC-13.2.0|x|x|x|x|x|x|x|x|-|x|
|OpenMPI/4.1.5-GCC-12.3.0|x|x|x|x|x|x|x|x|-|x|
|OpenMPI/4.1.4-GCC-12.2.0|x|x|x|x|x|x|x|x|-|x|
