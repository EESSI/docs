---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Scanpy is a scalable toolkit for analyzing single-cell gene expression
    data built jointly with anndata. It includes preprocessing, visualization, clustering,
    trajectory inference and differential expression testing. The Python-based implementation
    efficiently deals with datasets of more than one million cells.
  license: Not confirmed
  name: scanpy
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
  softwareVersion: '[''scanpy/1.9.8-foss-2023a'']'
  url: https://scanpy.readthedocs.io/en/stable/
---

scanpy
======


Scanpy is a scalable toolkit for analyzing single-cell gene expression data built jointly with anndata. It includes preprocessing, visualization, clustering, trajectory inference and differential expression testing. The Python-based implementation efficiently deals with datasets of more than one million cells.

https://scanpy.readthedocs.io/en/stable/
# Available modules


The overview below shows which scanpy installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using scanpy, load one of these modules using a `module load` command like:

```shell
module load scanpy/1.9.8-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|scanpy/1.9.8-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### scanpy/1.9.8-foss-2023a

This is a list of extensions included in the module:

joblib-1.3.2, legacy_api_wrap-1.4, natsort-8.4.0, packaging-23.2, scanpy-1.9.8, session-info-1.0.0, stdlib_list-0.10.0