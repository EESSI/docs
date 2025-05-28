---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: CMake, the cross-platform, open-source build system.  CMake is a family
    of tools designed to build, test and package software.
  license: Not confirmed
  name: CMake
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
  softwareVersion: '[''CMake/3.24.3-GCCcore-12.2.0'', ''CMake/3.26.3-GCCcore-12.3.0'',
    ''CMake/3.27.6-GCCcore-13.2.0'']'
  url: https://www.cmake.org
---

CMake
=====


CMake, the cross-platform, open-source build system.  CMake is a family of tools designed to build, test and package software.

https://www.cmake.org
# Available modules


The overview below shows which CMake installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using CMake, load one of these modules using a `module load` command like:

```shell
module load CMake/3.27.6-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|CMake/3.27.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|CMake/3.26.3-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|CMake/3.24.3-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
