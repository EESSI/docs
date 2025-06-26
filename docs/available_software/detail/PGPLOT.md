---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The PGPLOT Graphics Subroutine Library is a Fortran- or C-callable,device-independent
    graphics package for making simple scientific graphs. It is intendedfor making
    graphical images of publication quality with minimum effort on the part ofthe
    user. For most applications, the program can be device-independent, and the outputcan
    be directed to the appropriate device at run time.
  license: Not confirmed
  name: PGPLOT
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
  softwareVersion: '[''PGPLOT/5.2.2-GCCcore-13.2.0'']'
  url: https://sites.astro.caltech.edu/~tjp/pgplot/
---

PGPLOT
======


The PGPLOT Graphics Subroutine Library is a Fortran- or C-callable,device-independent graphics package for making simple scientific graphs. It is intendedfor making graphical images of publication quality with minimum effort on the part ofthe user. For most applications, the program can be device-independent, and the outputcan be directed to the appropriate device at run time.

https://sites.astro.caltech.edu/~tjp/pgplot/
# Available modules


The overview below shows which PGPLOT installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PGPLOT, load one of these modules using a `module load` command like:

```shell
module load PGPLOT/5.2.2-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PGPLOT/5.2.2-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
