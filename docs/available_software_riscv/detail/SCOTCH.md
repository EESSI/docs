---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Software package and libraries for sequential and parallel graph partitioning,

    static mapping, and sparse matrix block ordering, and sequential mesh and hypergraph
    partitioning.'
  license: Not confirmed
  name: SCOTCH
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
  softwareVersion: '[''7.0.10'']'
  url: https://www.labri.fr/perso/pelegrin/scotch/
---
# SCOTCH


Software package and libraries for sequential and parallel graph partitioning,
static mapping, and sparse matrix block ordering, and sequential mesh and hypergraph partitioning.

<small>homepage: </small><span class="software-link">[https://www.labri.fr/perso/pelegrin/scotch/](https://www.labri.fr/perso/pelegrin/scotch/)</span>

## Available installations


|SCOTCH version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.0.10|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`SCOTCH/7.0.10-gompi-2025b`|