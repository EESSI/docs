# GATK


The Genome Analysis Toolkit or GATK is a software package developed at the Broad Institute
 to analyse next-generation resequencing data. The toolkit offers a wide variety of tools,
 with a primary focus on variant discovery and genotyping as well as strong emphasis on
 data quality assurance. Its robust architecture, powerful processing engine and
 high-performance computing features make it capable of taking on projects of any size.

<small>homepage: </small><span class="software-link">[https://www.broadinstitute.org/gatk/](https://www.broadinstitute.org/gatk/)</span>

## Available installations


|GATK version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.5.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`GATK/4.5.0.0-GCCcore-12.3.0-Java-17`|