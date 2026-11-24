---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: meshio is a tool for reading/writing various mesh formats representing
    unstructured meshes
  license: Not confirmed
  name: meshio
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
  softwareVersion: '[''5.3.5'']'
  url: https://github.com/nschloe/meshio
---
# meshio


meshio is a tool for reading/writing various mesh formats representing unstructured meshes

<small>homepage: </small><span class="software-link">[https://github.com/nschloe/meshio](https://github.com/nschloe/meshio)</span>

## Available installations


|meshio version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.3.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`meshio/5.3.5-foss-2025b`|

## Extensions

Overview of extensions included in meshio installations


### appdirs


|`appdirs` version|meshio modules that include it|
| --- | --- |
|1.4.4|`meshio/5.3.5-foss-2025b`|

### meshio


|`meshio` version|meshio modules that include it|
| --- | --- |
|5.3.5|`meshio/5.3.5-foss-2025b`|

### pipdate


|`pipdate` version|meshio modules that include it|
| --- | --- |
|0.5.6|`meshio/5.3.5-foss-2025b`|