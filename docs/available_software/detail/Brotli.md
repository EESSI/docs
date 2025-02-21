---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Brotli is a generic-purpose lossless compression algorithm that compresses
    data using a combination of a modern variant of the LZ77 algorithm, Huffman coding
    and 2nd order context modeling, with a compression ratio comparable to the best
    currently available general-purpose compression methods. It is similar in speed
    with deflate but offers more dense compression.The specification of the Brotli
    Compressed Data Format is defined in RFC 7932.
  license: Not confirmed
  name: Brotli
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
  softwareVersion: '[''Brotli/1.0.9-GCCcore-12.2.0'', ''Brotli/1.0.9-GCCcore-12.3.0'',
    ''Brotli/1.1.0-GCCcore-13.2.0'']'
  url: https://github.com/google/brotli
---

Brotli
======


Brotli is a generic-purpose lossless compression algorithm that compresses data using a combination of a modern variant of the LZ77 algorithm, Huffman coding and 2nd order context modeling, with a compression ratio comparable to the best currently available general-purpose compression methods. It is similar in speed with deflate but offers more dense compression.The specification of the Brotli Compressed Data Format is defined in RFC 7932.

https://github.com/google/brotli
# Available modules


The overview below shows which Brotli installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Brotli, load one of these modules using a `module load` command like:

```shell
module load Brotli/1.1.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Brotli/1.1.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|-|x|
|Brotli/1.0.9-GCCcore-12.3.0|x|x|x|x|x|x|x|x|-|x|
|Brotli/1.0.9-GCCcore-12.2.0|x|x|x|x|x|x|x|x|-|x|
