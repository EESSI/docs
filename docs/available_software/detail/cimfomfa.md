---
hide:
  - toc
---

cimfomfa
========


This library supports both MCL, a cluster algorithm for graphs, and zoem, amacro/DSL language. It supplies abstractions for memory management, I/O,associative arrays, strings, heaps, and a few other things. The string libraryhas had heavy testing as part of zoem. Both understandably and regrettably Ichose long ago to make it C-string-compatible, hence nul bytes may not be partof a string. At some point I hope to rectify this, perhaps unrealistically.

https://github.com/micans/cimfomfa
# Available modules


The overview below shows which cimfomfa installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using cimfomfa, load one of these modules using a `module load` command like:

```shell
module load cimfomfa/22.273-GCCcore-12.3.0
```

*(This data was automatically generated on Wed, 07 Aug 2024 at 12:36:59 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|cimfomfa/22.273-GCCcore-12.3.0|x|x|x|x|x|x|-|x|x|
