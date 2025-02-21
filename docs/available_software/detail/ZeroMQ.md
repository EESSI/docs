---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ZeroMQ looks like an embeddable networking library but acts like a
    concurrency framework. It gives you sockets that carry atomic messages across
    various transports like in-process, inter-process, TCP, and multicast. You can
    connect sockets N-to-N with patterns like fanout, pub-sub, task distribution,
    and request-reply. It's fast enough to be the fabric for clustered products. Its
    asynchronous I/O model gives you scalable multicore applications, built as asynchronous
    message-processing tasks. It has a score of language APIs and runs on most operating
    systems.
  license: Not confirmed
  name: ZeroMQ
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
  softwareVersion: '[''ZeroMQ/4.3.4-GCCcore-12.3.0'', ''ZeroMQ/4.3.5-GCCcore-13.2.0'']'
  url: https://www.zeromq.org/
---

ZeroMQ
======


ZeroMQ looks like an embeddable networking library but acts like a concurrency framework. It gives you sockets that carry atomic messages across various transports like in-process, inter-process, TCP, and multicast. You can connect sockets N-to-N with patterns like fanout, pub-sub, task distribution, and request-reply. It's fast enough to be the fabric for clustered products. Its asynchronous I/O model gives you scalable multicore applications, built as asynchronous message-processing tasks. It has a score of language APIs and runs on most operating systems.

https://www.zeromq.org/
# Available modules


The overview below shows which ZeroMQ installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ZeroMQ, load one of these modules using a `module load` command like:

```shell
module load ZeroMQ/4.3.5-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ZeroMQ/4.3.5-GCCcore-13.2.0|x|x|x|x|x|x|x|x|-|x|
|ZeroMQ/4.3.4-GCCcore-12.3.0|x|x|x|x|x|x|x|x|-|x|
