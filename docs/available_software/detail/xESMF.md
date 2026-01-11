---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'xESMF: Universal Regridder for Geospatial Data'
  license: Not confirmed
  name: xESMF
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
  softwareVersion: '[''xESMF/0.8.6-foss-2023a'']'
  url: https://xesmf.readthedocs.io
---

xESMF
=====


xESMF: Universal Regridder for Geospatial Data

https://xesmf.readthedocs.io
# Available modules


The overview below shows which xESMF installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using xESMF, load one of these modules using a `module load` command like:

```shell
module load xESMF/0.8.6-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|xESMF/0.8.6-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### xESMF/0.8.6-foss-2023a

This is a list of extensions included in the module:

cf_xarray-0.9.3, cftime-1.6.2, sparse-0.14.0, xesmf-0.8.6