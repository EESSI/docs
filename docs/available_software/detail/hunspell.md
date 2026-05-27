---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Hunspell is a spell checker and morphological analyzer

    library and program designed for languages with rich morphology and

    complex word compounding or character encoding.'
  license: Not confirmed
  name: hunspell
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
  softwareVersion: '[''1.7.2'']'
  url: https://hunspell.github.io/
---
# hunspell


Hunspell is a spell checker and morphological analyzer
library and program designed for languages with rich morphology and
complex word compounding or character encoding.

<small>homepage: </small><span class="software-link">[https://hunspell.github.io/](https://hunspell.github.io/)</span>

## Available installations


|hunspell version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.7.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`hunspell/1.7.2-GCCcore-12.3.0`|