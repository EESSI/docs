---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The JUBE benchmarking environment provides a script based

    framework to easily create benchmark sets, run those sets on different

    computer systems and evaluate the results.

    '
  license: Not confirmed
  name: JUBE
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
  softwareVersion: '[''2.7.1'']'
  url: https://www.fz-juelich.de/jsc/jube
---
# JUBE


The JUBE benchmarking environment provides a script based
framework to easily create benchmark sets, run those sets on different
computer systems and evaluate the results.


<small>homepage: </small><span class="software-link">[https://www.fz-juelich.de/jsc/jube](https://www.fz-juelich.de/jsc/jube)</span>

## Available installations


|JUBE version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.7.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`JUBE/2.7.1-GCCcore-14.3.0`|