---
hide:
  - toc
---

pytest-shard
============


pytest plugin to support parallelism across multiple machines.Shards tests based on a hash of their test name enabling easy parallelism across machines,suitable for a wide variety of continuous integration services.Tests are split at the finest level of granularity, individual test cases,enabling parallelism even if all of your tests are in a single file(or even single parameterized test method).

https://github.com/AdamGleave/pytest-shard
# Available modules


The overview below shows which pytest-shard installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using pytest-shard, load one of these modules using a `module load` command like:

```shell
module load pytest-shard/0.1.2-GCCcore-12.3.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pytest-shard/0.1.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
