# FlexiBLAS


FlexiBLAS is a wrapper library that enables the exchange of the BLAS and LAPACK implementation
used by a program without recompiling or relinking it.

<small>homepage: </small><span class="software-link">[https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release](https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release)</span>

## Available installations


|FlexiBLAS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.2.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`FlexiBLAS/3.2.1-GCC-12.2.0`|
|3.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`FlexiBLAS/3.3.1-GCC-12.3.0`|
|3.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`FlexiBLAS/3.3.1-GCC-13.2.0`|
|3.4.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.4-GCC-13.3.0`|
|3.4.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.5-GCC-14.2.0`|
|3.4.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.5-GCC-14.3.0`|
|3.4.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.5-llvm-compilers-20.1.8`|

## Extensions

Overview of extensions included in FlexiBLAS installations


### FlexiBLAS


|`FlexiBLAS` version|FlexiBLAS modules that include it|
| --- | --- |
|3.2.1|`FlexiBLAS/3.2.1-GCC-12.2.0`|
|3.3.1|`FlexiBLAS/3.3.1-GCC-12.3.0`<br/>`FlexiBLAS/3.3.1-GCC-13.2.0`|
|3.4.4|`FlexiBLAS/3.4.4-GCC-13.3.0`|
|3.4.5|`FlexiBLAS/3.4.5-GCC-14.3.0`<br/>`FlexiBLAS/3.4.5-llvm-compilers-20.1.8`<br/>`FlexiBLAS/3.4.5-GCC-14.2.0`|

### LAPACK


|`LAPACK` version|FlexiBLAS modules that include it|
| --- | --- |
|3.10.1|`FlexiBLAS/3.2.1-GCC-12.2.0`|
|3.11.0|`FlexiBLAS/3.3.1-GCC-12.3.0`<br/>`FlexiBLAS/3.3.1-GCC-13.2.0`|
|3.12.0|`FlexiBLAS/3.4.4-GCC-13.3.0`<br/>`FlexiBLAS/3.4.5-GCC-14.2.0`|
|3.12.1|`FlexiBLAS/3.4.5-GCC-14.3.0`<br/>`FlexiBLAS/3.4.5-llvm-compilers-20.1.8`|