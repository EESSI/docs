---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "FLINT (Fast Library for Number Theory) is a C library in support of\
    \ computations\n in number theory. Operations that can be performed include conversions,\
    \ arithmetic, computing GCDs,\n factoring, solving linear systems, and evaluating\
    \ special functions. In addition, FLINT provides\n various low-level routines\
    \ for fast arithmetic. FLINT is extensively documented and tested."
  license: Not confirmed
  name: FLINT
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
  softwareVersion: '[''3.3.1'']'
  url: https://www.flintlib.org/
---
# FLINT


FLINT (Fast Library for Number Theory) is a C library in support of computations
 in number theory. Operations that can be performed include conversions, arithmetic, computing GCDs,
 factoring, solving linear systems, and evaluating special functions. In addition, FLINT provides
 various low-level routines for fast arithmetic. FLINT is extensively documented and tested.

<small>homepage: </small><span class="software-link">[https://www.flintlib.org/](https://www.flintlib.org/)</span>

## Available installations


|FLINT version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FLINT/3.3.1-gfbf-2025b`|