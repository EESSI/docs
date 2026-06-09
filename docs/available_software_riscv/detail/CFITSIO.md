---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'CFITSIO is a library of C and Fortran subroutines for reading and
    writing data files in

    FITS (Flexible Image Transport System) data format.'
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
  softwareVersion: '[''4.6.2'']'
  url: https://heasarc.gsfc.nasa.gov/fitsio/
---
# CFITSIO


CFITSIO is a library of C and Fortran subroutines for reading and writing data files in
FITS (Flexible Image Transport System) data format.

<small>homepage: </small><span class="software-link">[https://heasarc.gsfc.nasa.gov/fitsio/](https://heasarc.gsfc.nasa.gov/fitsio/)</span>

## Available installations


|CFITSIO version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.6.2|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`CFITSIO/4.6.2-GCCcore-14.3.0`|