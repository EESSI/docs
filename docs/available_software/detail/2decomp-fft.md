---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The 2DECOMP&FFT library is a software framework written in modern
    Fortran to build large-scale

    parallel applications.

    '
  license: Not confirmed
  name: 2decomp-fft
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
  softwareVersion: '[''2.0.4'']'
  url: https://2decomp-fft.github.io/
---
# 2decomp-fft


The 2DECOMP&FFT library is a software framework written in modern Fortran to build large-scale
parallel applications.


<small>homepage: </small><span class="software-link">[https://2decomp-fft.github.io/](https://2decomp-fft.github.io/)</span>

## Available installations


|2decomp-fft version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`2decomp-fft/2.0.4-foss-2025b`|