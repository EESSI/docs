---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: SIONlib is a scalable I/O library for parallel access to task-local
    files. The library not only supports writing and reading binary data to or from
    several thousands of processors into a single or a small number of physical files,
    but also provides global open and close functions to access SIONlib files in parallel.
    This package provides a stripped-down installation of SIONlib for use with performance
    tools (e.g., Score-P), with renamed symbols to avoid conflicts when an application
    using SIONlib itself is linked against a tool requiring a different SIONlib version.
  license: Not confirmed
  name: SIONlib
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
  softwareVersion: '[''SIONlib/1.7.7-GCCcore-13.2.0-tools'']'
  url: https://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/SIONlib/_node.html
---

SIONlib
=======


SIONlib is a scalable I/O library for parallel access to task-local files. The library not only supports writing and reading binary data to or from several thousands of processors into a single or a small number of physical files, but also provides global open and close functions to access SIONlib files in parallel. This package provides a stripped-down installation of SIONlib for use with performance tools (e.g., Score-P), with renamed symbols to avoid conflicts when an application using SIONlib itself is linked against a tool requiring a different SIONlib version.

https://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/SIONlib/_node.html
# Available modules


The overview below shows which SIONlib installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using SIONlib, load one of these modules using a `module load` command like:

```shell
module load SIONlib/1.7.7-GCCcore-13.2.0-tools
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|SIONlib/1.7.7-GCCcore-13.2.0-tools|x|x|x|x|x|x|x|x|x|x|
