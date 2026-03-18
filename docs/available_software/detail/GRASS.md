---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The Geographic Resources Analysis Support System - used\n for geospatial\
    \ data management and analysis, image processing,\n graphics and maps production,\
    \ spatial modeling, and visualization"
  license: Not confirmed
  name: GRASS
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
  softwareVersion: '[''8.4.0'']'
  url: https://grass.osgeo.org
---
# GRASS


The Geographic Resources Analysis Support System - used
 for geospatial data management and analysis, image processing,
 graphics and maps production, spatial modeling, and visualization

<small>homepage: </small><span class="software-link">[https://grass.osgeo.org](https://grass.osgeo.org)</span>

## Available installations


|GRASS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|8.4.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`GRASS/8.4.0-foss-2023a`|