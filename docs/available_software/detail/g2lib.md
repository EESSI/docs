---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Library contains GRIB2 encoder/decoder and search/indexing routines.
  license: Not confirmed
  name: g2lib
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
  softwareVersion: '[''4.0.0'']'
  url: https://github.com/NOAA-EMC/NCEPLIBS-g2
---
# g2lib


Library contains GRIB2 encoder/decoder and search/indexing routines.

<small>homepage: </small><span class="software-link">[https://github.com/NOAA-EMC/NCEPLIBS-g2](https://github.com/NOAA-EMC/NCEPLIBS-g2)</span>

## Available installations


|g2lib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`g2lib/4.0.0-gfbf-2025b`|