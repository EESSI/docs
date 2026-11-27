---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    A package for the extension of repetitive DNA cores. The RepeatAfterMe RAMExtend
    tool automatically

    extends a multiple sequence alignment (MSA) that may represent only a fragment
    of a longer repetitive

    sequence family.

    '
  license: Not confirmed
  name: RepeatAfterMe
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
  softwareVersion: '[''0.0.7'']'
  url: https://github.com/Dfam-consortium/RepeatAfterMe
---
# RepeatAfterMe



A package for the extension of repetitive DNA cores. The RepeatAfterMe RAMExtend tool automatically
extends a multiple sequence alignment (MSA) that may represent only a fragment of a longer repetitive
sequence family.


<small>homepage: </small><span class="software-link">[https://github.com/Dfam-consortium/RepeatAfterMe](https://github.com/Dfam-consortium/RepeatAfterMe)</span>

## Available installations


|RepeatAfterMe version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.0.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`RepeatAfterMe/0.0.7-GCC-14.2.0`|