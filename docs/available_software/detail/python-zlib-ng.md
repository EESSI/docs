---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Faster zlib and gzip compatible compression and decompression by providing
    Python bindings

    for the zlib-ng library.

    python-zlib-ng provides the bindings by offering three modules: zlib_ng, gzip_ng,
    gzip_ng_threaded.

    zlib_ng and gzip_ng are almost fully compatible with zlib and gzip from the Python
    standard library.'
  license: Not confirmed
  name: python-zlib-ng
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
  softwareVersion: '[''0.5.1'']'
  url: https://github.com/pycompression/python-zlib-ng
---
# python-zlib-ng


Faster zlib and gzip compatible compression and decompression by providing Python bindings
for the zlib-ng library.
python-zlib-ng provides the bindings by offering three modules: zlib_ng, gzip_ng, gzip_ng_threaded.
zlib_ng and gzip_ng are almost fully compatible with zlib and gzip from the Python standard library.

<small>homepage: </small><span class="software-link">[https://github.com/pycompression/python-zlib-ng](https://github.com/pycompression/python-zlib-ng)</span>

## Available installations


|python-zlib-ng version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`python-zlib-ng/0.5.1-GCCcore-14.3.0`|