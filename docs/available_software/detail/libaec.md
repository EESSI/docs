---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Libaec provides fast lossless compression of 1 up to 32 bit wide signed
    or unsigned integers(samples). The library achieves best results for low entropy
    data as often encountered in space imaginginstrument data or numerical model output
    from weather or climate simulations. While floating point representationsare not
    directly supported, they can also be efficiently coded by grouping exponents and
    mantissa.
  license: Not confirmed
  name: libaec
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
  softwareVersion: '[''libaec/1.0.6-GCCcore-13.2.0'']'
  url: https://gitlab.dkrz.de/k202009/libaec
---

libaec
======


Libaec provides fast lossless compression of 1 up to 32 bit wide signed or unsigned integers(samples). The library achieves best results for low entropy data as often encountered in space imaginginstrument data or numerical model output from weather or climate simulations. While floating point representationsare not directly supported, they can also be efficiently coded by grouping exponents and mantissa.

https://gitlab.dkrz.de/k202009/libaec
# Available modules


The overview below shows which libaec installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libaec, load one of these modules using a `module load` command like:

```shell
module load libaec/1.0.6-GCCcore-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 12:11:37 CEST)*

| |scv64/generic|
| :---: | :---: |
|libaec/1.0.6-GCCcore-13.2.0|x|
