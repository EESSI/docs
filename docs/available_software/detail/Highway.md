---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Highway is a C++ library for SIMD (Single Instruction, Multiple Data),
    i.e. applying the sameoperation to 'lanes'.
  license: Not confirmed
  name: Highway
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
  softwareVersion: '[''Highway/1.0.3-GCCcore-12.2.0'', ''Highway/1.0.4-GCCcore-12.3.0'']'
  url: https://github.com/google/highway
---

Highway
=======


Highway is a C++ library for SIMD (Single Instruction, Multiple Data), i.e. applying the sameoperation to 'lanes'.

https://github.com/google/highway
# Available modules


The overview below shows which Highway installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Highway, load one of these modules using a `module load` command like:

```shell
module load Highway/1.0.4-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Highway/1.0.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Highway/1.0.3-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
