---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: " Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing\
    \ reads\n to long reference sequences. It is particularly good at aligning reads\
    \ of about 50 up to 100s or 1,000s\n of characters, and particularly good at aligning\
    \ to relatively long (e.g. mammalian) genomes.\n Bowtie 2 indexes the genome with\
    \ an FM Index to keep its memory footprint small: for the human genome,\n its\
    \ memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local,\
    \ and paired-end alignment modes."
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
  softwareVersion: '[''2.5.1'']'
  url: https://bowtie-bio.sourceforge.net/bowtie2/index.shtml
---
# Bowtie2


 Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads
 to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s
 of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes.
 Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome,
 its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.

<small>homepage: </small><span class="software-link">[https://bowtie-bio.sourceforge.net/bowtie2/index.shtml](https://bowtie-bio.sourceforge.net/bowtie2/index.shtml)</span>

## Available installations


|Bowtie2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Bowtie2/2.5.1-GCC-12.2.0`|