---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Software package and libraries for sequential and parallel graph partitioning,static
    mapping, and sparse matrix block ordering, and sequential mesh and hypergraph
    partitioning.
  license: Not confirmed
  name: SCOTCH
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
  softwareVersion: '[''SCOTCH/7.0.3-gompi-2022b'', ''SCOTCH/7.0.3-gompi-2023a'']'
  url: https://www.labri.fr/perso/pelegrin/scotch/
---

SCOTCH
======


Software package and libraries for sequential and parallel graph partitioning,static mapping, and sparse matrix block ordering, and sequential mesh and hypergraph partitioning.

https://www.labri.fr/perso/pelegrin/scotch/
# Available modules


The overview below shows which SCOTCH installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using SCOTCH, load one of these modules using a `module load` command like:

```shell
module load SCOTCH/7.0.3-gompi-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|SCOTCH/7.0.3-gompi-2023a|x|x|x|x|x|x|x|x|x|
|SCOTCH/7.0.3-gompi-2022b|x|x|x|x|x|x|x|x|x|
