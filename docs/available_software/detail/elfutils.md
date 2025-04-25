---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The elfutils project provides libraries and tools for ELF files and
    DWARF data.
  license: Not confirmed
  name: elfutils
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
  softwareVersion: '[''elfutils/0.189-GCCcore-12.2.0'', ''elfutils/0.189-GCCcore-12.3.0'',
    ''elfutils/0.190-GCCcore-13.2.0'']'
  url: https://elfutils.org/
---

elfutils
========


The elfutils project provides libraries and tools for ELF files and DWARF data.

https://elfutils.org/
# Available modules


The overview below shows which elfutils installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using elfutils, load one of these modules using a `module load` command like:

```shell
module load elfutils/0.190-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|elfutils/0.190-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
|elfutils/0.189-GCCcore-12.3.0|x|x|x|-|x|x|x|x|x|x|x|x|
|elfutils/0.189-GCCcore-12.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
