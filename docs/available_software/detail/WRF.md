---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The Weather Research and Forecasting (WRF) Model is a next-generation\
    \ mesoscale\n numerical weather prediction system designed to serve both operational\
    \ forecasting and atmospheric\n research needs."
  license: Not confirmed
  name: WRF
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
  softwareVersion: '[''4.6.1'']'
  url: https://www.mmm.ucar.edu/models/wrf
---
# WRF


The Weather Research and Forecasting (WRF) Model is a next-generation mesoscale
 numerical weather prediction system designed to serve both operational forecasting and atmospheric
 research needs.

<small>homepage: </small><span class="software-link">[https://www.mmm.ucar.edu/models/wrf](https://www.mmm.ucar.edu/models/wrf)</span>

## Available installations


|WRF version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.6.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`WRF/4.6.1-foss-2024a-dmpar`|