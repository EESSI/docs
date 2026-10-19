---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: SMC++ is a program for estimating the size history of populations from
    whole genome sequence data.
  license: Not confirmed
  name: SMC++
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
  softwareVersion: '[''1.15.4'']'
  url: https://github.com/popgenmethods/smcpp
---
# SMC++


SMC++ is a program for estimating the size history of populations from whole genome sequence data.

<small>homepage: </small><span class="software-link">[https://github.com/popgenmethods/smcpp](https://github.com/popgenmethods/smcpp)</span>

## Available installations


|SMC++ version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.15.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`SMC++/1.15.4-gfbf-2025b`|

## Extensions

Overview of extensions included in SMC++ installations


### smcpp


|`smcpp` version|SMC++ modules that include it|
| --- | --- |
|1.15.4|`SMC++/1.15.4-gfbf-2025b`|