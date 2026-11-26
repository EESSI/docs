---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "libMemcached is an open source C/C++ client library and tools for\n\
    \ the memcached server (http://danga.com/memcached). It has been designed to be\
    \ light\n on memory usage, thread safe, and provide full access to server side\
    \ methods."
  license: Not confirmed
  name: libMemcached
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
  softwareVersion: '[''1.0.18'']'
  url: https://memcached.org
---
# libMemcached


libMemcached is an open source C/C++ client library and tools for
 the memcached server (http://danga.com/memcached). It has been designed to be light
 on memory usage, thread safe, and provide full access to server side methods.

<small>homepage: </small><span class="software-link">[https://memcached.org](https://memcached.org)</span>

## Available installations


|libMemcached version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.18|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libMemcached/1.0.18-GCCcore-14.3.0`|