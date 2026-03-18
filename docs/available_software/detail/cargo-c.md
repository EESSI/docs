---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Applet for cargo to build and install C-ABI compatible dynamic and
    static

    libraries. It produces and installs a correct pkg-config file, a static library

    and a dynamic library, and a C header to be used by any C (and C-compatible)

    software.'
  license: Not confirmed
  name: cargo-c
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
  softwareVersion: '[''0.9.32'', ''0.10.15'']'
  url: https://github.com/lu-zero/cargo-c
---
# cargo-c


Applet for cargo to build and install C-ABI compatible dynamic and static
libraries. It produces and installs a correct pkg-config file, a static library
and a dynamic library, and a C header to be used by any C (and C-compatible)
software.

<small>homepage: </small><span class="software-link">[https://github.com/lu-zero/cargo-c](https://github.com/lu-zero/cargo-c)</span>

## Available installations


|cargo-c version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.10.15|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`cargo-c/0.10.15-GCCcore-14.3.0`|
|0.9.32|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`cargo-c/0.9.32-GCCcore-13.3.0`|