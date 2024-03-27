---
hide:
  - toc
---

libaec
======


Libaec provides fast lossless compression of 1 up to 32 bit wide signed or unsigned integers(samples). The library achieves best results for low entropy data as often encountered in space imaginginstrument data or numerical model output from weather or climate simulations. While floating point representationsare not directly supported, they can also be efficiently coded by grouping exponents and mantissa.

https://gitlab.dkrz.de/k202009/libaec
# Available modules


The overview below shows which libaec installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using libaec, load one of these modules using a `module load` command like:

```shell
module load libaec/1.0.6-GCCcore-13.2.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libaec/1.0.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|
|libaec/1.0.6-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
