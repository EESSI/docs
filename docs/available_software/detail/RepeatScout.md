---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "De Novo Repeat Finder, Price A.L., Jones N.C. and Pevzner P.A. Developed\
    \ and\n tested with our multiple sequence version of RepeatScout ( 1.0.6 )"
  license: Not confirmed
  name: RepeatScout
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
  softwareVersion: '[''1.0.7'']'
  url: https://github.com/Dfam-consortium/RepeatScout
---
# RepeatScout


De Novo Repeat Finder, Price A.L., Jones N.C. and Pevzner P.A. Developed and
 tested with our multiple sequence version of RepeatScout ( 1.0.6 )

<small>homepage: </small><span class="software-link">[https://github.com/Dfam-consortium/RepeatScout](https://github.com/Dfam-consortium/RepeatScout)</span>

## Available installations


|RepeatScout version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`RepeatScout/1.0.7-GCC-14.2.0`|