---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Open Babel is a chemical toolbox designed to speak the many\n languages\
    \ of chemical data. It's an open, collaborative project allowing anyone\n to search,\
    \ convert, analyze, or store data from molecular modeling, chemistry,\n solid-state\
    \ materials, biochemistry, or related areas."
  license: Not confirmed
  name: OpenBabel
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
  softwareVersion: '[''3.1.1'']'
  url: https://openbabel.org
---
# OpenBabel


Open Babel is a chemical toolbox designed to speak the many
 languages of chemical data. It's an open, collaborative project allowing anyone
 to search, convert, analyze, or store data from molecular modeling, chemistry,
 solid-state materials, biochemistry, or related areas.

<small>homepage: </small><span class="software-link">[https://openbabel.org](https://openbabel.org)</span>

## Available installations


|OpenBabel version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`OpenBabel/3.1.1-gompi-2023a`|