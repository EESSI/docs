---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 're2c is a free and open-source lexer generator for C and C++. Its
    main goal is generatingfast lexers: at least as fast as their reasonably optimized
    hand-coded counterparts. Instead of usingtraditional table-driven approach, re2c
    encodes the generated finite state automata directly in the formof conditional
    jumps and comparisons.'
  license: Not confirmed
  name: re2c
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
  softwareVersion: '[''re2c/3.0-GCCcore-12.2.0'', ''re2c/3.1-GCCcore-12.3.0'', ''re2c/3.1-GCCcore-13.2.0'']'
  url: https://re2c.org
---

re2c
====


re2c is a free and open-source lexer generator for C and C++. Its main goal is generatingfast lexers: at least as fast as their reasonably optimized hand-coded counterparts. Instead of usingtraditional table-driven approach, re2c encodes the generated finite state automata directly in the formof conditional jumps and comparisons.

https://re2c.org
# Available modules


The overview below shows which re2c installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using re2c, load one of these modules using a `module load` command like:

```shell
module load re2c/3.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|re2c/3.1-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
|re2c/3.1-GCCcore-12.3.0|x|x|x|-|x|x|x|x|x|x|x|x|
|re2c/3.0-GCCcore-12.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
