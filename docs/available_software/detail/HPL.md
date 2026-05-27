---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "HPL is a software package that solves a (random) dense linear system\
    \ in double precision (64 bits)\n arithmetic on distributed-memory computers.\
    \ It can thus be regarded as a portable as well as freely available\n implementation\
    \ of the High Performance Computing Linpack Benchmark."
  license: Not confirmed
  name: HPL
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
  softwareVersion: '[''2.3'']'
  url: https://www.netlib.org/benchmark/hpl/
---
# HPL


HPL is a software package that solves a (random) dense linear system in double precision (64 bits)
 arithmetic on distributed-memory computers. It can thus be regarded as a portable as well as freely available
 implementation of the High Performance Computing Linpack Benchmark.

<small>homepage: </small><span class="software-link">[https://www.netlib.org/benchmark/hpl/](https://www.netlib.org/benchmark/hpl/)</span>

## Available installations


|HPL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`HPL/2.3-foss-2023b`|