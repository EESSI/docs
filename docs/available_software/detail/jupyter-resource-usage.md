---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Jupyter Notebook Extension for monitoring your own Resource Usage (memory
    and/or CPU)
  license: Not confirmed
  name: jupyter-resource-usage
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
  softwareVersion: '[''1.2.0'']'
  url: https://github.com/jupyter-server/jupyter-resource-usage
---
# jupyter-resource-usage


Jupyter Notebook Extension for monitoring your own Resource Usage (memory and/or CPU)

<small>homepage: </small><span class="software-link">[https://github.com/jupyter-server/jupyter-resource-usage](https://github.com/jupyter-server/jupyter-resource-usage)</span>

## Available installations


|jupyter-resource-usage version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`jupyter-resource-usage/1.2.0-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in jupyter-resource-usage installations


### jupyter_resource_usage


|`jupyter_resource_usage` version|jupyter-resource-usage modules that include it|
| --- | --- |
|1.2.0|`jupyter-resource-usage/1.2.0-GCCcore-14.3.0`|