---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: pkg-config is a helper tool used when compiling applications and libraries.
    It helps you insert the correct compiler options on the command line so an application
    can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0` for instance,
    rather than hard-coding values on where to find glib (or other libraries).
  license: Not confirmed
  name: pkg-config
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
  softwareVersion: '[''pkg-config/0.29.2-GCCcore-12.3.0'']'
  url: https://www.freedesktop.org/wiki/Software/pkg-config/
---

pkg-config
==========


pkg-config is a helper tool used when compiling applications and libraries. It helps you insert the correct compiler options on the command line so an application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0` for instance, rather than hard-coding values on where to find glib (or other libraries).

https://www.freedesktop.org/wiki/Software/pkg-config/
# Available modules


The overview below shows which pkg-config installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using pkg-config, load one of these modules using a `module load` command like:

```shell
module load pkg-config/0.29.2-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pkg-config/0.29.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
