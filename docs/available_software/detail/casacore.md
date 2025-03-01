---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A suite of C++ libraries for radio astronomy data processing.The ephemerides
    data needs to be in DATA_DIR and the location must be specified at runtime.Thus
    user's can update them.
  license: Not confirmed
  name: casacore
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
  softwareVersion: '[''casacore/3.5.0-foss-2023b'']'
  url: https://github.com/casacore/casacore
---

casacore
========


A suite of C++ libraries for radio astronomy data processing.The ephemerides data needs to be in DATA_DIR and the location must be specified at runtime.Thus user's can update them.

https://github.com/casacore/casacore
# Available modules


The overview below shows which casacore installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using casacore, load one of these modules using a `module load` command like:

```shell
module load casacore/3.5.0-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|casacore/3.5.0-foss-2023b|x|x|x|x|x|x|x|x|x|
