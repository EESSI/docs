---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The pytest framework makes it easy to write small,readable tests, and
    can scale to support complex functional testing forapplications and libraries.
  license: Not confirmed
  name: pytest
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
  softwareVersion: '[''pytest/7.4.2-GCCcore-12.3.0'']'
  url: https://docs.pytest.org/en/latest/
---

pytest
======


The pytest framework makes it easy to write small,readable tests, and can scale to support complex functional testing forapplications and libraries.

https://docs.pytest.org/en/latest/
# Available modules


The overview below shows which pytest installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using pytest, load one of these modules using a `module load` command like:

```shell
module load pytest/7.4.2-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pytest/7.4.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### pytest/7.4.2-GCCcore-12.3.0

This is a list of extensions included in the module:

elementpath-4.1.5, exceptiongroup-1.1.1, iniconfig-2.0.0, pluggy-1.2.0, pytest-7.4.2, xmlschema-2.5.0