---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Python interface to the Redis key-value store.
  license: Not confirmed
  name: redis-py
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
  softwareVersion: '[''redis-py/5.0.1-GCCcore-12.3.0'']'
  url: https://github.com/redis/redis-py
---

redis-py
========


The Python interface to the Redis key-value store.

https://github.com/redis/redis-py
# Available modules


The overview below shows which redis-py installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using redis-py, load one of these modules using a `module load` command like:

```shell
module load redis-py/5.0.1-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|redis-py/5.0.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### redis-py/5.0.1-GCCcore-12.3.0

This is a list of extensions included in the module:

async-timeout-4.0.3, redis-py-5.0.1