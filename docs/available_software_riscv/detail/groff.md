---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Groff (GNU troff) is a typesetting system that reads plain text mixed\
    \ with formatting commands\n and produces formatted output."
  license: Not confirmed
  name: groff
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
  softwareVersion: '[''1.23.0'']'
  url: https://www.gnu.org/software/groff
---
# groff


Groff (GNU troff) is a typesetting system that reads plain text mixed with formatting commands
 and produces formatted output.

<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/groff](https://www.gnu.org/software/groff)</span>

## Available installations


|groff version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.23.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`groff/1.23.0-GCCcore-14.3.0`|