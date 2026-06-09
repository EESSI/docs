---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    gperftools is a collection of a high-performance multi-threaded malloc()

    implementation, plus some pretty nifty performance analysis tools.

    Includes TCMalloc, heap-checker, heap-profiler and cpu-profiler.

    '
  license: Not confirmed
  name: gperftools
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
  softwareVersion: '[''2.17.2'']'
  url: https://github.com/gperftools/gperftools
---
# gperftools



gperftools is a collection of a high-performance multi-threaded malloc()
implementation, plus some pretty nifty performance analysis tools.
Includes TCMalloc, heap-checker, heap-profiler and cpu-profiler.


<small>homepage: </small><span class="software-link">[https://github.com/gperftools/gperftools](https://github.com/gperftools/gperftools)</span>

## Available installations


|gperftools version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.17.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`gperftools/2.17.2-GCCcore-14.3.0`|