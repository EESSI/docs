---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: LERC is an open-source image or raster format which supports rapid
    encoding and decodingfor any pixel type (not just RGB or Byte). Users set the
    maximum compression error per pixel while encoding,so the precision of the original
    input image is preserved (within user defined error bounds).
  license: Not confirmed
  name: LERC
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''LERC/4.0.0-GCCcore-12.2.0'', ''LERC/4.0.0-GCCcore-12.3.0'',
    ''LERC/4.0.0-GCCcore-13.2.0'']'
  url: https://github.com/Esri/lerc
---

LERC
====


LERC is an open-source image or raster format which supports rapid encoding and decodingfor any pixel type (not just RGB or Byte). Users set the maximum compression error per pixel while encoding,so the precision of the original input image is preserved (within user defined error bounds).

https://github.com/Esri/lerc
# Available modules


The overview below shows which LERC installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using LERC, load one of these modules using a `module load` command like:

```shell
module load LERC/4.0.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|LERC/4.0.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|LERC/4.0.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|LERC/4.0.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
