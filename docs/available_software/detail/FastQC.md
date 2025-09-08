---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: FastQC is a quality control application for high throughputsequence
    data. It reads in sequence data in a variety of formats and can eitherprovide
    an interactive application to review the results of several differentQC checks,
    or create an HTML based report which can be integrated into apipeline.
  license: Not confirmed
  name: FastQC
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
  softwareVersion: '[''FastQC/0.12.1-Java-11'']'
  url: https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
---

FastQC
======


FastQC is a quality control application for high throughputsequence data. It reads in sequence data in a variety of formats and can eitherprovide an interactive application to review the results of several differentQC checks, or create an HTML based report which can be integrated into apipeline.

https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
# Available modules


The overview below shows which FastQC installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using FastQC, load one of these modules using a `module load` command like:

```shell
module load FastQC/0.12.1-Java-11
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|FastQC/0.12.1-Java-11|x|x|x|x|x|x|x|x|x|x|x|x|x|
