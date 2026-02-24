# ReFrame


ReFrame is a framework for writing regression tests for HPC systems.

<small>homepage: </small><span class="software-link">[https://github.com/reframe-hpc/reframe](https://github.com/reframe-hpc/reframe)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|4.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`ReFrame/4.3.3`|
|4.6.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`ReFrame/4.6.2`|
|4.7.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`ReFrame/4.7.4`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://github.com/reframe-hpc/reframe', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'system', 'version': 'system'}, 'toolchain_families_compatibility': ['2022b_foss', '2023a_foss', '2023b_foss'], 'module': {'full_module_name': 'ReFrame/4.3.3', 'module_name': 'ReFrame', 'module_version': '4.3.3'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'ReFrame/4.3.3', 'module_name': 'ReFrame', 'module_version': '4.3.3'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'ReFrame is a framework for writing regression tests for HPC systems.', 'version': '4.3.3', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pip', 'version': '21.3.1'}, {'type': 'python', 'name': 'wheel', 'version': '0.37.1'}, {'type': 'python', 'name': 'reframe', 'version': '4.3.3'}]}, {'homepage': 'https://github.com/reframe-hpc/reframe', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'system', 'version': 'system'}, 'toolchain_families_compatibility': ['2022b_foss', '2023a_foss', '2023b_foss'], 'module': {'full_module_name': 'ReFrame/4.6.2', 'module_name': 'ReFrame', 'module_version': '4.6.2'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'ReFrame/4.6.2', 'module_name': 'ReFrame', 'module_version': '4.6.2'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'ReFrame is a framework for writing regression tests for HPC systems.', 'version': '4.6.2', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pip', 'version': '24.0'}, {'type': 'python', 'name': 'setuptools', 'version': '68.0.0'}, {'type': 'python', 'name': 'wheel', 'version': '0.42.0'}, {'type': 'python', 'name': 'reframe', 'version': '4.6.2'}]}, {'homepage': 'https://github.com/reframe-hpc/reframe', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'system', 'version': 'system'}, 'toolchain_families_compatibility': ['2024a_foss', '2025a_foss', '2025b_foss'], 'module': {'full_module_name': 'ReFrame/4.7.4', 'module_name': 'ReFrame', 'module_version': '4.7.4'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'ReFrame/4.7.4', 'module_name': 'ReFrame', 'module_version': '4.7.4'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'ReFrame is a framework for writing regression tests for HPC systems.', 'version': '4.7.4', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pip', 'version': '24.0'}, {'type': 'python', 'name': 'setuptools', 'version': '68.0.0'}, {'type': 'python', 'name': 'wheel', 'version': '0.42.0'}, {'type': 'python', 'name': 'reframe', 'version': '4.7.4'}]}], 'homepage': 'https://github.com/reframe-hpc/reframe', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'ReFrame is a framework for writing regression tests for HPC systems.'} installations


### pip


|`pip` version|ReFrame modules that include it|
| --- | --- |
|21.3.1|`ReFrame/4.3.3`|
|24.0|`ReFrame/4.7.4`<br/>`ReFrame/4.6.2`|

### reframe


|`reframe` version|ReFrame modules that include it|
| --- | --- |
|4.3.3|`ReFrame/4.3.3`|
|4.6.2|`ReFrame/4.6.2`|
|4.7.4|`ReFrame/4.7.4`|

### setuptools


|`setuptools` version|ReFrame modules that include it|
| --- | --- |
|68.0.0|`ReFrame/4.7.4`<br/>`ReFrame/4.6.2`|

### wheel


|`wheel` version|ReFrame modules that include it|
| --- | --- |
|0.37.1|`ReFrame/4.3.3`|
|0.42.0|`ReFrame/4.7.4`<br/>`ReFrame/4.6.2`|