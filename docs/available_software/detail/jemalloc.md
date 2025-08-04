---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: jemalloc is a general purpose malloc(3) implementation that emphasizes
    fragmentation avoidance and scalable concurrency support.
  license: Not confirmed
  name: jemalloc
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
  softwareVersion: '[''jemalloc/5.3.0-GCCcore-12.2.0'', ''jemalloc/5.3.0-GCCcore-12.3.0'']'
  url: http://jemalloc.net
---

jemalloc
========


jemalloc is a general purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support.

http://jemalloc.net
# Available modules


The overview below shows which jemalloc installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using jemalloc, load one of these modules using a `module load` command like:

```shell
module load jemalloc/5.3.0-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|jemalloc/5.3.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|jemalloc/5.3.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
