---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    The ROCm System Management Interface Library, or ROCm SMI library, is part of
    the Radeon Open Compute ROCm software

    stack. It is a C library for Linux that provides a user space interface for applications
    to monitor and control

    GPU applications.'
  license: Not confirmed
  name: rocm-smi
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
  softwareVersion: '[''7.6.0'']'
  url: https://github.com/ROCm/rocm_smi_lib
---
# rocm-smi



The ROCm System Management Interface Library, or ROCm SMI library, is part of the Radeon Open Compute ROCm software
stack. It is a C library for Linux that provides a user space interface for applications to monitor and control
GPU applications.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/rocm_smi_lib](https://github.com/ROCm/rocm_smi_lib)</span>

## Available installations


|rocm-smi version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`rocm-smi/7.6.0-GCCcore-14.2.0-ROCm-6.4.1`|