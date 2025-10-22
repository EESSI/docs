---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ParMETIS is an MPI-based parallel library that implements a variety
    of algorithms for partitioning unstructured graphs, meshes, and for computing
    fill-reducing orderings of sparse matrices. ParMETIS extends the functionality
    provided by METIS and includes routines that are especially suited for parallel
    AMR computations and large scale numerical simulations. The algorithms implemented
    in ParMETIS are based on the parallel multilevel k-way graph-partitioning, adaptive
    repartitioning, and parallel multi-constrained partitioning schemes.
  license: Not confirmed
  name: ParMETIS
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
  softwareVersion: '[''ParMETIS/4.0.3-gompi-2023b'']'
  url: http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview
---

ParMETIS
========


ParMETIS is an MPI-based parallel library that implements a variety of algorithms for partitioning unstructured graphs, meshes, and for computing fill-reducing orderings of sparse matrices. ParMETIS extends the functionality provided by METIS and includes routines that are especially suited for parallel AMR computations and large scale numerical simulations. The algorithms implemented in ParMETIS are based on the parallel multilevel k-way graph-partitioning, adaptive repartitioning, and parallel multi-constrained partitioning schemes.

http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview
# Available modules


The overview below shows which ParMETIS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ParMETIS, load one of these modules using a `module load` command like:

```shell
module load ParMETIS/4.0.3-gompi-2023b
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 12:19:02 CEST)*

| |scv64/generic|
| :---: | :---: |
|ParMETIS/4.0.3-gompi-2023b|x|
