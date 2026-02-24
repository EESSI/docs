# amdahl


This Python module contains a pseudo-application that can be used as a black
box to reproduce Amdahl's Law. It does not do real calculations, nor any real
communication, so can easily be overloaded.


<small>homepage: </small><span class="software-link">[https://github.com/hpc-carpentry/amdahl](https://github.com/hpc-carpentry/amdahl)</span>

## Available installations


|amdahl version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`amdahl/0.3.1-gompi-2023a`|