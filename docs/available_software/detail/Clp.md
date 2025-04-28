---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Clp (Coin-or linear programming) is an open-source linear programming
    solver.It is primarily meant to be used as a callable library, but a basic,stand-alone
    executable version is also available.
  license: Not confirmed
  name: Clp
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
  softwareVersion: '[''Clp/1.17.9-foss-2023a'']'
  url: https://github.com/coin-or/Clp
---

Clp
===


Clp (Coin-or linear programming) is an open-source linear programming solver.It is primarily meant to be used as a callable library, but a basic,stand-alone executable version is also available.

https://github.com/coin-or/Clp
# Available modules


The overview below shows which Clp installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Clp, load one of these modules using a `module load` command like:

```shell
module load Clp/1.17.9-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Clp/1.17.9-foss-2023a|x|x|x|x|x|x|x|x|x|x|
