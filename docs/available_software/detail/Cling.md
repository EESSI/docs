---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Cling is an interactive C++ interpreter, built on the top of LLVM and Clang libraries.

    Its advantages over the standard interpreters are that it has command line prompt

    and uses just-in-time (JIT) compiler for compilation.

    '
  license: Not confirmed
  name: Cling
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
  softwareVersion: '[''1.2'']'
  url: https://root.cern/cling/
---
# Cling



Cling is an interactive C++ interpreter, built on the top of LLVM and Clang libraries.
Its advantages over the standard interpreters are that it has command line prompt
and uses just-in-time (JIT) compiler for compilation.


<small>homepage: </small><span class="software-link">[https://root.cern/cling/](https://root.cern/cling/)</span>

## Available installations


|Cling version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Cling/1.2-GCCcore-14.3.0`|