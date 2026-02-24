# Osi


Osi (Open Solver Interface) provides an abstract base class to a generic linear
programming (LP) solver, along with derived classes for specific solvers. Many
applications may be able to use the Osi to insulate themselves from a specific
LP solver. That is, programs written to the OSI standard may be linked to any
solver with an OSI interface and should produce correct results. The OSI has
been significantly extended compared to its first incarnation. Currently, the
OSI supports linear programming solvers and has rudimentary support for integer
programming.

<small>homepage: </small><span class="software-link">[https://github.com/coin-or/Osi](https://github.com/coin-or/Osi)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.108.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Osi/0.108.9-GCC-12.3.0`|
|0.108.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Osi/0.108.9-GCC-13.2.0`|
|0.108.11|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Osi/0.108.11-GCC-13.3.0`|

## Extensions

Overview of extensions included in Osi installations
