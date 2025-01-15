---
hide:
  - toc
---

jemalloc
========


jemalloc is a general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.

http://jemalloc.net
# Available modules


The overview below shows which jemalloc installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using jemalloc, load one of these modules using a `module load` command like:

```shell
module load jemalloc/5.3.0-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphire_rapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|jemalloc/5.3.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|-|x|
|jemalloc/5.3.0-GCCcore-12.2.0|x|x|x|x|x|x|-|x|-|x|
