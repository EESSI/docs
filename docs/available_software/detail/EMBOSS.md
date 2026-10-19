---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "EMBOSS is 'The European Molecular Biology Open Software Suite'\n.\
    \ EMBOSS is a free Open Source software analysis package specially developed\n\
    \ for the needs of the molecular biology (e.g. EMBnet) user community."
  license: Not confirmed
  name: EMBOSS
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
  softwareVersion: '[''6.6.0'']'
  url: https://emboss.sourceforge.net/
---
# EMBOSS


EMBOSS is 'The European Molecular Biology Open Software Suite'
. EMBOSS is a free Open Source software analysis package specially developed
 for the needs of the molecular biology (e.g. EMBnet) user community.

<small>homepage: </small><span class="software-link">[https://emboss.sourceforge.net/](https://emboss.sourceforge.net/)</span>

## Available installations


|EMBOSS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|6.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`EMBOSS/6.6.0-foss-2025a`|