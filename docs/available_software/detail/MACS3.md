---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Model Based Analysis for ChIP-Seq data
  license: Not confirmed
  name: MACS3
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
  softwareVersion: '[''3.0.3'']'
  url: https://macs3-project.github.io/MACS/
---
# MACS3


Model Based Analysis for ChIP-Seq data

<small>homepage: </small><span class="software-link">[https://macs3-project.github.io/MACS/](https://macs3-project.github.io/MACS/)</span>

## Available installations


|MACS3 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MACS3/3.0.3-gfbf-2024a`|

## Extensions

Overview of extensions included in MACS3 installations


### cykhash


|`cykhash` version|MACS3 modules that include it|
| --- | --- |
|2.0.1|`MACS3/3.0.3-gfbf-2024a`|

### macs3


|`macs3` version|MACS3 modules that include it|
| --- | --- |
|3.0.3|`MACS3/3.0.3-gfbf-2024a`|