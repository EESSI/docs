---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Intel(R) Threading Building Blocks (Intel(R) TBB) lets you easily write
    parallel C++ programs that take full advantage of multicore performance, that
    are portable, composable and have future-proof scalability.
  license: Not confirmed
  name: tbb
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
  softwareVersion: '[''tbb/2021.10.0-GCCcore-12.2.0'', ''tbb/2021.11.0-GCCcore-12.3.0'',
    ''tbb/2021.13.0-GCCcore-13.2.0'']'
  url: https://github.com/oneapi-src/oneTBB
---

tbb
===


Intel(R) Threading Building Blocks (Intel(R) TBB) lets you easily write parallel C++ programs that take full advantage of multicore performance, that are portable, composable and have future-proof scalability.

https://github.com/oneapi-src/oneTBB
# Available modules


The overview below shows which tbb installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using tbb, load one of these modules using a `module load` command like:

```shell
module load tbb/2021.13.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|tbb/2021.13.0-GCCcore-13.2.0|-|-|-|-|x|x|x|x|x|x|x|x|x|
|tbb/2021.11.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|tbb/2021.10.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
