---
hide:
  - toc
---

MultiQC
=======


Aggregate results from bioinformatics analyses across many samples into a single report. MultiQC searches a given directory for analysis logs and compiles an HTML report. It's a general use tool, perfect for summarising the output from numerous bioinformatics tools.

https://multiqc.info
# Available modules


The overview below shows which MultiQC installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using MultiQC, load one of these modules using a `module load` command like:

```shell
module load MultiQC/1.14-foss-2022b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MultiQC/1.14-foss-2022b|x|x|x|x|x|x|x|x|x|


### MultiQC/1.14-foss-2022b

This is a list of extensions included in the module:

coloredlogs-15.0.1, colormath-3.0.0, commonmark-0.9.1, humanfriendly-10.0, lzstring-1.0.4, Markdown-3.4.1, markdown-it-py-2.1.0, mdurl-0.1.2, multiqc-1.14, Pygments-2.14.0, rich-13.3.1, rich-click-1.6.1, spectra-0.0.11