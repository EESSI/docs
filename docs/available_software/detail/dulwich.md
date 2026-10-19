---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Pure-Python Git implementation.
  license: Not confirmed
  name: dulwich
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
  url: https://github.com/jelmer/dulwich
---
# dulwich


Pure-Python Git implementation.

<small>homepage: </small><span class="software-link">[https://github.com/jelmer/dulwich](https://github.com/jelmer/dulwich)</span>

## Available installations


|dulwich version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`dulwich/1.2.0-GCCcore-15.2.0`|

## Extensions

Overview of extensions included in dulwich installations


### dulwich


|`dulwich` version|dulwich modules that include it|
| --- | --- |
|1.2.0|`dulwich/1.2.0-GCCcore-15.2.0`|

### urllib3


|`urllib3` version|dulwich modules that include it|
| --- | --- |
|2.6.3|`dulwich/1.2.0-GCCcore-15.2.0`|