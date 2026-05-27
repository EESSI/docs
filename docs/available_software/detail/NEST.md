---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "NEST is a simulator for spiking neural network models that focuses\
    \ on the\n dynamics, size and structure of neural systems rather than on the exact\
    \ morphology of individual neurons."
  license: Not confirmed
  name: NEST
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
  softwareVersion: '[''3.9'']'
  url: https://www.nest-simulator.org/
---
# NEST


NEST is a simulator for spiking neural network models that focuses on the
 dynamics, size and structure of neural systems rather than on the exact morphology of individual neurons.

<small>homepage: </small><span class="software-link">[https://www.nest-simulator.org/](https://www.nest-simulator.org/)</span>

## Available installations


|NEST version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`NEST/3.9-foss-2023a`|