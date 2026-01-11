---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: PyTables is a package for managing hierarchical datasets and designed
    to efficiently and easily cope with extremely large amounts of data. PyTables
    is built on top of the HDF5 library, using the Python language and the NumPy package.
    It features an object-oriented interface that, combined with C extensions for
    the performance-critical parts of the code (generated using Cython), makes it
    a fast, yet extremely easy to use tool for interactively browsing, processing
    and searching very large amounts of data. One important feature of PyTables is
    that it optimizes memory and disk resources so that data takes much less space
    (specially if on-flight compression is used) than other solutions such as relational
    or object oriented databases.
  license: Not confirmed
  name: PyTables
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
  softwareVersion: '[''PyTables/3.9.2-foss-2023b'']'
  url: https://www.pytables.org
---

PyTables
========


PyTables is a package for managing hierarchical datasets and designed to efficiently and easily cope with extremely large amounts of data. PyTables is built on top of the HDF5 library, using the Python language and the NumPy package. It features an object-oriented interface that, combined with C extensions for the performance-critical parts of the code (generated using Cython), makes it a fast, yet extremely easy to use tool for interactively browsing, processing and searching very large amounts of data. One important feature of PyTables is that it optimizes memory and disk resources so that data takes much less space (specially if on-flight compression is used) than other solutions such as relational or object oriented databases.

https://www.pytables.org
# Available modules


The overview below shows which PyTables installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PyTables, load one of these modules using a `module load` command like:

```shell
module load PyTables/3.9.2-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PyTables/3.9.2-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### PyTables/3.9.2-foss-2023b

This is a list of extensions included in the module:

blosc2-2.5.1, ndindex-1.8, tables-3.9.2