---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: DLB is a dynamic library designed to speed up HPC hybrid applications
    (i.e.,two levels of parallelism) by improving the load balance of the outer level
    ofparallelism (e.g., MPI) by dynamically redistributing the computationalresources
    at the inner level of parallelism (e.g., OpenMP). at run time.
  license: Not confirmed
  name: dlb
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
  softwareVersion: '[''dlb/3.4-gompi-2023b'']'
  url: https://pm.bsc.es/dlb/
---

dlb
===


DLB is a dynamic library designed to speed up HPC hybrid applications (i.e.,two levels of parallelism) by improving the load balance of the outer level ofparallelism (e.g., MPI) by dynamically redistributing the computationalresources at the inner level of parallelism (e.g., OpenMP). at run time.

https://pm.bsc.es/dlb/
# Available modules


The overview below shows which dlb installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using dlb, load one of these modules using a `module load` command like:

```shell
module load dlb/3.4-gompi-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|dlb/3.4-gompi-2023b|x|x|x|x|x|x|x|x|-|x|
