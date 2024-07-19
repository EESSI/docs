---
hide:
  - toc
---

PAPI
====


PAPI provides the tool designer and application engineer with a consistent interface and methodology for use of the performance counter hardware found in most major microprocessors. PAPI enables software engineers to see, in near real time, the relation between software performance and processor events. In addition Component PAPI provides access to a collection of components that expose performance measurement opportunites across the hardware and software stack.

https://icl.cs.utk.edu/projects/papi/
# Available modules


The overview below shows which PAPI installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PAPI, load one of these modules using a `module load` command like:

```shell
module load PAPI/7.1.0-GCCcore-13.2.0
```

*(This data was automatically generated on Fri, 19 Jul 2024 at 16:20:17 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PAPI/7.1.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|
