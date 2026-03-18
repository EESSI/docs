---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "GnuTLS is a secure communications library implementing the SSL, TLS\n\
    \ and DTLS protocols and technologies around them. It provides a simple\n C language\
    \ application programming interface (API) to access the secure\n communications\
    \ protocols as well as APIs to parse and write X.509, PKCS #12,\n OpenPGP and\
    \ other required structures. It is aimed to be portable\n and efficient with focus\
    \ on security and interoperability."
  license: Not confirmed
  name: GnuTLS
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
  softwareVersion: '[''3.8.10'', ''3.7.8'']'
  url: https://www.gnutls.org
---
# GnuTLS


GnuTLS is a secure communications library implementing the SSL, TLS
 and DTLS protocols and technologies around them. It provides a simple
 C language application programming interface (API) to access the secure
 communications protocols as well as APIs to parse and write X.509, PKCS #12,
 OpenPGP and other required structures. It is aimed to be portable
 and efficient with focus on security and interoperability.

<small>homepage: </small><span class="software-link">[https://www.gnutls.org](https://www.gnutls.org)</span>

## Available installations


|GnuTLS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.7.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`GnuTLS/3.7.8-GCCcore-12.3.0`|
|3.8.10|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`GnuTLS/3.8.10-GCCcore-14.3.0`|