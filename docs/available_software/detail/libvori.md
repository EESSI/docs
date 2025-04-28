---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: C++ library implementing the Voronoi integration as well as the compressed
    bqbfile format. The present version of libvori is a very early developmentversion,
    which is hard-coded to work with the CP2k program package.
  license: Not confirmed
  name: libvori
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
  softwareVersion: '[''libvori/220621-GCCcore-12.3.0'']'
  url: https://brehm-research.de/libvori.php
---

libvori
=======


C++ library implementing the Voronoi integration as well as the compressed bqbfile format. The present version of libvori is a very early developmentversion, which is hard-coded to work with the CP2k program package.

https://brehm-research.de/libvori.php
# Available modules


The overview below shows which libvori installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libvori, load one of these modules using a `module load` command like:

```shell
module load libvori/220621-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libvori/220621-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|
