---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'ecCodes is a package developed by ECMWF which provides an application
    programming interface and a set of tools for decoding and encoding messages in
    the following formats: WMO FM-92 GRIB edition 1 and edition 2, WMO FM-94 BUFR
    edition 3 and edition 4, WMO GTS abbreviated header (only decoding).'
  license: Not confirmed
  name: ecCodes
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
  softwareVersion: '[''ecCodes/2.31.0-gompi-2023a'', ''ecCodes/2.31.0-gompi-2023b'']'
  url: https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home
---

ecCodes
=======


ecCodes is a package developed by ECMWF which provides an application programming interface and a set of tools for decoding and encoding messages in the following formats: WMO FM-92 GRIB edition 1 and edition 2, WMO FM-94 BUFR edition 3 and edition 4, WMO GTS abbreviated header (only decoding).

https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home
# Available modules


The overview below shows which ecCodes installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ecCodes, load one of these modules using a `module load` command like:

```shell
module load ecCodes/2.31.0-gompi-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ecCodes/2.31.0-gompi-2023b|x|x|x|-|x|x|x|x|x|x|x|x|
|ecCodes/2.31.0-gompi-2023a|x|x|x|-|x|x|x|x|x|x|x|x|
