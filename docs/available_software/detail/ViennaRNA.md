---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The Vienna RNA Package consists of a C code library and several

    stand-alone programs for the prediction and comparison of RNA secondary structures.'
  license: Not confirmed
  name: ViennaRNA
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
  softwareVersion: '[''2.7.2'']'
  url: https://www.tbi.univie.ac.at/RNA/
---
# ViennaRNA


The Vienna RNA Package consists of a C code library and several
stand-alone programs for the prediction and comparison of RNA secondary structures.

<small>homepage: </small><span class="software-link">[https://www.tbi.univie.ac.at/RNA/](https://www.tbi.univie.ac.at/RNA/)</span>

## Available installations


|ViennaRNA version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.7.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ViennaRNA/2.7.2-gfbf-2025b`|