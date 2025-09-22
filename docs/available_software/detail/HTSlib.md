---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A C library for reading/writing high-throughput sequencing data. This
    package includes the utilities bgzip and tabix
  license: Not confirmed
  name: HTSlib
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
  softwareVersion: '[''HTSlib/1.17-GCC-12.2.0'', ''HTSlib/1.18-GCC-12.3.0'', ''HTSlib/1.19.1-GCC-13.2.0'']'
  url: https://www.htslib.org/
---

HTSlib
======


A C library for reading/writing high-throughput sequencing data. This package includes the utilities bgzip and tabix

https://www.htslib.org/
# Available modules


The overview below shows which HTSlib installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using HTSlib, load one of these modules using a `module load` command like:

```shell
module load HTSlib/1.19.1-GCC-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|HTSlib/1.19.1-GCC-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|HTSlib/1.18-GCC-12.3.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
|HTSlib/1.17-GCC-12.2.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
