---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This library performs binary I/O for the NCEP models,

    processing formatted and unformatted byte-addressable data records,

    and helping transform little endian files into big endian files.'
  license: Not confirmed
  name: ip
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
  softwareVersion: '[''5.4.0'']'
  url: https://github.com/NOAA-EMC/NCEPLIBS-ip
---
# ip


This library performs binary I/O for the NCEP models,
processing formatted and unformatted byte-addressable data records,
and helping transform little endian files into big endian files.

<small>homepage: </small><span class="software-link">[https://github.com/NOAA-EMC/NCEPLIBS-ip](https://github.com/NOAA-EMC/NCEPLIBS-ip)</span>

## Available installations


|ip version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.4.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ip/5.4.0-gfbf-2025b`|