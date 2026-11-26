---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: State-of-the-art Natural Language Processing for PyTorch and TensorFlow
    2.0
  license: Not confirmed
  name: Transformers
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
  softwareVersion: '[''4.39.3'']'
  url: https://github.com/huggingface/transformers
---
# Transformers


State-of-the-art Natural Language Processing for PyTorch and TensorFlow 2.0

<small>homepage: </small><span class="software-link">[https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)</span>

## Available installations


|Transformers version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.39.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Transformers/4.39.3-gfbf-2023a`|

## Extensions

Overview of extensions included in Transformers installations


### regex


|`regex` version|Transformers modules that include it|
| --- | --- |
|2023.12.25|`Transformers/4.39.3-gfbf-2023a`|

### transformers


|`transformers` version|Transformers modules that include it|
| --- | --- |
|4.39.3|`Transformers/4.39.3-gfbf-2023a`|