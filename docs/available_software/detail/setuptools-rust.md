---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: setuptools-rust is a plugin for setuptools to build Rust Python extensionsimplemented
    with PyO3 or rust-cpython.
  license: Not confirmed
  name: setuptools-rust
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
  softwareVersion: '[''setuptools-rust/1.6.0-GCCcore-12.3.0'', ''setuptools-rust/1.8.0-GCCcore-13.2.0'']'
  url: https://github.com/PyO3/setuptools-rust
---

setuptools-rust
===============


setuptools-rust is a plugin for setuptools to build Rust Python extensionsimplemented with PyO3 or rust-cpython.

https://github.com/PyO3/setuptools-rust
# Available modules


The overview below shows which setuptools-rust installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using setuptools-rust, load one of these modules using a `module load` command like:

```shell
module load setuptools-rust/1.8.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|setuptools-rust/1.8.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|setuptools-rust/1.6.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|


### setuptools-rust/1.8.0-GCCcore-13.2.0

This is a list of extensions included in the module:

semantic_version-2.10.0, setuptools-rust-1.8.0, typing_extensions-4.8.0

### setuptools-rust/1.6.0-GCCcore-12.3.0

This is a list of extensions included in the module:

semantic_version-2.10.0, setuptools-rust-1.6.0, typing_extensions-4.6.3