---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Libfabric is a core component of OFI. It is the library that defines and exports

    the user-space API of OFI, and is typically the only software that applications

    deal with directly. It works in conjunction with provider libraries, which are

    often integrated directly into libfabric.

    '
  license: Not confirmed
  name: libfabric
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
  softwareVersion: '[''2.1.0'', ''2.0.0'']'
  url: https://ofiwg.github.io/libfabric/
---
# libfabric



Libfabric is a core component of OFI. It is the library that defines and exports
the user-space API of OFI, and is typically the only software that applications
deal with directly. It works in conjunction with provider libraries, which are
often integrated directly into libfabric.


<small>homepage: </small><span class="software-link">[https://ofiwg.github.io/libfabric/](https://ofiwg.github.io/libfabric/)</span>

## Available installations


|libfabric version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.1.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libfabric/2.1.0-GCCcore-14.3.0`|
|2.0.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libfabric/2.0.0-GCCcore-14.2.0`|