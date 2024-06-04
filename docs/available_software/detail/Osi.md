---
hide:
  - toc
---

Osi
===


Osi (Open Solver Interface) provides an abstract base class to a generic linearprogramming (LP) solver, along with derived classes for specific solvers. Manyapplications may be able to use the Osi to insulate themselves from a specificLP solver. That is, programs written to the OSI standard may be linked to anysolver with an OSI interface and should produce correct results. The OSI hasbeen significantly extended compared to its first incarnation. Currently, theOSI supports linear programming solvers and has rudimentary support for integerprogramming.

https://github.com/coin-or/Osi
# Available modules


The overview below shows which Osi installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using Osi, load one of these modules using a `module load` command like:

```shell
module load Osi/0.108.9-GCC-12.3.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Osi/0.108.9-GCC-12.3.0|x|x|x|x|x|x|x|x|
