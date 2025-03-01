---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Groff (GNU troff) is a typesetting system that reads plain text mixed
    with formatting commands and produces formatted output.
  license: Not confirmed
  name: groff
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
  softwareVersion: '[''groff/1.22.4-GCCcore-12.2.0'', ''groff/1.22.4-GCCcore-12.3.0'']'
  url: https://www.gnu.org/software/groff
---

groff
=====


Groff (GNU troff) is a typesetting system that reads plain text mixed with formatting commands and produces formatted output.

https://www.gnu.org/software/groff
# Available modules


The overview below shows which groff installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using groff, load one of these modules using a `module load` command like:

```shell
module load groff/1.22.4-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|groff/1.22.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|
|groff/1.22.4-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|
