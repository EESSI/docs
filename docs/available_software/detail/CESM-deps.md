---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'CESM is a fully-coupled, community, global climate model that

    provides state-of-the-art computer simulations of the Earth''s past, present,

    and future climate states.'
  license: Not confirmed
  name: CESM-deps
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
  softwareVersion: '[''3'']'
  url: http://www.cesm.ucar.edu/
---
# CESM-deps


CESM is a fully-coupled, community, global climate model that
provides state-of-the-art computer simulations of the Earth's past, present,
and future climate states.

<small>homepage: </small><span class="software-link">[http://www.cesm.ucar.edu/](http://www.cesm.ucar.edu/)</span>

## Available installations


|CESM-deps version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`CESM-deps/3-foss-2025a`|

## Extensions

Overview of extensions included in CESM-deps installations


### cesm-config


|`cesm-config` version|CESM-deps modules that include it|
| --- | --- |
|2.0.1|`CESM-deps/3-foss-2025a`|