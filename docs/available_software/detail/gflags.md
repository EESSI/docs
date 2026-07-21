---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    The gflags package contains a C++ library that implements commandline flags

    processing.  It includes built-in support for standard types such as string

    and the ability to define flags in the source file in which they are used.

    '
  license: Not confirmed
  name: gflags
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
  softwareVersion: '[''2.2.2'']'
  url: https://github.com/gflags/gflags
---
# gflags



The gflags package contains a C++ library that implements commandline flags
processing.  It includes built-in support for standard types such as string
and the ability to define flags in the source file in which they are used.


<small>homepage: </small><span class="software-link">[https://github.com/gflags/gflags](https://github.com/gflags/gflags)</span>

## Available installations


|gflags version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.2.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`gflags/2.2.2-GCCcore-14.2.0`|