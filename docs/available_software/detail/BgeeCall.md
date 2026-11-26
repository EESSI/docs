---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Automatic RNA-Seq present/absent gene expression calls generation
  license: Not confirmed
  name: BgeeCall
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
  softwareVersion: '[''1.26.0'']'
  url: https://github.com/BgeeDB/BgeeCall
---
# BgeeCall


Automatic RNA-Seq present/absent gene expression calls generation

<small>homepage: </small><span class="software-link">[https://github.com/BgeeDB/BgeeCall](https://github.com/BgeeDB/BgeeCall)</span>

## Available installations


|BgeeCall version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.26.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BgeeCall/1.26.0-foss-2025a-R-4.5.1`|

## Extensions

Overview of extensions included in BgeeCall installations


### BgeeCall


|`BgeeCall` version|BgeeCall modules that include it|
| --- | --- |
|1.26.0|`BgeeCall/1.26.0-foss-2025a-R-4.5.1`|

### rslurm


|`rslurm` version|BgeeCall modules that include it|
| --- | --- |
|0.6.2|`BgeeCall/1.26.0-foss-2025a-R-4.5.1`|

### sjlabelled


|`sjlabelled` version|BgeeCall modules that include it|
| --- | --- |
|1.2.0|`BgeeCall/1.26.0-foss-2025a-R-4.5.1`|

### sjmisc


|`sjmisc` version|BgeeCall modules that include it|
| --- | --- |
|2.8.11|`BgeeCall/1.26.0-foss-2025a-R-4.5.1`|