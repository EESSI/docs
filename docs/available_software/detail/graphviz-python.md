---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Simple Python interface for Graphviz
  license: Not confirmed
  name: graphviz-python
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
  softwareVersion: '[''0.21'']'
  url: https://pypi.python.org/pypi/graphviz
---
# graphviz-python


Simple Python interface for Graphviz

<small>homepage: </small><span class="software-link">[https://pypi.python.org/pypi/graphviz](https://pypi.python.org/pypi/graphviz)</span>

## Available installations


|graphviz-python version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.21|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`graphviz-python/0.21-GCCcore-14.3.0-minimal`|

## Extensions

Overview of extensions included in graphviz-python installations


### graphviz


|`graphviz` version|graphviz-python modules that include it|
| --- | --- |
|0.21|`graphviz-python/0.21-GCCcore-14.3.0-minimal`|