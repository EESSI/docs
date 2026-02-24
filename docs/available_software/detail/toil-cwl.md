# toil-cwl



A scalable, efficient, cross-platform (Linux/macOS) and easy-to-use workflow engine in pure Python.
This installation contains toil, with the cwl extras.


<small>homepage: </small><span class="software-link">[https://github.com/DataBiosphere/toil](https://github.com/DataBiosphere/toil)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|8.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`toil-cwl/8.2.0-foss-2023b`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://github.com/DataBiosphere/toil', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023b'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'toil-cwl/8.2.0-foss-2023b', 'module_name': 'toil-cwl', 'module_version': '8.2.0-foss-2023b'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'GCC/13.2.0', 'module_name': 'GCC', 'module_version': '13.2.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-13.2.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-13.2.0'}, {'full_module_name': 'libxml2/2.11.5-GCCcore-13.2.0', 'module_name': 'libxml2', 'module_version': '2.11.5-GCCcore-13.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-13.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-13.2.0'}, {'full_module_name': 'hwloc/2.9.2-GCCcore-13.2.0', 'module_name': 'hwloc', 'module_version': '2.9.2-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.2.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.2.0'}, {'full_module_name': 'UCX/1.15.0-GCCcore-13.2.0', 'module_name': 'UCX', 'module_version': '1.15.0-GCCcore-13.2.0'}, {'full_module_name': 'libfabric/1.19.0-GCCcore-13.2.0', 'module_name': 'libfabric', 'module_version': '1.19.0-GCCcore-13.2.0'}, {'full_module_name': 'PMIx/4.2.6-GCCcore-13.2.0', 'module_name': 'PMIx', 'module_version': '4.2.6-GCCcore-13.2.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-13.2.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-13.2.0'}, {'full_module_name': 'OpenMPI/4.1.6-GCC-13.2.0', 'module_name': 'OpenMPI', 'module_version': '4.1.6-GCC-13.2.0'}, {'full_module_name': 'OpenBLAS/0.3.24-GCC-13.2.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.24-GCC-13.2.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-13.2.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-13.2.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.2.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.2.0'}, {'full_module_name': 'gompi/2023b', 'module_name': 'gompi', 'module_version': '2023b'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023b', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023b'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023b-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023b-fb'}, {'full_module_name': 'foss/2023b', 'module_name': 'foss', 'module_version': '2023b'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'dill/0.3.8-GCCcore-13.2.0', 'module_name': 'dill', 'module_version': '0.3.8-GCCcore-13.2.0'}, {'full_module_name': 'ICU/74.1-GCCcore-13.2.0', 'module_name': 'ICU', 'module_version': '74.1-GCCcore-13.2.0'}, {'full_module_name': 'nodejs/20.9.0-GCCcore-13.2.0', 'module_name': 'nodejs', 'module_version': '20.9.0-GCCcore-13.2.0'}, {'full_module_name': 'ruamel.yaml/0.18.6-GCCcore-13.2.0', 'module_name': 'ruamel.yaml', 'module_version': '0.18.6-GCCcore-13.2.0'}, {'full_module_name': 'RDFlib/7.1.4-GCCcore-13.2.0', 'module_name': 'RDFlib', 'module_version': '7.1.4-GCCcore-13.2.0'}, {'full_module_name': 'libxslt/1.1.38-GCCcore-13.2.0', 'module_name': 'libxslt', 'module_version': '1.1.38-GCCcore-13.2.0'}, {'full_module_name': 'lxml/4.9.3-GCCcore-13.2.0', 'module_name': 'lxml', 'module_version': '4.9.3-GCCcore-13.2.0'}, {'full_module_name': 'gfbf/2023b', 'module_name': 'gfbf', 'module_version': '2023b'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-13.2.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-13.2.0'}, {'full_module_name': 'SciPy-bundle/2023.11-gfbf-2023b', 'module_name': 'SciPy-bundle', 'module_version': '2023.11-gfbf-2023b'}, {'full_module_name': 'networkx/3.2.1-gfbf-2023b', 'module_name': 'networkx', 'module_version': '3.2.1-gfbf-2023b'}, {'full_module_name': 'pydot/2.0.0-GCCcore-13.2.0', 'module_name': 'pydot', 'module_version': '2.0.0-GCCcore-13.2.0'}, {'full_module_name': 'cwltool/3.1.20250110105449-foss-2023b', 'module_name': 'cwltool', 'module_version': '3.1.20250110105449-foss-2023b'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.2.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.2.0'}, {'full_module_name': 'PyYAML/6.0.1-GCCcore-13.2.0', 'module_name': 'PyYAML', 'module_version': '6.0.1-GCCcore-13.2.0'}, {'full_module_name': 'typing-extensions/4.10.0-GCCcore-13.2.0', 'module_name': 'typing-extensions', 'module_version': '4.10.0-GCCcore-13.2.0'}, {'full_module_name': 'psutil/6.1.0-GCCcore-13.2.0', 'module_name': 'psutil', 'module_version': '6.1.0-GCCcore-13.2.0'}, {'full_module_name': 'pydantic/2.7.4-GCCcore-13.2.0', 'module_name': 'pydantic', 'module_version': '2.7.4-GCCcore-13.2.0'}, {'full_module_name': 'toil-cwl/8.2.0-foss-2023b', 'module_name': 'toil-cwl', 'module_version': '8.2.0-foss-2023b'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nA scalable, efficient, cross-platform (Linux/macOS) and easy-to-use workflow engine in pure Python.\nThis installation contains toil, with the cwl extras.\n', 'version': '8.2.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'addict', 'version': '2.4.0'}, {'type': 'python', 'name': 'blessed', 'version': '1.21.0'}, {'type': 'python', 'name': 'prefixed', 'version': '0.9.0'}, {'type': 'python', 'name': 'enlighten', 'version': '1.14.1'}, {'type': 'python', 'name': 'docker', 'version': '7.1.0'}, {'type': 'python', 'name': 'PyPubSub', 'version': '4.0.3'}, {'type': 'python', 'name': 'configargparse', 'version': '1.7.1'}, {'type': 'python', 'name': 'prompt_toolkit', 'version': '3.0.51'}, {'type': 'python', 'name': 'bleach', 'version': '6.2.0'}, {'type': 'python', 'name': 'boltons', 'version': '25.0.0'}, {'type': 'python', 'name': 'repoze.lru', 'version': '0.7'}, {'type': 'python', 'name': 'Routes', 'version': '2.5.1'}, {'type': 'python', 'name': 'zipstream-new', 'version': '1.1.8'}, {'type': 'python', 'name': 'galaxy-util', 'version': '24.2.3'}, {'type': 'python', 'name': 'zstandard', 'version': '0.23.0'}, {'type': 'python', 'name': 'conda-package-streaming', 'version': '0.11.0'}, {'type': 'python', 'name': 'galaxy-tool-util', 'version': '24.2.3'}, {'type': 'python', 'name': 'toil', 'version': '8.2.0'}]}], 'homepage': 'https://github.com/DataBiosphere/toil', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\nA scalable, efficient, cross-platform (Linux/macOS) and easy-to-use workflow engine in pure Python.\nThis installation contains toil, with the cwl extras.\n'} installations


### addict


|`addict` version|toil-cwl modules that include it|
| --- | --- |
|2.4.0|`toil-cwl/8.2.0-foss-2023b`|

### bleach


|`bleach` version|toil-cwl modules that include it|
| --- | --- |
|6.2.0|`toil-cwl/8.2.0-foss-2023b`|

### blessed


|`blessed` version|toil-cwl modules that include it|
| --- | --- |
|1.21.0|`toil-cwl/8.2.0-foss-2023b`|

### boltons


|`boltons` version|toil-cwl modules that include it|
| --- | --- |
|25.0.0|`toil-cwl/8.2.0-foss-2023b`|

### conda-package-streaming


|`conda-package-streaming` version|toil-cwl modules that include it|
| --- | --- |
|0.11.0|`toil-cwl/8.2.0-foss-2023b`|

### configargparse


|`configargparse` version|toil-cwl modules that include it|
| --- | --- |
|1.7.1|`toil-cwl/8.2.0-foss-2023b`|

### docker


|`docker` version|toil-cwl modules that include it|
| --- | --- |
|7.1.0|`toil-cwl/8.2.0-foss-2023b`|

### enlighten


|`enlighten` version|toil-cwl modules that include it|
| --- | --- |
|1.14.1|`toil-cwl/8.2.0-foss-2023b`|

### galaxy-tool-util


|`galaxy-tool-util` version|toil-cwl modules that include it|
| --- | --- |
|24.2.3|`toil-cwl/8.2.0-foss-2023b`|

### galaxy-util


|`galaxy-util` version|toil-cwl modules that include it|
| --- | --- |
|24.2.3|`toil-cwl/8.2.0-foss-2023b`|

### prefixed


|`prefixed` version|toil-cwl modules that include it|
| --- | --- |
|0.9.0|`toil-cwl/8.2.0-foss-2023b`|

### prompt_toolkit


|`prompt_toolkit` version|toil-cwl modules that include it|
| --- | --- |
|3.0.51|`toil-cwl/8.2.0-foss-2023b`|

### PyPubSub


|`PyPubSub` version|toil-cwl modules that include it|
| --- | --- |
|4.0.3|`toil-cwl/8.2.0-foss-2023b`|

### repoze.lru


|`repoze.lru` version|toil-cwl modules that include it|
| --- | --- |
|0.7|`toil-cwl/8.2.0-foss-2023b`|

### Routes


|`Routes` version|toil-cwl modules that include it|
| --- | --- |
|2.5.1|`toil-cwl/8.2.0-foss-2023b`|

### toil


|`toil` version|toil-cwl modules that include it|
| --- | --- |
|8.2.0|`toil-cwl/8.2.0-foss-2023b`|

### zipstream-new


|`zipstream-new` version|toil-cwl modules that include it|
| --- | --- |
|1.1.8|`toil-cwl/8.2.0-foss-2023b`|

### zstandard


|`zstandard` version|toil-cwl modules that include it|
| --- | --- |
|0.23.0|`toil-cwl/8.2.0-foss-2023b`|