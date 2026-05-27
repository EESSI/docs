---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Ruby gem for colorizing text using ANSI escape sequences.

    Extends String class or add a ColorizedString with methods to set the text color,
    background color and text effects.'
  license: Not confirmed
  name: colorize
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
  softwareVersion: '[''0.7.7'']'
  url: https://github.com/fazibear/colorize
---
# colorize


Ruby gem for colorizing text using ANSI escape sequences.
Extends String class or add a ColorizedString with methods to set the text color, background color and text effects.

<small>homepage: </small><span class="software-link">[https://github.com/fazibear/colorize](https://github.com/fazibear/colorize)</span>

## Available installations


|colorize version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.7.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`colorize/0.7.7-GCC-12.3.0`|