# OpenGL



Open Graphics Library (OpenGL) is a cross-language, cross-platform application
programming interface (API) for rendering 2D and 3D vector graphics.

This module is a bundle of software required for OpenGL rendering.
It provides Mesa as an open-source implementation of the OpenGL specification
with software rendering and AMD GPU support, libglvnd for a vendor neutral
dispatch layer for rendering with both NVIDIA GPUs & Mesa, Mesa-demos for
sample applications, and GLU as an computer graphics library utilizing OpenGL.


<small>homepage: </small><span class="software-link">[http://www.opengl.org/](http://www.opengl.org/)</span>

## Available installations


|OpenGL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2025.09|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OpenGL/2025.09-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in OpenGL installations


### libGLU


|`libGLU` version|OpenGL modules that include it|
| --- | --- |
|9.0.3|`OpenGL/2025.09-GCCcore-14.3.0`|

### libglvnd


|`libglvnd` version|OpenGL modules that include it|
| --- | --- |
|1.7.0|`OpenGL/2025.09-GCCcore-14.3.0`|

### Mesa


|`Mesa` version|OpenGL modules that include it|
| --- | --- |
|25.2.2|`OpenGL/2025.09-GCCcore-14.3.0`|

### Mesa-demos


|`Mesa-demos` version|OpenGL modules that include it|
| --- | --- |
|9.0.0|`OpenGL/2025.09-GCCcore-14.3.0`|