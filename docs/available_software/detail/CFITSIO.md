---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: CFITSIO is a library of C and Fortran subroutines for reading and writing
    data files inFITS (Flexible Image Transport System) data format.
  license: Not confirmed
  name: CFITSIO
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
  softwareVersion: '[''CFITSIO/4.2.0-GCCcore-12.2.0'', ''CFITSIO/4.3.0-GCCcore-12.3.0'',
    ''CFITSIO/4.3.1-GCCcore-13.2.0'']'
  url: https://heasarc.gsfc.nasa.gov/fitsio/
---

CFITSIO
=======


CFITSIO is a library of C and Fortran subroutines for reading and writing data files inFITS (Flexible Image Transport System) data format.

https://heasarc.gsfc.nasa.gov/fitsio/
# Available modules


The overview below shows which CFITSIO installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using CFITSIO, load one of these modules using a `module load` command like:

```shell
module load CFITSIO/4.3.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|CFITSIO/4.3.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|CFITSIO/4.3.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|CFITSIO/4.2.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
