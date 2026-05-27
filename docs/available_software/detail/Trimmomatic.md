---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Trimmomatic performs a variety of useful trimming tasks for illumina\n\
    \ paired-end and single ended data.The selection of trimming steps and their associated\n\
    \ parameters are supplied on the command line. "
  license: Not confirmed
  name: Trimmomatic
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
  softwareVersion: '[''0.39'']'
  url: http://www.usadellab.org/cms/?page=trimmomatic
---
# Trimmomatic


Trimmomatic performs a variety of useful trimming tasks for illumina
 paired-end and single ended data.The selection of trimming steps and their associated
 parameters are supplied on the command line. 

<small>homepage: </small><span class="software-link">[http://www.usadellab.org/cms/?page=trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)</span>

## Available installations


|Trimmomatic version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.39|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Trimmomatic/0.39-Java-11`|