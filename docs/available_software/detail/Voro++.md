---
hide:
  - toc
---

Voro++
======


Voro++ is a software library for carrying out three-dimensional computations of the Voronoitessellation. A distinguishing feature of the Voro++ library is that it carries out cell-based calculations,computing the Voronoi cell for each particle individually. It is particularly well-suited for applications thatrely on cell-based statistics, where features of Voronoi cells (eg. volume, centroid, number of faces) can be usedto analyze a system of particles.

http://math.lbl.gov/voro++/
# Available modules


The overview below shows which Voro++ installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Voro++, load one of these modules using a `module load` command like:

```shell
module load Voro++/0.4.6-GCCcore-12.3.0
```

*(This data was automatically generated on Thu, 01 Aug 2024 at 01:13:19 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Voro++/0.4.6-GCCcore-12.3.0|x|x|x|x|x|x|x|x|
