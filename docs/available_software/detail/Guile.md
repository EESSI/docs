---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Guile is a programming language, designed to help programmers create\
    \ flexible\n applications that can be extended by users or other programmers with\
    \ plug-ins,\n modules, or scripts.\n"
  license: Not confirmed
  name: Guile
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
  softwareVersion: '[''3.0.9'']'
  url: https://www.gnu.org/software/guile/
---
# Guile



 Guile is a programming language, designed to help programmers create flexible
 applications that can be extended by users or other programmers with plug-ins,
 modules, or scripts.


<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/guile/](https://www.gnu.org/software/guile/)</span>

## Available installations


|Guile version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.0.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Guile/3.0.9-GCCcore-12.3.0`|