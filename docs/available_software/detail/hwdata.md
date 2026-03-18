---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'hwdata contains various hardware identification and configuration
    data, such as the pci.ids and

    usb.ids databases.'
  license: Not confirmed
  name: hwdata
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
  softwareVersion: '[''0.403'']'
  url: https://github.com/vcrhonek/hwdata
---
# hwdata


hwdata contains various hardware identification and configuration data, such as the pci.ids and
usb.ids databases.

<small>homepage: </small><span class="software-link">[https://github.com/vcrhonek/hwdata](https://github.com/vcrhonek/hwdata)</span>

## Available installations


|hwdata version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.403|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`hwdata/0.403-GCCcore-14.3.0`|