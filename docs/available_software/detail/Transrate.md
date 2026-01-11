---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Transrate is software for de-novo transcriptome assembly quality analysis.
    It examines your assembly in detail and compares it to experimental evidence such
    as the sequencing reads, reporting quality scores for contigs and assemblies.
    This allows you to choose between assemblers and parameters, filter out the bad
    contigs from an assembly, and help decide when to stop trying to improve the assembly.
  license: Not confirmed
  name: Transrate
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
  softwareVersion: '[''Transrate/1.0.3-GCC-12.3.0'']'
  url: https://hibberdlab.com/transrate
---

Transrate
=========


Transrate is software for de-novo transcriptome assembly quality analysis. It examines your assembly in detail and compares it to experimental evidence such as the sequencing reads, reporting quality scores for contigs and assemblies. This allows you to choose between assemblers and parameters, filter out the bad contigs from an assembly, and help decide when to stop trying to improve the assembly.

https://hibberdlab.com/transrate
# Available modules


The overview below shows which Transrate installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Transrate, load one of these modules using a `module load` command like:

```shell
module load Transrate/1.0.3-GCC-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Transrate/1.0.3-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
