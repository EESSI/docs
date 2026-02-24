# dlb



DLB is a dynamic library designed to speed up HPC hybrid applications (i.e.,
two levels of parallelism) by improving the load balance of the outer level of
parallelism (e.g., MPI) by dynamically redistributing the computational
resources at the inner level of parallelism (e.g., OpenMP). at run time.


<small>homepage: </small><span class="software-link">[https://pm.bsc.es/dlb/](https://pm.bsc.es/dlb/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|3.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`dlb/3.4-gompi-2023b`|

## Extensions

Overview of extensions included in dlb installations
