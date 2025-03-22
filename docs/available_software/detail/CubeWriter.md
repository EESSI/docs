---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Cube, which is used as performance report explorer for Scalasca and
    Score-P, is a generic tool for displaying a multi-dimensional performance space
    consisting of the dimensions (i) performance metric, (ii) call path, and (iii)
    system resource. Each dimension can be represented as a tree, where non-leaf nodes
    of the tree can be collapsed or expanded to achieve the desired level of granularity.
    This module provides the Cube high-performance C writer library component.
  license: Not confirmed
  name: CubeWriter
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
  softwareVersion: '[''CubeWriter/4.8.2-GCCcore-13.2.0'']'
  url: https://www.scalasca.org/software/cube-4.x/download.html
---

CubeWriter
==========


Cube, which is used as performance report explorer for Scalasca and Score-P, is a generic tool for displaying a multi-dimensional performance space consisting of the dimensions (i) performance metric, (ii) call path, and (iii) system resource. Each dimension can be represented as a tree, where non-leaf nodes of the tree can be collapsed or expanded to achieve the desired level of granularity. This module provides the Cube high-performance C writer library component.

https://www.scalasca.org/software/cube-4.x/download.html
# Available modules


The overview below shows which CubeWriter installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using CubeWriter, load one of these modules using a `module load` command like:

```shell
module load CubeWriter/4.8.2-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|CubeWriter/4.8.2-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|
