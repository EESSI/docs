# lit


lit is a portable tool for executing LLVM and Clang style test suites, summarizing their results, and
providing indication of failures.

<small>homepage: </small><span class="software-link">[https://llvm.org/docs/CommandGuide/lit.html](https://llvm.org/docs/CommandGuide/lit.html)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|18.1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`lit/18.1.2-GCCcore-12.3.0`|
|18.1.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`lit/18.1.7-GCCcore-13.2.0`|
|18.1.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`lit/18.1.7-GCCcore-13.3.0`|
|18.1.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`lit/18.1.8-GCCcore-13.3.0`|
|18.1.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`lit/18.1.8-GCCcore-14.2.0`|
|18.1.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`lit/18.1.8-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in lit installations


### lit


|`lit` version|lit modules that include it|
| --- | --- |
|18.1.2|`lit/18.1.2-GCCcore-12.3.0`|
|18.1.7|`lit/18.1.7-GCCcore-13.2.0`<br/>`lit/18.1.7-GCCcore-13.3.0`|
|18.1.8|`lit/18.1.8-GCCcore-14.3.0`<br/>`lit/18.1.8-GCCcore-13.3.0`<br/>`lit/18.1.8-GCCcore-14.2.0`|

### pexpect


|`pexpect` version|lit modules that include it|
| --- | --- |
|4.9.0|`lit/18.1.7-GCCcore-13.3.0`<br/>`lit/18.1.7-GCCcore-13.2.0`<br/>`lit/18.1.8-GCCcore-13.3.0`<br/>`lit/18.1.8-GCCcore-14.2.0`<br/>`lit/18.1.8-GCCcore-14.3.0`|

### ptyprocess


|`ptyprocess` version|lit modules that include it|
| --- | --- |
|0.7.0|`lit/18.1.7-GCCcore-13.3.0`<br/>`lit/18.1.7-GCCcore-13.2.0`<br/>`lit/18.1.8-GCCcore-13.3.0`<br/>`lit/18.1.8-GCCcore-14.2.0`<br/>`lit/18.1.8-GCCcore-14.3.0`|