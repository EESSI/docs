# MultiQC


Aggregate results from bioinformatics analyses across many samples into a single report.

 MultiQC searches a given directory for analysis logs and compiles an HTML report. It's a general
 use tool, perfect for summarising the output from numerous bioinformatics tools.

<small>homepage: </small><span class="software-link">[https://multiqc.info](https://multiqc.info)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.14|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MultiQC/1.14-foss-2022b`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://multiqc.info', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2022b'}, 'toolchain_families_compatibility': ['2022b_foss'], 'module': {'full_module_name': 'MultiQC/1.14-foss-2022b', 'module_name': 'MultiQC', 'module_version': '1.14-foss-2022b'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.2.0', 'module_name': 'GCCcore', 'module_version': '12.2.0'}, {'full_module_name': 'GCC/12.2.0', 'module_name': 'GCC', 'module_version': '12.2.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.2.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.2.0'}, {'full_module_name': 'libxml2/2.10.3-GCCcore-12.2.0', 'module_name': 'libxml2', 'module_version': '2.10.3-GCCcore-12.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.2.0'}, {'full_module_name': 'hwloc/2.8.0-GCCcore-12.2.0', 'module_name': 'hwloc', 'module_version': '2.8.0-GCCcore-12.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.2.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.2.0'}, {'full_module_name': 'UCX/1.13.1-GCCcore-12.2.0', 'module_name': 'UCX', 'module_version': '1.13.1-GCCcore-12.2.0'}, {'full_module_name': 'libfabric/1.16.1-GCCcore-12.2.0', 'module_name': 'libfabric', 'module_version': '1.16.1-GCCcore-12.2.0'}, {'full_module_name': 'PMIx/4.2.2-GCCcore-12.2.0', 'module_name': 'PMIx', 'module_version': '4.2.2-GCCcore-12.2.0'}, {'full_module_name': 'UCC/1.1.0-GCCcore-12.2.0', 'module_name': 'UCC', 'module_version': '1.1.0-GCCcore-12.2.0'}, {'full_module_name': 'OpenMPI/4.1.4-GCC-12.2.0', 'module_name': 'OpenMPI', 'module_version': '4.1.4-GCC-12.2.0'}, {'full_module_name': 'OpenBLAS/0.3.21-GCC-12.2.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.21-GCC-12.2.0'}, {'full_module_name': 'FlexiBLAS/3.2.1-GCC-12.2.0', 'module_name': 'FlexiBLAS', 'module_version': '3.2.1-GCC-12.2.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.2.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.2.0'}, {'full_module_name': 'gompi/2022b', 'module_name': 'gompi', 'module_version': '2022b'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2022b', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2022b'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2022b-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2022b-fb'}, {'full_module_name': 'foss/2022b', 'module_name': 'foss', 'module_version': '2022b'}, {'full_module_name': 'Tcl/8.6.12-GCCcore-12.2.0', 'module_name': 'Tcl', 'module_version': '8.6.12-GCCcore-12.2.0'}, {'full_module_name': 'SQLite/3.39.4-GCCcore-12.2.0', 'module_name': 'SQLite', 'module_version': '3.39.4-GCCcore-12.2.0'}, {'full_module_name': 'GMP/6.2.1-GCCcore-12.2.0', 'module_name': 'GMP', 'module_version': '6.2.1-GCCcore-12.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.2.0'}, {'full_module_name': 'Python/3.10.8-GCCcore-12.2.0', 'module_name': 'Python', 'module_version': '3.10.8-GCCcore-12.2.0'}, {'full_module_name': 'gfbf/2022b', 'module_name': 'gfbf', 'module_version': '2022b'}, {'full_module_name': 'pybind11/2.10.3-GCCcore-12.2.0', 'module_name': 'pybind11', 'module_version': '2.10.3-GCCcore-12.2.0'}, {'full_module_name': 'SciPy-bundle/2023.02-gfbf-2022b', 'module_name': 'SciPy-bundle', 'module_version': '2023.02-gfbf-2022b'}, {'full_module_name': 'libpng/1.6.38-GCCcore-12.2.0', 'module_name': 'libpng', 'module_version': '1.6.38-GCCcore-12.2.0'}, {'full_module_name': 'Brotli/1.0.9-GCCcore-12.2.0', 'module_name': 'Brotli', 'module_version': '1.0.9-GCCcore-12.2.0'}, {'full_module_name': 'freetype/2.12.1-GCCcore-12.2.0', 'module_name': 'freetype', 'module_version': '2.12.1-GCCcore-12.2.0'}, {'full_module_name': 'expat/2.4.9-GCCcore-12.2.0', 'module_name': 'expat', 'module_version': '2.4.9-GCCcore-12.2.0'}, {'full_module_name': 'fontconfig/2.14.1-GCCcore-12.2.0', 'module_name': 'fontconfig', 'module_version': '2.14.1-GCCcore-12.2.0'}, {'full_module_name': 'xorg-macros/1.19.3-GCCcore-12.2.0', 'module_name': 'xorg-macros', 'module_version': '1.19.3-GCCcore-12.2.0'}, {'full_module_name': 'X11/20221110-GCCcore-12.2.0', 'module_name': 'X11', 'module_version': '20221110-GCCcore-12.2.0'}, {'full_module_name': 'Tk/8.6.12-GCCcore-12.2.0', 'module_name': 'Tk', 'module_version': '8.6.12-GCCcore-12.2.0'}, {'full_module_name': 'Tkinter/3.10.8-GCCcore-12.2.0', 'module_name': 'Tkinter', 'module_version': '3.10.8-GCCcore-12.2.0'}, {'full_module_name': 'NASM/2.15.05-GCCcore-12.2.0', 'module_name': 'NASM', 'module_version': '2.15.05-GCCcore-12.2.0'}, {'full_module_name': 'libjpeg-turbo/2.1.4-GCCcore-12.2.0', 'module_name': 'libjpeg-turbo', 'module_version': '2.1.4-GCCcore-12.2.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-12.2.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-12.2.0'}, {'full_module_name': 'gzip/1.12-GCCcore-12.2.0', 'module_name': 'gzip', 'module_version': '1.12-GCCcore-12.2.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-12.2.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-12.2.0'}, {'full_module_name': 'zstd/1.5.2-GCCcore-12.2.0', 'module_name': 'zstd', 'module_version': '1.5.2-GCCcore-12.2.0'}, {'full_module_name': 'libdeflate/1.15-GCCcore-12.2.0', 'module_name': 'libdeflate', 'module_version': '1.15-GCCcore-12.2.0'}, {'full_module_name': 'LibTIFF/4.4.0-GCCcore-12.2.0', 'module_name': 'LibTIFF', 'module_version': '4.4.0-GCCcore-12.2.0'}, {'full_module_name': 'Pillow/9.4.0-GCCcore-12.2.0', 'module_name': 'Pillow', 'module_version': '9.4.0-GCCcore-12.2.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-12.2.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-12.2.0'}, {'full_module_name': 'matplotlib/3.7.0-gfbf-2022b', 'module_name': 'matplotlib', 'module_version': '3.7.0-gfbf-2022b'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-12.2.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-12.2.0'}, {'full_module_name': 'PyYAML/6.0-GCCcore-12.2.0', 'module_name': 'PyYAML', 'module_version': '6.0-GCCcore-12.2.0'}, {'full_module_name': 'networkx/3.0-gfbf-2022b', 'module_name': 'networkx', 'module_version': '3.0-gfbf-2022b'}, {'full_module_name': 'MultiQC/1.14-foss-2022b', 'module_name': 'MultiQC', 'module_version': '1.14-foss-2022b'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': "Aggregate results from bioinformatics analyses across many samples into a single report.\n\n MultiQC searches a given directory for analysis logs and compiles an HTML report. It's a general\n use tool, perfect for summarising the output from numerous bioinformatics tools.", 'version': '1.14', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'colormath', 'version': '3.0.0'}, {'type': 'python', 'name': 'spectra', 'version': '0.0.11'}, {'type': 'python', 'name': 'Markdown', 'version': '3.4.1'}, {'type': 'python', 'name': 'lzstring', 'version': '1.0.4'}, {'type': 'python', 'name': 'coloredlogs', 'version': '15.0.1'}, {'type': 'python', 'name': 'mdurl', 'version': '0.1.2'}, {'type': 'python', 'name': 'markdown-it-py', 'version': '2.1.0'}, {'type': 'python', 'name': 'Pygments', 'version': '2.14.0'}, {'type': 'python', 'name': 'rich', 'version': '13.3.1'}, {'type': 'python', 'name': 'commonmark', 'version': '0.9.1'}, {'type': 'python', 'name': 'humanfriendly', 'version': '10.0'}, {'type': 'python', 'name': 'rich-click', 'version': '1.6.1'}, {'type': 'python', 'name': 'multiqc', 'version': '1.14'}]}], 'homepage': 'https://multiqc.info', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': "Aggregate results from bioinformatics analyses across many samples into a single report.\n\n MultiQC searches a given directory for analysis logs and compiles an HTML report. It's a general\n use tool, perfect for summarising the output from numerous bioinformatics tools."} installations


### coloredlogs


|`coloredlogs` version|MultiQC modules that include it|
| --- | --- |
|15.0.1|`MultiQC/1.14-foss-2022b`|

### colormath


|`colormath` version|MultiQC modules that include it|
| --- | --- |
|3.0.0|`MultiQC/1.14-foss-2022b`|

### commonmark


|`commonmark` version|MultiQC modules that include it|
| --- | --- |
|0.9.1|`MultiQC/1.14-foss-2022b`|

### humanfriendly


|`humanfriendly` version|MultiQC modules that include it|
| --- | --- |
|10.0|`MultiQC/1.14-foss-2022b`|

### lzstring


|`lzstring` version|MultiQC modules that include it|
| --- | --- |
|1.0.4|`MultiQC/1.14-foss-2022b`|

### Markdown


|`Markdown` version|MultiQC modules that include it|
| --- | --- |
|3.4.1|`MultiQC/1.14-foss-2022b`|

### markdown-it-py


|`markdown-it-py` version|MultiQC modules that include it|
| --- | --- |
|2.1.0|`MultiQC/1.14-foss-2022b`|

### mdurl


|`mdurl` version|MultiQC modules that include it|
| --- | --- |
|0.1.2|`MultiQC/1.14-foss-2022b`|

### multiqc


|`multiqc` version|MultiQC modules that include it|
| --- | --- |
|1.14|`MultiQC/1.14-foss-2022b`|

### Pygments


|`Pygments` version|MultiQC modules that include it|
| --- | --- |
|2.14.0|`MultiQC/1.14-foss-2022b`|

### rich


|`rich` version|MultiQC modules that include it|
| --- | --- |
|13.3.1|`MultiQC/1.14-foss-2022b`|

### rich-click


|`rich-click` version|MultiQC modules that include it|
| --- | --- |
|1.6.1|`MultiQC/1.14-foss-2022b`|

### spectra


|`spectra` version|MultiQC modules that include it|
| --- | --- |
|0.0.11|`MultiQC/1.14-foss-2022b`|