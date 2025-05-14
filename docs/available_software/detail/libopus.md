---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Opus is a totally open, royalty-free, highly versatile audio codec.\
    \ Opus is unmatched for interactive speech and music transmission over the Internet,\
    \ but is also intended for storage and streaming applications. It is standardized\
    \ by the Internet Engineering Task Force (IETF) as RFC 6716 which incorporated\
    \ technology from Skype\u2019s SILK codec and Xiph.Org\u2019s CELT codec."
  license: Not confirmed
  name: libopus
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
  softwareVersion: '[''libopus/1.3.1-GCCcore-12.2.0'', ''libopus/1.4-GCCcore-12.3.0'',
    ''libopus/1.5.2-GCCcore-13.2.0'']'
  url: https://www.opus-codec.org/
---

libopus
=======


Opus is a totally open, royalty-free, highly versatile audio codec. Opus is unmatched for interactive speech and music transmission over the Internet, but is also intended for storage and streaming applications. It is standardized by the Internet Engineering Task Force (IETF) as RFC 6716 which incorporated technology from Skype’s SILK codec and Xiph.Org’s CELT codec.

https://www.opus-codec.org/
# Available modules


The overview below shows which libopus installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libopus, load one of these modules using a `module load` command like:

```shell
module load libopus/1.5.2-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libopus/1.5.2-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|libopus/1.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|libopus/1.3.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
