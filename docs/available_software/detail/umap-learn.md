# umap-learn



Uniform Manifold Approximation and Projection (UMAP) is a dimension reduction technique
that can be used for visualisation similarly to t-SNE, but also for general non-linear
dimension reduction.


<small>homepage: </small><span class="software-link">[https://umap-learn.readthedocs.io/en/latest/](https://umap-learn.readthedocs.io/en/latest/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.5.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`umap-learn/0.5.5-foss-2023a`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://umap-learn.readthedocs.io/en/latest/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023a'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'umap-learn/0.5.5-foss-2023a', 'module_name': 'umap-learn', 'module_version': '0.5.5-foss-2023a'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.3.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.3.0'}, {'full_module_name': 'libxml2/2.11.4-GCCcore-12.3.0', 'module_name': 'libxml2', 'module_version': '2.11.4-GCCcore-12.3.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.3.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.3.0'}, {'full_module_name': 'hwloc/2.9.1-GCCcore-12.3.0', 'module_name': 'hwloc', 'module_version': '2.9.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.3.0'}, {'full_module_name': 'UCX/1.14.1-GCCcore-12.3.0', 'module_name': 'UCX', 'module_version': '1.14.1-GCCcore-12.3.0'}, {'full_module_name': 'libfabric/1.18.0-GCCcore-12.3.0', 'module_name': 'libfabric', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'PMIx/4.2.4-GCCcore-12.3.0', 'module_name': 'PMIx', 'module_version': '4.2.4-GCCcore-12.3.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-12.3.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenMPI/4.1.5-GCC-12.3.0', 'module_name': 'OpenMPI', 'module_version': '4.1.5-GCC-12.3.0'}, {'full_module_name': 'OpenBLAS/0.3.23-GCC-12.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.23-GCC-12.3.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-12.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-12.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.3.0'}, {'full_module_name': 'gompi/2023a', 'module_name': 'gompi', 'module_version': '2023a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023a-fb'}, {'full_module_name': 'foss/2023a', 'module_name': 'foss', 'module_version': '2023a'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'gfbf/2023a', 'module_name': 'gfbf', 'module_version': '2023a'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-12.3.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-12.3.0'}, {'full_module_name': 'SciPy-bundle/2023.07-gfbf-2023a', 'module_name': 'SciPy-bundle', 'module_version': '2023.07-gfbf-2023a'}, {'full_module_name': 'scikit-learn/1.3.1-gfbf-2023a', 'module_name': 'scikit-learn', 'module_version': '1.3.1-gfbf-2023a'}, {'full_module_name': 'numba/0.58.1-foss-2023a', 'module_name': 'numba', 'module_version': '0.58.1-foss-2023a'}, {'full_module_name': 'LLVM/16.0.6-GCCcore-12.3.0', 'module_name': 'LLVM', 'module_version': '16.0.6-GCCcore-12.3.0'}, {'full_module_name': 'tqdm/4.66.1-GCCcore-12.3.0', 'module_name': 'tqdm', 'module_version': '4.66.1-GCCcore-12.3.0'}, {'full_module_name': 'umap-learn/0.5.5-foss-2023a', 'module_name': 'umap-learn', 'module_version': '0.5.5-foss-2023a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nUniform Manifold Approximation and Projection (UMAP) is a dimension reduction technique\nthat can be used for visualisation similarly to t-SNE, but also for general non-linear\ndimension reduction.\n', 'version': '0.5.5', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pynndescent', 'version': '0.5.11'}, {'type': 'python', 'name': 'umap-learn', 'version': '0.5.5'}]}], 'homepage': 'https://umap-learn.readthedocs.io/en/latest/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\nUniform Manifold Approximation and Projection (UMAP) is a dimension reduction technique\nthat can be used for visualisation similarly to t-SNE, but also for general non-linear\ndimension reduction.\n'} installations


### pynndescent


|`pynndescent` version|umap-learn modules that include it|
| --- | --- |
|0.5.11|`umap-learn/0.5.5-foss-2023a`|

### umap-learn


|`umap-learn` version|umap-learn modules that include it|
| --- | --- |
|0.5.5|`umap-learn/0.5.5-foss-2023a`|