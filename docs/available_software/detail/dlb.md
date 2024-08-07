---
hide:
  - toc
---

dlb
===


DLB is a dynamic library designed to speed up HPC hybrid applications (i.e.,two levels of parallelism) by improving the load balance of the outer level ofparallelism (e.g., MPI) by dynamically redistributing the computationalresources at the inner level of parallelism (e.g., OpenMP). at run time.

https://pm.bsc.es/dlb/
# Available modules


The overview below shows which dlb installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using dlb, load one of these modules using a `module load` command like:

```shell
module load dlb/3.4-gompi-2023b
```

*(This data was automatically generated on Wed, 07 Aug 2024 at 08:20:44 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|dlb/3.4-gompi-2023b|x|x|x|x|x|x|x|x|x|
