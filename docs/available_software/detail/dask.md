---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Dask natively scales Python. Dask provides advanced parallelism for
    analytics, enabling performance at scale for the tools you love.
  license: Not confirmed
  name: dask
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
  softwareVersion: '[''dask/2023.7.1-foss-2022b'', ''dask/2023.9.2-foss-2023a'']'
  url: https://dask.org/
---

dask
====


Dask natively scales Python. Dask provides advanced parallelism for analytics, enabling performance at scale for the tools you love.

https://dask.org/
# Available modules


The overview below shows which dask installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using dask, load one of these modules using a `module load` command like:

```shell
module load dask/2023.9.2-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|dask/2023.9.2-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|dask/2023.7.1-foss-2022b|x|-|x|x|x|x|x|x|x|x|x|x|x|x|


### dask/2023.9.2-foss-2023a

This is a list of extensions included in the module:

dask-2023.9.2, dask-jobqueue-0.8.2, dask-mpi-2022.4.0, distributed-2023.9.2, docrep-0.3.2, HeapDict-1.0.1, locket-1.0.0, partd-1.4.0, tblib-2.0.0, toolz-0.12.0, zict-3.0.0

### dask/2023.7.1-foss-2022b

This is a list of extensions included in the module:

dask-2023.7.1, dask-jobqueue-0.8.2, dask-mpi-2022.4.0, distributed-2023.7.1, docrep-0.3.2, HeapDict-1.0.1, locket-1.0.0, partd-1.4.0, tblib-2.0.0, toolz-0.12.0, versioneer-0.29, zict-3.0.0