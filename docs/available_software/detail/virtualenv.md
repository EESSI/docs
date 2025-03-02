---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A tool for creating isolated virtual python environments.
  license: Not confirmed
  name: virtualenv
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
  softwareVersion: '[''virtualenv/20.23.1-GCCcore-12.3.0'', ''virtualenv/20.24.6-GCCcore-13.2.0'']'
  url: https://github.com/pypa/virtualenv
---

virtualenv
==========


A tool for creating isolated virtual python environments.

https://github.com/pypa/virtualenv
# Available modules


The overview below shows which virtualenv installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using virtualenv, load one of these modules using a `module load` command like:

```shell
module load virtualenv/20.24.6-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|virtualenv/20.24.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|
|virtualenv/20.23.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|


### virtualenv/20.24.6-GCCcore-13.2.0

This is a list of extensions included in the module:

distlib-0.3.7, filelock-3.13.0, platformdirs-3.11.0, virtualenv-20.24.6

### virtualenv/20.23.1-GCCcore-12.3.0

This is a list of extensions included in the module:

distlib-0.3.6, filelock-3.12.2, platformdirs-3.8.0, virtualenv-20.23.1