---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Snakemake workflow management system is a tool to create reproducible
    and scalable data analyses.
  license: Not confirmed
  name: snakemake
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''snakemake/8.4.2-foss-2023a'']'
  url: https://snakemake.readthedocs.io
---

snakemake
=========


The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.

https://snakemake.readthedocs.io
# Available modules


The overview below shows which snakemake installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using snakemake, load one of these modules using a `module load` command like:

```shell
module load snakemake/8.4.2-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|snakemake/8.4.2-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|


### snakemake/8.4.2-foss-2023a

This is a list of extensions included in the module:

argparse-dataclass-2.0.0, conda-inject-1.3.1, ConfigArgParse-1.7, connection-pool-0.0.3, datrie-0.8.2, dpath-2.1.6, fastjsonschema-2.19.1, humanfriendly-10.0, immutables-0.20, jupyter-core-5.7.1, nbformat-5.9.2, plac-1.4.2, reretry-0.11.8, smart-open-6.4.0, snakemake-8.4.2, snakemake-executor-plugin-cluster-generic-1.0.7, snakemake-executor-plugin-cluster-sync-0.1.3, snakemake-executor-plugin-flux-0.1.0, snakemake-executor-plugin-slurm-0.2.1, snakemake-executor-plugin-slurm-jobstep-0.1.10, snakemake-interface-common-1.15.2, snakemake-interface-executor-plugins-8.2.0, snakemake-interface-storage-plugins-3.0.0, stopit-1.1.2, throttler-1.2.2, toposort-1.10, yte-1.5.4