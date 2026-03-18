---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The awk utility interprets a special-purpose programming language
    that makes it possible to handle

    simple data-reformatting jobs with just a few lines of code.'
  license: Not confirmed
  name: gawk
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
  softwareVersion: '[''5.3.0'']'
  url: https://www.gnu.org/software/gawk
---
# gawk


The awk utility interprets a special-purpose programming language that makes it possible to handle
simple data-reformatting jobs with just a few lines of code.

<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/gawk](https://www.gnu.org/software/gawk)</span>

## Available installations


|gawk version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`gawk/5.3.0-GCC-12.3.0`|