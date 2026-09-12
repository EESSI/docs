---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Intel oneAPI Math Kernel Library
  license: Not confirmed
  name: imkl
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
  softwareVersion: '[''2024.2.0'']'
  url: https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html
---
# imkl


Intel oneAPI Math Kernel Library

<small>homepage: </small><span class="software-link">[https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/onemkl.html)</span>

## Available installations


|imkl version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2024.2.0|`generic`: `x86_64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`imkl/2024.2.0`|