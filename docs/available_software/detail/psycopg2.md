---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Psycopg is the most popular PostgreSQL adapter for the Python programming
    language.
  license: Not confirmed
  name: psycopg2
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
  softwareVersion: '[''2.9.9'']'
  url: https://psycopg.org/
---
# psycopg2


Psycopg is the most popular PostgreSQL adapter for the Python programming language.

<small>homepage: </small><span class="software-link">[https://psycopg.org/](https://psycopg.org/)</span>

## Available installations


|psycopg2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.9.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`psycopg2/2.9.9-GCCcore-12.3.0`|

## Extensions

Overview of extensions included in psycopg2 installations


### psycopg2


|`psycopg2` version|psycopg2 modules that include it|
| --- | --- |
|2.9.9|`psycopg2/2.9.9-GCCcore-12.3.0`|