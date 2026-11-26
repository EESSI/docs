---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Python interface to the igraph high performance graph library, primarily\
    \ aimed at complex network\n research and analysis."
  license: Not confirmed
  name: python-igraph
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
  softwareVersion: '[''0.11.9'']'
  url: https://igraph.org/python
---
# python-igraph


Python interface to the igraph high performance graph library, primarily aimed at complex network
 research and analysis.

<small>homepage: </small><span class="software-link">[https://igraph.org/python](https://igraph.org/python)</span>

## Available installations


|python-igraph version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.11.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`python-igraph/0.11.9-foss-2025a`|

## Extensions

Overview of extensions included in python-igraph installations


### cairocffi


|`cairocffi` version|python-igraph modules that include it|
| --- | --- |
|1.7.1|`python-igraph/0.11.9-foss-2025a`|

### igraph


|`igraph` version|python-igraph modules that include it|
| --- | --- |
|0.11.9|`python-igraph/0.11.9-foss-2025a`|

### texttable


|`texttable` version|python-igraph modules that include it|
| --- | --- |
|1.7.0|`python-igraph/0.11.9-foss-2025a`|