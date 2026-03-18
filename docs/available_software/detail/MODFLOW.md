---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\nMODFLOW is the USGS's modular hydrologic model. MODFLOW is considered\
    \ an\n international standard for simulating and predicting groundwater conditions\n\
    \ and groundwater/surface-water interactions. \n"
  license: Not confirmed
  name: MODFLOW
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
  softwareVersion: '[''6.4.4'']'
  url: https://www.usgs.gov/mission-areas/water-resources/science/modflow-and-related-programs
---
# MODFLOW



MODFLOW is the USGS's modular hydrologic model. MODFLOW is considered an
 international standard for simulating and predicting groundwater conditions
 and groundwater/surface-water interactions. 


<small>homepage: </small><span class="software-link">[https://www.usgs.gov/mission-areas/water-resources/science/modflow-and-related-programs](https://www.usgs.gov/mission-areas/water-resources/science/modflow-and-related-programs)</span>

## Available installations


|MODFLOW version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|6.4.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`MODFLOW/6.4.4-foss-2023a`|