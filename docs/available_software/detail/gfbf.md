---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GNU Compiler Collection (GCC) based compiler toolchain, including FlexiBLAS
    (BLAS and LAPACK support) and (serial) FFTW.
  license: Not confirmed
  name: gfbf
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
  softwareVersion: '[''gfbf/2022b'', ''gfbf/2023a'', ''gfbf/2023b'']'
  url: (none)
---

gfbf
====


GNU Compiler Collection (GCC) based compiler toolchain, including FlexiBLAS (BLAS and LAPACK support) and (serial) FFTW.

(none)
# Available modules


The overview below shows which gfbf installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using gfbf, load one of these modules using a `module load` command like:

```shell
module load gfbf/2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|gfbf/2023b|x|x|x|x|x|x|x|x|-|x|
|gfbf/2023a|x|x|x|x|x|x|x|x|-|x|
|gfbf/2022b|x|x|x|x|x|x|x|x|-|x|
