---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'gRPC is a modern, open source, high-performance remote procedure call
    (RPC)

    framework that can run anywhere. gRPC enables client and server applications to

    communicate transparently, and simplifies the building of connected systems.'
  license: Not confirmed
  name: gRPC
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
  softwareVersion: '[''1.83.0'']'
  url: https://grpc.io/
---
# gRPC


gRPC is a modern, open source, high-performance remote procedure call (RPC)
framework that can run anywhere. gRPC enables client and server applications to
communicate transparently, and simplifies the building of connected systems.

<small>homepage: </small><span class="software-link">[https://grpc.io/](https://grpc.io/)</span>

## Available installations


|gRPC version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.83.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`gRPC/1.83.0-GCCcore-15.2.0`|