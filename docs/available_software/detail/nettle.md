---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Nettle is a cryptographic library that is designed to fit easily in
    more or less any context: In crypto toolkits for object-oriented languages (C++,
    Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.'
  license: Not confirmed
  name: nettle
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
  softwareVersion: '[''nettle/3.8.1-GCCcore-12.2.0'', ''nettle/3.9.1-GCCcore-12.3.0'',
    ''nettle/3.9.1-GCCcore-13.2.0'']'
  url: https://www.lysator.liu.se/~nisse/nettle/
---

nettle
======


Nettle is a cryptographic library that is designed to fit easily in more or less any context: In crypto toolkits for object-oriented languages (C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

https://www.lysator.liu.se/~nisse/nettle/
# Available modules


The overview below shows which nettle installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using nettle, load one of these modules using a `module load` command like:

```shell
module load nettle/3.9.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|nettle/3.9.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|nettle/3.9.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|nettle/3.8.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
