---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Berkeley DB enables the development of custom data management solutions,
    without the overhead traditionally associated with such custom projects.
  license: Not confirmed
  name: DB
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
  softwareVersion: '[''DB/18.1.40-GCCcore-12.2.0'', ''DB/18.1.40-GCCcore-12.3.0'']'
  url: https://www.oracle.com/technetwork/products/berkeleydb
---

DB
==


Berkeley DB enables the development of custom data management solutions, without the overhead traditionally associated with such custom projects.

https://www.oracle.com/technetwork/products/berkeleydb
# Available modules


The overview below shows which DB installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using DB, load one of these modules using a `module load` command like:

```shell
module load DB/18.1.40-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|DB/18.1.40-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|
|DB/18.1.40-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|
