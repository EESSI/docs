---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ' SPH-EXA is a C++20 simulation code for hydrodynamics simulations

    (with gravity and other physics), parallelized with MPI, OpenMP, CUDA, and HIP.'
  license: Not confirmed
  name: SPH-EXA
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
  softwareVersion: '[''0.96.2'']'
  url: https://github.com/sphexa-org/sphexa
---
# SPH-EXA


 SPH-EXA is a C++20 simulation code for hydrodynamics simulations
(with gravity and other physics), parallelized with MPI, OpenMP, CUDA, and HIP.

<small>homepage: </small><span class="software-link">[https://github.com/sphexa-org/sphexa](https://github.com/sphexa-org/sphexa)</span>

## Available installations


|SPH-EXA version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.96.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-nvidia">NVIDIA</span>: `cc100`, `cc120`, `cc70`, `cc80`, `cc90`<br/>|<span class="software-eessi-version-202506">2025.06</span>|`SPH-EXA/0.96.2-foss-2025b-CUDA-12.9.1`|