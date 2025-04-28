---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: This Python module contains a pseudo-application that can be used as
    a blackbox to reproduce Amdahl's Law. It does not do real calculations, nor any
    realcommunication, so can easily be overloaded.
  license: Not confirmed
  name: amdahl
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
  softwareVersion: '[''amdahl/0.3.1-gompi-2023a'']'
  url: https://github.com/hpc-carpentry/amdahl
---

amdahl
======


This Python module contains a pseudo-application that can be used as a blackbox to reproduce Amdahl's Law. It does not do real calculations, nor any realcommunication, so can easily be overloaded.

https://github.com/hpc-carpentry/amdahl
# Available modules


The overview below shows which amdahl installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using amdahl, load one of these modules using a `module load` command like:

```shell
module load amdahl/0.3.1-gompi-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|amdahl/0.3.1-gompi-2023a|x|x|x|x|x|x|x|x|x|x|
