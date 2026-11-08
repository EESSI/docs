---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Libwebsockets (LWS) is a flexible, lightweight pure C library for

    implementing modern network protocols easily with a tiny footprint, using a nonblocking

    event loop. It has been developed continuously since 2010 and is used in tens
    of millions

    of devices and by thousands of developers around the world.'
  license: Not confirmed
  name: libwebsockets
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
  softwareVersion: '[''4.5.8'']'
  url: https://libwebsockets.org/
---
# libwebsockets


Libwebsockets (LWS) is a flexible, lightweight pure C library for
implementing modern network protocols easily with a tiny footprint, using a nonblocking
event loop. It has been developed continuously since 2010 and is used in tens of millions
of devices and by thousands of developers around the world.

<small>homepage: </small><span class="software-link">[https://libwebsockets.org/](https://libwebsockets.org/)</span>

## Available installations


|libwebsockets version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.5.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`libwebsockets/4.5.8-GCCcore-15.2.0`|