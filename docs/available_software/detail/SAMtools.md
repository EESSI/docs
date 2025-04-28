---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: SAM Tools provide various utilities for manipulating alignments in
    the SAM format,  including sorting, merging, indexing and generating alignments
    in a per-position format.
  license: Not confirmed
  name: SAMtools
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
  softwareVersion: '[''SAMtools/1.17-GCC-12.2.0'', ''SAMtools/1.18-GCC-12.3.0'']'
  url: https://www.htslib.org/
---

SAMtools
========


SAM Tools provide various utilities for manipulating alignments in the SAM format,  including sorting, merging, indexing and generating alignments in a per-position format.

https://www.htslib.org/
# Available modules


The overview below shows which SAMtools installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using SAMtools, load one of these modules using a `module load` command like:

```shell
module load SAMtools/1.18-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|SAMtools/1.18-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|
|SAMtools/1.17-GCC-12.2.0|x|x|x|x|x|x|x|x|x|x|
