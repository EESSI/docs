---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The Dalton code is a powerful tool for a wide range of molecular properties\n\
    \ at different levels of theory.\n Any published work arising from use of one\
    \ of the Dalton2016 programs\n must acknowledge that by a proper reference,\n\
    \ https://www.daltonprogram.org/www/citation.html."
  license: Not confirmed
  name: Dalton
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
  softwareVersion: '[''2026'']'
  url: https://daltonprogram.org/
---
# Dalton


The Dalton code is a powerful tool for a wide range of molecular properties
 at different levels of theory.
 Any published work arising from use of one of the Dalton2016 programs
 must acknowledge that by a proper reference,
 https://www.daltonprogram.org/www/citation.html.

<small>homepage: </small><span class="software-link">[https://daltonprogram.org/](https://daltonprogram.org/)</span>

## Available installations


|Dalton version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2026|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Dalton/2026-foss-2025a-parallel`|