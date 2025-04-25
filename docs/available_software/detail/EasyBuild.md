---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: EasyBuild is a software build and installation framework written in
    Python that allows you to install software in a structured, repeatable and robust
    way.
  license: Not confirmed
  name: EasyBuild
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
  softwareVersion: '[''EasyBuild/4.8.2'', ''EasyBuild/4.9.0'', ''EasyBuild/4.9.1'',
    ''EasyBuild/4.9.2'', ''EasyBuild/4.9.3'', ''EasyBuild/4.9.4'', ''EasyBuild/5.0.0'']'
  url: https://easybuilders.github.io/easybuild
---

EasyBuild
=========


EasyBuild is a software build and installation framework written in Python that allows you to install software in a structured, repeatable and robust way.

https://easybuilders.github.io/easybuild
# Available modules


The overview below shows which EasyBuild installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using EasyBuild, load one of these modules using a `module load` command like:

```shell
module load EasyBuild/5.0.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|EasyBuild/5.0.0|x|x|x|-|x|x|x|x|x|x|x|
|EasyBuild/4.9.4|x|x|x|-|x|x|x|x|x|x|x|
|EasyBuild/4.9.3|x|x|x|-|x|x|x|x|x|x|x|
|EasyBuild/4.9.2|x|x|x|-|x|x|x|x|x|x|x|
|EasyBuild/4.9.1|x|x|x|-|x|x|x|x|x|x|x|
|EasyBuild/4.9.0|x|x|x|-|x|x|x|x|x|x|x|
|EasyBuild/4.8.2|x|x|x|-|x|x|x|x|x|x|x|
