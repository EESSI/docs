---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n MUMmer is a system for rapidly aligning entire genomes,\n whether\
    \ in complete or draft form. AMOS makes use of it.\n"
  license: Not confirmed
  name: MUMmer
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
  softwareVersion: '[''4.0.1'']'
  url: https://mummer.sourceforge.net/
---
# MUMmer



 MUMmer is a system for rapidly aligning entire genomes,
 whether in complete or draft form. AMOS makes use of it.


<small>homepage: </small><span class="software-link">[https://mummer.sourceforge.net/](https://mummer.sourceforge.net/)</span>

## Available installations


|MUMmer version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MUMmer/4.0.1-GCCcore-14.3.0`|