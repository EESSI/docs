---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Shapely is a BSD-licensed Python package for manipulation and analysis
    of planar geometric objects.

    It is based on the widely deployed GEOS (the engine of PostGIS) and JTS (from
    which GEOS is ported) libraries.'
  license: Not confirmed
  name: Shapely
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
  softwareVersion: '[''2.0.1'']'
  url: https://github.com/Toblerity/Shapely
---
# Shapely


Shapely is a BSD-licensed Python package for manipulation and analysis of planar geometric objects.
It is based on the widely deployed GEOS (the engine of PostGIS) and JTS (from which GEOS is ported) libraries.

<small>homepage: </small><span class="software-link">[https://github.com/Toblerity/Shapely](https://github.com/Toblerity/Shapely)</span>

## Available installations


|Shapely version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Shapely/2.0.1-gfbf-2023a`|