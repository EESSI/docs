---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The xprop utility is for displaying window and font properties in\
    \ an X server.\n One window or font is selected using the command line arguments\
    \ or possibly\n in the case of a window, by clicking on the desired window. A\
    \ list of\n properties is then given, possibly with formatting information."
  license: Not confirmed
  name: xprop
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
  softwareVersion: '[''1.2.8'', ''1.2.6'']'
  url: https://www.x.org/wiki/
---
# xprop


The xprop utility is for displaying window and font properties in an X server.
 One window or font is selected using the command line arguments or possibly
 in the case of a window, by clicking on the desired window. A list of
 properties is then given, possibly with formatting information.

<small>homepage: </small><span class="software-link">[https://www.x.org/wiki/](https://www.x.org/wiki/)</span>

## Available installations


|xprop version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2.6|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`xprop/1.2.6-GCCcore-12.3.0`|
|1.2.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`xprop/1.2.8-GCCcore-14.2.0`|