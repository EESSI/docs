---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "PycURL is a Python interface to libcurl. PycURL can be used to fetch\
    \ objects identified by a URL\n from a Python program, similar to the urllib Python\
    \ module. PycURL is mature, very fast, and supports a lot of\n features."
  license: Not confirmed
  name: PycURL
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
  softwareVersion: '[''7.45.7'']'
  url: http://pycurl.io/
---
# PycURL


PycURL is a Python interface to libcurl. PycURL can be used to fetch objects identified by a URL
 from a Python program, similar to the urllib Python module. PycURL is mature, very fast, and supports a lot of
 features.

<small>homepage: </small><span class="software-link">[http://pycurl.io/](http://pycurl.io/)</span>

## Available installations


|PycURL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.45.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`PycURL/7.45.7-GCCcore-14.3.0`|