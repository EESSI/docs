---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing
    reads to long reference sequences. It is particularly good at aligning reads of
    about 50 up to 100s or 1,000s of characters, and particularly good at aligning
    to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with
    an FM Index to keep its memory footprint small: for the human genome, its memory
    footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end
    alignment modes.'
  license: Not confirmed
  name: Bowtie2
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
  softwareVersion: '[''Bowtie2/2.5.1-GCC-12.2.0'']'
  url: https://bowtie-bio.sourceforge.net/bowtie2/index.shtml
---

Bowtie2
=======


Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.

https://bowtie-bio.sourceforge.net/bowtie2/index.shtml
# Available modules


The overview below shows which Bowtie2 installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Bowtie2, load one of these modules using a `module load` command like:

```shell
module load Bowtie2/2.5.1-GCC-12.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Bowtie2/2.5.1-GCC-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
