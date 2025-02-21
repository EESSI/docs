---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Libxc is a library of exchange-correlation functionals for density-functional
    theory. The aim is to provide a portable, well tested and reliable set of exchange
    and correlation functionals.
  license: Not confirmed
  name: libxc
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
  softwareVersion: '[''libxc/6.1.0-GCC-12.2.0'', ''libxc/6.2.2-GCC-12.3.0'']'
  url: https://www.tddft.org/programs/libxc
---

libxc
=====


Libxc is a library of exchange-correlation functionals for density-functional theory. The aim is to provide a portable, well tested and reliable set of exchange and correlation functionals.

https://www.tddft.org/programs/libxc
# Available modules


The overview below shows which libxc installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libxc, load one of these modules using a `module load` command like:

```shell
module load libxc/6.2.2-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libxc/6.2.2-GCC-12.3.0|x|x|x|x|x|x|x|x|-|x|
|libxc/6.1.0-GCC-12.2.0|x|x|x|x|x|x|x|x|-|x|
