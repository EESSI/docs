---
hide:
  - toc
---

ParMETIS
========


ParMETIS is an MPI-based parallel library that implements a variety of algorithms for partitioning unstructured graphs, meshes, and for computing fill-reducing orderings of sparse matrices. ParMETIS extends the functionality provided by METIS and includes routines that are especially suited for parallel AMR computations and large scale numerical simulations. The algorithms implemented in ParMETIS are based on the parallel multilevel k-way graph-partitioning, adaptive repartitioning, and parallel multi-constrained partitioning schemes.

http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview
# Available modules


The overview below shows which ParMETIS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ParMETIS, load one of these modules using a `module load` command like:

```shell
module load ParMETIS/4.0.3-gompi-2023a
```

*(This data was automatically generated on Tue, 11 Jun 2024 at 08:34:11 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ParMETIS/4.0.3-gompi-2023a|x|x|x|x|x|x|x|x|
