---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'MPFR C++ (MPREAL): Multiple precision floating point

    arithmetic library for C++.

    Thread-safe, cross-platform (MSVC, GCC, ICC), one-header C++ library.

    Supports C++11 features if available, C++03 compatible otherwise.'
  license: Not confirmed
  name: mpreal
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
  softwareVersion: '[''3.7.2'']'
  url: https://github.com/advanpix/mpreal
---
# mpreal


MPFR C++ (MPREAL): Multiple precision floating point
arithmetic library for C++.
Thread-safe, cross-platform (MSVC, GCC, ICC), one-header C++ library.
Supports C++11 features if available, C++03 compatible otherwise.

<small>homepage: </small><span class="software-link">[https://github.com/advanpix/mpreal](https://github.com/advanpix/mpreal)</span>

## Available installations


|mpreal version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.7.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`mpreal/3.7.2`|