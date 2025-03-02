---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Fast, correct Python JSON library supporting dataclasses, datetimes,
    and numpy.
  license: Not confirmed
  name: orjson
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
  softwareVersion: '[''orjson/3.9.15-GCCcore-12.3.0'']'
  url: https://github.com/ijl/orjson
---

orjson
======


Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy.

https://github.com/ijl/orjson
# Available modules


The overview below shows which orjson installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using orjson, load one of these modules using a `module load` command like:

```shell
module load orjson/3.9.15-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|orjson/3.9.15-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|


### orjson/3.9.15-GCCcore-12.3.0

This is a list of extensions included in the module:

mypy-1.10.0, mypy_extensions-1.0.0, orjson-3.9.15, ruff-0.4.8