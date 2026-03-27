---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Samples for CUDA Developers which demonstrates features in CUDA Toolkit
  license: Not confirmed
  name: CUDA-Samples
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
  softwareVersion: '[''12.1'']'
  url: https://github.com/NVIDIA/cuda-samples
---
# CUDA-Samples


Samples for CUDA Developers which demonstrates features in CUDA Toolkit

<small>homepage: </small><span class="software-link">[https://github.com/NVIDIA/cuda-samples](https://github.com/NVIDIA/cuda-samples)</span>

## Available installations


|CUDA-Samples version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|12.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-nvidia">NVIDIA</span>: `cc70`, `cc80`, `cc90`<br/>|<span class="software-eessi-version-202306">2023.06</span>|`CUDA-Samples/12.1-GCC-12.3.0-CUDA-12.1.1`|