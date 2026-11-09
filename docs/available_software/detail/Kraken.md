---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Kraken is a system for assigning taxonomic labels to short DNA sequences,\n\
    \ usually obtained through metagenomic studies. Previous attempts by other\n bioinformatics\
    \ software to accomplish this task have often used sequence\n alignment or machine\
    \ learning techniques that were quite slow, leading to\n the development of less\
    \ sensitive but much faster abundance estimation\n programs. Kraken aims to achieve\
    \ high sensitivity and high speed by\n utilizing exact alignments of k-mers and\
    \ a novel classification algorithm."
  license: Not confirmed
  name: Kraken
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
  softwareVersion: '[''1.1.1'']'
  url: https://ccb.jhu.edu/software/kraken/
---
# Kraken


Kraken is a system for assigning taxonomic labels to short DNA sequences,
 usually obtained through metagenomic studies. Previous attempts by other
 bioinformatics software to accomplish this task have often used sequence
 alignment or machine learning techniques that were quite slow, leading to
 the development of less sensitive but much faster abundance estimation
 programs. Kraken aims to achieve high sensitivity and high speed by
 utilizing exact alignments of k-mers and a novel classification algorithm.

<small>homepage: </small><span class="software-link">[https://ccb.jhu.edu/software/kraken/](https://ccb.jhu.edu/software/kraken/)</span>

## Available installations


|Kraken version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Kraken/1.1.1-GCCcore-14.3.0`|