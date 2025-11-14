---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A scalable, efficient, cross-platform (Linux/macOS) and easy-to-use
    workflow engine in pure Python.This installation contains toil, with the cwl extras.
  license: Not confirmed
  name: toil-cwl
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
  softwareVersion: '[''toil-cwl/8.2.0-foss-2023b'']'
  url: https://github.com/DataBiosphere/toil
---

toil-cwl
========


A scalable, efficient, cross-platform (Linux/macOS) and easy-to-use workflow engine in pure Python.This installation contains toil, with the cwl extras.

https://github.com/DataBiosphere/toil
# Available modules


The overview below shows which toil-cwl installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using toil-cwl, load one of these modules using a `module load` command like:

```shell
module load toil-cwl/8.2.0-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|toil-cwl/8.2.0-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### toil-cwl/8.2.0-foss-2023b

This is a list of extensions included in the module:

addict-2.4.0, bleach-6.2.0, blessed-1.21.0, boltons-25.0.0, conda-package-streaming-0.11.0, configargparse-1.7.1, docker-7.1.0, enlighten-1.14.1, galaxy-tool-util-24.2.3, galaxy-util-24.2.3, prefixed-0.9.0, prompt_toolkit-3.0.51, PyPubSub-4.0.3, repoze.lru-0.7, Routes-2.5.1, toil-8.2.0, zipstream-new-1.1.8, zstandard-0.23.0