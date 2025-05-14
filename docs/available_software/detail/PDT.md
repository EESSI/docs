---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Program Database Toolkit (PDT) is a framework for analyzing source
    code written in several programming languages and for making rich program knowledge
    accessible to developers of static and dynamic analysis tools. PDT implements
    a standard program representation, the program database (PDB), that can be accessed
    in a uniform way through a class library supporting common PDB operations.
  license: Not confirmed
  name: PDT
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
  softwareVersion: '[''PDT/3.25.2-GCCcore-13.2.0'']'
  url: https://www.cs.uoregon.edu/research/pdt/
---

PDT
===


Program Database Toolkit (PDT) is a framework for analyzing source code written in several programming languages and for making rich program knowledge accessible to developers of static and dynamic analysis tools. PDT implements a standard program representation, the program database (PDB), that can be accessed in a uniform way through a class library supporting common PDB operations.

https://www.cs.uoregon.edu/research/pdt/
# Available modules


The overview below shows which PDT installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PDT, load one of these modules using a `module load` command like:

```shell
module load PDT/3.25.2-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PDT/3.25.2-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
