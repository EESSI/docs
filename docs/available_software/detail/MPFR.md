---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The MPFR library is a C library for multiple-precision floating-point
    computations with correct rounding.
  license: Not confirmed
  name: MPFR
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
  softwareVersion: '[''MPFR/4.2.0-GCCcore-12.2.0'', ''MPFR/4.2.0-GCCcore-12.3.0'',
    ''MPFR/4.2.1-GCCcore-13.2.0'']'
  url: https://www.mpfr.org
---

MPFR
====


The MPFR library is a C library for multiple-precision floating-point computations with correct rounding.

https://www.mpfr.org
# Available modules


The overview below shows which MPFR installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using MPFR, load one of these modules using a `module load` command like:

```shell
module load MPFR/4.2.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MPFR/4.2.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|MPFR/4.2.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|MPFR/4.2.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
