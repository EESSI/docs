---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Imageio is a Python library that provides an easy interface to read\
    \ and write a wide range of\n image data, including animated images, video, volumetric\
    \ data, and scientific formats."
  license: Not confirmed
  name: imageio
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
  softwareVersion: '[''2.37.0'']'
  url: https://imageio.github.io
---
# imageio


Imageio is a Python library that provides an easy interface to read and write a wide range of
 image data, including animated images, video, volumetric data, and scientific formats.

<small>homepage: </small><span class="software-link">[https://imageio.github.io](https://imageio.github.io)</span>

## Available installations


|imageio version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.37.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`imageio/2.37.0-gfbf-2025a`|