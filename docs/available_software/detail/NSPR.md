---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Netscape Portable Runtime (NSPR) provides a platform-neutral API for
    system level and libc-like functions.
  license: Not confirmed
  name: NSPR
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
  softwareVersion: '[''NSPR/4.35-GCCcore-12.2.0'', ''NSPR/4.35-GCCcore-12.3.0'', ''NSPR/4.35-GCCcore-13.2.0'']'
  url: https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR
---

NSPR
====


Netscape Portable Runtime (NSPR) provides a platform-neutral API for system level and libc-like functions.

https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR
# Available modules


The overview below shows which NSPR installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using NSPR, load one of these modules using a `module load` command like:

```shell
module load NSPR/4.35-GCCcore-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|NSPR/4.35-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|NSPR/4.35-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|NSPR/4.35-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
