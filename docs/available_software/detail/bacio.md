---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This library performs binary I/O for the NCEP models,

    processing formatted and unformatted byte-addressable data records,

    and helping transform little endian files into big endian files.'
  license: Not confirmed
  name: bacio
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
  softwareVersion: '[''2.6.0'']'
  url: https://github.com/NOAA-EMC/NCEPLIBS-bacio
---
# bacio


This library performs binary I/O for the NCEP models,
processing formatted and unformatted byte-addressable data records,
and helping transform little endian files into big endian files.

<small>homepage: </small><span class="software-link">[https://github.com/NOAA-EMC/NCEPLIBS-bacio](https://github.com/NOAA-EMC/NCEPLIBS-bacio)</span>

## Available installations


|bacio version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`bacio/2.6.0-GCC-14.3.0`|