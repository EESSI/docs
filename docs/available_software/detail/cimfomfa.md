# cimfomfa


This library supports both MCL, a cluster algorithm for graphs, and zoem, a
macro/DSL language. It supplies abstractions for memory management, I/O,
associative arrays, strings, heaps, and a few other things. The string library
has had heavy testing as part of zoem. Both understandably and regrettably I
chose long ago to make it C-string-compatible, hence nul bytes may not be part
of a string. At some point I hope to rectify this, perhaps unrealistically.

<small>homepage: </small><span class="software-link">[https://github.com/micans/cimfomfa](https://github.com/micans/cimfomfa)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|22.273|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`cimfomfa/22.273-GCCcore-12.3.0`|

## Extensions

Overview of extensions included in cimfomfa installations
