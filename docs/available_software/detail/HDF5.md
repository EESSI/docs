---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: HDF5 is a data model, library, and file format for storing and managing
    data. It supports an unlimited variety of datatypes, and is designed for flexible
    and efficient I/O and for high volume and complex data.
  license: Not confirmed
  name: HDF5
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
  softwareVersion: '[''HDF5/1.14.0-gompi-2022b'', ''HDF5/1.14.0-gompi-2023a'', ''HDF5/1.14.3-gompi-2023b'']'
  url: https://portal.hdfgroup.org/display/support
---

HDF5
====


HDF5 is a data model, library, and file format for storing and managing data. It supports an unlimited variety of datatypes, and is designed for flexible and efficient I/O and for high volume and complex data.

https://portal.hdfgroup.org/display/support
# Available modules


The overview below shows which HDF5 installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using HDF5, load one of these modules using a `module load` command like:

```shell
module load HDF5/1.14.3-gompi-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|HDF5/1.14.3-gompi-2023b|x|x|x|x|x|x|x|x|x|x|x|
|HDF5/1.14.0-gompi-2023a|x|x|x|x|x|x|x|x|x|x|x|
|HDF5/1.14.0-gompi-2022b|x|x|x|x|x|x|x|x|x|x|x|
