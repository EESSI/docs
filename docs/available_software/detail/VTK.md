---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The Visualization Toolkit (VTK) is an open-source, freely available\
    \ software system for\n 3D computer graphics, image processing and visualization.\
    \ VTK consists of a C++ class library and several\n interpreted interface layers\
    \ including Tcl/Tk, Java, and Python. VTK supports a wide variety of visualization\n\
    \ algorithms including: scalar, vector, tensor, texture, and volumetric methods;\
    \ and advanced modeling techniques\n such as: implicit modeling, polygon reduction,\
    \ mesh smoothing, cutting, contouring, and Delaunay triangulation."
  license: Not confirmed
  name: VTK
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
  softwareVersion: '[''9.5.0'', ''9.3.1'', ''9.3.0'']'
  url: https://www.vtk.org
---
# VTK


The Visualization Toolkit (VTK) is an open-source, freely available software system for
 3D computer graphics, image processing and visualization. VTK consists of a C++ class library and several
 interpreted interface layers including Tcl/Tk, Java, and Python. VTK supports a wide variety of visualization
 algorithms including: scalar, vector, tensor, texture, and volumetric methods; and advanced modeling techniques
 such as: implicit modeling, polygon reduction, mesh smoothing, cutting, contouring, and Delaunay triangulation.

<small>homepage: </small><span class="software-link">[https://www.vtk.org](https://www.vtk.org)</span>

## Available installations


|VTK version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|9.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`VTK/9.3.0-foss-2023a`|
|9.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`VTK/9.3.0-foss-2023b`|
|9.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`VTK/9.3.1-foss-2024a`|
|9.5.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`VTK/9.5.0-foss-2025a`|