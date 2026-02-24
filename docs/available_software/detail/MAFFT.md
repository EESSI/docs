# MAFFT


MAFFT is a multiple sequence alignment program for unix-like operating systems.
It offers a range of multiple alignment methods, L-INS-i (accurate; for alignment
of <∼200 sequences), FFT-NS-2 (fast; for alignment of <∼30,000 sequences), etc.

<small>homepage: </small><span class="software-link">[https://mafft.cbrc.jp/alignment/software/source.html](https://mafft.cbrc.jp/alignment/software/source.html)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|7.505|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MAFFT/7.505-GCC-12.2.0-with-extensions`|
|7.520|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MAFFT/7.520-GCC-12.3.0-with-extensions`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://mafft.cbrc.jp/alignment/software/source.html', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCC', 'version': '12.2.0'}, 'toolchain_families_compatibility': ['2022b_foss'], 'module': {'full_module_name': 'MAFFT/7.505-GCC-12.2.0-with-extensions', 'module_name': 'MAFFT', 'module_version': '7.505-GCC-12.2.0-with-extensions'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.2.0', 'module_name': 'GCCcore', 'module_version': '12.2.0'}, {'full_module_name': 'GCC/12.2.0', 'module_name': 'GCC', 'module_version': '12.2.0'}, {'full_module_name': 'MAFFT/7.505-GCC-12.2.0-with-extensions', 'module_name': 'MAFFT', 'module_version': '7.505-GCC-12.2.0-with-extensions'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'MAFFT is a multiple sequence alignment program for unix-like operating systems.\nIt offers a range of multiple alignment methods, L-INS-i (accurate; for alignment\nof <∼200 sequences), FFT-NS-2 (fast; for alignment of <∼30,000 sequences), etc.', 'version': '7.505', 'versionsuffix': '-with-extensions', 'extensions': [{'type': 'component', 'name': 'MAFFT', 'version': '7.505'}, {'type': 'component', 'name': 'MAFFT Extensions', 'version': '7.505'}]}, {'homepage': 'https://mafft.cbrc.jp/alignment/software/source.html', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCC', 'version': '12.3.0'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'MAFFT/7.520-GCC-12.3.0-with-extensions', 'module_name': 'MAFFT', 'module_version': '7.520-GCC-12.3.0-with-extensions'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'MAFFT/7.520-GCC-12.3.0-with-extensions', 'module_name': 'MAFFT', 'module_version': '7.520-GCC-12.3.0-with-extensions'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'MAFFT is a multiple sequence alignment program for unix-like operating systems.\nIt offers a range of multiple alignment methods, L-INS-i (accurate; for alignment\nof <∼200 sequences), FFT-NS-2 (fast; for alignment of <∼30,000 sequences), etc.', 'version': '7.520', 'versionsuffix': '-with-extensions', 'extensions': [{'type': 'component', 'name': 'MAFFT', 'version': '7.520'}, {'type': 'component', 'name': 'MAFFT Extensions', 'version': '7.520'}]}], 'homepage': 'https://mafft.cbrc.jp/alignment/software/source.html', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'MAFFT is a multiple sequence alignment program for unix-like operating systems.\nIt offers a range of multiple alignment methods, L-INS-i (accurate; for alignment\nof <∼200 sequences), FFT-NS-2 (fast; for alignment of <∼30,000 sequences), etc.'} installations


### MAFFT


|`MAFFT` version|MAFFT modules that include it|
| --- | --- |
|7.505|`MAFFT/7.505-GCC-12.2.0-with-extensions`|
|7.520|`MAFFT/7.520-GCC-12.3.0-with-extensions`|

### MAFFT Extensions


|`MAFFT Extensions` version|MAFFT modules that include it|
| --- | --- |
|7.505|`MAFFT/7.505-GCC-12.2.0-with-extensions`|
|7.520|`MAFFT/7.520-GCC-12.3.0-with-extensions`|