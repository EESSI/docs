---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A minimal Python library for Apache Arrow, binding to the Rust Arrow
    implementation using pyo3.
  license: Not confirmed
  name: arro3
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
  softwareVersion: '[''0.8.1'']'
  url: https://kylebarron.dev/arro3/latest/
---
# arro3


A minimal Python library for Apache Arrow, binding to the Rust Arrow implementation using pyo3.

<small>homepage: </small><span class="software-link">[https://kylebarron.dev/arro3/latest/](https://kylebarron.dev/arro3/latest/)</span>

## Available installations


|arro3 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.8.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`arro3/0.8.1-gfbf-2026.1`|

## Extensions

Overview of extensions included in arro3 installations


### arro3_compute


|`arro3_compute` version|arro3 modules that include it|
| --- | --- |
|0.8.1|`arro3/0.8.1-gfbf-2026.1`|

### arro3_core


|`arro3_core` version|arro3 modules that include it|
| --- | --- |
|0.8.1|`arro3/0.8.1-gfbf-2026.1`|

### arro3_io


|`arro3_io` version|arro3 modules that include it|
| --- | --- |
|0.8.1|`arro3/0.8.1-gfbf-2026.1`|