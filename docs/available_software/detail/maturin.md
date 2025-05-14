---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: This project is meant as a zero configurationreplacement for setuptools-rust
    and milksnake. It supports buildingwheels for python 3.5+ on windows, linux, mac
    and freebsd, can uploadthem to pypi and has basic pypy and graalpy support.
  license: Not confirmed
  name: maturin
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
  softwareVersion: '[''maturin/1.1.0-GCCcore-12.3.0'', ''maturin/1.4.0-GCCcore-12.3.0-Rust-1.75.0'',
    ''maturin/1.5.0-GCCcore-13.2.0-Rust-1.76.0'']'
  url: https://github.com/pyo3/maturin
---

maturin
=======


This project is meant as a zero configurationreplacement for setuptools-rust and milksnake. It supports buildingwheels for python 3.5+ on windows, linux, mac and freebsd, can uploadthem to pypi and has basic pypy and graalpy support.

https://github.com/pyo3/maturin
# Available modules


The overview below shows which maturin installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using maturin, load one of these modules using a `module load` command like:

```shell
module load maturin/1.5.0-GCCcore-13.2.0-Rust-1.76.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|maturin/1.5.0-GCCcore-13.2.0-Rust-1.76.0|x|x|x|x|x|x|x|x|x|x|x|
|maturin/1.4.0-GCCcore-12.3.0-Rust-1.75.0|x|x|x|x|x|x|x|x|x|x|x|
|maturin/1.1.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
