---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Python bindings to the Rust rpds crate for persistent data structures.
  license: Not confirmed
  name: rpds-py
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
  softwareVersion: '[''2026.5.1'', ''0.30.0'']'
  url: https://github.com/crate-py/rpds
---
# rpds-py


Python bindings to the Rust rpds crate for persistent data structures.

<small>homepage: </small><span class="software-link">[https://github.com/crate-py/rpds](https://github.com/crate-py/rpds)</span>

## Available installations


|rpds-py version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2026.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`rpds-py/2026.5.1-GCCcore-14.3.0`|
|0.30.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`rpds-py/0.30.0-GCCcore-15.2.0`|