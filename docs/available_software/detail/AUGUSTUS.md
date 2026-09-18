---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: AUGUSTUS is a program that predicts genes in eukaryotic genomic sequences
  license: Not confirmed
  name: AUGUSTUS
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
  softwareVersion: '[''3.5.0'']'
  url: https://bioinf.uni-greifswald.de/augustus/
---
# AUGUSTUS


AUGUSTUS is a program that predicts genes in eukaryotic genomic sequences

<small>homepage: </small><span class="software-link">[https://bioinf.uni-greifswald.de/augustus/](https://bioinf.uni-greifswald.de/augustus/)</span>

## Available installations


|AUGUSTUS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.5.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`AUGUSTUS/3.5.0-foss-2025b`|