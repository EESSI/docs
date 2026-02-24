# GOTCHA


Gotcha is a library that wraps functions. Tools can use gotcha to install hooks into other
libraries, for example putting a wrapper function around libc's malloc. It is similar to LD_PRELOAD, but
operates via a programmable API. This enables easy methods of accomplishing tasks like code instrumentation
or wholesale replacement of mechanisms in programs without disrupting their source code.

<small>homepage: </small><span class="software-link">[https://gotcha.readthedocs.io/en/latest/](https://gotcha.readthedocs.io/en/latest/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.0.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`GOTCHA/1.0.8-GCCcore-14.2.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://gotcha.readthedocs.io/en/latest/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '14.2.0'}, 'toolchain_families_compatibility': ['2025a_foss'], 'module': {'full_module_name': 'GOTCHA/1.0.8-GCCcore-14.2.0', 'module_name': 'GOTCHA', 'module_version': '1.0.8-GCCcore-14.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/14.2.0', 'module_name': 'GCCcore', 'module_version': '14.2.0'}, {'full_module_name': 'GOTCHA/1.0.8-GCCcore-14.2.0', 'module_name': 'GOTCHA', 'module_version': '1.0.8-GCCcore-14.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': "Gotcha is a library that wraps functions. Tools can use gotcha to install hooks into other\nlibraries, for example putting a wrapper function around libc's malloc. It is similar to LD_PRELOAD, but\noperates via a programmable API. This enables easy methods of accomplishing tasks like code instrumentation\nor wholesale replacement of mechanisms in programs without disrupting their source code.", 'version': '1.0.8', 'versionsuffix': '', 'extensions': []}], 'homepage': 'https://gotcha.readthedocs.io/en/latest/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': "Gotcha is a library that wraps functions. Tools can use gotcha to install hooks into other\nlibraries, for example putting a wrapper function around libc's malloc. It is similar to LD_PRELOAD, but\noperates via a programmable API. This enables easy methods of accomplishing tasks like code instrumentation\nor wholesale replacement of mechanisms in programs without disrupting their source code."} installations
