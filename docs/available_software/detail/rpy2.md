---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: rpy2 is an interface to R running embedded in a Python process.
  license: Not confirmed
  name: rpy2
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
  softwareVersion: '[''rpy2/3.5.15-foss-2023a'']'
  url: https://rpy2.github.io
---

rpy2
====


rpy2 is an interface to R running embedded in a Python process.

https://rpy2.github.io
# Available modules


The overview below shows which rpy2 installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using rpy2, load one of these modules using a `module load` command like:

```shell
module load rpy2/3.5.15-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|rpy2/3.5.15-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|


### rpy2/3.5.15-foss-2023a

This is a list of extensions included in the module:

coverage-7.4.3, pytest-cov-4.1.0, rpy2-3.5.15, tzlocal-5.2