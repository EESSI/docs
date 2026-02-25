# numba


Numba is an Open Source NumPy-aware optimizing compiler for
Python sponsored by Continuum Analytics, Inc. It uses the remarkable LLVM
compiler infrastructure to compile Python syntax to machine code.

<small>homepage: </small><span class="software-link">[https://numba.pydata.org/](https://numba.pydata.org/)</span>

## Available installations


|numba version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.58.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`numba/0.58.1-foss-2023a`|

## Extensions

Overview of extensions included in numba installations


### llvmlite


|`llvmlite` version|numba modules that include it|
| --- | --- |
|0.41.1|`numba/0.58.1-foss-2023a`|

### numba


|`numba` version|numba modules that include it|
| --- | --- |
|0.58.1|`numba/0.58.1-foss-2023a`|