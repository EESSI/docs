# SlurmViewer


View the status of a Slurm cluster, including nodes and queue.

<small>homepage: </small><span class="software-link">[https://gitlab.com/lkeb/slurm_viewer](https://gitlab.com/lkeb/slurm_viewer)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`SlurmViewer/1.0.1-GCCcore-13.2.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://gitlab.com/lkeb/slurm_viewer', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.2.0'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'SlurmViewer/1.0.1-GCCcore-13.2.0', 'module_name': 'SlurmViewer', 'module_version': '1.0.1-GCCcore-13.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'typing-extensions/4.10.0-GCCcore-13.2.0', 'module_name': 'typing-extensions', 'module_version': '4.10.0-GCCcore-13.2.0'}, {'full_module_name': 'pydantic/2.7.4-GCCcore-13.2.0', 'module_name': 'pydantic', 'module_version': '2.7.4-GCCcore-13.2.0'}, {'full_module_name': 'SlurmViewer/1.0.1-GCCcore-13.2.0', 'module_name': 'SlurmViewer', 'module_version': '1.0.1-GCCcore-13.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'View the status of a Slurm cluster, including nodes and queue.', 'version': '1.0.1', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'plotext', 'version': '5.2.8'}, {'type': 'python', 'name': 'textual', 'version': '0.85.2'}, {'type': 'python', 'name': 'textual-plotext', 'version': '0.2.1'}, {'type': 'python', 'name': 'asyncssh', 'version': '2.18.0'}, {'type': 'python', 'name': 'slurm-viewer', 'version': '1.0.1'}]}], 'homepage': 'https://gitlab.com/lkeb/slurm_viewer', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'View the status of a Slurm cluster, including nodes and queue.'} installations


### asyncssh


|`asyncssh` version|SlurmViewer modules that include it|
| --- | --- |
|2.18.0|`SlurmViewer/1.0.1-GCCcore-13.2.0`|

### plotext


|`plotext` version|SlurmViewer modules that include it|
| --- | --- |
|5.2.8|`SlurmViewer/1.0.1-GCCcore-13.2.0`|

### slurm-viewer


|`slurm-viewer` version|SlurmViewer modules that include it|
| --- | --- |
|1.0.1|`SlurmViewer/1.0.1-GCCcore-13.2.0`|

### textual


|`textual` version|SlurmViewer modules that include it|
| --- | --- |
|0.85.2|`SlurmViewer/1.0.1-GCCcore-13.2.0`|

### textual-plotext


|`textual-plotext` version|SlurmViewer modules that include it|
| --- | --- |
|0.2.1|`SlurmViewer/1.0.1-GCCcore-13.2.0`|