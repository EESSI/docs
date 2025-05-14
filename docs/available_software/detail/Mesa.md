---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Mesa is an open-source implementation of the OpenGL specification -
    a system for rendering interactive 3D graphics.
  license: Not confirmed
  name: Mesa
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
  softwareVersion: '[''Mesa/22.2.4-GCCcore-12.2.0'', ''Mesa/23.1.4-GCCcore-12.3.0'',
    ''Mesa/23.1.9-GCCcore-13.2.0'']'
  url: https://www.mesa3d.org/
---

Mesa
====


Mesa is an open-source implementation of the OpenGL specification - a system for rendering interactive 3D graphics.

https://www.mesa3d.org/
# Available modules


The overview below shows which Mesa installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Mesa, load one of these modules using a `module load` command like:

```shell
module load Mesa/23.1.9-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Mesa/23.1.9-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|Mesa/23.1.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|Mesa/22.2.4-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
