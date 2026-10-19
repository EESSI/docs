---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "This Python module provides an xopen function that works like Python\u2019\
    s built-in open function but\nalso transparently deals with compressed files.\
    \ xopen selects the most efficient method for reading or writing a\ncompressed\
    \ file."
  license: Not confirmed
  name: xopen
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
  softwareVersion: '[''2.1.0'']'
  url: https://github.com/pycompression/xopen/
---
# xopen


This Python module provides an xopen function that works like Python’s built-in open function but
also transparently deals with compressed files. xopen selects the most efficient method for reading or writing a
compressed file.

<small>homepage: </small><span class="software-link">[https://github.com/pycompression/xopen/](https://github.com/pycompression/xopen/)</span>

## Available installations


|xopen version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`xopen/2.1.0-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in xopen installations


### backports-zstd


|`backports-zstd` version|xopen modules that include it|
| --- | --- |
|1.5.0|`xopen/2.1.0-GCCcore-14.3.0`|

### xopen


|`xopen` version|xopen modules that include it|
| --- | --- |
|2.1.0|`xopen/2.1.0-GCCcore-14.3.0`|

### zlib-ng


|`zlib-ng` version|xopen modules that include it|
| --- | --- |
|1.0.0|`xopen/2.1.0-GCCcore-14.3.0`|