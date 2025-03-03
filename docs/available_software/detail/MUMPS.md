---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A parallel sparse direct solver
  license: Not confirmed
  name: MUMPS
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
  softwareVersion: '[''MUMPS/5.6.1-foss-2022b-metis'', ''MUMPS/5.6.1-foss-2023a-metis'']'
  url: https://graal.ens-lyon.fr/MUMPS/
---

MUMPS
=====


A parallel sparse direct solver

https://graal.ens-lyon.fr/MUMPS/
# Available modules


The overview below shows which MUMPS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using MUMPS, load one of these modules using a `module load` command like:

```shell
module load MUMPS/5.6.1-foss-2023a-metis
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MUMPS/5.6.1-foss-2023a-metis|x|x|x|x|x|x|x|x|x|x|
|MUMPS/5.6.1-foss-2022b-metis|x|x|x|x|x|x|x|x|x|x|
