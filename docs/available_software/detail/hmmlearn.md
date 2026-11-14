---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: hmmlearn is a set of algorithms for unsupervised learning and inference
    of Hidden Markov Models
  license: Not confirmed
  name: hmmlearn
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
  softwareVersion: '[''0.3.3'']'
  url: https://github.com/hmmlearn/hmmlearn
---
# hmmlearn


hmmlearn is a set of algorithms for unsupervised learning and inference of Hidden Markov Models

<small>homepage: </small><span class="software-link">[https://github.com/hmmlearn/hmmlearn](https://github.com/hmmlearn/hmmlearn)</span>

## Available installations


|hmmlearn version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`hmmlearn/0.3.3-gfbf-2024a`|