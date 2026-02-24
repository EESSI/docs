# redis-py


The Python interface to the Redis key-value store.

<small>homepage: </small><span class="software-link">[https://github.com/redis/redis-py](https://github.com/redis/redis-py)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|5.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`redis-py/5.0.1-GCCcore-12.3.0`|
|5.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`redis-py/5.1.1-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://github.com/redis/redis-py', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'redis-py/5.0.1-GCCcore-12.3.0', 'module_name': 'redis-py', 'module_version': '5.0.1-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'typing-extensions/4.9.0-GCCcore-12.3.0', 'module_name': 'typing-extensions', 'module_version': '4.9.0-GCCcore-12.3.0'}, {'full_module_name': 'Redis/7.2.3-GCCcore-12.3.0', 'module_name': 'Redis', 'module_version': '7.2.3-GCCcore-12.3.0'}, {'full_module_name': 'redis-py/5.0.1-GCCcore-12.3.0', 'module_name': 'redis-py', 'module_version': '5.0.1-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The Python interface to the Redis key-value store.', 'version': '5.0.1', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'async-timeout', 'version': '4.0.3'}, {'type': 'python', 'name': 'redis-py', 'version': '5.0.1'}]}, {'homepage': 'https://github.com/redis/redis-py', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.3.0'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'redis-py/5.1.1-GCCcore-13.3.0', 'module_name': 'redis-py', 'module_version': '5.1.1-GCCcore-13.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'typing-extensions/4.11.0-GCCcore-13.3.0', 'module_name': 'typing-extensions', 'module_version': '4.11.0-GCCcore-13.3.0'}, {'full_module_name': 'Redis/7.4.1-GCCcore-13.3.0', 'module_name': 'Redis', 'module_version': '7.4.1-GCCcore-13.3.0'}, {'full_module_name': 'redis-py/5.1.1-GCCcore-13.3.0', 'module_name': 'redis-py', 'module_version': '5.1.1-GCCcore-13.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The Python interface to the Redis key-value store.', 'version': '5.1.1', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'async-timeout', 'version': '4.0.3'}, {'type': 'python', 'name': 'redis-py', 'version': '5.1.1'}]}], 'homepage': 'https://github.com/redis/redis-py', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'The Python interface to the Redis key-value store.'} installations


### async-timeout


|`async-timeout` version|redis-py modules that include it|
| --- | --- |
|4.0.3|`redis-py/5.0.1-GCCcore-12.3.0`<br/>`redis-py/5.1.1-GCCcore-13.3.0`|

### redis-py


|`redis-py` version|redis-py modules that include it|
| --- | --- |
|5.0.1|`redis-py/5.0.1-GCCcore-12.3.0`|
|5.1.1|`redis-py/5.1.1-GCCcore-13.3.0`|