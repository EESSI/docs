---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ReFrame is a framework for writing regression tests for HPC systems.
  license: Not confirmed
  name: ReFrame
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
  softwareVersion: '[''ReFrame/4.3.3'', ''ReFrame/4.6.2'']'
  url: https://github.com/reframe-hpc/reframe
---

ReFrame
=======


ReFrame is a framework for writing regression tests for HPC systems.

https://github.com/reframe-hpc/reframe
# Available modules


The overview below shows which ReFrame installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ReFrame, load one of these modules using a `module load` command like:

```shell
module load ReFrame/4.6.2
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ReFrame/4.6.2|x|x|x|x|x|x|x|x|x|x|x|x|x|
|ReFrame/4.3.3|x|x|x|x|x|x|x|x|x|x|x|x|x|


### ReFrame/4.6.2

This is a list of extensions included in the module:

pip-24.0, reframe-4.6.2, setuptools-68.0.0, wheel-0.42.0

### ReFrame/4.3.3

This is a list of extensions included in the module:

pip-21.3.1, reframe-4.3.3, wheel-0.37.1