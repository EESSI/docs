---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "A C library for reading/writing high-throughput sequencing data.\n\
    \ This package includes the utilities bgzip and tabix"
  license: Not confirmed
  name: HTSlib
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
  softwareVersion: '[''1.22.1'']'
  url: https://www.htslib.org/
---
# HTSlib


A C library for reading/writing high-throughput sequencing data.
 This package includes the utilities bgzip and tabix

<small>homepage: </small><span class="software-link">[https://www.htslib.org/](https://www.htslib.org/)</span>

## Available installations


|HTSlib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.22.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`HTSlib/1.22.1-GCC-14.3.0`|