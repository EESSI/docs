---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: f90wrap is a tool to automatically generate Python extension modules
    whichinterface to Fortran code that makes use of derived types. It builds on thecapabilities
    of the popular f2py utility by generating a simpler Fortran 90interface to the
    original Fortran code which is then suitable for wrapping withf2py, together with
    a higher-level Pythonic wrapper that makes the existance ofan additional layer
    transparent to the final user.
  license: Not confirmed
  name: f90wrap
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
  softwareVersion: '[''f90wrap/0.2.13-foss-2023a'']'
  url: https://github.com/jameskermode/f90wrap
---

f90wrap
=======


f90wrap is a tool to automatically generate Python extension modules whichinterface to Fortran code that makes use of derived types. It builds on thecapabilities of the popular f2py utility by generating a simpler Fortran 90interface to the original Fortran code which is then suitable for wrapping withf2py, together with a higher-level Pythonic wrapper that makes the existance ofan additional layer transparent to the final user.

https://github.com/jameskermode/f90wrap
# Available modules


The overview below shows which f90wrap installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using f90wrap, load one of these modules using a `module load` command like:

```shell
module load f90wrap/0.2.13-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|f90wrap/0.2.13-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
