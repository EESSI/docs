---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Network Security Services (NSS) is a set of libraries designed to support
    cross-platform development of security-enabled client and server applications.
  license: Not confirmed
  name: NSS
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
  softwareVersion: '[''NSS/3.85-GCCcore-12.2.0'', ''NSS/3.89.1-GCCcore-12.3.0'', ''NSS/3.94-GCCcore-13.2.0'']'
  url: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS
---

NSS
===


Network Security Services (NSS) is a set of libraries designed to support cross-platform development of security-enabled client and server applications.

https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS
# Available modules


The overview below shows which NSS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using NSS, load one of these modules using a `module load` command like:

```shell
module load NSS/3.94-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|NSS/3.94-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|NSS/3.89.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|NSS/3.85-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
