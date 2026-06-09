---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The OpenSSL Project is a collaborative effort to develop a robust,\
    \ commercial-grade, full-featured,\n and Open Source toolchain implementing the\
    \ Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)\n protocols\
    \ as well as a full-strength general purpose cryptography library. "
  license: Not confirmed
  name: OpenSSL
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
  softwareVersion: '[''3'']'
  url: https://www.openssl.org/
---
# OpenSSL


The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured,
 and Open Source toolchain implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
 protocols as well as a full-strength general purpose cryptography library. 

<small>homepage: </small><span class="software-link">[https://www.openssl.org/](https://www.openssl.org/)</span>

## Available installations


|OpenSSL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OpenSSL/3`|

## Extensions

Overview of extensions included in OpenSSL installations


### OpenSSL


|`OpenSSL` version|OpenSSL modules that include it|
| --- | --- |
|3.2.1|`OpenSSL/3`|