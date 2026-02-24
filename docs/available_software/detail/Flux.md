# Flux



 Flux is a flexible framework for resource management, built for your site. The
 framework consists of a suite of projects, tools, and libraries which may be
 used to build site-custom resource managers for High Performance Computing
 centers. Unlike traditional resource managers, Flux can run as a parallel job
 under most launchers that support MPI, including under Flux itself. This not
 only makes batch scripts and workflows for Flux portable to other resource
 managers (just launch Flux as a job), but it also means that batch jobs have
 all the features of a full resource manager at their disposal, as if they have
 an entire cluster to themselves.


<small>homepage: </small><span class="software-link">[https://flux-framework.org/](https://flux-framework.org/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.80.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Flux/0.80.0-GCC-13.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://flux-framework.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCC', 'version': '13.3.0'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'Flux/0.80.0-GCC-13.3.0', 'module_name': 'Flux', 'module_version': '0.80.0-GCC-13.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'GCC/13.3.0', 'module_name': 'GCC', 'module_version': '13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'libarchive/3.7.4-GCCcore-13.3.0', 'module_name': 'libarchive', 'module_version': '3.7.4-GCCcore-13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'cffi/1.16.0-GCCcore-13.3.0', 'module_name': 'cffi', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.3.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.3.0'}, {'full_module_name': 'cryptography/42.0.8-GCCcore-13.3.0', 'module_name': 'cryptography', 'module_version': '42.0.8-GCCcore-13.3.0'}, {'full_module_name': 'virtualenv/20.26.2-GCCcore-13.3.0', 'module_name': 'virtualenv', 'module_version': '20.26.2-GCCcore-13.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2024.06-GCCcore-13.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2024.06-GCCcore-13.3.0'}, {'full_module_name': 'PyYAML/6.0.2-GCCcore-13.3.0', 'module_name': 'PyYAML', 'module_version': '6.0.2-GCCcore-13.3.0'}, {'full_module_name': 'PLY/3.11-GCCcore-13.3.0', 'module_name': 'PLY', 'module_version': '3.11-GCCcore-13.3.0'}, {'full_module_name': 'Lua/5.4.7-GCCcore-13.3.0', 'module_name': 'Lua', 'module_version': '5.4.7-GCCcore-13.3.0'}, {'full_module_name': 'luaposix/36.3-GCCcore-13.3.0', 'module_name': 'luaposix', 'module_version': '36.3-GCCcore-13.3.0'}, {'full_module_name': 'Perl/5.38.2-GCCcore-13.3.0', 'module_name': 'Perl', 'module_version': '5.38.2-GCCcore-13.3.0'}, {'full_module_name': 'OpenPGM/5.2.122-GCCcore-13.3.0', 'module_name': 'OpenPGM', 'module_version': '5.2.122-GCCcore-13.3.0'}, {'full_module_name': 'libsodium/1.0.20-GCCcore-13.3.0', 'module_name': 'libsodium', 'module_version': '1.0.20-GCCcore-13.3.0'}, {'full_module_name': 'ZeroMQ/4.3.5-GCCcore-13.3.0', 'module_name': 'ZeroMQ', 'module_version': '4.3.5-GCCcore-13.3.0'}, {'full_module_name': 'Jansson/2.14.1-GCCcore-13.3.0', 'module_name': 'Jansson', 'module_version': '2.14.1-GCCcore-13.3.0'}, {'full_module_name': 'numactl/2.0.18-GCCcore-13.3.0', 'module_name': 'numactl', 'module_version': '2.0.18-GCCcore-13.3.0'}, {'full_module_name': 'libxml2/2.12.7-GCCcore-13.3.0', 'module_name': 'libxml2', 'module_version': '2.12.7-GCCcore-13.3.0'}, {'full_module_name': 'libpciaccess/0.18.1-GCCcore-13.3.0', 'module_name': 'libpciaccess', 'module_version': '0.18.1-GCCcore-13.3.0'}, {'full_module_name': 'hwloc/2.10.0-GCCcore-13.3.0', 'module_name': 'hwloc', 'module_version': '2.10.0-GCCcore-13.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-13.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-13.3.0'}, {'full_module_name': 'libedit/20240808-GCCcore-13.3.0', 'module_name': 'libedit', 'module_version': '20240808-GCCcore-13.3.0'}, {'full_module_name': 'gzip/1.13-GCCcore-13.3.0', 'module_name': 'gzip', 'module_version': '1.13-GCCcore-13.3.0'}, {'full_module_name': 'zstd/1.5.6-GCCcore-13.3.0', 'module_name': 'zstd', 'module_version': '1.5.6-GCCcore-13.3.0'}, {'full_module_name': 'ICU/75.1-GCCcore-13.3.0', 'module_name': 'ICU', 'module_version': '75.1-GCCcore-13.3.0'}, {'full_module_name': 'Boost/1.85.0-GCC-13.3.0', 'module_name': 'Boost', 'module_version': '1.85.0-GCC-13.3.0'}, {'full_module_name': 'yaml-cpp/0.8.0-GCCcore-13.3.0', 'module_name': 'yaml-cpp', 'module_version': '0.8.0-GCCcore-13.3.0'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.3.0'}, {'full_module_name': 'PMIx/5.0.2-GCCcore-13.3.0', 'module_name': 'PMIx', 'module_version': '5.0.2-GCCcore-13.3.0'}, {'full_module_name': 'Flux/0.80.0-GCC-13.3.0', 'module_name': 'Flux', 'module_version': '0.80.0-GCC-13.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\n Flux is a flexible framework for resource management, built for your site. The\n framework consists of a suite of projects, tools, and libraries which may be\n used to build site-custom resource managers for High Performance Computing\n centers. Unlike traditional resource managers, Flux can run as a parallel job\n under most launchers that support MPI, including under Flux itself. This not\n only makes batch scripts and workflows for Flux portable to other resource\n managers (just launch Flux as a job), but it also means that batch jobs have\n all the features of a full resource manager at their disposal, as if they have\n an entire cluster to themselves.\n', 'version': '0.80.0', 'versionsuffix': '', 'extensions': [{'type': 'component', 'name': 'flux-core', 'version': '0.80.0'}, {'type': 'component', 'name': 'flux-sched', 'version': '0.48.0'}, {'type': 'component', 'name': 'flux-pmix', 'version': '0.7.0'}]}], 'homepage': 'https://flux-framework.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\n Flux is a flexible framework for resource management, built for your site. The\n framework consists of a suite of projects, tools, and libraries which may be\n used to build site-custom resource managers for High Performance Computing\n centers. Unlike traditional resource managers, Flux can run as a parallel job\n under most launchers that support MPI, including under Flux itself. This not\n only makes batch scripts and workflows for Flux portable to other resource\n managers (just launch Flux as a job), but it also means that batch jobs have\n all the features of a full resource manager at their disposal, as if they have\n an entire cluster to themselves.\n'} installations


### flux-core


|`flux-core` version|Flux modules that include it|
| --- | --- |
|0.80.0|`Flux/0.80.0-GCC-13.3.0`|

### flux-pmix


|`flux-pmix` version|Flux modules that include it|
| --- | --- |
|0.7.0|`Flux/0.80.0-GCC-13.3.0`|

### flux-sched


|`flux-sched` version|Flux modules that include it|
| --- | --- |
|0.48.0|`Flux/0.80.0-GCC-13.3.0`|