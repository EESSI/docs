---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Unsupervised text tokenizer for Neural Network-based text generation.
  license: Not confirmed
  name: SentencePiece
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
  softwareVersion: '[''0.2.1'']'
  url: https://github.com/google/sentencepiece
---
# SentencePiece


Unsupervised text tokenizer for Neural Network-based text generation.

<small>homepage: </small><span class="software-link">[https://github.com/google/sentencepiece](https://github.com/google/sentencepiece)</span>

## Available installations


|SentencePiece version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.2.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`SentencePiece/0.2.1-GCC-14.3.0`|

## Extensions

Overview of extensions included in SentencePiece installations


### SentencePiece


|`SentencePiece` version|SentencePiece modules that include it|
| --- | --- |
|0.2.1|`SentencePiece/0.2.1-GCC-14.3.0`|

### sentencepiece


|`sentencepiece` version|SentencePiece modules that include it|
| --- | --- |
|0.2.1|`SentencePiece/0.2.1-GCC-14.3.0`|