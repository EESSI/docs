---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "HTTP proxy for node.js including a REST API for updating the routing\
    \ table.\n Developed as a part of the Jupyter Hub multi-user server."
  license: Not confirmed
  name: configurable-http-proxy
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
  softwareVersion: '[''5.1.0'']'
  url: https://github.com/jupyterhub/configurable-http-proxy
---
# configurable-http-proxy


HTTP proxy for node.js including a REST API for updating the routing table.
 Developed as a part of the Jupyter Hub multi-user server.

<small>homepage: </small><span class="software-link">[https://github.com/jupyterhub/configurable-http-proxy](https://github.com/jupyterhub/configurable-http-proxy)</span>

## Available installations


|configurable-http-proxy version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`configurable-http-proxy/5.1.0-GCCcore-14.3.0`|