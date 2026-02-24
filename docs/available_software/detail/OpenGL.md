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


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2025.09|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`OpenGL/2025.09-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'http://www.opengl.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '14.3.0'}, 'toolchain_families_compatibility': ['2025b_foss'], 'module': {'full_module_name': 'OpenGL/2025.09-GCCcore-14.3.0', 'module_name': 'OpenGL', 'module_version': '2025.09-GCCcore-14.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/14.3.0', 'module_name': 'GCCcore', 'module_version': '14.3.0'}, {'full_module_name': 'libffi/3.5.1-GCCcore-14.3.0', 'module_name': 'libffi', 'module_version': '3.5.1-GCCcore-14.3.0'}, {'full_module_name': 'libxml2/2.14.3-GCCcore-14.3.0', 'module_name': 'libxml2', 'module_version': '2.14.3-GCCcore-14.3.0'}, {'full_module_name': 'libtommath/1.3.0-GCCcore-14.3.0', 'module_name': 'libtommath', 'module_version': '1.3.0-GCCcore-14.3.0'}, {'full_module_name': 'Tcl/9.0.1-GCCcore-14.3.0', 'module_name': 'Tcl', 'module_version': '9.0.1-GCCcore-14.3.0'}, {'full_module_name': 'SQLite/3.50.1-GCCcore-14.3.0', 'module_name': 'SQLite', 'module_version': '3.50.1-GCCcore-14.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.13.5-GCCcore-14.3.0', 'module_name': 'Python', 'module_version': '3.13.5-GCCcore-14.3.0'}, {'full_module_name': 'GMP/6.3.0-GCCcore-14.3.0', 'module_name': 'GMP', 'module_version': '6.3.0-GCCcore-14.3.0'}, {'full_module_name': 'Z3/4.15.1-GCCcore-14.3.0', 'module_name': 'Z3', 'module_version': '4.15.1-GCCcore-14.3.0'}, {'full_module_name': 'gzip/1.14-GCCcore-14.3.0', 'module_name': 'gzip', 'module_version': '1.14-GCCcore-14.3.0'}, {'full_module_name': 'lz4/1.10.0-GCCcore-14.3.0', 'module_name': 'lz4', 'module_version': '1.10.0-GCCcore-14.3.0'}, {'full_module_name': 'zstd/1.5.7-GCCcore-14.3.0', 'module_name': 'zstd', 'module_version': '1.5.7-GCCcore-14.3.0'}, {'full_module_name': 'LLVM/20.1.8-GCCcore-14.3.0', 'module_name': 'LLVM', 'module_version': '20.1.8-GCCcore-14.3.0'}, {'full_module_name': 'expat/2.7.1-GCCcore-14.3.0', 'module_name': 'expat', 'module_version': '2.7.1-GCCcore-14.3.0'}, {'full_module_name': 'Wayland/1.24.0-GCCcore-14.3.0', 'module_name': 'Wayland', 'module_version': '1.24.0-GCCcore-14.3.0'}, {'full_module_name': 'libpng/1.6.50-GCCcore-14.3.0', 'module_name': 'libpng', 'module_version': '1.6.50-GCCcore-14.3.0'}, {'full_module_name': 'Brotli/1.1.0-GCCcore-14.3.0', 'module_name': 'Brotli', 'module_version': '1.1.0-GCCcore-14.3.0'}, {'full_module_name': 'freetype/2.13.3-GCCcore-14.3.0', 'module_name': 'freetype', 'module_version': '2.13.3-GCCcore-14.3.0'}, {'full_module_name': 'fontconfig/2.17.0-GCCcore-14.3.0', 'module_name': 'fontconfig', 'module_version': '2.17.0-GCCcore-14.3.0'}, {'full_module_name': 'xorg-macros/1.20.2-GCCcore-14.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.2-GCCcore-14.3.0'}, {'full_module_name': 'libpciaccess/0.18.1-GCCcore-14.3.0', 'module_name': 'libpciaccess', 'module_version': '0.18.1-GCCcore-14.3.0'}, {'full_module_name': 'X11/20250608-GCCcore-14.3.0', 'module_name': 'X11', 'module_version': '20250608-GCCcore-14.3.0'}, {'full_module_name': 'libiconv/1.18-GCCcore-14.3.0', 'module_name': 'libiconv', 'module_version': '1.18-GCCcore-14.3.0'}, {'full_module_name': 'libarchive/3.8.1-GCCcore-14.3.0', 'module_name': 'libarchive', 'module_version': '3.8.1-GCCcore-14.3.0'}, {'full_module_name': 'elfutils/0.193-GCCcore-14.3.0', 'module_name': 'elfutils', 'module_version': '0.193-GCCcore-14.3.0'}, {'full_module_name': 'libdrm/2.4.125-GCCcore-14.3.0', 'module_name': 'libdrm', 'module_version': '2.4.125-GCCcore-14.3.0'}, {'full_module_name': 'libunwind/1.8.2-GCCcore-14.3.0', 'module_name': 'libunwind', 'module_version': '1.8.2-GCCcore-14.3.0'}, {'full_module_name': 'nettle/3.10.2-GCCcore-14.3.0', 'module_name': 'nettle', 'module_version': '3.10.2-GCCcore-14.3.0'}, {'full_module_name': 'OpenGL/2025.09-GCCcore-14.3.0', 'module_name': 'OpenGL', 'module_version': '2025.09-GCCcore-14.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nOpen Graphics Library (OpenGL) is a cross-language, cross-platform application\nprogramming interface (API) for rendering 2D and 3D vector graphics.\n\nThis module is a bundle of software required for OpenGL rendering.\nIt provides Mesa as an open-source implementation of the OpenGL specification\nwith software rendering and AMD GPU support, libglvnd for a vendor neutral\ndispatch layer for rendering with both NVIDIA GPUs & Mesa, Mesa-demos for\nsample applications, and GLU as an computer graphics library utilizing OpenGL.\n', 'version': '2025.09', 'versionsuffix': '', 'extensions': [{'type': 'component', 'name': 'libglvnd', 'version': '1.7.0'}, {'type': 'component', 'name': 'Mesa', 'version': '25.2.2'}, {'type': 'component', 'name': 'libGLU', 'version': '9.0.3'}, {'type': 'component', 'name': 'Mesa-demos', 'version': '9.0.0'}]}], 'homepage': 'http://www.opengl.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\nOpen Graphics Library (OpenGL) is a cross-language, cross-platform application\nprogramming interface (API) for rendering 2D and 3D vector graphics.\n\nThis module is a bundle of software required for OpenGL rendering.\nIt provides Mesa as an open-source implementation of the OpenGL specification\nwith software rendering and AMD GPU support, libglvnd for a vendor neutral\ndispatch layer for rendering with both NVIDIA GPUs & Mesa, Mesa-demos for\nsample applications, and GLU as an computer graphics library utilizing OpenGL.\n'} installations


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