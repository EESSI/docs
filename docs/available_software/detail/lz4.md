---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: LZ4 is lossless compression algorithm, providing compression speed
    at 400 MB/s per core. It features an extremely fast decoder, with speed in multiple
    GB/s per core.
  license: Not confirmed
  name: lz4
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
  softwareVersion: '[''lz4/1.9.4-GCCcore-12.2.0'', ''lz4/1.9.4-GCCcore-12.3.0'', ''lz4/1.9.4-GCCcore-13.2.0'']'
  url: https://lz4.github.io/lz4/
---

lz4
===


LZ4 is lossless compression algorithm, providing compression speed at 400 MB/s per core. It features an extremely fast decoder, with speed in multiple GB/s per core.

https://lz4.github.io/lz4/
# Available modules


The overview below shows which lz4 installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using lz4, load one of these modules using a `module load` command like:

```shell
module load lz4/1.9.4-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|lz4/1.9.4-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|lz4/1.9.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|lz4/1.9.4-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
