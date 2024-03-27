---
hide:
  - toc
---

re2c
====


re2c is a free and open-source lexer generator for C and C++. Its main goal is generatingfast lexers: at least as fast as their reasonably optimized hand-coded counterparts. Instead of usingtraditional table-driven approach, re2c encodes the generated finite state automata directly in the formof conditional jumps and comparisons.

https://re2c.org
# Available modules


The overview below shows which re2c installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using re2c, load one of these modules using a `module load` command like:

```shell
module load re2c/3.1-GCCcore-12.3.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|re2c/3.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
|re2c/3.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|
