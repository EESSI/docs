# MLflow


MLflow is a platform to streamline machine learning development, including tracking experiments,
packaging code into reproducible runs, and sharing and deploying models.

<small>homepage: </small><span class="software-link">[https://mlflow.org](https://mlflow.org)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.10.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MLflow/2.10.2-gfbf-2023a`|
|2.18.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MLflow/2.18.0-gfbf-2023b`|
|2.22.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MLflow/2.22.4-gfbf-2024a`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://mlflow.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'gfbf', 'version': '2023a'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'MLflow/2.10.2-gfbf-2023a', 'module_name': 'MLflow', 'module_version': '2.10.2-gfbf-2023a'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'OpenBLAS/0.3.23-GCC-12.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.23-GCC-12.3.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-12.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-12.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.3.0'}, {'full_module_name': 'gfbf/2023a', 'module_name': 'gfbf', 'module_version': '2023a'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'cURL/8.0.1-GCCcore-12.3.0', 'module_name': 'cURL', 'module_version': '8.0.1-GCCcore-12.3.0'}, {'full_module_name': 'expat/2.5.0-GCCcore-12.3.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'Perl/5.36.1-GCCcore-12.3.0', 'module_name': 'Perl', 'module_version': '5.36.1-GCCcore-12.3.0'}, {'full_module_name': 'git/2.41.0-GCCcore-12.3.0-nodocs', 'module_name': 'git', 'module_version': '2.41.0-GCCcore-12.3.0-nodocs'}, {'full_module_name': 'GitPython/3.1.40-GCCcore-12.3.0', 'module_name': 'GitPython', 'module_version': '3.1.40-GCCcore-12.3.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-12.3.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-12.3.0'}, {'full_module_name': 'SciPy-bundle/2023.07-gfbf-2023a', 'module_name': 'SciPy-bundle', 'module_version': '2023.07-gfbf-2023a'}, {'full_module_name': 'libpng/1.6.39-GCCcore-12.3.0', 'module_name': 'libpng', 'module_version': '1.6.39-GCCcore-12.3.0'}, {'full_module_name': 'Brotli/1.0.9-GCCcore-12.3.0', 'module_name': 'Brotli', 'module_version': '1.0.9-GCCcore-12.3.0'}, {'full_module_name': 'freetype/2.13.0-GCCcore-12.3.0', 'module_name': 'freetype', 'module_version': '2.13.0-GCCcore-12.3.0'}, {'full_module_name': 'fontconfig/2.14.2-GCCcore-12.3.0', 'module_name': 'fontconfig', 'module_version': '2.14.2-GCCcore-12.3.0'}, {'full_module_name': 'xorg-macros/1.20.0-GCCcore-12.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.0-GCCcore-12.3.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.3.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.3.0'}, {'full_module_name': 'X11/20230603-GCCcore-12.3.0', 'module_name': 'X11', 'module_version': '20230603-GCCcore-12.3.0'}, {'full_module_name': 'Tk/8.6.13-GCCcore-12.3.0', 'module_name': 'Tk', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'Tkinter/3.11.3-GCCcore-12.3.0', 'module_name': 'Tkinter', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'NASM/2.16.01-GCCcore-12.3.0', 'module_name': 'NASM', 'module_version': '2.16.01-GCCcore-12.3.0'}, {'full_module_name': 'libjpeg-turbo/2.1.5.1-GCCcore-12.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '2.1.5.1-GCCcore-12.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-12.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-12.3.0'}, {'full_module_name': 'gzip/1.12-GCCcore-12.3.0', 'module_name': 'gzip', 'module_version': '1.12-GCCcore-12.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-12.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-12.3.0'}, {'full_module_name': 'zstd/1.5.5-GCCcore-12.3.0', 'module_name': 'zstd', 'module_version': '1.5.5-GCCcore-12.3.0'}, {'full_module_name': 'libdeflate/1.18-GCCcore-12.3.0', 'module_name': 'libdeflate', 'module_version': '1.18-GCCcore-12.3.0'}, {'full_module_name': 'LibTIFF/4.5.0-GCCcore-12.3.0', 'module_name': 'LibTIFF', 'module_version': '4.5.0-GCCcore-12.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-12.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-12.3.0'}, {'full_module_name': 'libwebp/1.3.1-GCCcore-12.3.0', 'module_name': 'libwebp', 'module_version': '1.3.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-12.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'LittleCMS/2.15-GCCcore-12.3.0', 'module_name': 'LittleCMS', 'module_version': '2.15-GCCcore-12.3.0'}, {'full_module_name': 'Pillow/10.0.0-GCCcore-12.3.0', 'module_name': 'Pillow', 'module_version': '10.0.0-GCCcore-12.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-12.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-12.3.0'}, {'full_module_name': 'Ninja/1.11.1-GCCcore-12.3.0', 'module_name': 'Ninja', 'module_version': '1.11.1-GCCcore-12.3.0'}, {'full_module_name': 'Meson/1.1.1-GCCcore-12.3.0', 'module_name': 'Meson', 'module_version': '1.1.1-GCCcore-12.3.0'}, {'full_module_name': 'meson-python/0.13.2-GCCcore-12.3.0', 'module_name': 'meson-python', 'module_version': '0.13.2-GCCcore-12.3.0'}, {'full_module_name': 'matplotlib/3.7.2-gfbf-2023a', 'module_name': 'matplotlib', 'module_version': '3.7.2-gfbf-2023a'}, {'full_module_name': 'scikit-learn/1.3.1-gfbf-2023a', 'module_name': 'scikit-learn', 'module_version': '1.3.1-gfbf-2023a'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-12.3.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-12.3.0'}, {'full_module_name': 'PyYAML/6.0-GCCcore-12.3.0', 'module_name': 'PyYAML', 'module_version': '6.0-GCCcore-12.3.0'}, {'full_module_name': 'PostgreSQL/16.1-GCCcore-12.3.0', 'module_name': 'PostgreSQL', 'module_version': '16.1-GCCcore-12.3.0'}, {'full_module_name': 'psycopg2/2.9.9-GCCcore-12.3.0', 'module_name': 'psycopg2', 'module_version': '2.9.9-GCCcore-12.3.0'}, {'full_module_name': 'Mako/1.2.4-GCCcore-12.3.0', 'module_name': 'Mako', 'module_version': '1.2.4-GCCcore-12.3.0'}, {'full_module_name': 'SQLAlchemy/2.0.25-GCCcore-12.3.0', 'module_name': 'SQLAlchemy', 'module_version': '2.0.25-GCCcore-12.3.0'}, {'full_module_name': 'Abseil/20230125.3-GCCcore-12.3.0', 'module_name': 'Abseil', 'module_version': '20230125.3-GCCcore-12.3.0'}, {'full_module_name': 'protobuf/24.0-GCCcore-12.3.0', 'module_name': 'protobuf', 'module_version': '24.0-GCCcore-12.3.0'}, {'full_module_name': 'protobuf-python/4.24.0-GCCcore-12.3.0', 'module_name': 'protobuf-python', 'module_version': '4.24.0-GCCcore-12.3.0'}, {'full_module_name': 'Flask/2.3.3-GCCcore-12.3.0', 'module_name': 'Flask', 'module_version': '2.3.3-GCCcore-12.3.0'}, {'full_module_name': 'ICU/73.2-GCCcore-12.3.0', 'module_name': 'ICU', 'module_version': '73.2-GCCcore-12.3.0'}, {'full_module_name': 'Boost/1.82.0-GCC-12.3.0', 'module_name': 'Boost', 'module_version': '1.82.0-GCC-12.3.0'}, {'full_module_name': 'snappy/1.1.10-GCCcore-12.3.0', 'module_name': 'snappy', 'module_version': '1.1.10-GCCcore-12.3.0'}, {'full_module_name': 'RapidJSON/1.1.0-20230928-GCCcore-12.3.0', 'module_name': 'RapidJSON', 'module_version': '1.1.0-20230928-GCCcore-12.3.0'}, {'full_module_name': 'RE2/2023-08-01-GCCcore-12.3.0', 'module_name': 'RE2', 'module_version': '2023-08-01-GCCcore-12.3.0'}, {'full_module_name': 'utf8proc/2.8.0-GCCcore-12.3.0', 'module_name': 'utf8proc', 'module_version': '2.8.0-GCCcore-12.3.0'}, {'full_module_name': 'Arrow/14.0.1-gfbf-2023a', 'module_name': 'Arrow', 'module_version': '14.0.1-gfbf-2023a'}, {'full_module_name': 'MLflow/2.10.2-gfbf-2023a', 'module_name': 'MLflow', 'module_version': '2.10.2-gfbf-2023a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'MLflow is a platform to streamline machine learning development, including tracking experiments,\npackaging code into reproducible runs, and sharing and deploying models.', 'version': '2.10.2', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'docker', 'version': '7.0.0'}, {'type': 'python', 'name': 'entrypoints', 'version': '0.4'}, {'type': 'python', 'name': 'gunicorn', 'version': '21.2.0'}, {'type': 'python', 'name': 'Markdown', 'version': '3.5.2'}, {'type': 'python', 'name': 'querystring_parser', 'version': '1.2.4'}, {'type': 'python', 'name': 'sqlparse', 'version': '0.4.4'}, {'type': 'python', 'name': 'mlflow', 'version': '2.10.2'}]}, {'homepage': 'https://mlflow.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'gfbf', 'version': '2023b'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'MLflow/2.18.0-gfbf-2023b', 'module_name': 'MLflow', 'module_version': '2.18.0-gfbf-2023b'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'GCC/13.2.0', 'module_name': 'GCC', 'module_version': '13.2.0'}, {'full_module_name': 'OpenBLAS/0.3.24-GCC-13.2.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.24-GCC-13.2.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-13.2.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-13.2.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.2.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.2.0'}, {'full_module_name': 'gfbf/2023b', 'module_name': 'gfbf', 'module_version': '2023b'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'cURL/8.3.0-GCCcore-13.2.0', 'module_name': 'cURL', 'module_version': '8.3.0-GCCcore-13.2.0'}, {'full_module_name': 'expat/2.5.0-GCCcore-13.2.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-13.2.0'}, {'full_module_name': 'Perl/5.38.0-GCCcore-13.2.0', 'module_name': 'Perl', 'module_version': '5.38.0-GCCcore-13.2.0'}, {'full_module_name': 'git/2.42.0-GCCcore-13.2.0', 'module_name': 'git', 'module_version': '2.42.0-GCCcore-13.2.0'}, {'full_module_name': 'GitPython/3.1.42-GCCcore-13.2.0', 'module_name': 'GitPython', 'module_version': '3.1.42-GCCcore-13.2.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-13.2.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-13.2.0'}, {'full_module_name': 'SciPy-bundle/2023.11-gfbf-2023b', 'module_name': 'SciPy-bundle', 'module_version': '2023.11-gfbf-2023b'}, {'full_module_name': 'libpng/1.6.40-GCCcore-13.2.0', 'module_name': 'libpng', 'module_version': '1.6.40-GCCcore-13.2.0'}, {'full_module_name': 'Brotli/1.1.0-GCCcore-13.2.0', 'module_name': 'Brotli', 'module_version': '1.1.0-GCCcore-13.2.0'}, {'full_module_name': 'freetype/2.13.2-GCCcore-13.2.0', 'module_name': 'freetype', 'module_version': '2.13.2-GCCcore-13.2.0'}, {'full_module_name': 'fontconfig/2.14.2-GCCcore-13.2.0', 'module_name': 'fontconfig', 'module_version': '2.14.2-GCCcore-13.2.0'}, {'full_module_name': 'xorg-macros/1.20.0-GCCcore-13.2.0', 'module_name': 'xorg-macros', 'module_version': '1.20.0-GCCcore-13.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-13.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-13.2.0'}, {'full_module_name': 'X11/20231019-GCCcore-13.2.0', 'module_name': 'X11', 'module_version': '20231019-GCCcore-13.2.0'}, {'full_module_name': 'Tk/8.6.13-GCCcore-13.2.0', 'module_name': 'Tk', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'Tkinter/3.11.5-GCCcore-13.2.0', 'module_name': 'Tkinter', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'NASM/2.16.01-GCCcore-13.2.0', 'module_name': 'NASM', 'module_version': '2.16.01-GCCcore-13.2.0'}, {'full_module_name': 'libjpeg-turbo/3.0.1-GCCcore-13.2.0', 'module_name': 'libjpeg-turbo', 'module_version': '3.0.1-GCCcore-13.2.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-13.2.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-13.2.0'}, {'full_module_name': 'gzip/1.13-GCCcore-13.2.0', 'module_name': 'gzip', 'module_version': '1.13-GCCcore-13.2.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-13.2.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-13.2.0'}, {'full_module_name': 'zstd/1.5.5-GCCcore-13.2.0', 'module_name': 'zstd', 'module_version': '1.5.5-GCCcore-13.2.0'}, {'full_module_name': 'libdeflate/1.19-GCCcore-13.2.0', 'module_name': 'libdeflate', 'module_version': '1.19-GCCcore-13.2.0'}, {'full_module_name': 'LibTIFF/4.6.0-GCCcore-13.2.0', 'module_name': 'LibTIFF', 'module_version': '4.6.0-GCCcore-13.2.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-13.2.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-13.2.0'}, {'full_module_name': 'libwebp/1.3.2-GCCcore-13.2.0', 'module_name': 'libwebp', 'module_version': '1.3.2-GCCcore-13.2.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-13.2.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-13.2.0'}, {'full_module_name': 'LittleCMS/2.15-GCCcore-13.2.0', 'module_name': 'LittleCMS', 'module_version': '2.15-GCCcore-13.2.0'}, {'full_module_name': 'Pillow/10.2.0-GCCcore-13.2.0', 'module_name': 'Pillow', 'module_version': '10.2.0-GCCcore-13.2.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-13.2.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-13.2.0'}, {'full_module_name': 'matplotlib/3.8.2-gfbf-2023b', 'module_name': 'matplotlib', 'module_version': '3.8.2-gfbf-2023b'}, {'full_module_name': 'scikit-learn/1.4.0-gfbf-2023b', 'module_name': 'scikit-learn', 'module_version': '1.4.0-gfbf-2023b'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.2.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.2.0'}, {'full_module_name': 'PyYAML/6.0.1-GCCcore-13.2.0', 'module_name': 'PyYAML', 'module_version': '6.0.1-GCCcore-13.2.0'}, {'full_module_name': 'Greenlet/3.0.3-GCCcore-13.2.0', 'module_name': 'Greenlet', 'module_version': '3.0.3-GCCcore-13.2.0'}, {'full_module_name': 'PostgreSQL/16.1-GCCcore-13.2.0', 'module_name': 'PostgreSQL', 'module_version': '16.1-GCCcore-13.2.0'}, {'full_module_name': 'psycopg/3.1.18-GCCcore-13.2.0', 'module_name': 'psycopg', 'module_version': '3.1.18-GCCcore-13.2.0'}, {'full_module_name': 'Mako/1.2.4-GCCcore-13.2.0', 'module_name': 'Mako', 'module_version': '1.2.4-GCCcore-13.2.0'}, {'full_module_name': 'SQLAlchemy/2.0.29-GCCcore-13.2.0', 'module_name': 'SQLAlchemy', 'module_version': '2.0.29-GCCcore-13.2.0'}, {'full_module_name': 'Abseil/20240116.1-GCCcore-13.2.0', 'module_name': 'Abseil', 'module_version': '20240116.1-GCCcore-13.2.0'}, {'full_module_name': 'protobuf/25.3-GCCcore-13.2.0', 'module_name': 'protobuf', 'module_version': '25.3-GCCcore-13.2.0'}, {'full_module_name': 'protobuf-python/4.25.3-GCCcore-13.2.0', 'module_name': 'protobuf-python', 'module_version': '4.25.3-GCCcore-13.2.0'}, {'full_module_name': 'Flask/3.0.0-GCCcore-13.2.0', 'module_name': 'Flask', 'module_version': '3.0.0-GCCcore-13.2.0'}, {'full_module_name': 'ICU/74.1-GCCcore-13.2.0', 'module_name': 'ICU', 'module_version': '74.1-GCCcore-13.2.0'}, {'full_module_name': 'Boost/1.83.0-GCC-13.2.0', 'module_name': 'Boost', 'module_version': '1.83.0-GCC-13.2.0'}, {'full_module_name': 'snappy/1.1.10-GCCcore-13.2.0', 'module_name': 'snappy', 'module_version': '1.1.10-GCCcore-13.2.0'}, {'full_module_name': 'RapidJSON/1.1.0-20240409-GCCcore-13.2.0', 'module_name': 'RapidJSON', 'module_version': '1.1.0-20240409-GCCcore-13.2.0'}, {'full_module_name': 'RE2/2024-03-01-GCCcore-13.2.0', 'module_name': 'RE2', 'module_version': '2024-03-01-GCCcore-13.2.0'}, {'full_module_name': 'utf8proc/2.9.0-GCCcore-13.2.0', 'module_name': 'utf8proc', 'module_version': '2.9.0-GCCcore-13.2.0'}, {'full_module_name': 'Arrow/16.1.0-gfbf-2023b', 'module_name': 'Arrow', 'module_version': '16.1.0-gfbf-2023b'}, {'full_module_name': 'Markdown/3.6-GCCcore-13.2.0', 'module_name': 'Markdown', 'module_version': '3.6-GCCcore-13.2.0'}, {'full_module_name': 'wrapt/1.16.0-GCCcore-13.2.0', 'module_name': 'wrapt', 'module_version': '1.16.0-GCCcore-13.2.0'}, {'full_module_name': 'Deprecated/1.2.14-GCCcore-13.2.0', 'module_name': 'Deprecated', 'module_version': '1.2.14-GCCcore-13.2.0'}, {'full_module_name': 'MLflow/2.18.0-gfbf-2023b', 'module_name': 'MLflow', 'module_version': '2.18.0-gfbf-2023b'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'MLflow is a platform to streamline machine learning development, including tracking experiments,\npackaging code into reproducible runs, and sharing and deploying models.', 'version': '2.18.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'pyasn1-modules', 'version': '0.4.1'}, {'type': 'python', 'name': 'rsa', 'version': '4.9'}, {'type': 'python', 'name': 'google-auth', 'version': '2.35.0'}, {'type': 'python', 'name': 'sqlparse', 'version': '0.5.1'}, {'type': 'python', 'name': 'opentelemetry_semantic_conventions', 'version': '0.48b0'}, {'type': 'python', 'name': 'opentelemetry_sdk', 'version': '1.27.0'}, {'type': 'python', 'name': 'opentelemetry_api', 'version': '1.27.0'}, {'type': 'python', 'name': 'databricks_sdk', 'version': '0.36.0'}, {'type': 'python', 'name': 'cachetools', 'version': '5.5.0'}, {'type': 'python', 'name': 'graphql-relay', 'version': '3.2.0'}, {'type': 'python', 'name': 'graphql_core', 'version': '3.2.5'}, {'type': 'python', 'name': 'graphene', 'version': '3.4.1'}, {'type': 'python', 'name': 'alembic', 'version': '1.14.0'}, {'type': 'python', 'name': 'docker', 'version': '7.1.0'}, {'type': 'python', 'name': 'gunicorn', 'version': '23.0.0'}, {'type': 'python', 'name': 'mlflow_skinny', 'version': '2.18.0'}, {'type': 'python', 'name': 'mlflow', 'version': '2.18.0'}]}, {'homepage': 'https://mlflow.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'gfbf', 'version': '2024a'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'MLflow/2.22.4-gfbf-2024a', 'module_name': 'MLflow', 'module_version': '2.22.4-gfbf-2024a'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'GCC/13.3.0', 'module_name': 'GCC', 'module_version': '13.3.0'}, {'full_module_name': 'OpenBLAS/0.3.27-GCC-13.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.27-GCC-13.3.0'}, {'full_module_name': 'FlexiBLAS/3.4.4-GCC-13.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.4.4-GCC-13.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.3.0'}, {'full_module_name': 'gfbf/2024a', 'module_name': 'gfbf', 'module_version': '2024a'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'cffi/1.16.0-GCCcore-13.3.0', 'module_name': 'cffi', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'cryptography/42.0.8-GCCcore-13.3.0', 'module_name': 'cryptography', 'module_version': '42.0.8-GCCcore-13.3.0'}, {'full_module_name': 'virtualenv/20.26.2-GCCcore-13.3.0', 'module_name': 'virtualenv', 'module_version': '20.26.2-GCCcore-13.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2024.06-GCCcore-13.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2024.06-GCCcore-13.3.0'}, {'full_module_name': 'SciPy-bundle/2024.05-gfbf-2024a', 'module_name': 'SciPy-bundle', 'module_version': '2024.05-gfbf-2024a'}, {'full_module_name': 'gzip/1.13-GCCcore-13.3.0', 'module_name': 'gzip', 'module_version': '1.13-GCCcore-13.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-13.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-13.3.0'}, {'full_module_name': 'zstd/1.5.6-GCCcore-13.3.0', 'module_name': 'zstd', 'module_version': '1.5.6-GCCcore-13.3.0'}, {'full_module_name': 'ICU/75.1-GCCcore-13.3.0', 'module_name': 'ICU', 'module_version': '75.1-GCCcore-13.3.0'}, {'full_module_name': 'Boost/1.85.0-GCC-13.3.0', 'module_name': 'Boost', 'module_version': '1.85.0-GCC-13.3.0'}, {'full_module_name': 'snappy/1.2.1-GCCcore-13.3.0', 'module_name': 'snappy', 'module_version': '1.2.1-GCCcore-13.3.0'}, {'full_module_name': 'RapidJSON/1.1.0-20240815-GCCcore-13.3.0', 'module_name': 'RapidJSON', 'module_version': '1.1.0-20240815-GCCcore-13.3.0'}, {'full_module_name': 'Abseil/20240722.0-GCCcore-13.3.0', 'module_name': 'Abseil', 'module_version': '20240722.0-GCCcore-13.3.0'}, {'full_module_name': 'RE2/2024-07-02-GCCcore-13.3.0', 'module_name': 'RE2', 'module_version': '2024-07-02-GCCcore-13.3.0'}, {'full_module_name': 'utf8proc/2.9.0-GCCcore-13.3.0', 'module_name': 'utf8proc', 'module_version': '2.9.0-GCCcore-13.3.0'}, {'full_module_name': 'Arrow/17.0.0-gfbf-2024a', 'module_name': 'Arrow', 'module_version': '17.0.0-gfbf-2024a'}, {'full_module_name': 'wrapt/1.16.0-gfbf-2024a', 'module_name': 'wrapt', 'module_version': '1.16.0-gfbf-2024a'}, {'full_module_name': 'Deprecated/1.2.18-gfbf-2024a', 'module_name': 'Deprecated', 'module_version': '1.2.18-gfbf-2024a'}, {'full_module_name': 'Flask/3.0.3-GCCcore-13.3.0', 'module_name': 'Flask', 'module_version': '3.0.3-GCCcore-13.3.0'}, {'full_module_name': 'cURL/8.7.1-GCCcore-13.3.0', 'module_name': 'cURL', 'module_version': '8.7.1-GCCcore-13.3.0'}, {'full_module_name': 'expat/2.6.2-GCCcore-13.3.0', 'module_name': 'expat', 'module_version': '2.6.2-GCCcore-13.3.0'}, {'full_module_name': 'Perl/5.38.2-GCCcore-13.3.0', 'module_name': 'Perl', 'module_version': '5.38.2-GCCcore-13.3.0'}, {'full_module_name': 'git/2.45.1-GCCcore-13.3.0', 'module_name': 'git', 'module_version': '2.45.1-GCCcore-13.3.0'}, {'full_module_name': 'GitPython/3.1.43-GCCcore-13.3.0', 'module_name': 'GitPython', 'module_version': '3.1.43-GCCcore-13.3.0'}, {'full_module_name': 'protobuf/28.0-GCCcore-13.3.0', 'module_name': 'protobuf', 'module_version': '28.0-GCCcore-13.3.0'}, {'full_module_name': 'protobuf-python/5.28.0-GCCcore-13.3.0', 'module_name': 'protobuf-python', 'module_version': '5.28.0-GCCcore-13.3.0'}, {'full_module_name': 'googleapis-python/2025.03-GCCcore-13.3.0', 'module_name': 'googleapis-python', 'module_version': '2025.03-GCCcore-13.3.0'}, {'full_module_name': 'Markdown/3.7-GCCcore-13.3.0', 'module_name': 'Markdown', 'module_version': '3.7-GCCcore-13.3.0'}, {'full_module_name': 'libpng/1.6.43-GCCcore-13.3.0', 'module_name': 'libpng', 'module_version': '1.6.43-GCCcore-13.3.0'}, {'full_module_name': 'Brotli/1.1.0-GCCcore-13.3.0', 'module_name': 'Brotli', 'module_version': '1.1.0-GCCcore-13.3.0'}, {'full_module_name': 'freetype/2.13.2-GCCcore-13.3.0', 'module_name': 'freetype', 'module_version': '2.13.2-GCCcore-13.3.0'}, {'full_module_name': 'fontconfig/2.15.0-GCCcore-13.3.0', 'module_name': 'fontconfig', 'module_version': '2.15.0-GCCcore-13.3.0'}, {'full_module_name': 'xorg-macros/1.20.1-GCCcore-13.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.1-GCCcore-13.3.0'}, {'full_module_name': 'libpciaccess/0.18.1-GCCcore-13.3.0', 'module_name': 'libpciaccess', 'module_version': '0.18.1-GCCcore-13.3.0'}, {'full_module_name': 'X11/20240607-GCCcore-13.3.0', 'module_name': 'X11', 'module_version': '20240607-GCCcore-13.3.0'}, {'full_module_name': 'Tk/8.6.14-GCCcore-13.3.0', 'module_name': 'Tk', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'Tkinter/3.12.3-GCCcore-13.3.0', 'module_name': 'Tkinter', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'NASM/2.16.03-GCCcore-13.3.0', 'module_name': 'NASM', 'module_version': '2.16.03-GCCcore-13.3.0'}, {'full_module_name': 'libjpeg-turbo/3.0.1-GCCcore-13.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '3.0.1-GCCcore-13.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-13.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-13.3.0'}, {'full_module_name': 'libdeflate/1.20-GCCcore-13.3.0', 'module_name': 'libdeflate', 'module_version': '1.20-GCCcore-13.3.0'}, {'full_module_name': 'LibTIFF/4.6.0-GCCcore-13.3.0', 'module_name': 'LibTIFF', 'module_version': '4.6.0-GCCcore-13.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-13.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-13.3.0'}, {'full_module_name': 'libwebp/1.4.0-GCCcore-13.3.0', 'module_name': 'libwebp', 'module_version': '1.4.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenJPEG/2.5.2-GCCcore-13.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.2-GCCcore-13.3.0'}, {'full_module_name': 'LittleCMS/2.16-GCCcore-13.3.0', 'module_name': 'LittleCMS', 'module_version': '2.16-GCCcore-13.3.0'}, {'full_module_name': 'Pillow/10.4.0-GCCcore-13.3.0', 'module_name': 'Pillow', 'module_version': '10.4.0-GCCcore-13.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-13.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-13.3.0'}, {'full_module_name': 'matplotlib/3.9.2-gfbf-2024a', 'module_name': 'matplotlib', 'module_version': '3.9.2-gfbf-2024a'}, {'full_module_name': 'typing-extensions/4.11.0-GCCcore-13.3.0', 'module_name': 'typing-extensions', 'module_version': '4.11.0-GCCcore-13.3.0'}, {'full_module_name': 'pydantic/2.9.1-GCCcore-13.3.0', 'module_name': 'pydantic', 'module_version': '2.9.1-GCCcore-13.3.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.3.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.3.0'}, {'full_module_name': 'PyYAML/6.0.2-GCCcore-13.3.0', 'module_name': 'PyYAML', 'module_version': '6.0.2-GCCcore-13.3.0'}, {'full_module_name': 'scikit-learn/1.5.2-gfbf-2024a', 'module_name': 'scikit-learn', 'module_version': '1.5.2-gfbf-2024a'}, {'full_module_name': 'Greenlet/3.1.1-GCCcore-13.3.0', 'module_name': 'Greenlet', 'module_version': '3.1.1-GCCcore-13.3.0'}, {'full_module_name': 'PostgreSQL/16.4-GCCcore-13.3.0', 'module_name': 'PostgreSQL', 'module_version': '16.4-GCCcore-13.3.0'}, {'full_module_name': 'psycopg/3.2.3-GCCcore-13.3.0', 'module_name': 'psycopg', 'module_version': '3.2.3-GCCcore-13.3.0'}, {'full_module_name': 'Mako/1.3.5-GCCcore-13.3.0', 'module_name': 'Mako', 'module_version': '1.3.5-GCCcore-13.3.0'}, {'full_module_name': 'SQLAlchemy/2.0.36-GCCcore-13.3.0', 'module_name': 'SQLAlchemy', 'module_version': '2.0.36-GCCcore-13.3.0'}, {'full_module_name': 'MLflow/2.22.4-gfbf-2024a', 'module_name': 'MLflow', 'module_version': '2.22.4-gfbf-2024a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'MLflow is a platform to streamline machine learning development, including tracking experiments,\npackaging code into reproducible runs, and sharing and deploying models.', 'version': '2.22.4', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'cachetools', 'version': '5.5.0'}, {'type': 'python', 'name': 'docker', 'version': '7.1.0'}, {'type': 'python', 'name': 'sniffio', 'version': '1.3.1'}, {'type': 'python', 'name': 'anyio', 'version': '4.9.0'}, {'type': 'python', 'name': 'starlette', 'version': '0.50.0'}, {'type': 'python', 'name': 'annotated_doc', 'version': '0.0.4'}, {'type': 'python', 'name': 'fastapi', 'version': '0.126.0'}, {'type': 'python', 'name': 'graphql_relay', 'version': '3.2.0'}, {'type': 'python', 'name': 'graphql_core', 'version': '3.2.7'}, {'type': 'python', 'name': 'graphene', 'version': '3.4.3'}, {'type': 'python', 'name': 'gunicorn', 'version': '23.0.0'}, {'type': 'python', 'name': 'opentelemetry_semantic_conventions', 'version': '0.57b0'}, {'type': 'python', 'name': 'opentelemetry_sdk', 'version': '1.36.0'}, {'type': 'python', 'name': 'opentelemetry_api', 'version': '1.36.0'}, {'type': 'python', 'name': 'databricks_sdk', 'version': '0.72.0'}, {'type': 'python', 'name': 'sqlparse', 'version': '0.5.5'}, {'type': 'python', 'name': 'h11', 'version': '0.16.0'}, {'type': 'python', 'name': 'uvicorn', 'version': '0.38.0'}, {'type': 'python', 'name': 'mlflow_skinny', 'version': '2.22.4'}, {'type': 'python', 'name': 'mlflow', 'version': '2.22.4'}]}], 'homepage': 'https://mlflow.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'MLflow is a platform to streamline machine learning development, including tracking experiments,\npackaging code into reproducible runs, and sharing and deploying models.'} installations


### alembic


|`alembic` version|MLflow modules that include it|
| --- | --- |
|1.14.0|`MLflow/2.18.0-gfbf-2023b`|

### annotated_doc


|`annotated_doc` version|MLflow modules that include it|
| --- | --- |
|0.0.4|`MLflow/2.22.4-gfbf-2024a`|

### anyio


|`anyio` version|MLflow modules that include it|
| --- | --- |
|4.9.0|`MLflow/2.22.4-gfbf-2024a`|

### cachetools


|`cachetools` version|MLflow modules that include it|
| --- | --- |
|5.5.0|`MLflow/2.22.4-gfbf-2024a`<br/>`MLflow/2.18.0-gfbf-2023b`|

### databricks_sdk


|`databricks_sdk` version|MLflow modules that include it|
| --- | --- |
|0.36.0|`MLflow/2.18.0-gfbf-2023b`|
|0.72.0|`MLflow/2.22.4-gfbf-2024a`|

### docker


|`docker` version|MLflow modules that include it|
| --- | --- |
|7.0.0|`MLflow/2.10.2-gfbf-2023a`|
|7.1.0|`MLflow/2.22.4-gfbf-2024a`<br/>`MLflow/2.18.0-gfbf-2023b`|

### entrypoints


|`entrypoints` version|MLflow modules that include it|
| --- | --- |
|0.4|`MLflow/2.10.2-gfbf-2023a`|

### fastapi


|`fastapi` version|MLflow modules that include it|
| --- | --- |
|0.126.0|`MLflow/2.22.4-gfbf-2024a`|

### google-auth


|`google-auth` version|MLflow modules that include it|
| --- | --- |
|2.35.0|`MLflow/2.18.0-gfbf-2023b`|

### graphene


|`graphene` version|MLflow modules that include it|
| --- | --- |
|3.4.1|`MLflow/2.18.0-gfbf-2023b`|
|3.4.3|`MLflow/2.22.4-gfbf-2024a`|

### graphql-relay


|`graphql-relay` version|MLflow modules that include it|
| --- | --- |
|3.2.0|`MLflow/2.18.0-gfbf-2023b`|

### graphql_core


|`graphql_core` version|MLflow modules that include it|
| --- | --- |
|3.2.5|`MLflow/2.18.0-gfbf-2023b`|
|3.2.7|`MLflow/2.22.4-gfbf-2024a`|

### graphql_relay


|`graphql_relay` version|MLflow modules that include it|
| --- | --- |
|3.2.0|`MLflow/2.22.4-gfbf-2024a`|

### gunicorn


|`gunicorn` version|MLflow modules that include it|
| --- | --- |
|21.2.0|`MLflow/2.10.2-gfbf-2023a`|
|23.0.0|`MLflow/2.22.4-gfbf-2024a`<br/>`MLflow/2.18.0-gfbf-2023b`|

### h11


|`h11` version|MLflow modules that include it|
| --- | --- |
|0.16.0|`MLflow/2.22.4-gfbf-2024a`|

### Markdown


|`Markdown` version|MLflow modules that include it|
| --- | --- |
|3.5.2|`MLflow/2.10.2-gfbf-2023a`|

### mlflow


|`mlflow` version|MLflow modules that include it|
| --- | --- |
|2.10.2|`MLflow/2.10.2-gfbf-2023a`|
|2.18.0|`MLflow/2.18.0-gfbf-2023b`|
|2.22.4|`MLflow/2.22.4-gfbf-2024a`|

### mlflow_skinny


|`mlflow_skinny` version|MLflow modules that include it|
| --- | --- |
|2.18.0|`MLflow/2.18.0-gfbf-2023b`|
|2.22.4|`MLflow/2.22.4-gfbf-2024a`|

### opentelemetry_api


|`opentelemetry_api` version|MLflow modules that include it|
| --- | --- |
|1.27.0|`MLflow/2.18.0-gfbf-2023b`|
|1.36.0|`MLflow/2.22.4-gfbf-2024a`|

### opentelemetry_sdk


|`opentelemetry_sdk` version|MLflow modules that include it|
| --- | --- |
|1.27.0|`MLflow/2.18.0-gfbf-2023b`|
|1.36.0|`MLflow/2.22.4-gfbf-2024a`|

### opentelemetry_semantic_conventions


|`opentelemetry_semantic_conventions` version|MLflow modules that include it|
| --- | --- |
|0.48b0|`MLflow/2.18.0-gfbf-2023b`|
|0.57b0|`MLflow/2.22.4-gfbf-2024a`|

### pyasn1-modules


|`pyasn1-modules` version|MLflow modules that include it|
| --- | --- |
|0.4.1|`MLflow/2.18.0-gfbf-2023b`|

### querystring_parser


|`querystring_parser` version|MLflow modules that include it|
| --- | --- |
|1.2.4|`MLflow/2.10.2-gfbf-2023a`|

### rsa


|`rsa` version|MLflow modules that include it|
| --- | --- |
|4.9|`MLflow/2.18.0-gfbf-2023b`|

### sniffio


|`sniffio` version|MLflow modules that include it|
| --- | --- |
|1.3.1|`MLflow/2.22.4-gfbf-2024a`|

### sqlparse


|`sqlparse` version|MLflow modules that include it|
| --- | --- |
|0.4.4|`MLflow/2.10.2-gfbf-2023a`|
|0.5.1|`MLflow/2.18.0-gfbf-2023b`|
|0.5.5|`MLflow/2.22.4-gfbf-2024a`|

### starlette


|`starlette` version|MLflow modules that include it|
| --- | --- |
|0.50.0|`MLflow/2.22.4-gfbf-2024a`|

### uvicorn


|`uvicorn` version|MLflow modules that include it|
| --- | --- |
|0.38.0|`MLflow/2.22.4-gfbf-2024a`|