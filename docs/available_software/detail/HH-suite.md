---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The HH-suite is an open-source software package\n for sensitive protein\
    \ sequence searching based on the pairwise\n alignment of hidden Markov models\
    \ (HMMs)."
  license: Not confirmed
  name: HH-suite
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
  softwareVersion: '[''3.3.0-20250812'']'
  url: https://github.com/soedinglab/hh-suite
---
# HH-suite


The HH-suite is an open-source software package
 for sensitive protein sequence searching based on the pairwise
 alignment of hidden Markov models (HMMs).

<small>homepage: </small><span class="software-link">[https://github.com/soedinglab/hh-suite](https://github.com/soedinglab/hh-suite)</span>

## Available installations


|HH-suite version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.3.0-20250812|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`HH-suite/3.3.0-20250812-gompi-2025b`|