---
hide:
  - toc
---

LERC
====


LERC is an open-source image or raster format which supports rapid encoding and decodingfor any pixel type (not just RGB or Byte). Users set the maximum compression error per pixel while encoding,so the precision of the original input image is preserved (within user defined error bounds).

https://github.com/Esri/lerc
# Available modules


The overview below shows which LERC installations are available per HPC-UGent Tier-2cluster, ordered based on software version (new to old).

To start using LERC, load one of these modules using a `module load` command like:

```shell
module load LERC/4.0.0-GCCcore-12.2.0
```

*(This data was automatically generated on Tue, 12 Mar 2024 at 18:02:07 CET)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|LERC/4.0.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|
