---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: WhatsHap is a software for phasing genomic variants using DNAsequencing
    reads, also called read-based phasing or haplotype assembly. It isespecially suitable
    for long reads, but works also well with short reads.
  license: Not confirmed
  name: WhatsHap
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
  softwareVersion: '[''WhatsHap/2.1-foss-2022b'', ''WhatsHap/2.2-foss-2023a'']'
  url: https://whatshap.readthedocs.io
---

WhatsHap
========


WhatsHap is a software for phasing genomic variants using DNAsequencing reads, also called read-based phasing or haplotype assembly. It isespecially suitable for long reads, but works also well with short reads.

https://whatshap.readthedocs.io
# Available modules


The overview below shows which WhatsHap installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using WhatsHap, load one of these modules using a `module load` command like:

```shell
module load WhatsHap/2.2-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|WhatsHap/2.2-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|WhatsHap/2.1-foss-2022b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### WhatsHap/2.2-foss-2023a

This is a list of extensions included in the module:

PuLP-2.8.0, whatshap-2.2, xopen-1.7.0

### WhatsHap/2.1-foss-2022b

This is a list of extensions included in the module:

pulp-2.8.0, WhatsHap-2.1, xopen-1.7.0