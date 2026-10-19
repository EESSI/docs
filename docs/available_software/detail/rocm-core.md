---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'ROCm-core is a foundational package that provides ROCm release versioning

    and installation path information via header files.'
  license: Not confirmed
  name: rocm-core
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
  softwareVersion: '[''6.4.1'']'
  url: https://github.com/ROCm/rocm-core
---
# rocm-core


ROCm-core is a foundational package that provides ROCm release versioning
and installation path information via header files.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/rocm-core](https://github.com/ROCm/rocm-core)</span>

## Available installations


|rocm-core version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|6.4.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`rocm-core/6.4.1-GCCcore-14.2.0-ROCm-6.4.1`|