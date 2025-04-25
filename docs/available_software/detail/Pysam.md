---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Pysam is a python module for reading and manipulating Samfiles. It's
    a lightweight wrapper of the samtools C-API. Pysam also includes an interface
    for tabix.
  license: Not confirmed
  name: Pysam
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
  softwareVersion: '[''Pysam/0.21.0-GCC-12.2.0'', ''Pysam/0.22.0-GCC-12.3.0'']'
  url: https://github.com/pysam-developers/pysam
---

Pysam
=====


Pysam is a python module for reading and manipulating Samfiles. It's a lightweight wrapper of the samtools C-API. Pysam also includes an interface for tabix.

https://github.com/pysam-developers/pysam
# Available modules


The overview below shows which Pysam installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Pysam, load one of these modules using a `module load` command like:

```shell
module load Pysam/0.22.0-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Pysam/0.22.0-GCC-12.3.0|x|x|x|-|x|x|x|x|x|x|x|
|Pysam/0.21.0-GCC-12.2.0|x|x|x|-|x|x|x|x|x|x|x|
