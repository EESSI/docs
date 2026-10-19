---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'A Jupyter kernel base class in Python which includes core magic functions
    (including help,

    command and file path completion, parallel and distributed processing, downloads,
    and much more).'
  license: Not confirmed
  name: metakernel
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
  softwareVersion: '[''1.0.0'', ''0.30.4'']'
  url: https://github.com/Calysto/metakernel
---
# metakernel


A Jupyter kernel base class in Python which includes core magic functions (including help,
command and file path completion, parallel and distributed processing, downloads, and much more).

<small>homepage: </small><span class="software-link">[https://github.com/Calysto/metakernel](https://github.com/Calysto/metakernel)</span>

## Available installations


|metakernel version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`metakernel/1.0.0-GCC-14.3.0`|
|0.30.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`metakernel/0.30.4-GCC-12.3.0`|

## Extensions

Overview of extensions included in metakernel installations


### metakernel


|`metakernel` version|metakernel modules that include it|
| --- | --- |
|1.0.0|`metakernel/1.0.0-GCC-14.3.0`|
|0.30.4|`metakernel/0.30.4-GCC-12.3.0`|