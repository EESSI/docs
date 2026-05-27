---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The RT Topology Library exposes an API to create and

    manage standard (ISO 13249 aka SQL/MM) topologies using user-provided

    data stores.'
  license: Not confirmed
  name: librttopo
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
  softwareVersion: '[''1.1.0'']'
  url: https://git.osgeo.org/gitea/rttopo/librttopo
---
# librttopo


The RT Topology Library exposes an API to create and
manage standard (ISO 13249 aka SQL/MM) topologies using user-provided
data stores.

<small>homepage: </small><span class="software-link">[https://git.osgeo.org/gitea/rttopo/librttopo](https://git.osgeo.org/gitea/rttopo/librttopo)</span>

## Available installations


|librttopo version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`librttopo/1.1.0-GCC-12.3.0`|