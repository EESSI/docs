---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ASE is a python package providing an open source Atomic Simulation
    Environment in the Python scripting language.From version 3.20.1 we also include
    the ase-ext package, it contains optional reimplementationsin C of functions in
    ASE.  ASE uses it automatically when installed.
  license: Not confirmed
  name: ASE
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
  softwareVersion: '[''ASE/3.22.1-gfbf-2022b'']'
  url: https://wiki.fysik.dtu.dk/ase
---

ASE
===


ASE is a python package providing an open source Atomic Simulation Environment in the Python scripting language.From version 3.20.1 we also include the ase-ext package, it contains optional reimplementationsin C of functions in ASE.  ASE uses it automatically when installed.

https://wiki.fysik.dtu.dk/ase
# Available modules


The overview below shows which ASE installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ASE, load one of these modules using a `module load` command like:

```shell
module load ASE/3.22.1-gfbf-2022b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ASE/3.22.1-gfbf-2022b|x|x|x|-|x|x|x|x|x|x|x|x|


### ASE/3.22.1-gfbf-2022b

This is a list of extensions included in the module:

ase-3.22.1, ase-ext-20.9.0, pytest-mock-3.8.2