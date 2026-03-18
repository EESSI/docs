---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n PAPI provides the tool designer and application engineer with a\
    \ consistent\n interface and methodology for use of the performance counter hardware\
    \ found\n in most major microprocessors. PAPI enables software engineers to see,\
    \ in near\n real time, the relation between software performance and processor\
    \ events.\n In addition Component PAPI provides access to a collection of components\n\
    \ that expose performance measurement opportunites across the hardware and\n software\
    \ stack.\n"
  license: Not confirmed
  name: PAPI
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
  softwareVersion: '[''7.2.0'', ''7.1.0'']'
  url: https://icl.cs.utk.edu/projects/papi/
---
# PAPI



 PAPI provides the tool designer and application engineer with a consistent
 interface and methodology for use of the performance counter hardware found
 in most major microprocessors. PAPI enables software engineers to see, in near
 real time, the relation between software performance and processor events.
 In addition Component PAPI provides access to a collection of components
 that expose performance measurement opportunites across the hardware and
 software stack.


<small>homepage: </small><span class="software-link">[https://icl.cs.utk.edu/projects/papi/](https://icl.cs.utk.edu/projects/papi/)</span>

## Available installations


|PAPI version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`PAPI/7.1.0-GCCcore-13.2.0`|
|7.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PAPI/7.2.0-GCCcore-14.2.0`|