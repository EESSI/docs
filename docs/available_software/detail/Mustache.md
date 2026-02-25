# Mustache


Mustache (Multi-scale Detection of Chromatin Loops from Hi-C and Micro-C Maps using
Scale-Space Representation) is a tool for multi-scale detection of chromatin loops from Hi-C and Micro-C
contact maps in high resolutions (10kbp all the way to 500bp and even more).
Mustache uses recent technical advances in scale-space theory in
Computer Vision to detect chromatin loops caused by interaction of DNA segments with a variable size.

<small>homepage: </small><span class="software-link">[https://github.com/ay-lab/mustache](https://github.com/ay-lab/mustache)</span>

## Available installations


|Mustache version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Mustache/1.3.3-foss-2023b`|