---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Pixman is a low-level software library for pixel manipulation,\
    \ providing\n features such as image compositing and trapezoid rasterization.\
    \ Important\n users of pixman are the cairo graphics library and the X server.\n"
  license: Not confirmed
  name: pixman
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
  softwareVersion: '[''0.46.4'']'
  url: http://www.pixman.org/
---
# pixman



 Pixman is a low-level software library for pixel manipulation, providing
 features such as image compositing and trapezoid rasterization. Important
 users of pixman are the cairo graphics library and the X server.


<small>homepage: </small><span class="software-link">[http://www.pixman.org/](http://www.pixman.org/)</span>

## Available installations


|pixman version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.46.4|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`pixman/0.46.4-GCCcore-14.3.0`|