---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The ScaLAPACK (or Scalable LAPACK) library includes a subset of LAPACK
    routines redesigned for distributed memory MIMD parallel computers.
  license: Not confirmed
  name: ScaLAPACK
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
  softwareVersion: '[''ScaLAPACK/2.2.0-gompi-2022b-fb'', ''ScaLAPACK/2.2.0-gompi-2023a-fb'',
    ''ScaLAPACK/2.2.0-gompi-2023b-fb'']'
  url: https://www.netlib.org/scalapack/
---

ScaLAPACK
=========


The ScaLAPACK (or Scalable LAPACK) library includes a subset of LAPACK routines redesigned for distributed memory MIMD parallel computers.

https://www.netlib.org/scalapack/
# Available modules


The overview below shows which ScaLAPACK installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ScaLAPACK, load one of these modules using a `module load` command like:

```shell
module load ScaLAPACK/2.2.0-gompi-2023b-fb
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ScaLAPACK/2.2.0-gompi-2023b-fb|x|x|x|x|x|x|x|x|-|x|
|ScaLAPACK/2.2.0-gompi-2023a-fb|x|x|x|x|x|x|x|x|-|x|
|ScaLAPACK/2.2.0-gompi-2022b-fb|x|x|x|x|x|x|x|x|-|x|
