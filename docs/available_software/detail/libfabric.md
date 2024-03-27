---
hide:
  - toc
---

libfabric
=========


Libfabric is a core component of OFI. It is the library that defines and exportsthe user-space API of OFI, and is typically the only software that applicationsdeal with directly. It works in conjunction with provider libraries, which areoften integrated directly into libfabric.

https://ofiwg.github.io/libfabric/
# Available modules


The overview below shows which libfabric installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using libfabric, load one of these modules using a `module load` command like:

```shell
module load libfabric/1.19.0-GCCcore-13.2.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libfabric/1.19.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|
|libfabric/1.18.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
|libfabric/1.16.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|
