# ccache


Ccache (or “ccache”) is a compiler cache. It speeds up recompilation by
caching previous compilations and detecting when the same compilation is being done again

<small>homepage: </small><span class="software-link">[https://ccache.dev/](https://ccache.dev/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|4.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`ccache/4.9-GCCcore-12.3.0`|