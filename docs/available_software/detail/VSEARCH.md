---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "VSEARCH supports de novo and reference based chimera detection,\n\
    \ clustering, full-length and prefix dereplication, rereplication,\n reverse complementation,\
    \ masking, all-vs-all pairwise global alignment,\n exact and global alignment\
    \ searching, shuffling, subsampling and sorting.\n It also supports FASTQ file\
    \ analysis, filtering,\n conversion and merging of paired-end reads."
  license: Not confirmed
  name: VSEARCH
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
  softwareVersion: '[''2.30.0'']'
  url: https://github.com/torognes/vsearch
---
# VSEARCH


VSEARCH supports de novo and reference based chimera detection,
 clustering, full-length and prefix dereplication, rereplication,
 reverse complementation, masking, all-vs-all pairwise global alignment,
 exact and global alignment searching, shuffling, subsampling and sorting.
 It also supports FASTQ file analysis, filtering,
 conversion and merging of paired-end reads.

<small>homepage: </small><span class="software-link">[https://github.com/torognes/vsearch](https://github.com/torognes/vsearch)</span>

## Available installations


|VSEARCH version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.30.0|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`VSEARCH/2.30.0-GCC-13.2.0`|