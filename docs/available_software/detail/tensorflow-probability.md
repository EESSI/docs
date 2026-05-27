---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: TensorFlow Probability (TFP) is a library for probabilistic reasoning
    and statistical analysis.
  license: Not confirmed
  name: tensorflow-probability
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
  softwareVersion: '[''0.20.0'']'
  url: https://www.tensorflow.org/probability
---
# tensorflow-probability


TensorFlow Probability (TFP) is a library for probabilistic reasoning and statistical analysis.

<small>homepage: </small><span class="software-link">[https://www.tensorflow.org/probability](https://www.tensorflow.org/probability)</span>

## Available installations


|tensorflow-probability version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.20.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`tensorflow-probability/0.20.0-foss-2023a`|

## Extensions

Overview of extensions included in tensorflow-probability installations


### cloudpickle


|`cloudpickle` version|tensorflow-probability modules that include it|
| --- | --- |
|3.0.0|`tensorflow-probability/0.20.0-foss-2023a`|

### tensorflow-probability


|`tensorflow-probability` version|tensorflow-probability modules that include it|
| --- | --- |
|0.20.0|`tensorflow-probability/0.20.0-foss-2023a`|