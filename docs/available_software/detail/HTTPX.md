---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'HTTPX is a fully featured HTTP client library for Python 3. It includes
    an

    integrated command line client, has support for both HTTP/1.1 and HTTP/2, and

    provides both sync and async APIs.'
  license: Not confirmed
  name: HTTPX
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
  softwareVersion: '[''0.28.1'']'
  url: https://www.python-httpx.org/
---
# HTTPX


HTTPX is a fully featured HTTP client library for Python 3. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2, and
provides both sync and async APIs.

<small>homepage: </small><span class="software-link">[https://www.python-httpx.org/](https://www.python-httpx.org/)</span>

## Available installations


|HTTPX version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.28.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`HTTPX/0.28.1-GCCcore-14.2.0`|

## Extensions

Overview of extensions included in HTTPX installations


### anyio


|`anyio` version|HTTPX modules that include it|
| --- | --- |
|4.10.0|`HTTPX/0.28.1-GCCcore-14.2.0`|

### h11


|`h11` version|HTTPX modules that include it|
| --- | --- |
|0.16.0|`HTTPX/0.28.1-GCCcore-14.2.0`|

### httpcore


|`httpcore` version|HTTPX modules that include it|
| --- | --- |
|1.0.9|`HTTPX/0.28.1-GCCcore-14.2.0`|

### httpx


|`httpx` version|HTTPX modules that include it|
| --- | --- |
|0.28.1|`HTTPX/0.28.1-GCCcore-14.2.0`|

### sniffio


|`sniffio` version|HTTPX modules that include it|
| --- | --- |
|1.3.1|`HTTPX/0.28.1-GCCcore-14.2.0`|