---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Protocol Buffers (a.k.a., protobuf) are Google's language-neutral,
    platform-neutral, extensible mechanism for serializing structured data.
  license: Not confirmed
  name: protobuf
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
  softwareVersion: '[''protobuf/23.0-GCCcore-12.2.0'', ''protobuf/24.0-GCCcore-12.3.0'']'
  url: https://github.com/protocolbuffers/protobuf
---

protobuf
========


Protocol Buffers (a.k.a., protobuf) are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.

https://github.com/protocolbuffers/protobuf
# Available modules


The overview below shows which protobuf installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using protobuf, load one of these modules using a `module load` command like:

```shell
module load protobuf/24.0-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|protobuf/24.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|protobuf/23.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
