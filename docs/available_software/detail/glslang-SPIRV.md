---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Glslang is the official reference compiler front end for the OpenGL
    ES and OpenGL shading languages.

    It implements a strict interpretation of the specifications for these languages.
    It is open and free for anyone to use,

    either from a command line or programmatically. The OpenGL and OpenGL ES working
    groups are committed to maintaining

    consistency between the reference compiler and the corresponding shading language
    specifications.'
  license: Not confirmed
  name: glslang-SPIRV
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
  softwareVersion: '[''15.4.0'', ''15.3.0'']'
  url: https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/
---
# glslang-SPIRV


Glslang is the official reference compiler front end for the OpenGL ES and OpenGL shading languages.
It implements a strict interpretation of the specifications for these languages. It is open and free for anyone to use,
either from a command line or programmatically. The OpenGL and OpenGL ES working groups are committed to maintaining
consistency between the reference compiler and the corresponding shading language specifications.

<small>homepage: </small><span class="software-link">[https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/](https://www.khronos.org/opengles/sdk/tools/Reference-Compiler/)</span>

## Available installations


|glslang-SPIRV version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|15.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`glslang-SPIRV/15.3.0-GCCcore-14.2.0`|
|15.4.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`glslang-SPIRV/15.4.0-GCCcore-14.3.0`|