---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The wradlib project has been initiated in order to facilitate the use
    of weatherradar data as well as to provide a common platform for research on newalgorithms.
  license: Not confirmed
  name: wradlib
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
  softwareVersion: '[''wradlib/2.0.3-foss-2023a'']'
  url: https://docs.wradlib.org/
---

wradlib
=======


The wradlib project has been initiated in order to facilitate the use of weatherradar data as well as to provide a common platform for research on newalgorithms.

https://docs.wradlib.org/
# Available modules


The overview below shows which wradlib installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using wradlib, load one of these modules using a `module load` command like:

```shell
module load wradlib/2.0.3-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|wradlib/2.0.3-foss-2023a|x|-|x|x|x|x|x|x|x|x|x|x|x|x|


### wradlib/2.0.3-foss-2023a

This is a list of extensions included in the module:

cmweather-0.3.2, deprecation-2.1.0, lat_lon_parser-1.3.0, wradlib-2.0.3, xarray-datatree-0.0.13, xmltodict-0.13.0, xradar-0.5.1