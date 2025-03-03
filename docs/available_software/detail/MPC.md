---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Gnu Mpc is a C library for the arithmetic of complex numbers with arbitrarily
    high precision and correct rounding of the result. It extends the principles of
    the IEEE-754 standard for fixed precision real floating point numbers to complex
    numbers, providing well-defined semantics for every operation. At the same time,
    speed of operation at high precision is a major design goal.
  license: Not confirmed
  name: MPC
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
  softwareVersion: '[''MPC/1.3.1-GCCcore-12.2.0'', ''MPC/1.3.1-GCCcore-12.3.0'', ''MPC/1.3.1-GCCcore-13.2.0'']'
  url: http://www.multiprecision.org/
---

MPC
===


Gnu Mpc is a C library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding of the result. It extends the principles of the IEEE-754 standard for fixed precision real floating point numbers to complex numbers, providing well-defined semantics for every operation. At the same time, speed of operation at high precision is a major design goal.

http://www.multiprecision.org/
# Available modules


The overview below shows which MPC installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using MPC, load one of these modules using a `module load` command like:

```shell
module load MPC/1.3.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MPC/1.3.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|
|MPC/1.3.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|
|MPC/1.3.1-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|
