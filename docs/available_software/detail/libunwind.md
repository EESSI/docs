---
hide:
  - toc
---

libunwind
=========


The primary goal of libunwind is to define a portable and efficient C programming interface (API) to determine the call-chain of a program. The API additionally provides the means to manipulate the preserved (callee-saved) state of each call-frame and to resume execution at any point in the call-chain (non-local goto). The API supports both local (same-process) and remote (across-process) operation. As such, the API is useful in a number of applications

https://www.nongnu.org/libunwind/
# Available modules


The overview below shows which libunwind installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libunwind, load one of these modules using a `module load` command like:

```shell
module load libunwind/1.6.2-GCCcore-13.2.0
```

*(This data was automatically generated on Thu, 06 Jun 2024 at 08:26:56 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libunwind/1.6.2-GCCcore-13.2.0|x|x|x|x|x|x|x|x|
|libunwind/1.6.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
|libunwind/1.6.2-GCCcore-12.2.0|x|x|x|x|x|x|x|x|
