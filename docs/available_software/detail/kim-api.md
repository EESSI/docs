---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Open Knowledgebase of Interatomic Models.KIM is an API and OpenKIM
    is a collection of interatomic models (potentials) foratomistic simulations.  This
    is a library that can be used by simulation programsto get access to the models
    in the OpenKIM database.This EasyBuild only installs the API, the models can be
    installed with thepackage openkim-models, or the user can install them manually
    by running    kim-api-collections-management install user MODELNAMEor    kim-api-collections-management
    install user OpenKIMto install them all.
  license: Not confirmed
  name: kim-api
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
  softwareVersion: '[''kim-api/2.3.0-GCC-12.3.0'', ''kim-api/2.3.0-GCC-13.2.0'']'
  url: https://openkim.org/
---

kim-api
=======


Open Knowledgebase of Interatomic Models.KIM is an API and OpenKIM is a collection of interatomic models (potentials) foratomistic simulations.  This is a library that can be used by simulation programsto get access to the models in the OpenKIM database.This EasyBuild only installs the API, the models can be installed with thepackage openkim-models, or the user can install them manually by running    kim-api-collections-management install user MODELNAMEor    kim-api-collections-management install user OpenKIMto install them all.

https://openkim.org/
# Available modules


The overview below shows which kim-api installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using kim-api, load one of these modules using a `module load` command like:

```shell
module load kim-api/2.3.0-GCC-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|kim-api/2.3.0-GCC-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|kim-api/2.3.0-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
