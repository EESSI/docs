---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 're2c is a free and open-source lexer generator for C and C++. Its
    main goal is generating

    fast lexers: at least as fast as their reasonably optimized hand-coded counterparts.
    Instead of using

    traditional table-driven approach, re2c encodes the generated finite state automata
    directly in the form

    of conditional jumps and comparisons.'
  license: Not confirmed
  name: re2c
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
  softwareVersion: '[''4.3'']'
  url: https://re2c.org
---
# re2c


re2c is a free and open-source lexer generator for C and C++. Its main goal is generating
fast lexers: at least as fast as their reasonably optimized hand-coded counterparts. Instead of using
traditional table-driven approach, re2c encodes the generated finite state automata directly in the form
of conditional jumps and comparisons.

<small>homepage: </small><span class="software-link">[https://re2c.org](https://re2c.org)</span>

## Available installations


|re2c version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.3|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`re2c/4.3-GCCcore-14.3.0`|