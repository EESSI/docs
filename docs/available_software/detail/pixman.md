---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Pixman is a low-level software library for pixel manipulation, providing
    features such as image compositing and trapezoid rasterization. Important users
    of pixman are the cairo graphics library and the X server.
  license: Not confirmed
  name: pixman
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
  softwareVersion: '[''pixman/0.42.2-GCCcore-12.2.0'', ''pixman/0.42.2-GCCcore-12.3.0'',
    ''pixman/0.42.2-GCCcore-13.2.0'']'
  url: http://www.pixman.org/
---

pixman
======


Pixman is a low-level software library for pixel manipulation, providing features such as image compositing and trapezoid rasterization. Important users of pixman are the cairo graphics library and the X server.

http://www.pixman.org/
# Available modules


The overview below shows which pixman installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using pixman, load one of these modules using a `module load` command like:

```shell
module load pixman/0.42.2-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pixman/0.42.2-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|
|pixman/0.42.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|
|pixman/0.42.2-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|
