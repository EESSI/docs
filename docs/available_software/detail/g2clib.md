---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Library contains GRIB2 encoder/decoder ('C' version).
  license: Not confirmed
  name: g2clib
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
  softwareVersion: '[''2.3.0'']'
  url: https://github.com/NOAA-EMC/NCEPLIBS-g2c
---
# g2clib


Library contains GRIB2 encoder/decoder ('C' version).

<small>homepage: </small><span class="software-link">[https://github.com/NOAA-EMC/NCEPLIBS-g2c](https://github.com/NOAA-EMC/NCEPLIBS-g2c)</span>

## Available installations


|g2clib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`g2clib/2.3.0-GCCcore-14.3.0`|