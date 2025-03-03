---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: OpenPGM is an open source implementation of the Pragmatic General Multicast
    (PGM) specification in RFC 3208 available at www.ietf.org. PGM is a reliable and
    scalable multicast protocol that enables receivers to detect loss, request retransmission
    of lost data, or notify an application of unrecoverable loss. PGM is a receiver-reliable
    protocol, which means the receiver is responsible for ensuring all data is received,
    absolving the sender of reception responsibility.
  license: Not confirmed
  name: OpenPGM
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
  softwareVersion: '[''OpenPGM/5.2.122-GCCcore-12.3.0'', ''OpenPGM/5.2.122-GCCcore-13.2.0'']'
  url: https://code.google.com/p/openpgm/
---

OpenPGM
=======


OpenPGM is an open source implementation of the Pragmatic General Multicast (PGM) specification in RFC 3208 available at www.ietf.org. PGM is a reliable and scalable multicast protocol that enables receivers to detect loss, request retransmission of lost data, or notify an application of unrecoverable loss. PGM is a receiver-reliable protocol, which means the receiver is responsible for ensuring all data is received, absolving the sender of reception responsibility.

https://code.google.com/p/openpgm/
# Available modules


The overview below shows which OpenPGM installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using OpenPGM, load one of these modules using a `module load` command like:

```shell
module load OpenPGM/5.2.122-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|OpenPGM/5.2.122-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|
|OpenPGM/5.2.122-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|
