# jupyter-server


The Jupyter Server provides the backend (i.e. the core services, APIs, and REST
endpoints) for Jupyter web applications like Jupyter notebook, JupyterLab, and
Voila.

<small>homepage: </small><span class="software-link">[https://jupyter.org/](https://jupyter.org/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.7.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|2.14.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`jupyter-server/2.14.2-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://jupyter.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'jupyter-server/2.7.2-GCCcore-12.3.0', 'module_name': 'jupyter-server', 'module_version': '2.7.2-GCCcore-12.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'hatchling/1.18.0-GCCcore-12.3.0', 'module_name': 'hatchling', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'OpenPGM/5.2.122-GCCcore-12.3.0', 'module_name': 'OpenPGM', 'module_version': '5.2.122-GCCcore-12.3.0'}, {'full_module_name': 'libsodium/1.0.18-GCCcore-12.3.0', 'module_name': 'libsodium', 'module_version': '1.0.18-GCCcore-12.3.0'}, {'full_module_name': 'ZeroMQ/4.3.4-GCCcore-12.3.0', 'module_name': 'ZeroMQ', 'module_version': '4.3.4-GCCcore-12.3.0'}, {'full_module_name': 'libxml2/2.11.4-GCCcore-12.3.0', 'module_name': 'libxml2', 'module_version': '2.11.4-GCCcore-12.3.0'}, {'full_module_name': 'libxslt/1.1.38-GCCcore-12.3.0', 'module_name': 'libxslt', 'module_version': '1.1.38-GCCcore-12.3.0'}, {'full_module_name': 'lxml/4.9.2-GCCcore-12.3.0', 'module_name': 'lxml', 'module_version': '4.9.2-GCCcore-12.3.0'}, {'full_module_name': 'BeautifulSoup/4.12.2-GCCcore-12.3.0', 'module_name': 'BeautifulSoup', 'module_version': '4.12.2-GCCcore-12.3.0'}, {'full_module_name': 'IPython/8.14.0-GCCcore-12.3.0', 'module_name': 'IPython', 'module_version': '8.14.0-GCCcore-12.3.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-12.3.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-12.3.0'}, {'full_module_name': 'PyYAML/6.0-GCCcore-12.3.0', 'module_name': 'PyYAML', 'module_version': '6.0-GCCcore-12.3.0'}, {'full_module_name': 'PyZMQ/25.1.1-GCCcore-12.3.0', 'module_name': 'PyZMQ', 'module_version': '25.1.1-GCCcore-12.3.0'}, {'full_module_name': 'tornado/6.3.2-GCCcore-12.3.0', 'module_name': 'tornado', 'module_version': '6.3.2-GCCcore-12.3.0'}, {'full_module_name': 'jupyter-server/2.7.2-GCCcore-12.3.0', 'module_name': 'jupyter-server', 'module_version': '2.7.2-GCCcore-12.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The Jupyter Server provides the backend (i.e. the core services, APIs, and REST\nendpoints) for Jupyter web applications like Jupyter notebook, JupyterLab, and\nVoila.', 'version': '2.7.2', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'hatch_nodejs_version', 'version': '0.3.1'}, {'type': 'python', 'name': 'hatch_jupyter_builder', 'version': '0.8.3'}, {'type': 'python', 'name': 'websocket-client', 'version': '1.6.1'}, {'type': 'python', 'name': 'terminado', 'version': '0.17.1'}, {'type': 'python', 'name': 'Send2Trash', 'version': '1.8.2'}, {'type': 'python', 'name': 'prometheus_client', 'version': '0.17.1'}, {'type': 'python', 'name': 'overrides', 'version': '7.4.0'}, {'type': 'python', 'name': 'jupyter_core', 'version': '5.3.1'}, {'type': 'python', 'name': 'fastjsonschema', 'version': '2.18.0'}, {'type': 'python', 'name': 'tinycss2', 'version': '1.2.1'}, {'type': 'python', 'name': 'pandocfilters', 'version': '1.5.0'}, {'type': 'python', 'name': 'mistune', 'version': '3.0.1'}, {'type': 'python', 'name': 'deprecation', 'version': '2.1.0'}, {'type': 'python', 'name': 'jupyter_packaging', 'version': '0.12.3'}, {'type': 'python', 'name': 'jupyterlab_pygments', 'version': '0.2.2'}, {'type': 'python', 'name': 'defusedxml', 'version': '0.7.1'}, {'type': 'python', 'name': 'bleach', 'version': '6.0.0'}, {'type': 'python', 'name': 'arrow', 'version': '1.2.3'}, {'type': 'python', 'name': 'nbformat', 'version': '5.9.2'}, {'type': 'python', 'name': 'nbclient', 'version': '0.8.0'}, {'type': 'python', 'name': 'jupyter_client', 'version': '8.3.0'}, {'type': 'python', 'name': 'nbconvert', 'version': '7.7.4'}, {'type': 'python', 'name': 'jupyter_server_terminals', 'version': '0.4.4'}, {'type': 'python', 'name': 'rfc3986_validator', 'version': '0.1.1'}, {'type': 'python', 'name': 'rfc3339_validator', 'version': '0.1.4'}, {'type': 'python', 'name': 'rpds_py', 'version': '0.9.2'}, {'type': 'python', 'name': 'referencing', 'version': '0.30.2'}, {'type': 'python', 'name': 'python-json-logger', 'version': '2.0.7'}, {'type': 'python', 'name': 'jsonschema_specifications', 'version': '2023.7.1'}, {'type': 'python', 'name': 'jsonschema', 'version': '4.18.0'}, {'type': 'python', 'name': 'jupyter_events', 'version': '0.7.0'}, {'type': 'python', 'name': 'argon2-cffi-bindings', 'version': '21.2.0'}, {'type': 'python', 'name': 'argon2_cffi', 'version': '23.1.0'}, {'type': 'python', 'name': 'sniffio', 'version': '1.3.0'}, {'type': 'python', 'name': 'anyio', 'version': '3.7.1'}, {'type': 'python', 'name': 'jupyter_server', 'version': '2.7.2'}, {'type': 'python', 'name': 'jupyterlab_widgets', 'version': '3.0.8'}, {'type': 'python', 'name': 'widgetsnbextension', 'version': '4.0.8'}, {'type': 'python', 'name': 'comm', 'version': '0.1.4'}, {'type': 'python', 'name': 'ipywidgets', 'version': '8.1.0'}, {'type': 'python', 'name': 'notebook_shim', 'version': '0.2.3'}, {'type': 'python', 'name': 'nest_asyncio', 'version': '1.5.7'}, {'type': 'python', 'name': 'ipykernel', 'version': '6.25.1'}, {'type': 'python', 'name': 'ipython_genutils', 'version': '0.2.0'}, {'type': 'python', 'name': 'debugpy', 'version': '1.6.7.post1'}]}, {'homepage': 'https://jupyter.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '13.3.0'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'jupyter-server/2.14.2-GCCcore-13.3.0', 'module_name': 'jupyter-server', 'module_version': '2.14.2-GCCcore-13.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'cffi/1.16.0-GCCcore-13.3.0', 'module_name': 'cffi', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'cryptography/42.0.8-GCCcore-13.3.0', 'module_name': 'cryptography', 'module_version': '42.0.8-GCCcore-13.3.0'}, {'full_module_name': 'virtualenv/20.26.2-GCCcore-13.3.0', 'module_name': 'virtualenv', 'module_version': '20.26.2-GCCcore-13.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2024.06-GCCcore-13.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2024.06-GCCcore-13.3.0'}, {'full_module_name': 'Perl/5.38.2-GCCcore-13.3.0', 'module_name': 'Perl', 'module_version': '5.38.2-GCCcore-13.3.0'}, {'full_module_name': 'OpenPGM/5.2.122-GCCcore-13.3.0', 'module_name': 'OpenPGM', 'module_version': '5.2.122-GCCcore-13.3.0'}, {'full_module_name': 'libsodium/1.0.20-GCCcore-13.3.0', 'module_name': 'libsodium', 'module_version': '1.0.20-GCCcore-13.3.0'}, {'full_module_name': 'ZeroMQ/4.3.5-GCCcore-13.3.0', 'module_name': 'ZeroMQ', 'module_version': '4.3.5-GCCcore-13.3.0'}, {'full_module_name': 'libxml2/2.12.7-GCCcore-13.3.0', 'module_name': 'libxml2', 'module_version': '2.12.7-GCCcore-13.3.0'}, {'full_module_name': 'libxslt/1.1.42-GCCcore-13.3.0', 'module_name': 'libxslt', 'module_version': '1.1.42-GCCcore-13.3.0'}, {'full_module_name': 'lxml/5.3.0-GCCcore-13.3.0', 'module_name': 'lxml', 'module_version': '5.3.0-GCCcore-13.3.0'}, {'full_module_name': 'jedi/0.19.1-GCCcore-13.3.0', 'module_name': 'jedi', 'module_version': '0.19.1-GCCcore-13.3.0'}, {'full_module_name': 'IPython/8.28.0-GCCcore-13.3.0', 'module_name': 'IPython', 'module_version': '8.28.0-GCCcore-13.3.0'}, {'full_module_name': 'libyaml/0.2.5-GCCcore-13.3.0', 'module_name': 'libyaml', 'module_version': '0.2.5-GCCcore-13.3.0'}, {'full_module_name': 'PyYAML/6.0.2-GCCcore-13.3.0', 'module_name': 'PyYAML', 'module_version': '6.0.2-GCCcore-13.3.0'}, {'full_module_name': 'PyZMQ/26.2.0-GCCcore-13.3.0', 'module_name': 'PyZMQ', 'module_version': '26.2.0-GCCcore-13.3.0'}, {'full_module_name': 'tornado/6.4.1-GCCcore-13.3.0', 'module_name': 'tornado', 'module_version': '6.4.1-GCCcore-13.3.0'}, {'full_module_name': 'BeautifulSoup/4.12.3-GCCcore-13.3.0', 'module_name': 'BeautifulSoup', 'module_version': '4.12.3-GCCcore-13.3.0'}, {'full_module_name': 'jupyter-server/2.14.2-GCCcore-13.3.0', 'module_name': 'jupyter-server', 'module_version': '2.14.2-GCCcore-13.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The Jupyter Server provides the backend (i.e. the core services, APIs, and REST\nendpoints) for Jupyter web applications like Jupyter notebook, JupyterLab, and\nVoila.', 'version': '2.14.2', 'versionsuffix': '', 'extensions': [{'type': 'python', 'name': 'websocket_client', 'version': '1.8.0'}, {'type': 'python', 'name': 'terminado', 'version': '0.18.1'}, {'type': 'python', 'name': 'Send2Trash', 'version': '1.8.3'}, {'type': 'python', 'name': 'prometheus_client', 'version': '0.21.0'}, {'type': 'python', 'name': 'overrides', 'version': '7.7.0'}, {'type': 'python', 'name': 'jupyter_core', 'version': '5.7.2'}, {'type': 'python', 'name': 'fastjsonschema', 'version': '2.20.0'}, {'type': 'python', 'name': 'tinycss2', 'version': '1.3.0'}, {'type': 'python', 'name': 'pandocfilters', 'version': '1.5.1'}, {'type': 'python', 'name': 'mistune', 'version': '3.0.2'}, {'type': 'python', 'name': 'deprecation', 'version': '2.1.0'}, {'type': 'python', 'name': 'jupyter_packaging', 'version': '0.12.3'}, {'type': 'python', 'name': 'jupyterlab_pygments', 'version': '0.3.0'}, {'type': 'python', 'name': 'defusedxml', 'version': '0.7.1'}, {'type': 'python', 'name': 'bleach', 'version': '6.1.0'}, {'type': 'python', 'name': 'nbformat', 'version': '5.10.4'}, {'type': 'python', 'name': 'nbclient', 'version': '0.10.0'}, {'type': 'python', 'name': 'jupyter_client', 'version': '8.6.3'}, {'type': 'python', 'name': 'nbconvert', 'version': '7.16.4'}, {'type': 'python', 'name': 'jupyter_server_terminals', 'version': '0.5.3'}, {'type': 'python', 'name': 'rfc3986_validator', 'version': '0.1.1'}, {'type': 'python', 'name': 'rfc3339_validator', 'version': '0.1.4'}, {'type': 'python', 'name': 'rpds_py', 'version': '0.20.0'}, {'type': 'python', 'name': 'referencing', 'version': '0.35.1'}, {'type': 'python', 'name': 'python-json-logger', 'version': '2.0.7'}, {'type': 'python', 'name': 'jsonschema_specifications', 'version': '2024.10.1'}, {'type': 'python', 'name': 'jsonschema', 'version': '4.23.0'}, {'type': 'python', 'name': 'jupyter_events', 'version': '0.10.0'}, {'type': 'python', 'name': 'argon2-cffi-bindings', 'version': '21.2.0'}, {'type': 'python', 'name': 'argon2_cffi', 'version': '23.1.0'}, {'type': 'python', 'name': 'sniffio', 'version': '1.3.1'}, {'type': 'python', 'name': 'anyio', 'version': '4.3.0'}, {'type': 'python', 'name': 'jupyter_server', 'version': '2.14.2'}, {'type': 'python', 'name': 'jupyterlab_widgets', 'version': '3.0.13'}, {'type': 'python', 'name': 'widgetsnbextension', 'version': '4.0.13'}, {'type': 'python', 'name': 'comm', 'version': '0.2.2'}, {'type': 'python', 'name': 'ipywidgets', 'version': '8.1.5'}, {'type': 'python', 'name': 'notebook_shim', 'version': '0.2.4'}, {'type': 'python', 'name': 'nest_asyncio', 'version': '1.6.0'}, {'type': 'python', 'name': 'ipykernel', 'version': '6.29.5'}, {'type': 'python', 'name': 'ipython_genutils', 'version': '0.2.0'}, {'type': 'python', 'name': 'debugpy', 'version': '1.8.7'}]}], 'homepage': 'https://jupyter.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'The Jupyter Server provides the backend (i.e. the core services, APIs, and REST\nendpoints) for Jupyter web applications like Jupyter notebook, JupyterLab, and\nVoila.'} installations


### anyio


|`anyio` version|jupyter-server modules that include it|
| --- | --- |
|3.7.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|4.3.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### argon2-cffi-bindings


|`argon2-cffi-bindings` version|jupyter-server modules that include it|
| --- | --- |
|21.2.0|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### argon2_cffi


|`argon2_cffi` version|jupyter-server modules that include it|
| --- | --- |
|23.1.0|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### arrow


|`arrow` version|jupyter-server modules that include it|
| --- | --- |
|1.2.3|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### bleach


|`bleach` version|jupyter-server modules that include it|
| --- | --- |
|6.0.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|6.1.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### comm


|`comm` version|jupyter-server modules that include it|
| --- | --- |
|0.1.4|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.2.2|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### debugpy


|`debugpy` version|jupyter-server modules that include it|
| --- | --- |
|1.6.7.post1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|1.8.7|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### defusedxml


|`defusedxml` version|jupyter-server modules that include it|
| --- | --- |
|0.7.1|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### deprecation


|`deprecation` version|jupyter-server modules that include it|
| --- | --- |
|2.1.0|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### fastjsonschema


|`fastjsonschema` version|jupyter-server modules that include it|
| --- | --- |
|2.18.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|2.20.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### hatch_jupyter_builder


|`hatch_jupyter_builder` version|jupyter-server modules that include it|
| --- | --- |
|0.8.3|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### hatch_nodejs_version


|`hatch_nodejs_version` version|jupyter-server modules that include it|
| --- | --- |
|0.3.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### ipykernel


|`ipykernel` version|jupyter-server modules that include it|
| --- | --- |
|6.25.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|6.29.5|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### ipython_genutils


|`ipython_genutils` version|jupyter-server modules that include it|
| --- | --- |
|0.2.0|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### ipywidgets


|`ipywidgets` version|jupyter-server modules that include it|
| --- | --- |
|8.1.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|8.1.5|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jsonschema


|`jsonschema` version|jupyter-server modules that include it|
| --- | --- |
|4.18.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|4.23.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jsonschema_specifications


|`jsonschema_specifications` version|jupyter-server modules that include it|
| --- | --- |
|2023.7.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|2024.10.1|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jupyter_client


|`jupyter_client` version|jupyter-server modules that include it|
| --- | --- |
|8.3.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|8.6.3|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jupyter_core


|`jupyter_core` version|jupyter-server modules that include it|
| --- | --- |
|5.3.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|5.7.2|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jupyter_events


|`jupyter_events` version|jupyter-server modules that include it|
| --- | --- |
|0.10.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|0.7.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### jupyter_packaging


|`jupyter_packaging` version|jupyter-server modules that include it|
| --- | --- |
|0.12.3|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### jupyter_server


|`jupyter_server` version|jupyter-server modules that include it|
| --- | --- |
|2.14.2|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|2.7.2|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### jupyter_server_terminals


|`jupyter_server_terminals` version|jupyter-server modules that include it|
| --- | --- |
|0.4.4|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.5.3|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jupyterlab_pygments


|`jupyterlab_pygments` version|jupyter-server modules that include it|
| --- | --- |
|0.2.2|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.3.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### jupyterlab_widgets


|`jupyterlab_widgets` version|jupyter-server modules that include it|
| --- | --- |
|3.0.13|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|3.0.8|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### mistune


|`mistune` version|jupyter-server modules that include it|
| --- | --- |
|3.0.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|3.0.2|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### nbclient


|`nbclient` version|jupyter-server modules that include it|
| --- | --- |
|0.10.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|0.8.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### nbconvert


|`nbconvert` version|jupyter-server modules that include it|
| --- | --- |
|7.16.4|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|7.7.4|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### nbformat


|`nbformat` version|jupyter-server modules that include it|
| --- | --- |
|5.10.4|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|5.9.2|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### nest_asyncio


|`nest_asyncio` version|jupyter-server modules that include it|
| --- | --- |
|1.5.7|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|1.6.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### notebook_shim


|`notebook_shim` version|jupyter-server modules that include it|
| --- | --- |
|0.2.3|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.2.4|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### overrides


|`overrides` version|jupyter-server modules that include it|
| --- | --- |
|7.4.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|7.7.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### pandocfilters


|`pandocfilters` version|jupyter-server modules that include it|
| --- | --- |
|1.5.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|1.5.1|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### prometheus_client


|`prometheus_client` version|jupyter-server modules that include it|
| --- | --- |
|0.17.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.21.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### python-json-logger


|`python-json-logger` version|jupyter-server modules that include it|
| --- | --- |
|2.0.7|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### referencing


|`referencing` version|jupyter-server modules that include it|
| --- | --- |
|0.30.2|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.35.1|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### rfc3339_validator


|`rfc3339_validator` version|jupyter-server modules that include it|
| --- | --- |
|0.1.4|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### rfc3986_validator


|`rfc3986_validator` version|jupyter-server modules that include it|
| --- | --- |
|0.1.1|`jupyter-server/2.14.2-GCCcore-13.3.0`<br/>`jupyter-server/2.7.2-GCCcore-12.3.0`|

### rpds_py


|`rpds_py` version|jupyter-server modules that include it|
| --- | --- |
|0.20.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|0.9.2|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### Send2Trash


|`Send2Trash` version|jupyter-server modules that include it|
| --- | --- |
|1.8.2|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|1.8.3|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### sniffio


|`sniffio` version|jupyter-server modules that include it|
| --- | --- |
|1.3.0|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|1.3.1|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### terminado


|`terminado` version|jupyter-server modules that include it|
| --- | --- |
|0.17.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|0.18.1|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### tinycss2


|`tinycss2` version|jupyter-server modules that include it|
| --- | --- |
|1.2.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|
|1.3.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### websocket-client


|`websocket-client` version|jupyter-server modules that include it|
| --- | --- |
|1.6.1|`jupyter-server/2.7.2-GCCcore-12.3.0`|

### websocket_client


|`websocket_client` version|jupyter-server modules that include it|
| --- | --- |
|1.8.0|`jupyter-server/2.14.2-GCCcore-13.3.0`|

### widgetsnbextension


|`widgetsnbextension` version|jupyter-server modules that include it|
| --- | --- |
|4.0.13|`jupyter-server/2.14.2-GCCcore-13.3.0`|
|4.0.8|`jupyter-server/2.7.2-GCCcore-12.3.0`|