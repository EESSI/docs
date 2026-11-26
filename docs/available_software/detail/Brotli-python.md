---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Brotli is a generic-purpose lossless compression algorithm that compresses\
    \ data using a combination\n of a modern variant of the LZ77 algorithm, Huffman\
    \ coding and 2nd order context modeling, with a compression ratio\n comparable\
    \ to the best currently available general-purpose compression methods. It is similar\
    \ in speed with deflate\n but offers more dense compression.\nThe specification\
    \ of the Brotli Compressed Data Format is defined in RFC 7932."
  license: Not confirmed
  name: Brotli-python
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
  softwareVersion: '[''1.1.0'']'
  url: https://github.com/google/brotli
---
# Brotli-python


Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination
 of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio
 comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate
 but offers more dense compression.
The specification of the Brotli Compressed Data Format is defined in RFC 7932.

<small>homepage: </small><span class="software-link">[https://github.com/google/brotli](https://github.com/google/brotli)</span>

## Available installations


|Brotli-python version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Brotli-python/1.1.0-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in Brotli-python installations


### brotli


|`brotli` version|Brotli-python modules that include it|
| --- | --- |
|1.1.0|`Brotli-python/1.1.0-GCCcore-14.3.0`|