---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'LIBXSMM is a library for small dense and small sparse matrix-matrix
    multiplications

    targeting Intel Architecture (x86).'
  license: Not confirmed
  name: libxsmm
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
  softwareVersion: '[''1.17'']'
  url: https://github.com/hfp/libxsmm
---
# libxsmm


LIBXSMM is a library for small dense and small sparse matrix-matrix multiplications
targeting Intel Architecture (x86).

<small>homepage: </small><span class="software-link">[https://github.com/hfp/libxsmm](https://github.com/hfp/libxsmm)</span>

## Available installations


|libxsmm version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.17|`generic`: `x86_64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libxsmm/1.17-GCC-12.3.0`|