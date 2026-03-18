---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\nThe BIOM file format (canonically pronounced biome) is designed\
    \ to be\n a general-use format for representing biological sample by observation\n\
    \ contingency tables. BIOM is a recognized standard for the Earth Microbiome\n\
    \ Project and is a Genomics Standards Consortium supported project.\n"
  license: Not confirmed
  name: biom-format
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
  softwareVersion: '[''2.1.15'']'
  url: https://biom-format.org
---
# biom-format



The BIOM file format (canonically pronounced biome) is designed to be
 a general-use format for representing biological sample by observation
 contingency tables. BIOM is a recognized standard for the Earth Microbiome
 Project and is a Genomics Standards Consortium supported project.


<small>homepage: </small><span class="software-link">[https://biom-format.org](https://biom-format.org)</span>

## Available installations


|biom-format version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.1.15|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`biom-format/2.1.15-foss-2023a`|