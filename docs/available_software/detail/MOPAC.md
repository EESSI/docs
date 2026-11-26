---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'MOPAC is a general-purpose semiempirical molecular orbital package

    for the study of solid state and molecular structures and reactions.'
  license: Not confirmed
  name: MOPAC
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
  softwareVersion: '[''23.2.2'']'
  url: https://github.com/openmopac/mopac
---
# MOPAC


MOPAC is a general-purpose semiempirical molecular orbital package
for the study of solid state and molecular structures and reactions.

<small>homepage: </small><span class="software-link">[https://github.com/openmopac/mopac](https://github.com/openmopac/mopac)</span>

## Available installations


|MOPAC version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|23.2.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MOPAC/23.2.2-gfbf-2025a`|