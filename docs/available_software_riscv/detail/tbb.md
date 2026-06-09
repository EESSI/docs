---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Intel(R) Threading Building Blocks (Intel(R) TBB) lets you easily\
    \ write parallel C++ programs that\n take full advantage of multicore performance,\
    \ that are portable, composable and have future-proof scalability."
  license: Not confirmed
  name: tbb
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
  softwareVersion: '[''2022.2.0'']'
  url: https://github.com/oneapi-src/oneTBB
---
# tbb


Intel(R) Threading Building Blocks (Intel(R) TBB) lets you easily write parallel C++ programs that
 take full advantage of multicore performance, that are portable, composable and have future-proof scalability.

<small>homepage: </small><span class="software-link">[https://github.com/oneapi-src/oneTBB](https://github.com/oneapi-src/oneTBB)</span>

## Available installations


|tbb version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2022.2.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`tbb/2022.2.0-GCCcore-14.3.0`|