---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "AmberTools consists of several independently developed packages that\
    \ work well by themselves,\n and with Amber itself. The suite can also be used\
    \ to carry out complete molecular dynamics simulations,\n with either explicit\
    \ water or generalized Born solvent models."
  license: Not confirmed
  name: AmberTools
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
  softwareVersion: '[''25.2'', ''23.6'']'
  url: https://ambermd.org/
---
# AmberTools


AmberTools consists of several independently developed packages that work well by themselves,
 and with Amber itself. The suite can also be used to carry out complete molecular dynamics simulations,
 with either explicit water or generalized Born solvent models.

<small>homepage: </small><span class="software-link">[https://ambermd.org/](https://ambermd.org/)</span>

## Available installations


|AmberTools version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|23.6|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`AmberTools/23.6-foss-2023a`|
|25.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`AmberTools/25.2-foss-2025a`|