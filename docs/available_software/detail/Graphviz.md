---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Graphviz is open source graph visualization software. Graph visualization\n\
    \ is a way of representing structural information as diagrams of\n abstract graphs\
    \ and networks. It has important applications in networking,\n bioinformatics,\
    \  software engineering, database and web design, machine learning,\n and in visual\
    \ interfaces for other technical domains."
  license: Not confirmed
  name: Graphviz
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
  softwareVersion: '[''8.1.0'', ''13.1.2'']'
  url: https://www.graphviz.org/
---
# Graphviz


Graphviz is open source graph visualization software. Graph visualization
 is a way of representing structural information as diagrams of
 abstract graphs and networks. It has important applications in networking,
 bioinformatics,  software engineering, database and web design, machine learning,
 and in visual interfaces for other technical domains.

<small>homepage: </small><span class="software-link">[https://www.graphviz.org/](https://www.graphviz.org/)</span>

## Available installations


|Graphviz version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|13.1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Graphviz/13.1.2-GCCcore-14.3.0-minimal`|
|8.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Graphviz/8.1.0-GCCcore-12.3.0`|