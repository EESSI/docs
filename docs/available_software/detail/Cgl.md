---
hide:
  - toc
---

Cgl
===


The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators thatcan be used with other COIN-OR packages that make use of cuts, such as, amongothers, the linear solver Clp or the mixed integer linear programming solversCbc or BCP. Cgl uses the abstract class OsiSolverInterface (see Osi) to use orcommunicate with a solver. It does not directly call a solver.

https://github.com/coin-or/Cgl
# Available modules


The overview below shows which Cgl installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using Cgl, load one of these modules using a `module load` command like:

```shell
module load Cgl/0.60.8-foss-2023a
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Cgl/0.60.8-foss-2023a|x|x|x|x|x|x|x|x|
