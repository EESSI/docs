---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The libffi library provides a portable, high level programming interface\
    \ to\n various calling conventions. This allows a programmer to call any function\n\
    \ specified by a call interface description at run-time."
  license: Not confirmed
  name: libffi
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
  softwareVersion: '[''3.5.1'', ''3.4.5'']'
  url: https://sourceware.org/libffi/
---
# libffi


The libffi library provides a portable, high level programming interface to
 various calling conventions. This allows a programmer to call any function
 specified by a call interface description at run-time.

<small>homepage: </small><span class="software-link">[https://sourceware.org/libffi/](https://sourceware.org/libffi/)</span>

## Available installations


|libffi version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.5.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libffi/3.5.1-GCCcore-14.3.0`|
|3.4.5|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libffi/3.4.5-GCCcore-14.2.0`|