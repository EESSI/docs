---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Process Management for Exascale Environments

    PMI Exascale (PMIx) represents an attempt to

    provide an extended version of the PMI standard specifically designed

    to support clusters up to and including exascale sizes. The overall

    objective of the project is not to branch the existing pseudo-standard

    definitions - in fact, PMIx fully supports both of the existing PMI-1

    and PMI-2 APIs - but rather to (a) augment and extend those APIs to

    eliminate some current restrictions that impact scalability, and (b)

    provide a reference implementation of the PMI-server that demonstrates

    the desired level of scalability.

    '
  license: Not confirmed
  name: PMIx
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
  softwareVersion: '[''5.0.8'', ''5.0.6'']'
  url: https://pmix.org/
---
# PMIx


Process Management for Exascale Environments
PMI Exascale (PMIx) represents an attempt to
provide an extended version of the PMI standard specifically designed
to support clusters up to and including exascale sizes. The overall
objective of the project is not to branch the existing pseudo-standard
definitions - in fact, PMIx fully supports both of the existing PMI-1
and PMI-2 APIs - but rather to (a) augment and extend those APIs to
eliminate some current restrictions that impact scalability, and (b)
provide a reference implementation of the PMI-server that demonstrates
the desired level of scalability.


<small>homepage: </small><span class="software-link">[https://pmix.org/](https://pmix.org/)</span>

## Available installations


|PMIx version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.0.8|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PMIx/5.0.8-GCCcore-14.3.0`|
|5.0.6|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PMIx/5.0.6-GCCcore-14.2.0`|