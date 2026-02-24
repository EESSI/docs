# MAQAO


MAQAO (Modular Assembly Quality Analyzer and Optimizer) is a performance
analysis and optimization framework operating at binary level with a focus on core
performance. Its main goal of is to guide application developers along the optimization
process through synthetic reports and hints.

MAQAO mixes both dynamic and static analyses based on its ability to reconstruct high
level structures such as functions and loops from an application binary. Since MAQAO
operates at binary level, it is agnostic with regard to the language used in the source
code and does not require recompiling the application to perform analyses.

<small>homepage: </small><span class="software-link">[https://maqao.org](https://maqao.org)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.21.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`MAQAO/2.21.1`|

## Extensions

Overview of extensions included in MAQAO installations
