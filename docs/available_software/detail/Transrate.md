# Transrate


Transrate is software for de-novo transcriptome assembly quality analysis.
 It examines your assembly in detail and compares it to experimental evidence such as the sequencing reads,
 reporting quality scores for contigs and assemblies. This allows you to choose between assemblers and parameters,
 filter out the bad contigs from an assembly, and help decide when to stop trying to improve the assembly.

<small>homepage: </small><span class="software-link">[https://hibberdlab.com/transrate](https://hibberdlab.com/transrate)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Transrate/1.0.3-GCC-12.3.0`|