---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The R kernel for the 'Jupyter' environment executes R code\n which\
    \ the front-end (Jupyter Notebook or other front-ends) submits to the\n kernel\
    \ via the network."
  license: Not confirmed
  name: IRkernel
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
  softwareVersion: '[''1.3.2'']'
  url: https://irkernel.github.io
---
# IRkernel


The R kernel for the 'Jupyter' environment executes R code
 which the front-end (Jupyter Notebook or other front-ends) submits to the
 kernel via the network.

<small>homepage: </small><span class="software-link">[https://irkernel.github.io](https://irkernel.github.io)</span>

## Available installations


|IRkernel version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.3.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`IRkernel/1.3.2-gfbf-2025b-R-4.5.2`|

## Extensions

Overview of extensions included in IRkernel installations


### IRdisplay


|`IRdisplay` version|IRkernel modules that include it|
| --- | --- |
|1.1|`IRkernel/1.3.2-gfbf-2025b-R-4.5.2`|

### IRkernel


|`IRkernel` version|IRkernel modules that include it|
| --- | --- |
|1.3.2|`IRkernel/1.3.2-gfbf-2025b-R-4.5.2`|

### pbdZMQ


|`pbdZMQ` version|IRkernel modules that include it|
| --- | --- |
|0.3-14|`IRkernel/1.3.2-gfbf-2025b-R-4.5.2`|

### repr


|`repr` version|IRkernel modules that include it|
| --- | --- |
|1.1.7|`IRkernel/1.3.2-gfbf-2025b-R-4.5.2`|

### uuid


|`uuid` version|IRkernel modules that include it|
| --- | --- |
|1.2-2|`IRkernel/1.3.2-gfbf-2025b-R-4.5.2`|