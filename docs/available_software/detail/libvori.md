# libvori


C++ library implementing the Voronoi integration as well as the compressed bqb
file format. The present version of libvori is a very early development
version, which is hard-coded to work with the CP2k program package.

<small>homepage: </small><span class="software-link">[https://brehm-research.de/libvori.php](https://brehm-research.de/libvori.php)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|220621|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`libvori/220621-GCCcore-12.3.0`|