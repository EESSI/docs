# pigz



 pigz, which stands for parallel implementation of gzip, is a fully
 functional replacement for gzip that exploits multiple processors and multiple
 cores to the hilt when compressing data. pigz was written by Mark Adler, and
 uses the zlib and pthread libraries.


<small>homepage: </small><span class="software-link">[https://zlib.net/pigz/](https://zlib.net/pigz/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`pigz/2.8-GCCcore-13.2.0`|