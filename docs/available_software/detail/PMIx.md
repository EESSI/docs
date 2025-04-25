---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Process Management for Exascale EnvironmentsPMI Exascale (PMIx) represents
    an attempt toprovide an extended version of the PMI standard specifically designedto
    support clusters up to and including exascale sizes. The overallobjective of the
    project is not to branch the existing pseudo-standarddefinitions - in fact, PMIx
    fully supports both of the existing PMI-1and PMI-2 APIs - but rather to (a) augment
    and extend those APIs toeliminate some current restrictions that impact scalability,
    and (b)provide a reference implementation of the PMI-server that demonstratesthe
    desired level of scalability.
  license: Not confirmed
  name: PMIx
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
  softwareVersion: '[''PMIx/4.2.2-GCCcore-12.2.0'', ''PMIx/4.2.4-GCCcore-12.3.0'',
    ''PMIx/4.2.6-GCCcore-13.2.0'']'
  url: https://pmix.org/
---

PMIx
====


Process Management for Exascale EnvironmentsPMI Exascale (PMIx) represents an attempt toprovide an extended version of the PMI standard specifically designedto support clusters up to and including exascale sizes. The overallobjective of the project is not to branch the existing pseudo-standarddefinitions - in fact, PMIx fully supports both of the existing PMI-1and PMI-2 APIs - but rather to (a) augment and extend those APIs toeliminate some current restrictions that impact scalability, and (b)provide a reference implementation of the PMI-server that demonstratesthe desired level of scalability.

https://pmix.org/
# Available modules


The overview below shows which PMIx installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PMIx, load one of these modules using a `module load` command like:

```shell
module load PMIx/4.2.6-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PMIx/4.2.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|PMIx/4.2.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|PMIx/4.2.2-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
