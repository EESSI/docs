# scanpy


Scanpy is a scalable toolkit for analyzing single-cell gene expression data built
 jointly with anndata. It includes preprocessing, visualization, clustering, trajectory inference
 and differential expression testing. The Python-based implementation efficiently deals with
 datasets of more than one million cells.


<small>homepage: </small><span class="software-link">[https://scanpy.readthedocs.io/en/stable/](https://scanpy.readthedocs.io/en/stable/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.9.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`scanpy/1.9.8-foss-2023a`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://scanpy.readthedocs.io/en/stable/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023a'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'scanpy/1.9.8-foss-2023a', 'module_name': 'scanpy', 'module_version': '1.9.8-foss-2023a'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.3.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.3.0'}, {'full_module_name': 'libxml2/2.11.4-GCCcore-12.3.0', 'module_name': 'libxml2', 'module_version': '2.11.4-GCCcore-12.3.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.3.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.3.0'}, {'full_module_name': 'hwloc/2.9.1-GCCcore-12.3.0', 'module_name': 'hwloc', 'module_version': '2.9.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.3.0'}, {'full_module_name': 'UCX/1.14.1-GCCcore-12.3.0', 'module_name': 'UCX', 'module_version': '1.14.1-GCCcore-12.3.0'}, {'full_module_name': 'libfabric/1.18.0-GCCcore-12.3.0', 'module_name': 'libfabric', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'PMIx/4.2.4-GCCcore-12.3.0', 'module_name': 'PMIx', 'module_version': '4.2.4-GCCcore-12.3.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-12.3.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenMPI/4.1.5-GCC-12.3.0', 'module_name': 'OpenMPI', 'module_version': '4.1.5-GCC-12.3.0'}, {'full_module_name': 'OpenBLAS/0.3.23-GCC-12.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.23-GCC-12.3.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-12.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-12.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.3.0'}, {'full_module_name': 'gompi/2023a', 'module_name': 'gompi', 'module_version': '2023a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023a-fb'}, {'full_module_name': 'foss/2023a', 'module_name': 'foss', 'module_version': '2023a'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'gfbf/2023a', 'module_name': 'gfbf', 'module_version': '2023a'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-12.3.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-12.3.0'}, {'full_module_name': 'SciPy-bundle/2023.07-gfbf-2023a', 'module_name': 'SciPy-bundle', 'module_version': '2023.07-gfbf-2023a'}, {'full_module_name': 'libpng/1.6.39-GCCcore-12.3.0', 'module_name': 'libpng', 'module_version': '1.6.39-GCCcore-12.3.0'}, {'full_module_name': 'Brotli/1.0.9-GCCcore-12.3.0', 'module_name': 'Brotli', 'module_version': '1.0.9-GCCcore-12.3.0'}, {'full_module_name': 'freetype/2.13.0-GCCcore-12.3.0', 'module_name': 'freetype', 'module_version': '2.13.0-GCCcore-12.3.0'}, {'full_module_name': 'expat/2.5.0-GCCcore-12.3.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'fontconfig/2.14.2-GCCcore-12.3.0', 'module_name': 'fontconfig', 'module_version': '2.14.2-GCCcore-12.3.0'}, {'full_module_name': 'xorg-macros/1.20.0-GCCcore-12.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.0-GCCcore-12.3.0'}, {'full_module_name': 'X11/20230603-GCCcore-12.3.0', 'module_name': 'X11', 'module_version': '20230603-GCCcore-12.3.0'}, {'full_module_name': 'Tk/8.6.13-GCCcore-12.3.0', 'module_name': 'Tk', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'Tkinter/3.11.3-GCCcore-12.3.0', 'module_name': 'Tkinter', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'NASM/2.16.01-GCCcore-12.3.0', 'module_name': 'NASM', 'module_version': '2.16.01-GCCcore-12.3.0'}, {'full_module_name': 'libjpeg-turbo/2.1.5.1-GCCcore-12.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '2.1.5.1-GCCcore-12.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-12.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-12.3.0'}, {'full_module_name': 'gzip/1.12-GCCcore-12.3.0', 'module_name': 'gzip', 'module_version': '1.12-GCCcore-12.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-12.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-12.3.0'}, {'full_module_name': 'zstd/1.5.5-GCCcore-12.3.0', 'module_name': 'zstd', 'module_version': '1.5.5-GCCcore-12.3.0'}, {'full_module_name': 'libdeflate/1.18-GCCcore-12.3.0', 'module_name': 'libdeflate', 'module_version': '1.18-GCCcore-12.3.0'}, {'full_module_name': 'LibTIFF/4.5.0-GCCcore-12.3.0', 'module_name': 'LibTIFF', 'module_version': '4.5.0-GCCcore-12.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-12.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-12.3.0'}, {'full_module_name': 'libwebp/1.3.1-GCCcore-12.3.0', 'module_name': 'libwebp', 'module_version': '1.3.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-12.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'LittleCMS/2.15-GCCcore-12.3.0', 'module_name': 'LittleCMS', 'module_version': '2.15-GCCcore-12.3.0'}, {'full_module_name': 'Pillow/10.0.0-GCCcore-12.3.0', 'module_name': 'Pillow', 'module_version': '10.0.0-GCCcore-12.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-12.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-12.3.0'}, {'full_module_name': 'Ninja/1.11.1-GCCcore-12.3.0', 'module_name': 'Ninja', 'module_version': '1.11.1-GCCcore-12.3.0'}, {'full_module_name': 'Meson/1.1.1-GCCcore-12.3.0', 'module_name': 'Meson', 'module_version': '1.1.1-GCCcore-12.3.0'}, {'full_module_name': 'meson-python/0.13.2-GCCcore-12.3.0', 'module_name': 'meson-python', 'module_version': '0.13.2-GCCcore-12.3.0'}, {'full_module_name': 'matplotlib/3.7.2-gfbf-2023a', 'module_name': 'matplotlib', 'module_version': '3.7.2-gfbf-2023a'}, {'full_module_name': 'Seaborn/0.13.2-gfbf-2023a', 'module_name': 'Seaborn', 'module_version': '0.13.2-gfbf-2023a'}, {'full_module_name': 'mpi4py/3.1.4-gompi-2023a', 'module_name': 'mpi4py', 'module_version': '3.1.4-gompi-2023a'}, {'full_module_name': 'Szip/2.1.1-GCCcore-12.3.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-12.3.0'}, {'full_module_name': 'HDF5/1.14.0-gompi-2023a', 'module_name': 'HDF5', 'module_version': '1.14.0-gompi-2023a'}, {'full_module_name': 'h5py/3.9.0-foss-2023a', 'module_name': 'h5py', 'module_version': '3.9.0-foss-2023a'}, {'full_module_name': 'tqdm/4.66.1-GCCcore-12.3.0', 'module_name': 'tqdm', 'module_version': '4.66.1-GCCcore-12.3.0'}, {'full_module_name': 'scikit-learn/1.3.1-gfbf-2023a', 'module_name': 'scikit-learn', 'module_version': '1.3.1-gfbf-2023a'}, {'full_module_name': 'statsmodels/0.14.1-gfbf-2023a', 'module_name': 'statsmodels', 'module_version': '0.14.1-gfbf-2023a'}, {'full_module_name': 'networkx/3.1-gfbf-2023a', 'module_name': 'networkx', 'module_version': '3.1-gfbf-2023a'}, {'full_module_name': 'numba/0.58.1-foss-2023a', 'module_name': 'numba', 'module_version': '0.58.1-foss-2023a'}, {'full_module_name': 'LLVM/16.0.6-GCCcore-12.3.0', 'module_name': 'LLVM', 'module_version': '16.0.6-GCCcore-12.3.0'}, {'full_module_name': 'umap-learn/0.5.5-foss-2023a', 'module_name': 'umap-learn', 'module_version': '0.5.5-foss-2023a'}, {'full_module_name': 'anndata/0.10.5.post1-foss-2023a', 'module_name': 'anndata', 'module_version': '0.10.5.post1-foss-2023a'}, {'full_module_name': 'scanpy/1.9.8-foss-2023a', 'module_name': 'scanpy', 'module_version': '1.9.8-foss-2023a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Scanpy is a scalable toolkit for analyzing single-cell gene expression data built\n jointly with anndata. It includes preprocessing, visualization, clustering, trajectory inference\n and differential expression testing. The Python-based implementation efficiently deals with\n datasets of more than one million cells.\n', 'version': '1.9.8', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'stdlib_list', 'version': '0.10.0'}, {'type': 'python', 'name': 'packaging', 'version': '23.2'}, {'type': 'python', 'name': 'natsort', 'version': '8.4.0'}, {'type': 'python', 'name': 'joblib', 'version': '1.3.2'}, {'type': 'python', 'name': 'session-info', 'version': '1.0.0'}, {'type': 'python', 'name': 'legacy_api_wrap', 'version': '1.4'}, {'type': 'python', 'name': 'scanpy', 'version': '1.9.8'}]}], 'homepage': 'https://scanpy.readthedocs.io/en/stable/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'Scanpy is a scalable toolkit for analyzing single-cell gene expression data built\n jointly with anndata. It includes preprocessing, visualization, clustering, trajectory inference\n and differential expression testing. The Python-based implementation efficiently deals with\n datasets of more than one million cells.\n'} installations


### joblib


|`joblib` version|scanpy modules that include it|
| --- | --- |
|1.3.2|`scanpy/1.9.8-foss-2023a`|

### legacy_api_wrap


|`legacy_api_wrap` version|scanpy modules that include it|
| --- | --- |
|1.4|`scanpy/1.9.8-foss-2023a`|

### natsort


|`natsort` version|scanpy modules that include it|
| --- | --- |
|8.4.0|`scanpy/1.9.8-foss-2023a`|

### packaging


|`packaging` version|scanpy modules that include it|
| --- | --- |
|23.2|`scanpy/1.9.8-foss-2023a`|

### scanpy


|`scanpy` version|scanpy modules that include it|
| --- | --- |
|1.9.8|`scanpy/1.9.8-foss-2023a`|

### session-info


|`session-info` version|scanpy modules that include it|
| --- | --- |
|1.0.0|`scanpy/1.9.8-foss-2023a`|

### stdlib_list


|`stdlib_list` version|scanpy modules that include it|
| --- | --- |
|0.10.0|`scanpy/1.9.8-foss-2023a`|