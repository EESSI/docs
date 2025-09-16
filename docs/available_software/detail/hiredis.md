---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Hiredis is a minimalistic C client library for the Redis database.It
    is minimalistic because it just adds minimal support for the protocol,but at the
    same time it uses a high level printf-alike API in order tomake it much higher
    level than otherwise suggested by its minimal code baseand the lack of explicit
    bindings for every Redis command.
  license: Not confirmed
  name: hiredis
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
  softwareVersion: '[''hiredis/1.2.0-GCCcore-12.3.0'']'
  url: https://github.com/redis/hiredis
---

hiredis
=======


Hiredis is a minimalistic C client library for the Redis database.It is minimalistic because it just adds minimal support for the protocol,but at the same time it uses a high level printf-alike API in order tomake it much higher level than otherwise suggested by its minimal code baseand the lack of explicit bindings for every Redis command.

https://github.com/redis/hiredis
# Available modules


The overview below shows which hiredis installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using hiredis, load one of these modules using a `module load` command like:

```shell
module load hiredis/1.2.0-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|hiredis/1.2.0-GCCcore-12.3.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
