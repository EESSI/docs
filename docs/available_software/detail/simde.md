---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The SIMDe header-only library provides fast, portable

    implementations of SIMD intrinsics on hardware which doesn''t natively

    support them, such as calling SSE functions on ARM. There is no performance

    penalty if the hardware supports the native implementation (e.g., SSE/AVX

    runs at full speed on x86, NEON on ARM, etc.).'
  license: Not confirmed
  name: simde
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
  softwareVersion: '[''0.8.2'']'
  url: https://github.com/simd-everywhere/simde
---
# simde


The SIMDe header-only library provides fast, portable
implementations of SIMD intrinsics on hardware which doesn't natively
support them, such as calling SSE functions on ARM. There is no performance
penalty if the hardware supports the native implementation (e.g., SSE/AVX
runs at full speed on x86, NEON on ARM, etc.).

<small>homepage: </small><span class="software-link">[https://github.com/simd-everywhere/simde](https://github.com/simd-everywhere/simde)</span>

## Available installations


|simde version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.8.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`simde/0.8.2-GCCcore-14.2.0`|