---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Burrows-Wheeler Aligner (BWA) is an efficient program that aligns\
    \ relatively\n short nucleotide sequences against a long reference sequence such\
    \ as the human\n genome.\n"
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
  softwareVersion: '[''0.7.19'']'
  url: https://bio-bwa.sourceforge.net/
---
# BWA



 Burrows-Wheeler Aligner (BWA) is an efficient program that aligns relatively
 short nucleotide sequences against a long reference sequence such as the human
 genome.


<small>homepage: </small><span class="software-link">[https://bio-bwa.sourceforge.net/](https://bio-bwa.sourceforge.net/)</span>

## Available installations


|BWA version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.7.19|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BWA/0.7.19-GCCcore-14.3.0`|