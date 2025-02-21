---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GMP is a free library for arbitrary precision arithmetic, operating
    on signed integers, rational numbers, and floating point numbers.
  license: Not confirmed
  name: GMP
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
  softwareVersion: '[''GMP/6.2.1-GCCcore-12.2.0'', ''GMP/6.2.1-GCCcore-12.3.0'', ''GMP/6.3.0-GCCcore-13.2.0'']'
  url: https://gmplib.org/
---

GMP
===


GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating point numbers.

https://gmplib.org/
# Available modules


The overview below shows which GMP installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GMP, load one of these modules using a `module load` command like:

```shell
module load GMP/6.3.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GMP/6.3.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|-|x|
|GMP/6.2.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|-|x|
|GMP/6.2.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|-|x|
