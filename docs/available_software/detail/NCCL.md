---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The NVIDIA Collective Communications Library (NCCL) implements multi-GPU
    and multi-node collective

    communication primitives that are performance optimized for NVIDIA GPUs.'
  license: Not confirmed
  name: NCCL
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
  softwareVersion: '[''2.27.7'', ''2.22.3'', ''2.20.5'', ''2.18.3'']'
  url: https://developer.nvidia.com/nccl
---
# NCCL


The NVIDIA Collective Communications Library (NCCL) implements multi-GPU and multi-node collective
communication primitives that are performance optimized for NVIDIA GPUs.

<small>homepage: </small><span class="software-link">[https://developer.nvidia.com/nccl](https://developer.nvidia.com/nccl)</span>

## Available installations


|NCCL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.27.7|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`NCCL/2.27.7-GCCcore-14.3.0-CUDA-12.9.1`|
|2.27.7|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`NCCL/2.27.7-GCCcore-14.2.0-CUDA-12.8.0`|
|2.22.3|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`NCCL/2.22.3-GCCcore-13.3.0-CUDA-12.6.0`|
|2.20.5|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`NCCL/2.20.5-GCCcore-13.2.0-CUDA-12.4.0`|
|2.18.3|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`NCCL/2.18.3-GCCcore-12.3.0-CUDA-12.1.1`|