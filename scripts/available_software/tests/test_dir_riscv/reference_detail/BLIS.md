---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'BLIS is a portable software framework for instantiating high-performance

    BLAS-like dense linear algebra libraries.'
  license: Not confirmed
  name: BLIS
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
  softwareVersion: '[''2.0'', ''1.1'']'
  url: https://github.com/flame/blis/
---
# BLIS


BLIS is a portable software framework for instantiating high-performance
BLAS-like dense linear algebra libraries.

<small>homepage: </small><span class="software-link">[https://github.com/flame/blis/](https://github.com/flame/blis/)</span>

## Available installations


|BLIS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BLIS/1.1-GCC-14.2.0`|
|2.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BLIS/2.0-GCC-14.3.0`|