---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ARPACK is a collection of Fortran77 subroutines designed to solve large
    scale eigenvalue problems.
  license: Not confirmed
  name: arpack-ng
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
  softwareVersion: '[''arpack-ng/3.8.0-foss-2022b'', ''arpack-ng/3.9.0-foss-2023a'',
    ''arpack-ng/3.9.0-foss-2023b'']'
  url: https://github.com/opencollab/arpack-ng
---

arpack-ng
=========


ARPACK is a collection of Fortran77 subroutines designed to solve large scale eigenvalue problems.

https://github.com/opencollab/arpack-ng
# Available modules


The overview below shows which arpack-ng installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using arpack-ng, load one of these modules using a `module load` command like:

```shell
module load arpack-ng/3.9.0-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|arpack-ng/3.9.0-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|arpack-ng/3.9.0-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|arpack-ng/3.8.0-foss-2022b|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
