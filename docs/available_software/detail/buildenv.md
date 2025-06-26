---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This module sets a group of environment variables for compilers, linkers,
    maths libraries, etc., that you can use to easily transition between toolchains
    when building your software. To query the variables being set please use: module
    show <this module name>'
  license: Not confirmed
  name: buildenv
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
  softwareVersion: '[''buildenv/default-foss-2022b'', ''buildenv/default-foss-2023a'',
    ''buildenv/default-foss-2023b'']'
  url: None
---

buildenv
========


This module sets a group of environment variables for compilers, linkers, maths libraries, etc., that you can use to easily transition between toolchains when building your software. To query the variables being set please use: module show <this module name>

None
# Available modules


The overview below shows which buildenv installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using buildenv, load one of these modules using a `module load` command like:

```shell
module load buildenv/default-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|buildenv/default-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|
|buildenv/default-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|
|buildenv/default-foss-2022b|x|x|x|x|x|x|x|x|x|x|x|x|x|
