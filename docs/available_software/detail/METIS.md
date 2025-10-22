---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: METIS is a set of serial programs for partitioning graphs, partitioning
    finite element meshes, and producing fill reducing orderings for sparse matrices.
    The algorithms implemented in METIS are based on the multilevel recursive-bisection,
    multilevel k-way, and multi-constraint partitioning schemes.
  license: Not confirmed
  name: METIS
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
  softwareVersion: '[''METIS/5.1.0-GCCcore-12.2.0'', ''METIS/5.1.0-GCCcore-12.3.0'',
    ''METIS/5.1.0-GCCcore-13.2.0'']'
  url: https://karypis.github.io/glaros/projects/gp.html
---

METIS
=====


METIS is a set of serial programs for partitioning graphs, partitioning finite element meshes, and producing fill reducing orderings for sparse matrices. The algorithms implemented in METIS are based on the multilevel recursive-bisection, multilevel k-way, and multi-constraint partitioning schemes.

https://karypis.github.io/glaros/projects/gp.html
# Available modules


The overview below shows which METIS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using METIS, load one of these modules using a `module load` command like:

```shell
module load METIS/5.1.0-GCCcore-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|METIS/5.1.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|METIS/5.1.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|METIS/5.1.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
