---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'GTS stands for the GNU Triangulated Surface Library.

    It is an Open Source Free Software Library intended to provide a set of useful

    functions to deal with 3D surfaces meshed with interconnected triangles.'
  license: Not confirmed
  name: GTS
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
  softwareVersion: '[''0.7.6'']'
  url: http://gts.sourceforge.net/
---
# GTS


GTS stands for the GNU Triangulated Surface Library.
It is an Open Source Free Software Library intended to provide a set of useful
functions to deal with 3D surfaces meshed with interconnected triangles.

<small>homepage: </small><span class="software-link">[http://gts.sourceforge.net/](http://gts.sourceforge.net/)</span>

## Available installations


|GTS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.7.6|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`GTS/0.7.6-GCCcore-12.3.0`|