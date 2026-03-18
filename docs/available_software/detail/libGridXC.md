---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "A library to compute the exchange and correlation energy\n and potential\
    \ in spherical (i.e. atoms) or periodic systems."
  license: Not confirmed
  name: libGridXC
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
  softwareVersion: '[''2.0.2'']'
  url: https://gitlab.com/siesta-project/libraries/libgridxc
---
# libGridXC


A library to compute the exchange and correlation energy
 and potential in spherical (i.e. atoms) or periodic systems.

<small>homepage: </small><span class="software-link">[https://gitlab.com/siesta-project/libraries/libgridxc](https://gitlab.com/siesta-project/libraries/libgridxc)</span>

## Available installations


|libGridXC version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libGridXC/2.0.2-gompi-2023a`|