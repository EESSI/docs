---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The bdbag utilities are a collection of software programs for

    working with BagIt packages that conform to the Bagit and Bagit/RO profiles.'
  license: Not confirmed
  name: BDBag
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
  softwareVersion: '[''1.8.0'']'
  url: https://github.com/fair-research/bdbag
---
# BDBag


The bdbag utilities are a collection of software programs for
working with BagIt packages that conform to the Bagit and Bagit/RO profiles.

<small>homepage: </small><span class="software-link">[https://github.com/fair-research/bdbag](https://github.com/fair-research/bdbag)</span>

## Available installations


|BDBag version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.8.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BDBag/1.8.0-foss-2025a`|

## Extensions

Overview of extensions included in BDBag installations


### bagit


|`bagit` version|BDBag modules that include it|
| --- | --- |
|1.9.0|`BDBag/1.8.0-foss-2025a`|

### bagit_profile


|`bagit_profile` version|BDBag modules that include it|
| --- | --- |
|1.3.1|`BDBag/1.8.0-foss-2025a`|

### bdbag


|`bdbag` version|BDBag modules that include it|
| --- | --- |
|1.8.0|`BDBag/1.8.0-foss-2025a`|

### tzlocal


|`tzlocal` version|BDBag modules that include it|
| --- | --- |
|5.3.1|`BDBag/1.8.0-foss-2025a`|