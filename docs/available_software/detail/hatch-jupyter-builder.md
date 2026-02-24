# hatch-jupyter-builder


Hatch Jupyter Builder is a plugin for the hatchling Python build backend. It is
primarily targeted for package authors who are providing JavaScript as part of
their Python packages.
Typical use cases are Jupyter Lab Extensions and Jupyter Widgets.

<small>homepage: </small><span class="software-link">[https://hatch-jupyter-builder.readthedocs.io](https://hatch-jupyter-builder.readthedocs.io)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.9.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatch-jupyter-builder/0.9.1-GCCcore-12.3.0`|
|0.9.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`hatch-jupyter-builder/0.9.1-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://hatch-jupyter-builder.readthedocs.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'hatch-jupyter-builder/0.9.1-GCCcore-12.3.0', 'module_name': 'hatch-jupyter-builder', 'module_version': '0.9.1-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'hatchling/1.18.0-GCCcore-12.3.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'hatch-jupyter-builder/0.9.1-GCCcore-12.3.0', 'module_name': 'hatch-jupyter-builder', 'module_version': '0.9.1-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Hatch Jupyter Builder is a plugin for the hatchling Python build backend. It is\nprimarily targeted for package authors who are providing JavaScript as part of\ntheir Python packages.\nTypical use cases are Jupyter Lab Extensions and Jupyter Widgets.', 'version': '0.9.1', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'hatch_nodejs_version', 'version': '0.3.2'}, {'type': 'python', 'name': 'hatch_jupyter_builder', 'version': '0.9.1'}]}, {'homepage': 'https://hatch-jupyter-builder.readthedocs.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.3.0'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'hatch-jupyter-builder/0.9.1-GCCcore-13.3.0', 'module_name': 'hatch-jupyter-builder', 'module_version': '0.9.1-GCCcore-13.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'hatchling/1.24.2-GCCcore-13.3.0', 'module_name': 'hatchling', 'module_version': '1.24.2-GCCcore-13.3.0'}, {'full_module_name': 'hatch-jupyter-builder/0.9.1-GCCcore-13.3.0', 'module_name': 'hatch-jupyter-builder', 'module_version': '0.9.1-GCCcore-13.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Hatch Jupyter Builder is a plugin for the hatchling Python build backend. It is\nprimarily targeted for package authors who are providing JavaScript as part of\ntheir Python packages.\nTypical use cases are Jupyter Lab Extensions and Jupyter Widgets.', 'version': '0.9.1', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'hatch_nodejs_version', 'version': '0.3.2'}, {'type': 'python', 'name': 'hatch_jupyter_builder', 'version': '0.9.1'}]}], 'homepage': 'https://hatch-jupyter-builder.readthedocs.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'Hatch Jupyter Builder is a plugin for the hatchling Python build backend. It is\nprimarily targeted for package authors who are providing JavaScript as part of\ntheir Python packages.\nTypical use cases are Jupyter Lab Extensions and Jupyter Widgets.'} installations


### hatch_jupyter_builder


|`hatch_jupyter_builder` version|hatch-jupyter-builder modules that include it|
| --- | --- |
|0.9.1|`hatch-jupyter-builder/0.9.1-GCCcore-13.3.0`<br/>`hatch-jupyter-builder/0.9.1-GCCcore-12.3.0`|

### hatch_nodejs_version


|`hatch_nodejs_version` version|hatch-jupyter-builder modules that include it|
| --- | --- |
|0.3.2|`hatch-jupyter-builder/0.9.1-GCCcore-13.3.0`<br/>`hatch-jupyter-builder/0.9.1-GCCcore-12.3.0`|