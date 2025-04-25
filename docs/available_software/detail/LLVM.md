---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The LLVM Core libraries provide a modern source- and target-independent
    optimizer, along with code generation support for many popular CPUs (as well as
    some less common ones!) These libraries are built around a well specified code
    representation known as the LLVM intermediate representation ("LLVM IR"). The
    LLVM Core libraries are well documented, and it is particularly easy to invent
    your own language (or port an existing compiler) to use LLVM as an optimizer and
    code generator.
  license: Not confirmed
  name: LLVM
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
  softwareVersion: '[''LLVM/14.0.6-GCCcore-12.3.0-llvmlite'', ''LLVM/15.0.5-GCCcore-12.2.0'',
    ''LLVM/16.0.6-GCCcore-12.3.0'', ''LLVM/16.0.6-GCCcore-13.2.0'']'
  url: https://llvm.org/
---

LLVM
====


The LLVM Core libraries provide a modern source- and target-independent optimizer, along with code generation support for many popular CPUs (as well as some less common ones!) These libraries are built around a well specified code representation known as the LLVM intermediate representation ("LLVM IR"). The LLVM Core libraries are well documented, and it is particularly easy to invent your own language (or port an existing compiler) to use LLVM as an optimizer and code generator.

https://llvm.org/
# Available modules


The overview below shows which LLVM installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using LLVM, load one of these modules using a `module load` command like:

```shell
module load LLVM/16.0.6-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|LLVM/16.0.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|LLVM/16.0.6-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|LLVM/15.0.5-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
|LLVM/14.0.6-GCCcore-12.3.0-llvmlite|x|x|x|x|x|x|x|x|x|x|x|
