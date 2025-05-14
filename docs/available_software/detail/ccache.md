---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Ccache (or \u201Cccache\u201D) is a compiler cache. It speeds up recompilation\
    \ bycaching previous compilations and detecting when the same compilation is being\
    \ done again"
  license: Not confirmed
  name: ccache
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
  softwareVersion: '[''ccache/4.9-GCCcore-12.3.0'']'
  url: https://ccache.dev/
---

ccache
======


Ccache (or “ccache”) is a compiler cache. It speeds up recompilation bycaching previous compilations and detecting when the same compilation is being done again

https://ccache.dev/
# Available modules


The overview below shows which ccache installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ccache, load one of these modules using a `module load` command like:

```shell
module load ccache/4.9-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ccache/4.9-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
