---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: LIBXSMM is a library for small dense and small sparse matrix-matrix
    multiplicationstargeting Intel Architecture (x86).
  license: Not confirmed
  name: libxsmm
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
  softwareVersion: '[''libxsmm/1.17-GCC-12.3.0'']'
  url: https://github.com/hfp/libxsmm
---

libxsmm
=======


LIBXSMM is a library for small dense and small sparse matrix-matrix multiplicationstargeting Intel Architecture (x86).

https://github.com/hfp/libxsmm
# Available modules


The overview below shows which libxsmm installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libxsmm, load one of these modules using a `module load` command like:

```shell
module load libxsmm/1.17-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libxsmm/1.17-GCC-12.3.0|-|-|-|x|x|x|x|x|x|
