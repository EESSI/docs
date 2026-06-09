---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "ZeroMQ looks like an embeddable networking library but acts like a\
    \ concurrency framework.\n It gives you sockets that carry atomic messages across\
    \ various transports like in-process,\n inter-process, TCP, and multicast. You\
    \ can connect sockets N-to-N with patterns like fanout,\n pub-sub, task distribution,\
    \ and request-reply. It's fast enough to be the fabric for clustered\n products.\
    \ Its asynchronous I/O model gives you scalable multicore applications, built\
    \ as asynchronous\n message-processing tasks. It has a score of language APIs\
    \ and runs on most operating systems."
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
  softwareVersion: '[''4.3.5'']'
  url: https://www.zeromq.org/
---
# ZeroMQ


ZeroMQ looks like an embeddable networking library but acts like a concurrency framework.
 It gives you sockets that carry atomic messages across various transports like in-process,
 inter-process, TCP, and multicast. You can connect sockets N-to-N with patterns like fanout,
 pub-sub, task distribution, and request-reply. It's fast enough to be the fabric for clustered
 products. Its asynchronous I/O model gives you scalable multicore applications, built as asynchronous
 message-processing tasks. It has a score of language APIs and runs on most operating systems.

<small>homepage: </small><span class="software-link">[https://www.zeromq.org/](https://www.zeromq.org/)</span>

## Available installations


|ZeroMQ version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.3.5|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ZeroMQ/4.3.5-GCCcore-14.3.0`|