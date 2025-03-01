---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Image Domain Gridding (IDG) is a fast method for convolutional resampling
    (gridding/degridding)of radio astronomical data (visibilities). Direction dependent
    effects (DDEs) or A-tems can be appliedin the gridding process.The algorithm is
    described in "Image Domain Gridding: a fast method for convolutional resampling
    of visibilities",Van der Tol (2018).The implementation is described in "Radio-astronomical
    imaging on graphics processors", Veenboer (2020).Please cite these papers in publications
    using IDG.'
  license: Not confirmed
  name: IDG
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
  softwareVersion: '[''IDG/1.2.0-foss-2023b'']'
  url: https://idg.readthedocs.io/
---

IDG
===


Image Domain Gridding (IDG) is a fast method for convolutional resampling (gridding/degridding)of radio astronomical data (visibilities). Direction dependent effects (DDEs) or A-tems can be appliedin the gridding process.The algorithm is described in "Image Domain Gridding: a fast method for convolutional resampling of visibilities",Van der Tol (2018).The implementation is described in "Radio-astronomical imaging on graphics processors", Veenboer (2020).Please cite these papers in publications using IDG.

https://idg.readthedocs.io/
# Available modules


The overview below shows which IDG installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using IDG, load one of these modules using a `module load` command like:

```shell
module load IDG/1.2.0-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|IDG/1.2.0-foss-2023b|x|x|x|x|x|x|x|x|x|
