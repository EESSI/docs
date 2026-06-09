---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "NetCDF (network Common Data Form) is a set of software libraries\n\
    \ and machine-independent data formats that support the creation, access, and\
    \ sharing of array-oriented\n scientific data."
  license: Not confirmed
  name: netCDF
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
  softwareVersion: '[''4.9.3'']'
  url: https://www.unidata.ucar.edu/software/netcdf/
---
# netCDF


NetCDF (network Common Data Form) is a set of software libraries
 and machine-independent data formats that support the creation, access, and sharing of array-oriented
 scientific data.

<small>homepage: </small><span class="software-link">[https://www.unidata.ucar.edu/software/netcdf/](https://www.unidata.ucar.edu/software/netcdf/)</span>

## Available installations


|netCDF version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.9.3|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`netCDF/4.9.3-gompi-2025b`|