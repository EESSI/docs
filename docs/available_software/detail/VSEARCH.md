# VSEARCH


VSEARCH supports de novo and reference based chimera detection,
 clustering, full-length and prefix dereplication, rereplication,
 reverse complementation, masking, all-vs-all pairwise global alignment,
 exact and global alignment searching, shuffling, subsampling and sorting.
 It also supports FASTQ file analysis, filtering,
 conversion and merging of paired-end reads.

<small>homepage: </small><span class="software-link">[https://github.com/torognes/vsearch](https://github.com/torognes/vsearch)</span>

## Available installations


|VSEARCH version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.30.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`VSEARCH/2.30.0-GCC-13.2.0`|