---
hide:
  - toc
---

GObject-Introspection
=====================


GObject introspection is a middleware layer between C libraries (using GObject) and language bindings. The C library can be scanned at compile time and generate a metadata file, in addition to the actual native C library. Then at runtime, language bindings can read this metadata and automatically provide bindings to call into the C library.

https://gi.readthedocs.io/en/latest/
# Available modules


The overview below shows which GObject-Introspection installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using GObject-Introspection, load one of these modules using a `module load` command like:

```shell
module load GObject-Introspection/1.76.1-GCCcore-12.3.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GObject-Introspection/1.76.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
|GObject-Introspection/1.74.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|
