---
hide:
  - toc
---

hiredis
=======


Hiredis is a minimalistic C client library for the Redis database.It is minimalistic because it just adds minimal support for the protocol,but at the same time it uses a high level printf-alike API in order tomake it much higher level than otherwise suggested by its minimal code baseand the lack of explicit bindings for every Redis command.

https://github.com/redis/hiredis
# Available modules


The overview below shows which hiredis installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using hiredis, load one of these modules using a `module load` command like:

```shell
module load hiredis/1.2.0-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphire_rapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|hiredis/1.2.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|-|x|
