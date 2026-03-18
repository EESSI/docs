---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: FFCx provides the ufcx.h interface header for generated finite element
    kernels, used by DOLFINx.
  license: Not confirmed
  name: FEniCS-ufcx
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
  softwareVersion: '[''0.9.0'']'
  url: https://github.com/FEniCS/ffcx
---
# FEniCS-ufcx


FFCx provides the ufcx.h interface header for generated finite element kernels, used by DOLFINx.

<small>homepage: </small><span class="software-link">[https://github.com/FEniCS/ffcx](https://github.com/FEniCS/ffcx)</span>

## Available installations


|FEniCS-ufcx version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.9.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`FEniCS-ufcx/0.9.0-GCCcore-13.2.0`|