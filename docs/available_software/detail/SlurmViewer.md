---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: View the status of a Slurm cluster, including nodes and queue.
  license: Not confirmed
  name: SlurmViewer
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
  softwareVersion: '[''SlurmViewer/1.0.1-GCCcore-13.2.0'']'
  url: https://gitlab.com/lkeb/slurm_viewer
---

SlurmViewer
===========


View the status of a Slurm cluster, including nodes and queue.

https://gitlab.com/lkeb/slurm_viewer
# Available modules


The overview below shows which SlurmViewer installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using SlurmViewer, load one of these modules using a `module load` command like:

```shell
module load SlurmViewer/1.0.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|SlurmViewer/1.0.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|


### SlurmViewer/1.0.1-GCCcore-13.2.0

This is a list of extensions included in the module:

asyncssh-2.18.0, plotext-5.2.8, slurm-viewer-1.0.1, textual-0.85.2, textual-plotext-0.2.1