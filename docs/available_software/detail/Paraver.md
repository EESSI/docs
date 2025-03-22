---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A very powerful performance visualization and analysis tool based on
    traces that can be used to analyse any information that is expressed on its input
    trace format. Traces for parallel MPI, OpenMP and other programs can be genereated
    with Extrae.
  license: Not confirmed
  name: Paraver
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
  softwareVersion: '[''Paraver/4.11.4-GCC-12.3.0'']'
  url: https://tools.bsc.es/paraver
---

Paraver
=======


A very powerful performance visualization and analysis tool based on traces that can be used to analyse any information that is expressed on its input trace format. Traces for parallel MPI, OpenMP and other programs can be genereated with Extrae.

https://tools.bsc.es/paraver
# Available modules


The overview below shows which Paraver installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Paraver, load one of these modules using a `module load` command like:

```shell
module load Paraver/4.11.4-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Paraver/4.11.4-GCC-12.3.0|x|x|x|-|x|x|x|x|x|x|x|
