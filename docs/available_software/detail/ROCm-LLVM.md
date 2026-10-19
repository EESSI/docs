---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'ROCm-LLVM is an open source Clang/LLVM based compiler.

    It is an AMD Fork of The LLVM Compiler Infrastructure, and aims to contain all
    of upstream LLVM.

    It also includes several AMD-specific additions in the llvm-project/amd directory.'
  license: Not confirmed
  name: ROCm-LLVM
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
  softwareVersion: '[''19.0.0'']'
  url: https://github.com/ROCm/llvm-project
---
# ROCm-LLVM


ROCm-LLVM is an open source Clang/LLVM based compiler.
It is an AMD Fork of The LLVM Compiler Infrastructure, and aims to contain all of upstream LLVM.
It also includes several AMD-specific additions in the llvm-project/amd directory.

<small>homepage: </small><span class="software-link">[https://github.com/ROCm/llvm-project](https://github.com/ROCm/llvm-project)</span>

## Available installations


|ROCm-LLVM version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|19.0.0|`generic`: `x86_64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-amd">AMD</span>: `gfx1030`, `gfx1100`, `gfx1101`, `gfx1200`, `gfx1201`, `gfx908`, `gfx90a`, `gfx942`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`ROCm-LLVM/19.0.0-GCCcore-14.2.0-ROCm-6.4.1`|

## Extensions

Overview of extensions included in ROCm-LLVM installations


### aomp-extras


|`aomp-extras` version|ROCm-LLVM modules that include it|
| --- | --- |
|rocm-6.4.1|`ROCm-LLVM/19.0.0-GCCcore-14.2.0-ROCm-6.4.1`|

### llvm-project


|`llvm-project` version|ROCm-LLVM modules that include it|
| --- | --- |
|19.0.0-rocm-6.4.1|`ROCm-LLVM/19.0.0-GCCcore-14.2.0-ROCm-6.4.1`|

### llvm-project-openmp


|`llvm-project-openmp` version|ROCm-LLVM modules that include it|
| --- | --- |
|19.0.0-rocm-6.4.1|`ROCm-LLVM/19.0.0-GCCcore-14.2.0-ROCm-6.4.1`|

### ROCm-comgr


|`ROCm-comgr` version|ROCm-LLVM modules that include it|
| --- | --- |
|rocm-6.4.1|`ROCm-LLVM/19.0.0-GCCcore-14.2.0-ROCm-6.4.1`|

### ROCR-Runtime


|`ROCR-Runtime` version|ROCm-LLVM modules that include it|
| --- | --- |
|rocm-6.4.1|`ROCm-LLVM/19.0.0-GCCcore-14.2.0-ROCm-6.4.1`|