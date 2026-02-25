# SIONlib



 SIONlib is a scalable I/O library for parallel access to task-local files.
 The library not only supports writing and reading binary data to or from
 several thousands of processors into a single or a small number of physical
 files, but also provides global open and close functions to access SIONlib
 files in parallel. This package provides a stripped-down installation of
 SIONlib for use with performance tools (e.g., Score-P), with renamed symbols
 to avoid conflicts when an application using SIONlib itself is linked against
 a tool requiring a different SIONlib version.


<small>homepage: </small><span class="software-link">[https://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/SIONlib/_node.html](https://www.fz-juelich.de/ias/jsc/EN/Expertise/Support/Software/SIONlib/_node.html)</span>

## Available installations


|SIONlib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.7.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`SIONlib/1.7.7-GCCcore-13.2.0-tools`|
|1.7.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`SIONlib/1.7.7-GCCcore-14.2.0-tools`|