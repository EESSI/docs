---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Nettle is a cryptographic library that is designed to fit easily\n\
    \ in more or less any context: In crypto toolkits for object-oriented\n languages\
    \ (C++, Python, Pike, ...), in applications like LSH or GNUPG,\n or even in kernel\
    \ space."
  license: Not confirmed
  name: nettle
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
  softwareVersion: '[''3.10.2'']'
  url: https://www.lysator.liu.se/~nisse/nettle/
---
# nettle


Nettle is a cryptographic library that is designed to fit easily
 in more or less any context: In crypto toolkits for object-oriented
 languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
 or even in kernel space.

<small>homepage: </small><span class="software-link">[https://www.lysator.liu.se/~nisse/nettle/](https://www.lysator.liu.se/~nisse/nettle/)</span>

## Available installations


|nettle version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.10.2|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`nettle/3.10.2-GCCcore-14.3.0`|