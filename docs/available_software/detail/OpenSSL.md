---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The OpenSSL Project is a collaborative effort to develop a robust,
    commercial-grade, full-featured, and Open Source toolchain implementing the Secure
    Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) protocols as well
    as a full-strength general purpose cryptography library.
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
  softwareVersion: '[''OpenSSL/1.1'']'
  url: https://www.openssl.org/
---

OpenSSL
=======


The OpenSSL Project is a collaborative effort to develop a robust, commercial-grade, full-featured, and Open Source toolchain implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) protocols as well as a full-strength general purpose cryptography library.

https://www.openssl.org/
# Available modules


The overview below shows which OpenSSL installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using OpenSSL, load one of these modules using a `module load` command like:

```shell
module load OpenSSL/1.1
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|OpenSSL/1.1|x|x|x|-|x|x|x|x|x|x|x|
