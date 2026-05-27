---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "A Load Balancing Library (ALL) aims to provide an easy way to include\
    \ dynamic\ndomain-based load balancing into particle based simulation codes. The\
    \ library\nis developed in the Simulation Laboratory Molecular Systems of the\
    \ J\xFClich\nSupercomputing Centre at Forschungszentrum J\xFClich."
  license: Not confirmed
  name: ALL
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
  softwareVersion: '[''0.9.2'']'
  url: https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing
---
# ALL


A Load Balancing Library (ALL) aims to provide an easy way to include dynamic
domain-based load balancing into particle based simulation codes. The library
is developed in the Simulation Laboratory Molecular Systems of the Jülich
Supercomputing Centre at Forschungszentrum Jülich.

<small>homepage: </small><span class="software-link">[https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing](https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing)</span>

## Available installations


|ALL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.9.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ALL/0.9.2-foss-2023a`|