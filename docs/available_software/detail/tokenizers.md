---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Fast State-of-the-Art Tokenizers optimized for Research and Production
  license: Not confirmed
  name: tokenizers
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
  softwareVersion: '[''0.15.2'']'
  url: https://github.com/huggingface/tokenizers
---
# tokenizers


Fast State-of-the-Art Tokenizers optimized for Research and Production

<small>homepage: </small><span class="software-link">[https://github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers)</span>

## Available installations


|tokenizers version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.15.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`tokenizers/0.15.2-GCCcore-12.3.0`|

## Extensions

Overview of extensions included in tokenizers installations


### huggingface-hub


|`huggingface-hub` version|tokenizers modules that include it|
| --- | --- |
|0.21.4|`tokenizers/0.15.2-GCCcore-12.3.0`|

### tokenizers


|`tokenizers` version|tokenizers modules that include it|
| --- | --- |
|0.15.2|`tokenizers/0.15.2-GCCcore-12.3.0`|