---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Model Based Analysis for ChIP-Seq data
  license: Not confirmed
  name: MACS2
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
  softwareVersion: '[''2.2.9.1'']'
  url: https://github.com/taoliu/MACS
---
# MACS2


Model Based Analysis for ChIP-Seq data

<small>homepage: </small><span class="software-link">[https://github.com/taoliu/MACS](https://github.com/taoliu/MACS)</span>

## Available installations


|MACS2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.2.9.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`MACS2/2.2.9.1-foss-2023b`|

## Extensions

Overview of extensions included in MACS2 installations


### Cython


|`Cython` version|MACS2 modules that include it|
| --- | --- |
|0.29.37|`MACS2/2.2.9.1-foss-2023b`|

### MACS2


|`MACS2` version|MACS2 modules that include it|
| --- | --- |
|2.2.9.1|`MACS2/2.2.9.1-foss-2023b`|