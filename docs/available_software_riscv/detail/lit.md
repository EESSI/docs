---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'lit is a portable tool for executing LLVM and Clang style test suites,
    summarizing their results, and

    providing indication of failures.'
  license: Not confirmed
  name: lit
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
  softwareVersion: '[''18.1.8'']'
  url: https://llvm.org/docs/CommandGuide/lit.html
---
# lit


lit is a portable tool for executing LLVM and Clang style test suites, summarizing their results, and
providing indication of failures.

<small>homepage: </small><span class="software-link">[https://llvm.org/docs/CommandGuide/lit.html](https://llvm.org/docs/CommandGuide/lit.html)</span>

## Available installations


|lit version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|18.1.8|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`lit/18.1.8-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in lit installations


### lit


|`lit` version|lit modules that include it|
| --- | --- |
|18.1.8|`lit/18.1.8-GCCcore-14.3.0`|

### pexpect


|`pexpect` version|lit modules that include it|
| --- | --- |
|4.9.0|`lit/18.1.8-GCCcore-14.3.0`|

### ptyprocess


|`ptyprocess` version|lit modules that include it|
| --- | --- |
|0.7.0|`lit/18.1.8-GCCcore-14.3.0`|