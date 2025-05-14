---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Ncdu is a disk usage analyzer with an ncurses interface. It is designed
    to find space hogs on a remote server where you don't have an entire graphical
    setup available, but it is a useful tool even on regular desktop systems. Ncdu
    aims to be fast, simple and easy to use, and should be able to run in any minimal
    POSIX-like environment with ncurses installed.
  license: Not confirmed
  name: ncdu
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
  softwareVersion: '[''ncdu/1.18-GCC-12.3.0'']'
  url: https://dev.yorhel.nl/ncdu
---

ncdu
====


Ncdu is a disk usage analyzer with an ncurses interface. It is designed to find space hogs on a remote server where you don't have an entire graphical setup available, but it is a useful tool even on regular desktop systems. Ncdu aims to be fast, simple and easy to use, and should be able to run in any minimal POSIX-like environment with ncurses installed.

https://dev.yorhel.nl/ncdu
# Available modules


The overview below shows which ncdu installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ncdu, load one of these modules using a `module load` command like:

```shell
module load ncdu/1.18-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ncdu/1.18-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
