# Bowtie2


 Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads
 to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s
 of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes.
 Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome,
 its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.

<small>homepage: </small><span class="software-link">[https://bowtie-bio.sourceforge.net/bowtie2/index.shtml](https://bowtie-bio.sourceforge.net/bowtie2/index.shtml)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Bowtie2/2.5.1-GCC-12.2.0`|