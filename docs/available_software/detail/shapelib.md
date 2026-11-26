---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The Shapefile C Library provides the ability to write simple C

    programs for reading, writing and updating (to a limited extent) ESRI

    Shapefiles, and the associated attribute file (.dbf).'
  license: Not confirmed
  name: shapelib
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
  softwareVersion: '[''1.6.3'']'
  url: http://shapelib.maptools.org/
---
# shapelib


The Shapefile C Library provides the ability to write simple C
programs for reading, writing and updating (to a limited extent) ESRI
Shapefiles, and the associated attribute file (.dbf).

<small>homepage: </small><span class="software-link">[http://shapelib.maptools.org/](http://shapelib.maptools.org/)</span>

## Available installations


|shapelib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.6.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`shapelib/1.6.3-GCCcore-14.3.0`|