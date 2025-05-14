---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ICU is a mature, widely used set of C/C++ and Java libraries providing
    Unicode and Globalization support for software applications.
  license: Not confirmed
  name: ICU
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
  softwareVersion: '[''ICU/72.1-GCCcore-12.2.0'', ''ICU/73.2-GCCcore-12.3.0'', ''ICU/74.1-GCCcore-13.2.0'']'
  url: https://icu.unicode.org
---

ICU
===


ICU is a mature, widely used set of C/C++ and Java libraries providing Unicode and Globalization support for software applications.

https://icu.unicode.org
# Available modules


The overview below shows which ICU installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ICU, load one of these modules using a `module load` command like:

```shell
module load ICU/74.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ICU/74.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|ICU/73.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|ICU/72.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
