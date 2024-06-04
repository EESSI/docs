---
hide:
  - toc
---

MDI
===


The MolSSI Driver Interface (MDI) project provides a standardized API for fast, on-the-fly communication between computational chemistry codes. This greatly simplifies the process of implementing methods that require the cooperation of multiple software packages and enables developers to write a single implementation that works across many different codes. The API is sufficiently general to support a wide variety of techniques, including QM/MM, ab initio MD, machine learning, advanced sampling, and path integral MD, while also being straightforwardly extensible. Communication between codes is handled by the MDI Library, which enables tight coupling between codes using either the MPI or TCP/IP methods.

https://github.com/MolSSI-MDI/MDI_Library
# Available modules


The overview below shows which MDI installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using MDI, load one of these modules using a `module load` command like:

```shell
module load MDI/1.4.26-gompi-2023a
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MDI/1.4.26-gompi-2023a|x|x|x|x|x|x|x|x|
