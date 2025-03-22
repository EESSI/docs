---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Extrae is the package devoted to generate Paraver trace-files for a
    post-mortem analysis.Extrae is a tool that uses different interposition mechanisms
    to inject probes into the target applicationso as to gather information regarding
    the application performance.
  license: Not confirmed
  name: Extrae
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
  softwareVersion: '[''Extrae/4.2.0-gompi-2023b'']'
  url: https://tools.bsc.es/extrae
---

Extrae
======


Extrae is the package devoted to generate Paraver trace-files for a post-mortem analysis.Extrae is a tool that uses different interposition mechanisms to inject probes into the target applicationso as to gather information regarding the application performance.

https://tools.bsc.es/extrae
# Available modules


The overview below shows which Extrae installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Extrae, load one of these modules using a `module load` command like:

```shell
module load Extrae/4.2.0-gompi-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Extrae/4.2.0-gompi-2023b|x|x|x|-|x|x|x|x|x|x|x|
