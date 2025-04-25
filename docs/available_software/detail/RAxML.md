---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: RAxML search algorithm for maximum likelihood based inference of phylogenetic
    trees.
  license: Not confirmed
  name: RAxML
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
  softwareVersion: '[''RAxML/8.2.13-gompi-2023a-avx2'', ''RAxML/8.2.13-gompi-2023a-standard'']'
  url: https://github.com/stamatak/standard-RAxML
---

RAxML
=====


RAxML search algorithm for maximum likelihood based inference of phylogenetic trees.

https://github.com/stamatak/standard-RAxML
# Available modules


The overview below shows which RAxML installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using RAxML, load one of these modules using a `module load` command like:

```shell
module load RAxML/8.2.13-gompi-2023a-standard
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|RAxML/8.2.13-gompi-2023a-standard|x|x|x|-|-|-|-|-|-|-|x|
|RAxML/8.2.13-gompi-2023a-avx2|-|-|-|x|x|x|x|x|x|x|-|
