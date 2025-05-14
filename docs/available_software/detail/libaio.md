---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Asynchronous input/output library that uses the kernels native interface.
  license: Not confirmed
  name: libaio
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
  softwareVersion: '[''libaio/0.3.113-GCCcore-12.2.0'', ''libaio/0.3.113-GCCcore-12.3.0'']'
  url: https://pagure.io/libaio
---

libaio
======


Asynchronous input/output library that uses the kernels native interface.

https://pagure.io/libaio
# Available modules


The overview below shows which libaio installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libaio, load one of these modules using a `module load` command like:

```shell
module load libaio/0.3.113-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libaio/0.3.113-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|libaio/0.3.113-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
