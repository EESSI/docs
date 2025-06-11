---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: libglvnd is a vendor-neutral dispatch layer for arbitrating OpenGL
    API calls between multiple vendors.
  license: Not confirmed
  name: libglvnd
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
  softwareVersion: '[''libglvnd/1.6.0-GCCcore-12.2.0'', ''libglvnd/1.6.0-GCCcore-12.3.0'',
    ''libglvnd/1.7.0-GCCcore-13.2.0'']'
  url: https://gitlab.freedesktop.org/glvnd/libglvnd
---

libglvnd
========


libglvnd is a vendor-neutral dispatch layer for arbitrating OpenGL API calls between multiple vendors.

https://gitlab.freedesktop.org/glvnd/libglvnd
# Available modules


The overview below shows which libglvnd installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libglvnd, load one of these modules using a `module load` command like:

```shell
module load libglvnd/1.7.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libglvnd/1.7.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|libglvnd/1.6.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|libglvnd/1.6.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
