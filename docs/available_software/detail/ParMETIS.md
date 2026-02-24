# ParMETIS


ParMETIS is an MPI-based parallel library that implements a variety of algorithms for partitioning
 unstructured graphs, meshes, and for computing fill-reducing orderings of sparse matrices. ParMETIS extends the
 functionality provided by METIS and includes routines that are especially suited for parallel AMR computations and
 large scale numerical simulations. The algorithms implemented in ParMETIS are based on the parallel multilevel k-way
 graph-partitioning, adaptive repartitioning, and parallel multi-constrained partitioning schemes.

<small>homepage: </small><span class="software-link">[http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview](http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|4.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`ParMETIS/4.0.3-gompi-2023a`|