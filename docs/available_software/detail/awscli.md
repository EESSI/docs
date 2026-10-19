---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Universal Command Line Environment for AWS
  license: Not confirmed
  name: awscli
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
  softwareVersion: '[''2.35.11'']'
  url: https://github.com/aws/aws-cli/
---
# awscli


Universal Command Line Environment for AWS

<small>homepage: </small><span class="software-link">[https://github.com/aws/aws-cli/](https://github.com/aws/aws-cli/)</span>

## Available installations


|awscli version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.35.11|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`awscli/2.35.11-GCCcore-15.2.0`|

## Extensions

Overview of extensions included in awscli installations


### awscli


|`awscli` version|awscli modules that include it|
| --- | --- |
|2.35.11|`awscli/2.35.11-GCCcore-15.2.0`|

### awscrt


|`awscrt` version|awscli modules that include it|
| --- | --- |
|0.32.2|`awscli/2.35.11-GCCcore-15.2.0`|

### prompt_toolkit


|`prompt_toolkit` version|awscli modules that include it|
| --- | --- |
|3.0.52|`awscli/2.35.11-GCCcore-15.2.0`|

### wcwidth


|`wcwidth` version|awscli modules that include it|
| --- | --- |
|0.2.14|`awscli/2.35.11-GCCcore-15.2.0`|