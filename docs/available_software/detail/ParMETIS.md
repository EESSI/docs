---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "ParMETIS is an MPI-based parallel library that implements a variety\
    \ of algorithms for partitioning\n unstructured graphs, meshes, and for computing\
    \ fill-reducing orderings of sparse matrices. ParMETIS extends the\n functionality\
    \ provided by METIS and includes routines that are especially suited for parallel\
    \ AMR computations and\n large scale numerical simulations. The algorithms implemented\
    \ in ParMETIS are based on the parallel multilevel k-way\n graph-partitioning,\
    \ adaptive repartitioning, and parallel multi-constrained partitioning schemes."
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
  softwareVersion: '[''4.0.3'']'
  url: http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview
---
# ParMETIS


ParMETIS is an MPI-based parallel library that implements a variety of algorithms for partitioning
 unstructured graphs, meshes, and for computing fill-reducing orderings of sparse matrices. ParMETIS extends the
 functionality provided by METIS and includes routines that are especially suited for parallel AMR computations and
 large scale numerical simulations. The algorithms implemented in ParMETIS are based on the parallel multilevel k-way
 graph-partitioning, adaptive repartitioning, and parallel multi-constrained partitioning schemes.

<small>homepage: </small><span class="software-link">[http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview](http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview)</span>

## Available installations


|ParMETIS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ParMETIS/4.0.3-gompi-2023a`|