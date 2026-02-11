---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Bundle of Python packages required to run plumpy:A python workflows
    library that supports writing Processes with a well defined set ofinputs and outputs
    that can be strung together.
  license: Not confirmed
  name: plumpy
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
  softwareVersion: '[''plumpy/0.25.0-GCCcore-12.3.0'']'
  url: https://python.org/
---

plumpy
======


Bundle of Python packages required to run plumpy:A python workflows library that supports writing Processes with a well defined set ofinputs and outputs that can be strung together.

https://python.org/
# Available modules


The overview below shows which plumpy installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using plumpy, load one of these modules using a `module load` command like:

```shell
module load plumpy/0.25.0-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|plumpy/0.25.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### plumpy/0.25.0-GCCcore-12.3.0

This is a list of extensions included in the module:

aio-pika-9.4.3, aiormq-6.8.1, deprecation-2.1.0, kiwipy-0.8.5, nest-asyncio-1.6.0, pamqp-3.3.0, plumpy-0.25.0, shortuuid-1.0.13