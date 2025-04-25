---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: This bundle contains all dependencies needed to test astropy using
    pytest.
  license: Not confirmed
  name: astropy-testing
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
  softwareVersion: '[''astropy-testing/7.0.0-gfbf-2023b'']'
  url: https://www.astropy.org/
---

astropy-testing
===============


This bundle contains all dependencies needed to test astropy using pytest.

https://www.astropy.org/
# Available modules


The overview below shows which astropy-testing installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using astropy-testing, load one of these modules using a `module load` command like:

```shell
module load astropy-testing/7.0.0-gfbf-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|astropy-testing/7.0.0-gfbf-2023b|x|x|x|-|x|x|x|x|x|x|x|x|


### astropy-testing/7.0.0-gfbf-2023b

This is a list of extensions included in the module:

pytest-arraydiff-0.6.1, pytest-astropy-0.11.0, pytest-astropy-header-0.2.2, pytest-cov-5.0.0, pytest-doctestplus-1.3.0, pytest-filter-subpackage-0.2.0, pytest-mock-3.14.0, pytest-remotedata-0.4.1