---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Abseil is an open-source collection of C++ library code designed to
    augment theC++ standard library. The Abseil library code is collected from Google's
    ownC++ code base, has been extensively tested and used in production, and is thesame
    code we depend on in our daily coding lives.
  license: Not confirmed
  name: Abseil
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
  softwareVersion: '[''Abseil/20230125.2-GCCcore-12.2.0'', ''Abseil/20230125.3-GCCcore-12.3.0'',
    ''Abseil/20240116.1-GCCcore-13.2.0'']'
  url: https://abseil.io/
---

Abseil
======


Abseil is an open-source collection of C++ library code designed to augment theC++ standard library. The Abseil library code is collected from Google's ownC++ code base, has been extensively tested and used in production, and is thesame code we depend on in our daily coding lives.

https://abseil.io/
# Available modules


The overview below shows which Abseil installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Abseil, load one of these modules using a `module load` command like:

```shell
module load Abseil/20240116.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Abseil/20240116.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Abseil/20230125.3-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Abseil/20230125.2-GCCcore-12.2.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
