---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Samtools is a suite of programs for interacting with high-throughput\
    \ sequencing data.\n BCFtools - Reading/writing BCF2/VCF/gVCF files and calling/filtering/summarising\
    \ SNP and short indel sequence\n variants"
  license: Not confirmed
  name: BCFtools
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
  softwareVersion: '[''1.22'']'
  url: https://www.htslib.org/
---
# BCFtools


Samtools is a suite of programs for interacting with high-throughput sequencing data.
 BCFtools - Reading/writing BCF2/VCF/gVCF files and calling/filtering/summarising SNP and short indel sequence
 variants

<small>homepage: </small><span class="software-link">[https://www.htslib.org/](https://www.htslib.org/)</span>

## Available installations


|BCFtools version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.22|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BCFtools/1.22-GCC-14.3.0`|