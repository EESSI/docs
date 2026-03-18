---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'A full-featured and high-performance (see benchmark)

    event loop that is loosely modelled after libevent, but without its

    limitations and bugs. It is used in GNU Virtual Private Ethernet,

    rxvt-unicode, auditd, the Deliantra MORPG Server and Client, and many

    other programs.'
  license: Not confirmed
  name: libev
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
  softwareVersion: '[''4.33'']'
  url: http://software.schmorp.de/pkg/libev.html
---
# libev


A full-featured and high-performance (see benchmark)
event loop that is loosely modelled after libevent, but without its
limitations and bugs. It is used in GNU Virtual Private Ethernet,
rxvt-unicode, auditd, the Deliantra MORPG Server and Client, and many
other programs.

<small>homepage: </small><span class="software-link">[http://software.schmorp.de/pkg/libev.html](http://software.schmorp.de/pkg/libev.html)</span>

## Available installations


|libev version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.33|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libev/4.33-GCC-12.3.0`|
|4.33|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libev/4.33-GCCcore-13.3.0`|