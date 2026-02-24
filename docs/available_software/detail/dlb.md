# dlb



DLB is a dynamic library designed to speed up HPC hybrid applications (i.e.,
two levels of parallelism) by improving the load balance of the outer level of
parallelism (e.g., MPI) by dynamically redistributing the computational
resources at the inner level of parallelism (e.g., OpenMP). at run time.


<small>homepage: </small><span class="software-link">[https://pm.bsc.es/dlb/](https://pm.bsc.es/dlb/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|3.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`dlb/3.4-gompi-2023b`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://pm.bsc.es/dlb/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'gompi', 'version': '2023b'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'dlb/3.4-gompi-2023b', 'module_name': 'dlb', 'module_version': '3.4-gompi-2023b'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'GCC/13.2.0', 'module_name': 'GCC', 'module_version': '13.2.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-13.2.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-13.2.0'}, {'full_module_name': 'libxml2/2.11.5-GCCcore-13.2.0', 'module_name': 'libxml2', 'module_version': '2.11.5-GCCcore-13.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-13.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-13.2.0'}, {'full_module_name': 'hwloc/2.9.2-GCCcore-13.2.0', 'module_name': 'hwloc', 'module_version': '2.9.2-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.2.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.2.0'}, {'full_module_name': 'UCX/1.15.0-GCCcore-13.2.0', 'module_name': 'UCX', 'module_version': '1.15.0-GCCcore-13.2.0'}, {'full_module_name': 'libfabric/1.19.0-GCCcore-13.2.0', 'module_name': 'libfabric', 'module_version': '1.19.0-GCCcore-13.2.0'}, {'full_module_name': 'PMIx/4.2.6-GCCcore-13.2.0', 'module_name': 'PMIx', 'module_version': '4.2.6-GCCcore-13.2.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-13.2.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-13.2.0'}, {'full_module_name': 'OpenMPI/4.1.6-GCC-13.2.0', 'module_name': 'OpenMPI', 'module_version': '4.1.6-GCC-13.2.0'}, {'full_module_name': 'gompi/2023b', 'module_name': 'gompi', 'module_version': '2023b'}, {'full_module_name': 'dlb/3.4-gompi-2023b', 'module_name': 'dlb', 'module_version': '3.4-gompi-2023b'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nDLB is a dynamic library designed to speed up HPC hybrid applications (i.e.,\ntwo levels of parallelism) by improving the load balance of the outer level of\nparallelism (e.g., MPI) by dynamically redistributing the computational\nresources at the inner level of parallelism (e.g., OpenMP). at run time.\n', 'version': '3.4', 'versionsuffix': '', 'extensions': []}], 'homepage': 'https://pm.bsc.es/dlb/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\nDLB is a dynamic library designed to speed up HPC hybrid applications (i.e.,\ntwo levels of parallelism) by improving the load balance of the outer level of\nparallelism (e.g., MPI) by dynamically redistributing the computational\nresources at the inner level of parallelism (e.g., OpenMP). at run time.\n'} installations
