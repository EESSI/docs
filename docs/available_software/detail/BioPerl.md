---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Bioperl is the product of a community effort to produce Perl code which
    is useful in biology. Examples include Sequence objects, Alignment objects and
    database searching objects.
  license: Not confirmed
  name: BioPerl
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
  softwareVersion: '[''BioPerl/1.7.8-GCCcore-12.2.0'', ''BioPerl/1.7.8-GCCcore-12.3.0'']'
  url: https://bioperl.org/
---

BioPerl
=======


Bioperl is the product of a community effort to produce Perl code which is useful in biology. Examples include Sequence objects, Alignment objects and database searching objects.

https://bioperl.org/
# Available modules


The overview below shows which BioPerl installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using BioPerl, load one of these modules using a `module load` command like:

```shell
module load BioPerl/1.7.8-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|BioPerl/1.7.8-GCCcore-12.3.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
|BioPerl/1.7.8-GCCcore-12.2.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|


### BioPerl/1.7.8-GCCcore-12.3.0

This is a list of extensions included in the module:

Bio::Procedural-1.7.4, BioPerl-1.7.8, XML::Writer-0.900

### BioPerl/1.7.8-GCCcore-12.2.0

This is a list of extensions included in the module:

Bio::Procedural-1.7.4, BioPerl-1.7.8, XML::Writer-0.900