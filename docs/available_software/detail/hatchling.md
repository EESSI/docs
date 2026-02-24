# hatchling


Extensible, standards compliant build backend used by Hatch,
a modern, extensible Python project manager.

<small>homepage: </small><span class="software-link">[https://hatch.pypa.io](https://hatch.pypa.io)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.18.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatchling/1.18.0-GCCcore-12.3.0`|
|1.18.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatchling/1.18.0-GCCcore-13.2.0`|
|1.24.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatchling/1.24.2-GCCcore-13.3.0`|
|1.27.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatchling/1.27.0-GCCcore-14.2.0`|
|1.27.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatchling/1.27.0-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://hatch.pypa.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'hatchling/1.18.0-GCCcore-12.3.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'hatchling/1.18.0-GCCcore-12.3.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Extensible, standards compliant build backend used by Hatch,\na modern, extensible Python project manager.', 'version': '1.18.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pathspec', 'version': '0.11.1'}, {'type': 'python', 'name': 'pluggy', 'version': '1.2.0'}, {'type': 'python', 'name': 'editables', 'version': '0.3'}, {'type': 'python', 'name': 'trove_classifiers', 'version': '2023.5.24'}, {'type': 'python', 'name': 'hatchling', 'version': '1.18.0'}, {'type': 'python', 'name': 'hatch_vcs', 'version': '0.3.0'}, {'type': 'python', 'name': 'hatch_fancy_pypi_readme', 'version': '23.1.0'}, {'type': 'python', 'name': 'hatch-requirements-txt', 'version': '0.4.1'}]}, {'homepage': 'https://hatch.pypa.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.2.0'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'hatchling/1.18.0-GCCcore-13.2.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-13.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'hatchling/1.18.0-GCCcore-13.2.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-13.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Extensible, standards compliant build backend used by Hatch,\na modern, extensible Python project manager.', 'version': '1.18.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pathspec', 'version': '0.11.2'}, {'type': 'python', 'name': 'pluggy', 'version': '1.3.0'}, {'type': 'python', 'name': 'editables', 'version': '0.5'}, {'type': 'python', 'name': 'trove_classifiers', 'version': '2023.10.18'}, {'type': 'python', 'name': 'hatchling', 'version': '1.18.0'}, {'type': 'python', 'name': 'hatch_vcs', 'version': '0.3.0'}, {'type': 'python', 'name': 'hatch_fancy_pypi_readme', 'version': '23.1.0'}, {'type': 'python', 'name': 'hatch-requirements-txt', 'version': '0.4.1'}]}, {'homepage': 'https://hatch.pypa.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.3.0'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'hatchling/1.24.2-GCCcore-13.3.0', 'module_name': 'hatchling', 'module_version': '1.24.2-GCCcore-13.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'hatchling/1.24.2-GCCcore-13.3.0', 'module_name': 'hatchling', 'module_version': '1.24.2-GCCcore-13.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Extensible, standards compliant build backend used by Hatch,\na modern, extensible Python project manager.', 'version': '1.24.2', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pathspec', 'version': '0.12.1'}, {'type': 'python', 'name': 'pluggy', 'version': '1.5.0'}, {'type': 'python', 'name': 'editables', 'version': '0.5'}, {'type': 'python', 'name': 'trove-classifiers', 'version': '2024.5.22'}, {'type': 'python', 'name': 'hatchling', 'version': '1.24.2'}, {'type': 'python', 'name': 'hatch-vcs', 'version': '0.4.0'}, {'type': 'python', 'name': 'hatch-fancy-pypi-readme', 'version': '24.1.0'}, {'type': 'python', 'name': 'hatch-requirements-txt', 'version': '0.4.1'}]}, {'homepage': 'https://hatch.pypa.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '14.2.0'}, 'toolchain_families_compatibility': ['2025a_foss'], 'module': {'full_module_name': 'hatchling/1.27.0-GCCcore-14.2.0', 'module_name': 'hatchling', 'module_version': '1.27.0-GCCcore-14.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/14.2.0', 'module_name': 'GCCcore', 'module_version': '14.2.0'}, {'full_module_name': 'Tcl/8.6.16-GCCcore-14.2.0', 'module_name': 'Tcl', 'module_version': '8.6.16-GCCcore-14.2.0'}, {'full_module_name': 'SQLite/3.47.2-GCCcore-14.2.0', 'module_name': 'SQLite', 'module_version': '3.47.2-GCCcore-14.2.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-14.2.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-14.2.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.13.1-GCCcore-14.2.0', 'module_name': 'Python', 'module_version': '3.13.1-GCCcore-14.2.0'}, {'full_module_name': 'hatchling/1.27.0-GCCcore-14.2.0', 'module_name': 'hatchling', 'module_version': '1.27.0-GCCcore-14.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Extensible, standards compliant build backend used by Hatch,\na modern, extensible Python project manager.', 'version': '1.27.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pathspec', 'version': '0.12.1'}, {'type': 'python', 'name': 'pluggy', 'version': '1.5.0'}, {'type': 'python', 'name': 'editables', 'version': '0.5'}, {'type': 'python', 'name': 'trove-classifiers', 'version': '2025.2.18.16'}, {'type': 'python', 'name': 'hatchling', 'version': '1.27.0'}, {'type': 'python', 'name': 'hatch-vcs', 'version': '0.4.0'}, {'type': 'python', 'name': 'hatch-fancy-pypi-readme', 'version': '24.1.0'}, {'type': 'python', 'name': 'hatch-requirements-txt', 'version': '0.4.1'}]}, {'homepage': 'https://hatch.pypa.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '14.3.0'}, 'toolchain_families_compatibility': ['2025b_foss'], 'module': {'full_module_name': 'hatchling/1.27.0-GCCcore-14.3.0', 'module_name': 'hatchling', 'module_version': '1.27.0-GCCcore-14.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/14.3.0', 'module_name': 'GCCcore', 'module_version': '14.3.0'}, {'full_module_name': 'libtommath/1.3.0-GCCcore-14.3.0', 'module_name': 'libtommath', 'module_version': '1.3.0-GCCcore-14.3.0'}, {'full_module_name': 'Tcl/9.0.1-GCCcore-14.3.0', 'module_name': 'Tcl', 'module_version': '9.0.1-GCCcore-14.3.0'}, {'full_module_name': 'SQLite/3.50.1-GCCcore-14.3.0', 'module_name': 'SQLite', 'module_version': '3.50.1-GCCcore-14.3.0'}, {'full_module_name': 'libffi/3.5.1-GCCcore-14.3.0', 'module_name': 'libffi', 'module_version': '3.5.1-GCCcore-14.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.13.5-GCCcore-14.3.0', 'module_name': 'Python', 'module_version': '3.13.5-GCCcore-14.3.0'}, {'full_module_name': 'hatchling/1.27.0-GCCcore-14.3.0', 'module_name': 'hatchling', 'module_version': '1.27.0-GCCcore-14.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Extensible, standards compliant build backend used by Hatch,\na modern, extensible Python project manager.', 'version': '1.27.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pathspec', 'version': '0.12.1'}, {'type': 'python', 'name': 'pluggy', 'version': '1.6.0'}, {'type': 'python', 'name': 'editables', 'version': '0.5'}, {'type': 'python', 'name': 'trove-classifiers', 'version': '2025.5.9.12'}, {'type': 'python', 'name': 'hatchling', 'version': '1.27.0'}, {'type': 'python', 'name': 'hatch-vcs', 'version': '0.5.0'}, {'type': 'python', 'name': 'hatch-fancy-pypi-readme', 'version': '25.1.0'}, {'type': 'python', 'name': 'hatch-requirements-txt', 'version': '0.4.1'}, {'type': 'python', 'name': 'hatch-docstring-description', 'version': '1.1.1'}]}], 'homepage': 'https://hatch.pypa.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'Extensible, standards compliant build backend used by Hatch,\na modern, extensible Python project manager.'} installations


### editables


|`editables` version|hatchling modules that include it|
| --- | --- |
|0.3|`hatchling/1.18.0-GCCcore-12.3.0`|
|0.5|`hatchling/1.27.0-GCCcore-14.3.0`<br/>`hatchling/1.24.2-GCCcore-13.3.0`<br/>`hatchling/1.18.0-GCCcore-13.2.0`<br/>`hatchling/1.27.0-GCCcore-14.2.0`|

### hatch-docstring-description


|`hatch-docstring-description` version|hatchling modules that include it|
| --- | --- |
|1.1.1|`hatchling/1.27.0-GCCcore-14.3.0`|

### hatch-fancy-pypi-readme


|`hatch-fancy-pypi-readme` version|hatchling modules that include it|
| --- | --- |
|24.1.0|`hatchling/1.24.2-GCCcore-13.3.0`<br/>`hatchling/1.27.0-GCCcore-14.2.0`|
|25.1.0|`hatchling/1.27.0-GCCcore-14.3.0`|

### hatch-requirements-txt


|`hatch-requirements-txt` version|hatchling modules that include it|
| --- | --- |
|0.4.1|`hatchling/1.27.0-GCCcore-14.2.0`<br/>`hatchling/1.27.0-GCCcore-14.3.0`<br/>`hatchling/1.18.0-GCCcore-12.3.0`<br/>`hatchling/1.24.2-GCCcore-13.3.0`<br/>`hatchling/1.18.0-GCCcore-13.2.0`|

### hatch-vcs


|`hatch-vcs` version|hatchling modules that include it|
| --- | --- |
|0.4.0|`hatchling/1.24.2-GCCcore-13.3.0`<br/>`hatchling/1.27.0-GCCcore-14.2.0`|
|0.5.0|`hatchling/1.27.0-GCCcore-14.3.0`|

### hatch_fancy_pypi_readme


|`hatch_fancy_pypi_readme` version|hatchling modules that include it|
| --- | --- |
|23.1.0|`hatchling/1.18.0-GCCcore-12.3.0`<br/>`hatchling/1.18.0-GCCcore-13.2.0`|

### hatch_vcs


|`hatch_vcs` version|hatchling modules that include it|
| --- | --- |
|0.3.0|`hatchling/1.18.0-GCCcore-12.3.0`<br/>`hatchling/1.18.0-GCCcore-13.2.0`|

### hatchling


|`hatchling` version|hatchling modules that include it|
| --- | --- |
|1.18.0|`hatchling/1.18.0-GCCcore-12.3.0`<br/>`hatchling/1.18.0-GCCcore-13.2.0`|
|1.24.2|`hatchling/1.24.2-GCCcore-13.3.0`|
|1.27.0|`hatchling/1.27.0-GCCcore-14.3.0`<br/>`hatchling/1.27.0-GCCcore-14.2.0`|

### pathspec


|`pathspec` version|hatchling modules that include it|
| --- | --- |
|0.11.1|`hatchling/1.18.0-GCCcore-12.3.0`|
|0.11.2|`hatchling/1.18.0-GCCcore-13.2.0`|
|0.12.1|`hatchling/1.27.0-GCCcore-14.3.0`<br/>`hatchling/1.24.2-GCCcore-13.3.0`<br/>`hatchling/1.27.0-GCCcore-14.2.0`|

### pluggy


|`pluggy` version|hatchling modules that include it|
| --- | --- |
|1.2.0|`hatchling/1.18.0-GCCcore-12.3.0`|
|1.3.0|`hatchling/1.18.0-GCCcore-13.2.0`|
|1.5.0|`hatchling/1.24.2-GCCcore-13.3.0`<br/>`hatchling/1.27.0-GCCcore-14.2.0`|
|1.6.0|`hatchling/1.27.0-GCCcore-14.3.0`|

### trove-classifiers


|`trove-classifiers` version|hatchling modules that include it|
| --- | --- |
|2024.5.22|`hatchling/1.24.2-GCCcore-13.3.0`|
|2025.2.18.16|`hatchling/1.27.0-GCCcore-14.2.0`|
|2025.5.9.12|`hatchling/1.27.0-GCCcore-14.3.0`|

### trove_classifiers


|`trove_classifiers` version|hatchling modules that include it|
| --- | --- |
|2023.10.18|`hatchling/1.18.0-GCCcore-13.2.0`|
|2023.5.24|`hatchling/1.18.0-GCCcore-12.3.0`|