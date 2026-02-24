# pre-commit


A framework for managing and maintaining multi-language pre-commit hooks.

Git hook scripts are useful for identifying simple issues before submission to code review.
 We run our hooks on every commit to automatically point out issues in code such as missing semicolons,
 trailing whitespace, and debug statements. By pointing these issues out before code review,
 this allows a code reviewer to focus on the architecture of a change while not wasting time
 with trivial style nitpicks.

<small>homepage: </small><span class="software-link">[https://pre-commit.com/](https://pre-commit.com/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|3.7.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`pre-commit/3.7.0-GCCcore-13.2.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://pre-commit.com/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.2.0'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'pre-commit/3.7.0-GCCcore-13.2.0', 'module_name': 'pre-commit', 'module_version': '3.7.0-GCCcore-13.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.2.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'PyYAML/6.0.1-GCCcore-13.2.0', 'module_name': 'PyYAML', 'module_version': '6.0.1-GCCcore-13.2.0'}, {'full_module_name': 'pre-commit/3.7.0-GCCcore-13.2.0', 'module_name': 'pre-commit', 'module_version': '3.7.0-GCCcore-13.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'A framework for managing and maintaining multi-language pre-commit hooks.\n\nGit hook scripts are useful for identifying simple issues before submission to code review.\n We run our hooks on every commit to automatically point out issues in code such as missing semicolons,\n trailing whitespace, and debug statements. By pointing these issues out before code review,\n this allows a code reviewer to focus on the architecture of a change while not wasting time\n with trivial style nitpicks.', 'version': '3.7.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'nodeenv', 'version': '1.8.0'}, {'type': 'python', 'name': 'identify', 'version': '2.5.35'}, {'type': 'python', 'name': 'cfgv', 'version': '3.4.0'}, {'type': 'python', 'name': 'pre-commit', 'version': '3.7.0'}]}], 'homepage': 'https://pre-commit.com/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'A framework for managing and maintaining multi-language pre-commit hooks.\n\nGit hook scripts are useful for identifying simple issues before submission to code review.\n We run our hooks on every commit to automatically point out issues in code such as missing semicolons,\n trailing whitespace, and debug statements. By pointing these issues out before code review,\n this allows a code reviewer to focus on the architecture of a change while not wasting time\n with trivial style nitpicks.'} installations


### cfgv


|`cfgv` version|pre-commit modules that include it|
| --- | --- |
|3.4.0|`pre-commit/3.7.0-GCCcore-13.2.0`|

### identify


|`identify` version|pre-commit modules that include it|
| --- | --- |
|2.5.35|`pre-commit/3.7.0-GCCcore-13.2.0`|

### nodeenv


|`nodeenv` version|pre-commit modules that include it|
| --- | --- |
|1.8.0|`pre-commit/3.7.0-GCCcore-13.2.0`|

### pre-commit


|`pre-commit` version|pre-commit modules that include it|
| --- | --- |
|3.7.0|`pre-commit/3.7.0-GCCcore-13.2.0`|