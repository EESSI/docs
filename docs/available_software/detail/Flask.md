# Flask



Flask is a lightweight WSGI web application framework. It is designed to make
getting started quick and easy, with the ability to scale up to complex
applications.
This module includes the Flask extensions: Flask-Cors

<small>homepage: </small><span class="software-link">[https://www.palletsprojects.com/p/flask/](https://www.palletsprojects.com/p/flask/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.2.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Flask/2.2.3-GCCcore-12.2.0`|
|2.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Flask/2.3.3-GCCcore-12.3.0`|
|3.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Flask/3.0.0-GCCcore-13.2.0`|
|3.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Flask/3.0.3-GCCcore-13.3.0`|
|3.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Flask/3.1.1-GCCcore-14.2.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://www.palletsprojects.com/p/flask/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.2.0'}, 'toolchain_families_compatibility': ['2022b_foss'], 'module': {'full_module_name': 'Flask/2.2.3-GCCcore-12.2.0', 'module_name': 'Flask', 'module_version': '2.2.3-GCCcore-12.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.2.0', 'module_name': 'GCCcore', 'module_version': '12.2.0'}, {'full_module_name': 'Tcl/8.6.12-GCCcore-12.2.0', 'module_name': 'Tcl', 'module_version': '8.6.12-GCCcore-12.2.0'}, {'full_module_name': 'SQLite/3.39.4-GCCcore-12.2.0', 'module_name': 'SQLite', 'module_version': '3.39.4-GCCcore-12.2.0'}, {'full_module_name': 'GMP/6.2.1-GCCcore-12.2.0', 'module_name': 'GMP', 'module_version': '6.2.1-GCCcore-12.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.10.8-GCCcore-12.2.0', 'module_name': 'Python', 'module_version': '3.10.8-GCCcore-12.2.0'}, {'full_module_name': 'Flask/2.2.3-GCCcore-12.2.0', 'module_name': 'Flask', 'module_version': '2.2.3-GCCcore-12.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nFlask is a lightweight WSGI web application framework. It is designed to make\ngetting started quick and easy, with the ability to scale up to complex\napplications.\nThis module includes the Flask extensions: Flask-Cors', 'version': '2.2.3', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'itsdangerous', 'version': '2.1.2'}, {'type': 'python', 'name': 'Werkzeug', 'version': '2.2.3'}, {'type': 'python', 'name': 'asgiref', 'version': '3.6.0'}, {'type': 'python', 'name': 'Flask', 'version': '2.2.3'}, {'type': 'python', 'name': 'Flask-Cors', 'version': '3.0.10'}, {'type': 'python', 'name': 'cachelib', 'version': '0.10.2'}, {'type': 'python', 'name': 'Flask-Session', 'version': '0.4.0'}]}, {'homepage': 'https://www.palletsprojects.com/p/flask/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'Flask/2.3.3-GCCcore-12.3.0', 'module_name': 'Flask', 'module_version': '2.3.3-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'Flask/2.3.3-GCCcore-12.3.0', 'module_name': 'Flask', 'module_version': '2.3.3-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nFlask is a lightweight WSGI web application framework. It is designed to make\ngetting started quick and easy, with the ability to scale up to complex\napplications.\nThis module includes the Flask extensions: Flask-Cors', 'version': '2.3.3', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'itsdangerous', 'version': '2.1.2'}, {'type': 'python', 'name': 'werkzeug', 'version': '2.3.7'}, {'type': 'python', 'name': 'asgiref', 'version': '3.7.2'}, {'type': 'python', 'name': 'blinker', 'version': '1.6.2'}, {'type': 'python', 'name': 'flask', 'version': '2.3.3'}, {'type': 'python', 'name': 'Flask-Cors', 'version': '4.0.0'}, {'type': 'python', 'name': 'cachelib', 'version': '0.10.2'}, {'type': 'python', 'name': 'Flask-Session', 'version': '0.5.0'}]}, {'homepage': 'https://www.palletsprojects.com/p/flask/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.2.0'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'Flask/3.0.0-GCCcore-13.2.0', 'module_name': 'Flask', 'module_version': '3.0.0-GCCcore-13.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'Flask/3.0.0-GCCcore-13.2.0', 'module_name': 'Flask', 'module_version': '3.0.0-GCCcore-13.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nFlask is a lightweight WSGI web application framework. It is designed to make\ngetting started quick and easy, with the ability to scale up to complex\napplications.\nThis module includes the Flask extensions: Flask-Cors', 'version': '3.0.0', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'itsdangerous', 'version': '2.1.2'}, {'type': 'python', 'name': 'werkzeug', 'version': '3.0.1'}, {'type': 'python', 'name': 'asgiref', 'version': '3.7.2'}, {'type': 'python', 'name': 'blinker', 'version': '1.7.0'}, {'type': 'python', 'name': 'flask', 'version': '3.0.0'}, {'type': 'python', 'name': 'Flask-Cors', 'version': '4.0.0'}, {'type': 'python', 'name': 'cachelib', 'version': '0.10.2'}, {'type': 'python', 'name': 'Flask-Session', 'version': '0.5.0'}]}, {'homepage': 'https://flask.palletsprojects.com/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.3.0'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'Flask/3.0.3-GCCcore-13.3.0', 'module_name': 'Flask', 'module_version': '3.0.3-GCCcore-13.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'cffi/1.16.0-GCCcore-13.3.0', 'module_name': 'cffi', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'cryptography/42.0.8-GCCcore-13.3.0', 'module_name': 'cryptography', 'module_version': '42.0.8-GCCcore-13.3.0'}, {'full_module_name': 'virtualenv/20.26.2-GCCcore-13.3.0', 'module_name': 'virtualenv', 'module_version': '20.26.2-GCCcore-13.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2024.06-GCCcore-13.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2024.06-GCCcore-13.3.0'}, {'full_module_name': 'Flask/3.0.3-GCCcore-13.3.0', 'module_name': 'Flask', 'module_version': '3.0.3-GCCcore-13.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nFlask is a lightweight WSGI web application framework. It is designed to make\ngetting started quick and easy, with the ability to scale up to complex\napplications.\nThis module includes the Flask extensions: Flask-Cors', 'version': '3.0.3', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'itsdangerous', 'version': '2.2.0'}, {'type': 'python', 'name': 'werkzeug', 'version': '3.0.4'}, {'type': 'python', 'name': 'asgiref', 'version': '3.7.2'}, {'type': 'python', 'name': 'blinker', 'version': '1.8.2'}, {'type': 'python', 'name': 'flask', 'version': '3.0.3'}, {'type': 'python', 'name': 'msgspec', 'version': '0.18.6'}, {'type': 'python', 'name': 'Flask-Cors', 'version': '5.0.0'}, {'type': 'python', 'name': 'cachelib', 'version': '0.13.0'}, {'type': 'python', 'name': 'Flask-Session', 'version': '0.8.0'}]}, {'homepage': 'https://flask.palletsprojects.com/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '14.2.0'}, 'toolchain_families_compatibility': ['2025a_foss'], 'module': {'full_module_name': 'Flask/3.1.1-GCCcore-14.2.0', 'module_name': 'Flask', 'module_version': '3.1.1-GCCcore-14.2.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/14.2.0', 'module_name': 'GCCcore', 'module_version': '14.2.0'}, {'full_module_name': 'Tcl/8.6.16-GCCcore-14.2.0', 'module_name': 'Tcl', 'module_version': '8.6.16-GCCcore-14.2.0'}, {'full_module_name': 'SQLite/3.47.2-GCCcore-14.2.0', 'module_name': 'SQLite', 'module_version': '3.47.2-GCCcore-14.2.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-14.2.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-14.2.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.13.1-GCCcore-14.2.0', 'module_name': 'Python', 'module_version': '3.13.1-GCCcore-14.2.0'}, {'full_module_name': 'cffi/1.17.1-GCCcore-14.2.0', 'module_name': 'cffi', 'module_version': '1.17.1-GCCcore-14.2.0'}, {'full_module_name': 'cryptography/44.0.2-GCCcore-14.2.0', 'module_name': 'cryptography', 'module_version': '44.0.2-GCCcore-14.2.0'}, {'full_module_name': 'virtualenv/20.29.2-GCCcore-14.2.0', 'module_name': 'virtualenv', 'module_version': '20.29.2-GCCcore-14.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2025.04-GCCcore-14.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2025.04-GCCcore-14.2.0'}, {'full_module_name': 'Flask/3.1.1-GCCcore-14.2.0', 'module_name': 'Flask', 'module_version': '3.1.1-GCCcore-14.2.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': '\nFlask is a lightweight WSGI web application framework. It is designed to make\ngetting started quick and easy, with the ability to scale up to complex\napplications.\nThis module includes the Flask extensions: Flask-Cors', 'version': '3.1.1', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'itsdangerous', 'version': '2.2.0'}, {'type': 'python', 'name': 'werkzeug', 'version': '3.1.3'}, {'type': 'python', 'name': 'asgiref', 'version': '3.9.1'}, {'type': 'python', 'name': 'blinker', 'version': '1.9.0'}, {'type': 'python', 'name': 'flask', 'version': '3.1.1'}, {'type': 'python', 'name': 'msgspec', 'version': '0.19.0'}, {'type': 'python', 'name': 'Flask-Cors', 'version': '6.0.1'}, {'type': 'python', 'name': 'cachelib', 'version': '0.13.0'}, {'type': 'python', 'name': 'Flask-Session', 'version': '0.8.0'}]}], 'homepage': 'https://www.palletsprojects.com/p/flask/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': '\nFlask is a lightweight WSGI web application framework. It is designed to make\ngetting started quick and easy, with the ability to scale up to complex\napplications.\nThis module includes the Flask extensions: Flask-Cors'} installations


### asgiref


|`asgiref` version|Flask modules that include it|
| --- | --- |
|3.6.0|`Flask/2.2.3-GCCcore-12.2.0`|
|3.7.2|`Flask/2.3.3-GCCcore-12.3.0`<br/>`Flask/3.0.3-GCCcore-13.3.0`<br/>`Flask/3.0.0-GCCcore-13.2.0`|
|3.9.1|`Flask/3.1.1-GCCcore-14.2.0`|

### blinker


|`blinker` version|Flask modules that include it|
| --- | --- |
|1.6.2|`Flask/2.3.3-GCCcore-12.3.0`|
|1.7.0|`Flask/3.0.0-GCCcore-13.2.0`|
|1.8.2|`Flask/3.0.3-GCCcore-13.3.0`|
|1.9.0|`Flask/3.1.1-GCCcore-14.2.0`|

### cachelib


|`cachelib` version|Flask modules that include it|
| --- | --- |
|0.10.2|`Flask/2.3.3-GCCcore-12.3.0`<br/>`Flask/2.2.3-GCCcore-12.2.0`<br/>`Flask/3.0.0-GCCcore-13.2.0`|
|0.13.0|`Flask/3.1.1-GCCcore-14.2.0`<br/>`Flask/3.0.3-GCCcore-13.3.0`|

### Flask


|`Flask` version|Flask modules that include it|
| --- | --- |
|2.2.3|`Flask/2.2.3-GCCcore-12.2.0`|

### flask


|`flask` version|Flask modules that include it|
| --- | --- |
|2.3.3|`Flask/2.3.3-GCCcore-12.3.0`|
|3.0.0|`Flask/3.0.0-GCCcore-13.2.0`|
|3.0.3|`Flask/3.0.3-GCCcore-13.3.0`|
|3.1.1|`Flask/3.1.1-GCCcore-14.2.0`|

### Flask-Cors


|`Flask-Cors` version|Flask modules that include it|
| --- | --- |
|3.0.10|`Flask/2.2.3-GCCcore-12.2.0`|
|4.0.0|`Flask/2.3.3-GCCcore-12.3.0`<br/>`Flask/3.0.0-GCCcore-13.2.0`|
|5.0.0|`Flask/3.0.3-GCCcore-13.3.0`|
|6.0.1|`Flask/3.1.1-GCCcore-14.2.0`|

### Flask-Session


|`Flask-Session` version|Flask modules that include it|
| --- | --- |
|0.4.0|`Flask/2.2.3-GCCcore-12.2.0`|
|0.5.0|`Flask/2.3.3-GCCcore-12.3.0`<br/>`Flask/3.0.0-GCCcore-13.2.0`|
|0.8.0|`Flask/3.1.1-GCCcore-14.2.0`<br/>`Flask/3.0.3-GCCcore-13.3.0`|

### itsdangerous


|`itsdangerous` version|Flask modules that include it|
| --- | --- |
|2.1.2|`Flask/2.3.3-GCCcore-12.3.0`<br/>`Flask/2.2.3-GCCcore-12.2.0`<br/>`Flask/3.0.0-GCCcore-13.2.0`|
|2.2.0|`Flask/3.1.1-GCCcore-14.2.0`<br/>`Flask/3.0.3-GCCcore-13.3.0`|

### msgspec


|`msgspec` version|Flask modules that include it|
| --- | --- |
|0.18.6|`Flask/3.0.3-GCCcore-13.3.0`|
|0.19.0|`Flask/3.1.1-GCCcore-14.2.0`|

### Werkzeug


|`Werkzeug` version|Flask modules that include it|
| --- | --- |
|2.2.3|`Flask/2.2.3-GCCcore-12.2.0`|

### werkzeug


|`werkzeug` version|Flask modules that include it|
| --- | --- |
|2.3.7|`Flask/2.3.3-GCCcore-12.3.0`|
|3.0.1|`Flask/3.0.0-GCCcore-13.2.0`|
|3.0.4|`Flask/3.0.3-GCCcore-13.3.0`|
|3.1.3|`Flask/3.1.1-GCCcore-14.2.0`|