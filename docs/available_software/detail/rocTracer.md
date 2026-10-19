---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'ROCM cmake modules provides cmake modules for common build

    tasks needed for the ROCM software stack'
  license: Not confirmed
  name: rocTracer
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
  softwareVersion: '[''4.1.0'']'
  url: https://github.com/ROCm/roctracer
---
# rocTracer


ROCM cmake modules provides cmake modules for common build
tasks needed for the ROCM software stack

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/roctracer](https://github.com/ROCm/roctracer)</span>

## Available installations


|rocTracer version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.1.0|`generic`: `x86_64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-amd">AMD</span>: `gfx1030`, `gfx1100`, `gfx1101`, `gfx1200`, `gfx1201`, `gfx908`, `gfx90a`, `gfx942`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`rocTracer/4.1.0-rocm-compilers-19.0.0-ROCm-6.4.1`|