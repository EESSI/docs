---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Cairo is a 2D graphics library with support for multiple output devices.\n\
    \ Currently supported output targets include the X Window System (via both Xlib\
    \ and XCB), Quartz, Win32, image buffers,\n PostScript, PDF, and SVG file output.\
    \ Experimental backends include OpenGL, BeOS, OS/2, and DirectFB"
  license: Not confirmed
  name: cairo
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
  softwareVersion: '[''1.18.4'']'
  url: https://cairographics.org
---
# cairo


Cairo is a 2D graphics library with support for multiple output devices.
 Currently supported output targets include the X Window System (via both Xlib and XCB), Quartz, Win32, image buffers,
 PostScript, PDF, and SVG file output. Experimental backends include OpenGL, BeOS, OS/2, and DirectFB

<small>homepage: </small><span class="software-link">[https://cairographics.org](https://cairographics.org)</span>

## Available installations


|cairo version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.18.4|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`cairo/1.18.4-GCCcore-14.3.0`|