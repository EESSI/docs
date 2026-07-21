---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The rocprofiler-register library is a helper library that coordinates
    the

    modification of the intercept API table(s) of the HSA/HIP/ROCTx runtime libraries
    by the

    ROCprofiler (v2) library. The purpose of this library is to provide a consistent
    and automated

    mechanism of enabling performance analysis in the ROCm runtimes which does not
    rely on

    environment variables or unique methods for each runtime library.'
  license: Not confirmed
  name: rocprofiler-register
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
  softwareVersion: '[''0.4.0'']'
  url: https://github.com/ROCm/rocprofiler-register
---
# rocprofiler-register


The rocprofiler-register library is a helper library that coordinates the
modification of the intercept API table(s) of the HSA/HIP/ROCTx runtime libraries by the
ROCprofiler (v2) library. The purpose of this library is to provide a consistent and automated
mechanism of enabling performance analysis in the ROCm runtimes which does not rely on
environment variables or unique methods for each runtime library.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/rocprofiler-register](https://github.com/ROCm/rocprofiler-register)</span>

## Available installations


|rocprofiler-register version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.4.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`rocprofiler-register/0.4.0-GCCcore-14.2.0-ROCm-6.4.1`|