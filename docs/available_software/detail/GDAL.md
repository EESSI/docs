---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GDAL is a translator library for raster geospatial data formats that
    is released under an X/MIT style Open Source license by the Open Source Geospatial
    Foundation. As a library, it presents a single abstract data model to the calling
    application for all supported formats. It also comes with a variety of useful
    commandline utilities for data translation and processing.
  license: Not confirmed
  name: GDAL
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
  softwareVersion: '[''GDAL/3.6.2-foss-2022b'', ''GDAL/3.7.1-foss-2023a'', ''GDAL/3.9.0-foss-2023b'']'
  url: https://www.gdal.org
---

GDAL
====


GDAL is a translator library for raster geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation. As a library, it presents a single abstract data model to the calling application for all supported formats. It also comes with a variety of useful commandline utilities for data translation and processing.

https://www.gdal.org
# Available modules


The overview below shows which GDAL installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GDAL, load one of these modules using a `module load` command like:

```shell
module load GDAL/3.9.0-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GDAL/3.9.0-foss-2023b|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
|GDAL/3.7.1-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GDAL/3.6.2-foss-2022b|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
