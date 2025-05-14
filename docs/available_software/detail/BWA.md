---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Burrows-Wheeler Aligner (BWA) is an efficient program that aligns relatively
    short nucleotide sequences against a long reference sequence such as the human
    genome.
  license: Not confirmed
  name: BWA
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
  softwareVersion: '[''BWA/0.7.17-20220923-GCCcore-12.3.0'', ''BWA/0.7.18-GCCcore-12.3.0'']'
  url: http://bio-bwa.sourceforge.net/
---

BWA
===


Burrows-Wheeler Aligner (BWA) is an efficient program that aligns relatively short nucleotide sequences against a long reference sequence such as the human genome.

http://bio-bwa.sourceforge.net/
# Available modules


The overview below shows which BWA installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using BWA, load one of these modules using a `module load` command like:

```shell
module load BWA/0.7.18-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|BWA/0.7.18-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|BWA/0.7.17-20220923-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
