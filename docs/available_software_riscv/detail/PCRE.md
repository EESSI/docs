---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    The PCRE library is a set of functions that implement regular expression

    pattern matching using the same syntax and semantics as Perl 5.

    '
  license: Not confirmed
  name: PCRE
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
  softwareVersion: '[''8.45'']'
  url: https://www.pcre.org/
---
# PCRE



The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl 5.


<small>homepage: </small><span class="software-link">[https://www.pcre.org/](https://www.pcre.org/)</span>

## Available installations


|PCRE version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|8.45|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PCRE/8.45-GCCcore-14.3.0`|