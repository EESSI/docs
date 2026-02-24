# robin-map


robin-map is a C++ implementation of a fast and memory efficient hash table.
It is based on Robin Hood hashing with backward shift deletion.

<small>homepage: </small><span class="software-link">[https://github.com/Tessil/robin-map](https://github.com/Tessil/robin-map)</span>

## Available installations


|robin-map version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`robin-map/1.3.0-GCCcore-13.2.0`|