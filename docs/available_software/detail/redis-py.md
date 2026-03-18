---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Python interface to the Redis key-value store.
  license: Not confirmed
  name: redis-py
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
  softwareVersion: '[''5.1.1'', ''5.0.1'']'
  url: https://github.com/redis/redis-py
---
# redis-py


The Python interface to the Redis key-value store.

<small>homepage: </small><span class="software-link">[https://github.com/redis/redis-py](https://github.com/redis/redis-py)</span>

## Available installations


|redis-py version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`redis-py/5.0.1-GCCcore-12.3.0`|
|5.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`redis-py/5.1.1-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in redis-py installations


### async-timeout


|`async-timeout` version|redis-py modules that include it|
| --- | --- |
|4.0.3|`redis-py/5.0.1-GCCcore-12.3.0`<br/>`redis-py/5.1.1-GCCcore-13.3.0`|

### redis-py


|`redis-py` version|redis-py modules that include it|
| --- | --- |
|5.0.1|`redis-py/5.0.1-GCCcore-12.3.0`|
|5.1.1|`redis-py/5.1.1-GCCcore-13.3.0`|