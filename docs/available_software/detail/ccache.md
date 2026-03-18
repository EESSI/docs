---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Ccache (or \u201Cccache\u201D) is a compiler cache. It speeds up recompilation\
    \ by\ncaching previous compilations and detecting when the same compilation is\
    \ being done again"
  license: Not confirmed
  name: ccache
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
  softwareVersion: '[''4.9'']'
  url: https://ccache.dev/
---
# ccache


Ccache (or “ccache”) is a compiler cache. It speeds up recompilation by
caching previous compilations and detecting when the same compilation is being done again

<small>homepage: </small><span class="software-link">[https://ccache.dev/](https://ccache.dev/)</span>

## Available installations


|ccache version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ccache/4.9-GCCcore-12.3.0`|