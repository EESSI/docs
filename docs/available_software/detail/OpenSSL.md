# OpenSSL


The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured,
 and Open Source toolchain implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
 protocols as well as a full-strength general purpose cryptography library. 

<small>homepage: </small><span class="software-link">[https://www.openssl.org/](https://www.openssl.org/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`OpenSSL/1.1`|
|3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`OpenSSL/3`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://www.openssl.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'system', 'version': 'system'}, 'toolchain_families_compatibility': ['2022b_foss', '2023a_foss', '2023b_foss'], 'module': {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured,\n and Open Source toolchain implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)\n protocols as well as a full-strength general purpose cryptography library. ', 'version': '1.1', 'versionsuffix': '', 'extensions': [{'type': 'component', 'name': 'OpenSSL', 'version': '1.1.1w'}]}, {'homepage': 'https://www.openssl.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'system', 'version': 'system'}, 'toolchain_families_compatibility': ['2024a_foss', '2025a_foss', '2025b_foss'], 'module': {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured,\n and Open Source toolchain implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)\n protocols as well as a full-strength general purpose cryptography library. ', 'version': '3', 'versionsuffix': '', 'extensions': [{'type': 'component', 'name': 'OpenSSL', 'version': '3.2.1'}]}], 'homepage': 'https://www.openssl.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured,\n and Open Source toolchain implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)\n protocols as well as a full-strength general purpose cryptography library. '} installations


### OpenSSL


|`OpenSSL` version|OpenSSL modules that include it|
| --- | --- |
|1.1.1w|`OpenSSL/1.1`|
|3.2.1|`OpenSSL/3`|