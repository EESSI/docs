---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Eigen is a C++ template library for linear algebra: matrices, vectors,
    numerical solvers, and related algorithms.'
  license: Not confirmed
  name: Eigen
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
  softwareVersion: '[''Eigen/3.4.0-GCCcore-12.2.0'', ''Eigen/3.4.0-GCCcore-12.3.0'',
    ''Eigen/3.4.0-GCCcore-13.2.0'']'
  url: https://eigen.tuxfamily.org
---

Eigen
=====


Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

https://eigen.tuxfamily.org
# Available modules


The overview below shows which Eigen installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Eigen, load one of these modules using a `module load` command like:

```shell
module load Eigen/3.4.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Eigen/3.4.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|
|Eigen/3.4.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|
|Eigen/3.4.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|
