---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Apache Arrow (incl. PyArrow Python bindings), a cross-language development
    platform for in-memory data.
  license: Not confirmed
  name: Arrow
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
  softwareVersion: '[''Arrow/11.0.0-gfbf-2022b'', ''Arrow/14.0.1-gfbf-2023a'', ''Arrow/16.1.0-gfbf-2023b'']'
  url: https://arrow.apache.org
---

Arrow
=====


Apache Arrow (incl. PyArrow Python bindings), a cross-language development platform for in-memory data.

https://arrow.apache.org
# Available modules


The overview below shows which Arrow installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Arrow, load one of these modules using a `module load` command like:

```shell
module load Arrow/16.1.0-gfbf-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Arrow/16.1.0-gfbf-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Arrow/14.0.1-gfbf-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Arrow/11.0.0-gfbf-2022b|x|-|x|x|x|x|x|x|x|x|x|x|x|x|


### Arrow/16.1.0-gfbf-2023b

This is a list of extensions included in the module:

pyarrow-16.1.0

### Arrow/14.0.1-gfbf-2023a

This is a list of extensions included in the module:

pyarrow-14.0.1