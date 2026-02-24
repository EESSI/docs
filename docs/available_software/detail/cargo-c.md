# cargo-c


Applet for cargo to build and install C-ABI compatible dynamic and static
libraries. It produces and installs a correct pkg-config file, a static library
and a dynamic library, and a C header to be used by any C (and C-compatible)
software.

<small>homepage: </small><span class="software-link">[https://github.com/lu-zero/cargo-c](https://github.com/lu-zero/cargo-c)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.10.15|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`cargo-c/0.10.15-GCCcore-14.3.0`|
|0.9.32|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`cargo-c/0.9.32-GCCcore-13.3.0`|