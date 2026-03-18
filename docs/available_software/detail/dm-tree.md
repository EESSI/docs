---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'dm-tree provides tree, a library for working with nested data structures.
    In a way,

    tree generalizes the builtin map function which only supports flat sequences,
    and

    allows to apply a function to each "leaf" preserving the overall structure.'
  license: Not confirmed
  name: dm-tree
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
  softwareVersion: '[''0.1.8'']'
  url: https://github.com/deepmind/tree
---
# dm-tree


dm-tree provides tree, a library for working with nested data structures. In a way,
tree generalizes the builtin map function which only supports flat sequences, and
allows to apply a function to each "leaf" preserving the overall structure.

<small>homepage: </small><span class="software-link">[https://github.com/deepmind/tree](https://github.com/deepmind/tree)</span>

## Available installations


|dm-tree version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.1.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`dm-tree/0.1.8-GCCcore-12.3.0`|