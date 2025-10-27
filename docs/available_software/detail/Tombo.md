---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Tombo is a suite of tools primarily for the identification of modified
    nucleotides from raw nanopore sequencing data.
  license: Not confirmed
  name: Tombo
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
  softwareVersion: '[''Tombo/1.5.1-foss-2023a'']'
  url: https://github.com/nanoporetech/tombo
---

Tombo
=====


Tombo is a suite of tools primarily for the identification of modified nucleotides from raw nanopore sequencing data.

https://github.com/nanoporetech/tombo
# Available modules


The overview below shows which Tombo installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Tombo, load one of these modules using a `module load` command like:

```shell
module load Tombo/1.5.1-foss-2023a
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Tombo/1.5.1-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### Tombo/1.5.1-foss-2023a

This is a list of extensions included in the module:

mappy-2.28, ont-tombo-1.5.1, pyfaidx-0.5.8