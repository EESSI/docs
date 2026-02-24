# cimfomfa


This library supports both MCL, a cluster algorithm for graphs, and zoem, a
macro/DSL language. It supplies abstractions for memory management, I/O,
associative arrays, strings, heaps, and a few other things. The string library
has had heavy testing as part of zoem. Both understandably and regrettably I
chose long ago to make it C-string-compatible, hence nul bytes may not be part
of a string. At some point I hope to rectify this, perhaps unrealistically.

<small>homepage: </small><span class="software-link">[https://github.com/micans/cimfomfa](https://github.com/micans/cimfomfa)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|22.273|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`cimfomfa/22.273-GCCcore-12.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://github.com/micans/cimfomfa', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'cimfomfa/22.273-GCCcore-12.3.0', 'module_name': 'cimfomfa', 'module_version': '22.273-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'cimfomfa/22.273-GCCcore-12.3.0', 'module_name': 'cimfomfa', 'module_version': '22.273-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'This library supports both MCL, a cluster algorithm for graphs, and zoem, a\nmacro/DSL language. It supplies abstractions for memory management, I/O,\nassociative arrays, strings, heaps, and a few other things. The string library\nhas had heavy testing as part of zoem. Both understandably and regrettably I\nchose long ago to make it C-string-compatible, hence nul bytes may not be part\nof a string. At some point I hope to rectify this, perhaps unrealistically.', 'version': '22.273', 'versionsuffix': '', 'extensions': []}], 'homepage': 'https://github.com/micans/cimfomfa', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'This library supports both MCL, a cluster algorithm for graphs, and zoem, a\nmacro/DSL language. It supplies abstractions for memory management, I/O,\nassociative arrays, strings, heaps, and a few other things. The string library\nhas had heavy testing as part of zoem. Both understandably and regrettably I\nchose long ago to make it C-string-compatible, hence nul bytes may not be part\nof a string. At some point I hope to rectify this, perhaps unrealistically.'} installations
