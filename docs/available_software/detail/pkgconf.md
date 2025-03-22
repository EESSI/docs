---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: pkgconf is a program which helps to configure compiler and linker flags
    for development libraries. It is similar to pkg-config from freedesktop.org.
  license: Not confirmed
  name: pkgconf
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
  softwareVersion: '[''pkgconf/1.8.0'', ''pkgconf/1.9.3-GCCcore-12.2.0'', ''pkgconf/1.9.5-GCCcore-12.3.0'',
    ''pkgconf/2.0.3-GCCcore-13.2.0'']'
  url: https://github.com/pkgconf/pkgconf
---

pkgconf
=======


pkgconf is a program which helps to configure compiler and linker flags for development libraries. It is similar to pkg-config from freedesktop.org.

https://github.com/pkgconf/pkgconf
# Available modules


The overview below shows which pkgconf installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using pkgconf, load one of these modules using a `module load` command like:

```shell
module load pkgconf/2.0.3-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pkgconf/2.0.3-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|
|pkgconf/1.9.5-GCCcore-12.3.0|x|x|x|-|x|x|x|x|x|x|x|
|pkgconf/1.9.3-GCCcore-12.2.0|x|x|x|-|x|x|x|x|x|x|x|
|pkgconf/1.8.0|x|x|x|-|x|x|x|x|x|x|x|
