# snakemake


The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.

<small>homepage: </small><span class="software-link">[https://snakemake.readthedocs.io](https://snakemake.readthedocs.io)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|8.28.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`snakemake/8.28.0-foss-2023b`|
|8.4.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`snakemake/8.4.2-foss-2023a`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://snakemake.readthedocs.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023b'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'snakemake/8.28.0-foss-2023b', 'module_name': 'snakemake', 'module_version': '8.28.0-foss-2023b'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'GCC/13.2.0', 'module_name': 'GCC', 'module_version': '13.2.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-13.2.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-13.2.0'}, {'full_module_name': 'libxml2/2.11.5-GCCcore-13.2.0', 'module_name': 'libxml2', 'module_version': '2.11.5-GCCcore-13.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-13.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-13.2.0'}, {'full_module_name': 'hwloc/2.9.2-GCCcore-13.2.0', 'module_name': 'hwloc', 'module_version': '2.9.2-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.2.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.2.0'}, {'full_module_name': 'UCX/1.15.0-GCCcore-13.2.0', 'module_name': 'UCX', 'module_version': '1.15.0-GCCcore-13.2.0'}, {'full_module_name': 'libfabric/1.19.0-GCCcore-13.2.0', 'module_name': 'libfabric', 'module_version': '1.19.0-GCCcore-13.2.0'}, {'full_module_name': 'PMIx/4.2.6-GCCcore-13.2.0', 'module_name': 'PMIx', 'module_version': '4.2.6-GCCcore-13.2.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-13.2.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-13.2.0'}, {'full_module_name': 'OpenMPI/4.1.6-GCC-13.2.0', 'module_name': 'OpenMPI', 'module_version': '4.1.6-GCC-13.2.0'}, {'full_module_name': 'OpenBLAS/0.3.24-GCC-13.2.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.24-GCC-13.2.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-13.2.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-13.2.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.2.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.2.0'}, {'full_module_name': 'gompi/2023b', 'module_name': 'gompi', 'module_version': '2023b'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023b', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023b'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023b-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023b-fb'}, {'full_module_name': 'foss/2023b', 'module_name': 'foss', 'module_version': '2023b'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'gfbf/2023b', 'module_name': 'gfbf', 'module_version': '2023b'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-13.2.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-13.2.0'}, {'full_module_name': 'SciPy-bundle/2023.11-gfbf-2023b', 'module_name': 'SciPy-bundle', 'module_version': '2023.11-gfbf-2023b'}, {'full_module_name': 'cURL/8.3.0-GCCcore-13.2.0', 'module_name': 'cURL', 'module_version': '8.3.0-GCCcore-13.2.0'}, {'full_module_name': 'expat/2.5.0-GCCcore-13.2.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-13.2.0'}, {'full_module_name': 'Perl/5.38.0-GCCcore-13.2.0', 'module_name': 'Perl', 'module_version': '5.38.0-GCCcore-13.2.0'}, {'full_module_name': 'git/2.42.0-GCCcore-13.2.0', 'module_name': 'git', 'module_version': '2.42.0-GCCcore-13.2.0'}, {'full_module_name': 'GitPython/3.1.42-GCCcore-13.2.0', 'module_name': 'GitPython', 'module_version': '3.1.42-GCCcore-13.2.0'}, {'full_module_name': 'OpenPGM/5.2.122-GCCcore-13.2.0', 'module_name': 'OpenPGM', 'module_version': '5.2.122-GCCcore-13.2.0'}, {'full_module_name': 'libsodium/1.0.19-GCCcore-13.2.0', 'module_name': 'libsodium', 'module_version': '1.0.19-GCCcore-13.2.0'}, {'full_module_name': 'ZeroMQ/4.3.5-GCCcore-13.2.0', 'module_name': 'ZeroMQ', 'module_version': '4.3.5-GCCcore-13.2.0'}, {'full_module_name': 'libxslt/1.1.38-GCCcore-13.2.0', 'module_name': 'libxslt', 'module_version': '1.1.38-GCCcore-13.2.0'}, {'full_module_name': 'lxml/4.9.3-GCCcore-13.2.0', 'module_name': 'lxml', 'module_version': '4.9.3-GCCcore-13.2.0'}, {'full_module_name': 'jedi/0.19.1-GCCcore-13.2.0', 'module_name': 'jedi', 'module_version': '0.19.1-GCCcore-13.2.0'}, {'full_module_name': 'IPython/8.17.2-GCCcore-13.2.0', 'module_name': 'IPython', 'module_version': '8.17.2-GCCcore-13.2.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.2.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.2.0'}, {'full_module_name': 'PyYAML/6.0.1-GCCcore-13.2.0', 'module_name': 'PyYAML', 'module_version': '6.0.1-GCCcore-13.2.0'}, {'full_module_name': 'GMP/6.3.0-GCCcore-13.2.0', 'module_name': 'GMP', 'module_version': '6.3.0-GCCcore-13.2.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-13.2.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-13.2.0'}, {'full_module_name': 'METIS/5.1.0-GCCcore-13.2.0', 'module_name': 'METIS', 'module_version': '5.1.0-GCCcore-13.2.0'}, {'full_module_name': 'SCOTCH/7.0.4-gompi-2023b', 'module_name': 'SCOTCH', 'module_version': '7.0.4-gompi-2023b'}, {'full_module_name': 'MUMPS/5.6.1-foss-2023b-metis', 'module_name': 'MUMPS', 'module_version': '5.6.1-foss-2023b-metis'}, {'full_module_name': 'CoinUtils/2.11.10-GCC-13.2.0', 'module_name': 'CoinUtils', 'module_version': '2.11.10-GCC-13.2.0'}, {'full_module_name': 'Osi/0.108.9-GCC-13.2.0', 'module_name': 'Osi', 'module_version': '0.108.9-GCC-13.2.0'}, {'full_module_name': 'Clp/1.17.9-foss-2023b', 'module_name': 'Clp', 'module_version': '1.17.9-foss-2023b'}, {'full_module_name': 'Cgl/0.60.8-foss-2023b', 'module_name': 'Cgl', 'module_version': '0.60.8-foss-2023b'}, {'full_module_name': 'Cbc/2.10.11-foss-2023b', 'module_name': 'Cbc', 'module_version': '2.10.11-foss-2023b'}, {'full_module_name': 'PuLP/2.8.0-foss-2023b', 'module_name': 'PuLP', 'module_version': '2.8.0-foss-2023b'}, {'full_module_name': 'snakemake/8.28.0-foss-2023b', 'module_name': 'snakemake', 'module_version': '8.28.0-foss-2023b'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.', 'version': '8.28.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'wrapt', 'version': '1.16.0'}, {'type': 'python', 'name': 'datrie', 'version': '0.8.2'}, {'type': 'python', 'name': 'plac', 'version': '1.4.3'}, {'type': 'python', 'name': 'dpath', 'version': '2.2.0'}, {'type': 'python', 'name': 'yte', 'version': '1.5.5'}, {'type': 'python', 'name': 'toposort', 'version': '1.10'}, {'type': 'python', 'name': 'throttler', 'version': '1.2.2'}, {'type': 'python', 'name': 'stopit', 'version': '1.1.2'}, {'type': 'python', 'name': 'ConfigArgParse', 'version': '1.7'}, {'type': 'python', 'name': 'argparse-dataclass', 'version': '2.0.0'}, {'type': 'python', 'name': 'snakemake-interface-common', 'version': '1.17.4'}, {'type': 'python', 'name': 'reretry', 'version': '0.11.8'}, {'type': 'python', 'name': 'snakemake-interface-storage-plugins', 'version': '3.3.0'}, {'type': 'python', 'name': 'snakemake-interface-report-plugins', 'version': '1.1.0'}, {'type': 'python', 'name': 'snakemake-interface-executor-plugins', 'version': '9.3.3'}, {'type': 'python', 'name': 'smart-open', 'version': '7.1.0'}, {'type': 'python', 'name': 'jupyter-core', 'version': '5.7.2'}, {'type': 'python', 'name': 'fastjsonschema', 'version': '2.19.1'}, {'type': 'python', 'name': 'nbformat', 'version': '5.10.4'}, {'type': 'python', 'name': 'immutables', 'version': '0.21'}, {'type': 'python', 'name': 'humanfriendly', 'version': '10.0'}, {'type': 'python', 'name': 'connection-pool', 'version': '0.0.3'}, {'type': 'python', 'name': 'conda-inject', 'version': '1.3.2'}, {'type': 'python', 'name': 'snakemake', 'version': '8.28.0'}, {'type': 'python', 'name': 'snakemake-executor-plugin-slurm-jobstep', 'version': '0.2.1'}, {'type': 'python', 'name': 'snakemake-executor-plugin-flux', 'version': '0.1.1'}, {'type': 'python', 'name': 'snakemake-executor-plugin-slurm', 'version': '0.12.0'}, {'type': 'python', 'name': 'snakemake-executor-plugin-cluster-sync', 'version': '0.1.4'}, {'type': 'python', 'name': 'snakemake-executor-plugin-cluster-generic', 'version': '1.0.9'}]}, {'homepage': 'https://snakemake.readthedocs.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023a'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'snakemake/8.4.2-foss-2023a', 'module_name': 'snakemake', 'module_version': '8.4.2-foss-2023a'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.3.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.3.0'}, {'full_module_name': 'libxml2/2.11.4-GCCcore-12.3.0', 'module_name': 'libxml2', 'module_version': '2.11.4-GCCcore-12.3.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.3.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.3.0'}, {'full_module_name': 'hwloc/2.9.1-GCCcore-12.3.0', 'module_name': 'hwloc', 'module_version': '2.9.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.3.0'}, {'full_module_name': 'UCX/1.14.1-GCCcore-12.3.0', 'module_name': 'UCX', 'module_version': '1.14.1-GCCcore-12.3.0'}, {'full_module_name': 'libfabric/1.18.0-GCCcore-12.3.0', 'module_name': 'libfabric', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'PMIx/4.2.4-GCCcore-12.3.0', 'module_name': 'PMIx', 'module_version': '4.2.4-GCCcore-12.3.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-12.3.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenMPI/4.1.5-GCC-12.3.0', 'module_name': 'OpenMPI', 'module_version': '4.1.5-GCC-12.3.0'}, {'full_module_name': 'OpenBLAS/0.3.23-GCC-12.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.23-GCC-12.3.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-12.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-12.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.3.0'}, {'full_module_name': 'gompi/2023a', 'module_name': 'gompi', 'module_version': '2023a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023a-fb'}, {'full_module_name': 'foss/2023a', 'module_name': 'foss', 'module_version': '2023a'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'gfbf/2023a', 'module_name': 'gfbf', 'module_version': '2023a'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-12.3.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-12.3.0'}, {'full_module_name': 'SciPy-bundle/2023.07-gfbf-2023a', 'module_name': 'SciPy-bundle', 'module_version': '2023.07-gfbf-2023a'}, {'full_module_name': 'cURL/8.0.1-GCCcore-12.3.0', 'module_name': 'cURL', 'module_version': '8.0.1-GCCcore-12.3.0'}, {'full_module_name': 'expat/2.5.0-GCCcore-12.3.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'Perl/5.36.1-GCCcore-12.3.0', 'module_name': 'Perl', 'module_version': '5.36.1-GCCcore-12.3.0'}, {'full_module_name': 'git/2.41.0-GCCcore-12.3.0-nodocs', 'module_name': 'git', 'module_version': '2.41.0-GCCcore-12.3.0-nodocs'}, {'full_module_name': 'GitPython/3.1.40-GCCcore-12.3.0', 'module_name': 'GitPython', 'module_version': '3.1.40-GCCcore-12.3.0'}, {'full_module_name': 'OpenPGM/5.2.122-GCCcore-12.3.0', 'module_name': 'OpenPGM', 'module_version': '5.2.122-GCCcore-12.3.0'}, {'full_module_name': 'libsodium/1.0.18-GCCcore-12.3.0', 'module_name': 'libsodium', 'module_version': '1.0.18-GCCcore-12.3.0'}, {'full_module_name': 'ZeroMQ/4.3.4-GCCcore-12.3.0', 'module_name': 'ZeroMQ', 'module_version': '4.3.4-GCCcore-12.3.0'}, {'full_module_name': 'libxslt/1.1.38-GCCcore-12.3.0', 'module_name': 'libxslt', 'module_version': '1.1.38-GCCcore-12.3.0'}, {'full_module_name': 'lxml/4.9.2-GCCcore-12.3.0', 'module_name': 'lxml', 'module_version': '4.9.2-GCCcore-12.3.0'}, {'full_module_name': 'hatchling/1.18.0-GCCcore-12.3.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'BeautifulSoup/4.12.2-GCCcore-12.3.0', 'module_name': 'BeautifulSoup', 'module_version': '4.12.2-GCCcore-12.3.0'}, {'full_module_name': 'IPython/8.14.0-GCCcore-12.3.0', 'module_name': 'IPython', 'module_version': '8.14.0-GCCcore-12.3.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-12.3.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-12.3.0'}, {'full_module_name': 'PyYAML/6.0-GCCcore-12.3.0', 'module_name': 'PyYAML', 'module_version': '6.0-GCCcore-12.3.0'}, {'full_module_name': 'wrapt/1.15.0-gfbf-2023a', 'module_name': 'wrapt', 'module_version': '1.15.0-gfbf-2023a'}, {'full_module_name': 'GMP/6.2.1-GCCcore-12.3.0', 'module_name': 'GMP', 'module_version': '6.2.1-GCCcore-12.3.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-12.3.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-12.3.0'}, {'full_module_name': 'METIS/5.1.0-GCCcore-12.3.0', 'module_name': 'METIS', 'module_version': '5.1.0-GCCcore-12.3.0'}, {'full_module_name': 'SCOTCH/7.0.3-gompi-2023a', 'module_name': 'SCOTCH', 'module_version': '7.0.3-gompi-2023a'}, {'full_module_name': 'MUMPS/5.6.1-foss-2023a-metis', 'module_name': 'MUMPS', 'module_version': '5.6.1-foss-2023a-metis'}, {'full_module_name': 'CoinUtils/2.11.10-GCC-12.3.0', 'module_name': 'CoinUtils', 'module_version': '2.11.10-GCC-12.3.0'}, {'full_module_name': 'Osi/0.108.9-GCC-12.3.0', 'module_name': 'Osi', 'module_version': '0.108.9-GCC-12.3.0'}, {'full_module_name': 'Clp/1.17.9-foss-2023a', 'module_name': 'Clp', 'module_version': '1.17.9-foss-2023a'}, {'full_module_name': 'Cgl/0.60.8-foss-2023a', 'module_name': 'Cgl', 'module_version': '0.60.8-foss-2023a'}, {'full_module_name': 'Cbc/2.10.11-foss-2023a', 'module_name': 'Cbc', 'module_version': '2.10.11-foss-2023a'}, {'full_module_name': 'PuLP/2.8.0-foss-2023a', 'module_name': 'PuLP', 'module_version': '2.8.0-foss-2023a'}, {'full_module_name': 'snakemake/8.4.2-foss-2023a', 'module_name': 'snakemake', 'module_version': '8.4.2-foss-2023a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.', 'version': '8.4.2', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'datrie', 'version': '0.8.2'}, {'type': 'python', 'name': 'plac', 'version': '1.4.2'}, {'type': 'python', 'name': 'dpath', 'version': '2.1.6'}, {'type': 'python', 'name': 'yte', 'version': '1.5.4'}, {'type': 'python', 'name': 'toposort', 'version': '1.10'}, {'type': 'python', 'name': 'throttler', 'version': '1.2.2'}, {'type': 'python', 'name': 'stopit', 'version': '1.1.2'}, {'type': 'python', 'name': 'ConfigArgParse', 'version': '1.7'}, {'type': 'python', 'name': 'argparse-dataclass', 'version': '2.0.0'}, {'type': 'python', 'name': 'snakemake-interface-common', 'version': '1.15.2'}, {'type': 'python', 'name': 'reretry', 'version': '0.11.8'}, {'type': 'python', 'name': 'snakemake-interface-storage-plugins', 'version': '3.0.0'}, {'type': 'python', 'name': 'snakemake-interface-executor-plugins', 'version': '8.2.0'}, {'type': 'python', 'name': 'smart-open', 'version': '6.4.0'}, {'type': 'python', 'name': 'jupyter-core', 'version': '5.7.1'}, {'type': 'python', 'name': 'fastjsonschema', 'version': '2.19.1'}, {'type': 'python', 'name': 'nbformat', 'version': '5.9.2'}, {'type': 'python', 'name': 'immutables', 'version': '0.20'}, {'type': 'python', 'name': 'humanfriendly', 'version': '10.0'}, {'type': 'python', 'name': 'connection-pool', 'version': '0.0.3'}, {'type': 'python', 'name': 'conda-inject', 'version': '1.3.1'}, {'type': 'python', 'name': 'snakemake', 'version': '8.4.2'}, {'type': 'python', 'name': 'snakemake-executor-plugin-slurm-jobstep', 'version': '0.1.10'}, {'type': 'python', 'name': 'snakemake-executor-plugin-flux', 'version': '0.1.0'}, {'type': 'python', 'name': 'snakemake-executor-plugin-slurm', 'version': '0.2.1'}, {'type': 'python', 'name': 'snakemake-executor-plugin-cluster-sync', 'version': '0.1.3'}, {'type': 'python', 'name': 'snakemake-executor-plugin-cluster-generic', 'version': '1.0.7'}]}], 'homepage': 'https://snakemake.readthedocs.io', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.'} installations


### argparse-dataclass


|`argparse-dataclass` version|snakemake modules that include it|
| --- | --- |
|2.0.0|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### conda-inject


|`conda-inject` version|snakemake modules that include it|
| --- | --- |
|1.3.1|`snakemake/8.4.2-foss-2023a`|
|1.3.2|`snakemake/8.28.0-foss-2023b`|

### ConfigArgParse


|`ConfigArgParse` version|snakemake modules that include it|
| --- | --- |
|1.7|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### connection-pool


|`connection-pool` version|snakemake modules that include it|
| --- | --- |
|0.0.3|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### datrie


|`datrie` version|snakemake modules that include it|
| --- | --- |
|0.8.2|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### dpath


|`dpath` version|snakemake modules that include it|
| --- | --- |
|2.1.6|`snakemake/8.4.2-foss-2023a`|
|2.2.0|`snakemake/8.28.0-foss-2023b`|

### fastjsonschema


|`fastjsonschema` version|snakemake modules that include it|
| --- | --- |
|2.19.1|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### humanfriendly


|`humanfriendly` version|snakemake modules that include it|
| --- | --- |
|10.0|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### immutables


|`immutables` version|snakemake modules that include it|
| --- | --- |
|0.20|`snakemake/8.4.2-foss-2023a`|
|0.21|`snakemake/8.28.0-foss-2023b`|

### jupyter-core


|`jupyter-core` version|snakemake modules that include it|
| --- | --- |
|5.7.1|`snakemake/8.4.2-foss-2023a`|
|5.7.2|`snakemake/8.28.0-foss-2023b`|

### nbformat


|`nbformat` version|snakemake modules that include it|
| --- | --- |
|5.10.4|`snakemake/8.28.0-foss-2023b`|
|5.9.2|`snakemake/8.4.2-foss-2023a`|

### plac


|`plac` version|snakemake modules that include it|
| --- | --- |
|1.4.2|`snakemake/8.4.2-foss-2023a`|
|1.4.3|`snakemake/8.28.0-foss-2023b`|

### reretry


|`reretry` version|snakemake modules that include it|
| --- | --- |
|0.11.8|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### smart-open


|`smart-open` version|snakemake modules that include it|
| --- | --- |
|6.4.0|`snakemake/8.4.2-foss-2023a`|
|7.1.0|`snakemake/8.28.0-foss-2023b`|

### snakemake


|`snakemake` version|snakemake modules that include it|
| --- | --- |
|8.28.0|`snakemake/8.28.0-foss-2023b`|
|8.4.2|`snakemake/8.4.2-foss-2023a`|

### snakemake-executor-plugin-cluster-generic


|`snakemake-executor-plugin-cluster-generic` version|snakemake modules that include it|
| --- | --- |
|1.0.7|`snakemake/8.4.2-foss-2023a`|
|1.0.9|`snakemake/8.28.0-foss-2023b`|

### snakemake-executor-plugin-cluster-sync


|`snakemake-executor-plugin-cluster-sync` version|snakemake modules that include it|
| --- | --- |
|0.1.3|`snakemake/8.4.2-foss-2023a`|
|0.1.4|`snakemake/8.28.0-foss-2023b`|

### snakemake-executor-plugin-flux


|`snakemake-executor-plugin-flux` version|snakemake modules that include it|
| --- | --- |
|0.1.0|`snakemake/8.4.2-foss-2023a`|
|0.1.1|`snakemake/8.28.0-foss-2023b`|

### snakemake-executor-plugin-slurm


|`snakemake-executor-plugin-slurm` version|snakemake modules that include it|
| --- | --- |
|0.12.0|`snakemake/8.28.0-foss-2023b`|
|0.2.1|`snakemake/8.4.2-foss-2023a`|

### snakemake-executor-plugin-slurm-jobstep


|`snakemake-executor-plugin-slurm-jobstep` version|snakemake modules that include it|
| --- | --- |
|0.1.10|`snakemake/8.4.2-foss-2023a`|
|0.2.1|`snakemake/8.28.0-foss-2023b`|

### snakemake-interface-common


|`snakemake-interface-common` version|snakemake modules that include it|
| --- | --- |
|1.15.2|`snakemake/8.4.2-foss-2023a`|
|1.17.4|`snakemake/8.28.0-foss-2023b`|

### snakemake-interface-executor-plugins


|`snakemake-interface-executor-plugins` version|snakemake modules that include it|
| --- | --- |
|8.2.0|`snakemake/8.4.2-foss-2023a`|
|9.3.3|`snakemake/8.28.0-foss-2023b`|

### snakemake-interface-report-plugins


|`snakemake-interface-report-plugins` version|snakemake modules that include it|
| --- | --- |
|1.1.0|`snakemake/8.28.0-foss-2023b`|

### snakemake-interface-storage-plugins


|`snakemake-interface-storage-plugins` version|snakemake modules that include it|
| --- | --- |
|3.0.0|`snakemake/8.4.2-foss-2023a`|
|3.3.0|`snakemake/8.28.0-foss-2023b`|

### stopit


|`stopit` version|snakemake modules that include it|
| --- | --- |
|1.1.2|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### throttler


|`throttler` version|snakemake modules that include it|
| --- | --- |
|1.2.2|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### toposort


|`toposort` version|snakemake modules that include it|
| --- | --- |
|1.10|`snakemake/8.28.0-foss-2023b`<br/>`snakemake/8.4.2-foss-2023a`|

### wrapt


|`wrapt` version|snakemake modules that include it|
| --- | --- |
|1.16.0|`snakemake/8.28.0-foss-2023b`|

### yte


|`yte` version|snakemake modules that include it|
| --- | --- |
|1.5.4|`snakemake/8.4.2-foss-2023a`|
|1.5.5|`snakemake/8.28.0-foss-2023b`|