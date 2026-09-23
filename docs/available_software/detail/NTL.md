---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'NTL is a high-performance, portable C++ library providing data structures
    and

    algorithms for manipulating signed, arbitrary length integers, and for vectors,

    matrices, and polynomials over the integers and over finite fields.'
  license: Not confirmed
  name: NTL
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
  softwareVersion: '[''11.5.1'']'
  url: https://shoup.net/ntl/
---
# NTL


NTL is a high-performance, portable C++ library providing data structures and
algorithms for manipulating signed, arbitrary length integers, and for vectors,
matrices, and polynomials over the integers and over finite fields.

<small>homepage: </small><span class="software-link">[https://shoup.net/ntl/](https://shoup.net/ntl/)</span>

## Available installations


|NTL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|11.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`NTL/11.5.1-GCC-14.3.0`|