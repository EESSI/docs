---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Genome Analysis Toolkit or GATK is a software package developed
    at the Broad Institute to analyse next-generation resequencing data. The toolkit
    offers a wide variety of tools, with a primary focus on variant discovery and
    genotyping as well as strong emphasis on data quality assurance. Its robust architecture,
    powerful processing engine and high-performance computing features make it capable
    of taking on projects of any size.
  license: Not confirmed
  name: GATK
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
  softwareVersion: '[''GATK/4.5.0.0-GCCcore-12.3.0-Java-17'']'
  url: https://www.broadinstitute.org/gatk/
---

GATK
====


The Genome Analysis Toolkit or GATK is a software package developed at the Broad Institute to analyse next-generation resequencing data. The toolkit offers a wide variety of tools, with a primary focus on variant discovery and genotyping as well as strong emphasis on data quality assurance. Its robust architecture, powerful processing engine and high-performance computing features make it capable of taking on projects of any size.

https://www.broadinstitute.org/gatk/
# Available modules


The overview below shows which GATK installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GATK, load one of these modules using a `module load` command like:

```shell
module load GATK/4.5.0.0-GCCcore-12.3.0-Java-17
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GATK/4.5.0.0-GCCcore-12.3.0-Java-17|x|x|x|-|x|x|x|x|x|x|x|x|
