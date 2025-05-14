---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Conditional Reciprocal Best BLAST - high confidence ortholog assignment.
  license: Not confirmed
  name: crb-blast
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
  softwareVersion: '[''crb-blast/0.6.9-GCC-12.3.0'']'
  url: https://github.com/cboursnell/crb-blast
---

crb-blast
=========


Conditional Reciprocal Best BLAST - high confidence ortholog assignment.

https://github.com/cboursnell/crb-blast
# Available modules


The overview below shows which crb-blast installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using crb-blast, load one of these modules using a `module load` command like:

```shell
module load crb-blast/0.6.9-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|crb-blast/0.6.9-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|


### crb-blast/0.6.9-GCC-12.3.0

This is a list of extensions included in the module:

bindeps-1.2.1, bio-1.6.0.pre.20181210, crb-blast-0.6.9, facade-1.2.1, fixwhich-1.0.2, pathname2-1.8.4, threach-0.2.0, trollop-2.9.10