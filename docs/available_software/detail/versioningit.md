---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "versioningit is yet another Python packaging plugin for automatically\
    \ determining your\npackage\u2019s version based on your version control repository\u2019\
    s tags.\nUnlike others, it allows easy customization of the version format and\
    \ even lets you easily override\nthe separate functions used for version extraction\
    \ & calculation."
  license: Not confirmed
  name: versioningit
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
  softwareVersion: '[''3.3.0'']'
  url: https://github.com/jwodder/versioningit
---
# versioningit


versioningit is yet another Python packaging plugin for automatically determining your
package’s version based on your version control repository’s tags.
Unlike others, it allows easy customization of the version format and even lets you easily override
the separate functions used for version extraction & calculation.

<small>homepage: </small><span class="software-link">[https://github.com/jwodder/versioningit](https://github.com/jwodder/versioningit)</span>

## Available installations


|versioningit version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`versioningit/3.3.0-GCCcore-14.3.0`|