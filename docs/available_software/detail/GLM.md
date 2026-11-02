---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    OpenGL Mathematics (GLM) is a header only C++ mathematics library for graphics

    software based on  the OpenGL Shading Language (GLSL) specifications.'
  license: Not confirmed
  name: GLM
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
  softwareVersion: '[''1.0.3'']'
  url: https://github.com/g-truc/glm
---
# GLM



OpenGL Mathematics (GLM) is a header only C++ mathematics library for graphics
software based on  the OpenGL Shading Language (GLSL) specifications.

<small>homepage: </small><span class="software-link">[https://github.com/g-truc/glm](https://github.com/g-truc/glm)</span>

## Available installations


|GLM version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`GLM/1.0.3-GCCcore-15.2.0`|