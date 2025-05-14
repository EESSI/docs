---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A small C++ header library which makes it easier to writePython extension
    modules. The primary feature is a PyObject smart pointerwhich automatically handles
    reference counting and provides conveniencemethods for performing common object
    operations.
  license: Not confirmed
  name: cppy
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
  softwareVersion: '[''cppy/1.2.1-GCCcore-12.2.0'', ''cppy/1.2.1-GCCcore-12.3.0'',
    ''cppy/1.2.1-GCCcore-13.2.0'']'
  url: https://github.com/nucleic/cppy
---

cppy
====


A small C++ header library which makes it easier to writePython extension modules. The primary feature is a PyObject smart pointerwhich automatically handles reference counting and provides conveniencemethods for performing common object operations.

https://github.com/nucleic/cppy
# Available modules


The overview below shows which cppy installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using cppy, load one of these modules using a `module load` command like:

```shell
module load cppy/1.2.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|cppy/1.2.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|cppy/1.2.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|cppy/1.2.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
