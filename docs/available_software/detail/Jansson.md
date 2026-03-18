---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Jansson is a C library for encoding, decoding and manipulating JSON\
    \ data.\n Its main features and design principles are:\n * Simple and intuitive\
    \ API and data model\n * Comprehensive documentation\n * No dependencies on other\
    \ libraries\n * Full Unicode support (UTF-8)\n * Extensive test suite"
  license: Not confirmed
  name: Jansson
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
  softwareVersion: '[''2.14.1'', ''2.14'']'
  url: https://www.digip.org/jansson/
---
# Jansson


Jansson is a C library for encoding, decoding and manipulating JSON data.
 Its main features and design principles are:
 * Simple and intuitive API and data model
 * Comprehensive documentation
 * No dependencies on other libraries
 * Full Unicode support (UTF-8)
 * Extensive test suite

<small>homepage: </small><span class="software-link">[https://www.digip.org/jansson/](https://www.digip.org/jansson/)</span>

## Available installations


|Jansson version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.14|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Jansson/2.14-GCC-12.3.0`|
|2.14.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Jansson/2.14.1-GCCcore-13.3.0`|