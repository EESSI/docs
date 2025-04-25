---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Snappy is a compression/decompression library. It does not aimfor maximum
    compression, or compatibility with any other compression library;instead, it aims
    for very high speeds and reasonable compression.
  license: Not confirmed
  name: snappy
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
  softwareVersion: '[''snappy/1.1.9-GCCcore-12.2.0'', ''snappy/1.1.10-GCCcore-12.3.0'',
    ''snappy/1.1.10-GCCcore-13.2.0'']'
  url: https://github.com/google/snappy
---

snappy
======


Snappy is a compression/decompression library. It does not aimfor maximum compression, or compatibility with any other compression library;instead, it aims for very high speeds and reasonable compression.

https://github.com/google/snappy
# Available modules


The overview below shows which snappy installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using snappy, load one of these modules using a `module load` command like:

```shell
module load snappy/1.1.10-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|snappy/1.1.10-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|snappy/1.1.10-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|snappy/1.1.9-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
