# Extrae


Extrae is the package devoted to generate Paraver trace-files for a post-mortem analysis.
Extrae is a tool that uses different interposition mechanisms to inject probes into the target application
so as to gather information regarding the application performance.

<small>homepage: </small><span class="software-link">[https://tools.bsc.es/extrae](https://tools.bsc.es/extrae)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|4.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Extrae/4.2.0-gompi-2023b`|