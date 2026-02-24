# pkg-config



 pkg-config is a helper tool used when compiling applications and libraries.
 It helps you insert the correct compiler options on the command line so an
 application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
 for instance, rather than hard-coding values on where to find glib (or other
 libraries).


<small>homepage: </small><span class="software-link">[https://www.freedesktop.org/wiki/Software/pkg-config/](https://www.freedesktop.org/wiki/Software/pkg-config/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.29.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`pkg-config/0.29.2-GCCcore-12.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://www.freedesktop.org/wiki/Software/pkg-config/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'pkg-config/0.29.2-GCCcore-12.3.0', 'module_name': 'pkg-config', 'module_version': '0.29.2-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'pkg-config/0.29.2-GCCcore-12.3.0', 'module_name': 'pkg-config', 'module_version': '0.29.2-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\n pkg-config is a helper tool used when compiling applications and libraries.\n It helps you insert the correct compiler options on the command line so an\n application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`\n for instance, rather than hard-coding values on where to find glib (or other\n libraries).\n', 'version': '0.29.2', 'versionsuffix': '', 'extensions': []}], 'homepage': 'https://www.freedesktop.org/wiki/Software/pkg-config/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\n pkg-config is a helper tool used when compiling applications and libraries.\n It helps you insert the correct compiler options on the command line so an\n application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`\n for instance, rather than hard-coding values on where to find glib (or other\n libraries).\n'} installations
