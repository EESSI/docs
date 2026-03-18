---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Cube, which is used as performance report explorer for Scalasca\
    \ and Score-P,\n is a generic tool for displaying a multi-dimensional performance\
    \ space\n consisting of the dimensions (i) performance metric, (ii) call path,\
    \ and\n (iii) system resource. Each dimension can be represented as a tree, where\n\
    \ non-leaf nodes of the tree can be collapsed or expanded to achieve the\n desired\
    \ level of granularity.\n\n This module provides the Cube high-performance C writer\
    \ library component.\n"
  license: Not confirmed
  name: CubeWriter
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
  softwareVersion: '[''4.9'', ''4.8.2'']'
  url: https://www.scalasca.org/software/cube-4.x/download.html
---
# CubeWriter



 Cube, which is used as performance report explorer for Scalasca and Score-P,
 is a generic tool for displaying a multi-dimensional performance space
 consisting of the dimensions (i) performance metric, (ii) call path, and
 (iii) system resource. Each dimension can be represented as a tree, where
 non-leaf nodes of the tree can be collapsed or expanded to achieve the
 desired level of granularity.

 This module provides the Cube high-performance C writer library component.


<small>homepage: </small><span class="software-link">[https://www.scalasca.org/software/cube-4.x/download.html](https://www.scalasca.org/software/cube-4.x/download.html)</span>

## Available installations


|CubeWriter version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.8.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`CubeWriter/4.8.2-GCCcore-13.2.0`|
|4.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`CubeWriter/4.9-GCCcore-14.2.0`|