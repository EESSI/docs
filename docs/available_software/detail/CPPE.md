---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'CPPE is an open-source, light-weight C++ and Python library for Polarizable

    Embedding (PE)1,2 calculations. It provides an easy-to-use API to implement PE

    for ground-state self-consistent field (SCF) calculations and post-SCF methods.

    A convenient Python interface is also available.'
  license: Not confirmed
  name: CPPE
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
  softwareVersion: '[''0.3.1'']'
  url: https://github.com/maxscheurer/cppe
---
# CPPE


CPPE is an open-source, light-weight C++ and Python library for Polarizable
Embedding (PE)1,2 calculations. It provides an easy-to-use API to implement PE
for ground-state self-consistent field (SCF) calculations and post-SCF methods.
A convenient Python interface is also available.

<small>homepage: </small><span class="software-link">[https://github.com/maxscheurer/cppe](https://github.com/maxscheurer/cppe)</span>

## Available installations


|CPPE version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`CPPE/0.3.1-GCC-14.2.0`|

## Extensions

Overview of extensions included in CPPE installations


### cppe


|`cppe` version|CPPE modules that include it|
| --- | --- |
|0.3.1|`CPPE/0.3.1-GCC-14.2.0`|