---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: pigz, which stands for parallel implementation of gzip, is a fully
    functional replacement for gzip that exploits multiple processors and multiple
    cores to the hilt when compressing data. pigz was written by Mark Adler, and uses
    the zlib and pthread libraries.
  license: Not confirmed
  name: pigz
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
  softwareVersion: '[''pigz/2.8-GCCcore-13.2.0'']'
  url: https://zlib.net/pigz/
---

pigz
====


pigz, which stands for parallel implementation of gzip, is a fully functional replacement for gzip that exploits multiple processors and multiple cores to the hilt when compressing data. pigz was written by Mark Adler, and uses the zlib and pthread libraries.

https://zlib.net/pigz/
# Available modules


The overview below shows which pigz installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using pigz, load one of these modules using a `module load` command like:

```shell
module load pigz/2.8-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pigz/2.8-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
