---
hide:
  - toc
---

LLVM
====


The LLVM Core libraries provide a modern source- and target-independent optimizer, along with code generation support for many popular CPUs (as well as some less common ones!) These libraries are built around a well specified code representation known as the LLVM intermediate representation ("LLVM IR"). The LLVM Core libraries are well documented, and it is particularly easy to invent your own language (or port an existing compiler) to use LLVM as an optimizer and code generator.

https://llvm.org/
# Available modules


The overview below shows which LLVM installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using LLVM, load one of these modules using a `module load` command like:

```shell
module load LLVM/16.0.6-GCCcore-12.3.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|LLVM/16.0.6-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
|LLVM/15.0.5-GCCcore-12.2.0|x|x|x|x|x|x|x|x|
