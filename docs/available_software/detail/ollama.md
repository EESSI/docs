---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Get up and running with large language models.
  license: Not confirmed
  name: ollama
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
  softwareVersion: '[''0.6.0'']'
  url: https://ollama.com/
---
# ollama


Get up and running with large language models.

<small>homepage: </small><span class="software-link">[https://ollama.com/](https://ollama.com/)</span>

## Available installations


|ollama version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ollama/0.6.0-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in ollama installations


### ggml-cpu


|`ggml-cpu` version|ollama modules that include it|
| --- | --- |
|0.6.0|`ollama/0.6.0-GCCcore-13.3.0`|

### ollama


|`ollama` version|ollama modules that include it|
| --- | --- |
|0.6.0|`ollama/0.6.0-GCCcore-13.3.0`|