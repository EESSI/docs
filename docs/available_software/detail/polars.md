---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Polars is a blazingly fast DataFrame library for manipulating

    structured data. The core is written in Rust and this module provides its

    interface for Python.'
  license: Not confirmed
  name: polars
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
  softwareVersion: '[''1.41.2'']'
  url: https://pola.rs/
---
# polars


Polars is a blazingly fast DataFrame library for manipulating
structured data. The core is written in Rust and this module provides its
interface for Python.

<small>homepage: </small><span class="software-link">[https://pola.rs/](https://pola.rs/)</span>

## Available installations


|polars version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.41.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`polars/1.41.2-gfbf-2026.1`|

## Extensions

Overview of extensions included in polars installations


### polars


|`polars` version|polars modules that include it|
| --- | --- |
|1.41.2|`polars/1.41.2-gfbf-2026.1`|

### polars-runtime-32


|`polars-runtime-32` version|polars modules that include it|
| --- | --- |
|1.41.2|`polars/1.41.2-gfbf-2026.1`|