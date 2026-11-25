---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n muParser is an extensible high performance math expression parser\
    \ library\n written in C++. It works by transforming a mathematical expression\
    \ into\n bytecode and precalculating constant parts of the expression.\n"
  license: Not confirmed
  name: muParser
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
  softwareVersion: '[''2.3.5'']'
  url: https://beltoforion.de/article.php?a=muparser
---
# muParser



 muParser is an extensible high performance math expression parser library
 written in C++. It works by transforming a mathematical expression into
 bytecode and precalculating constant parts of the expression.


<small>homepage: </small><span class="software-link">[https://beltoforion.de/article.php?a=muparser](https://beltoforion.de/article.php?a=muparser)</span>

## Available installations


|muParser version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.3.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`muParser/2.3.5-GCC-14.2.0`|