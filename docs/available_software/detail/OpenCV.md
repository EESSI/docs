---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "OpenCV (Open Source Computer Vision Library) is an open source computer\
    \ vision\n and machine learning software library. OpenCV was built to provide\n\
    \ a common infrastructure for computer vision applications and to accelerate\n\
    \ the use of machine perception in the commercial products.\n Includes extra modules\
    \ for OpenCV from the contrib repository."
  license: Not confirmed
  name: OpenCV
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
  softwareVersion: '[''4.8.1'']'
  url: https://opencv.org/
---
# OpenCV


OpenCV (Open Source Computer Vision Library) is an open source computer vision
 and machine learning software library. OpenCV was built to provide
 a common infrastructure for computer vision applications and to accelerate
 the use of machine perception in the commercial products.
 Includes extra modules for OpenCV from the contrib repository.

<small>homepage: </small><span class="software-link">[https://opencv.org/](https://opencv.org/)</span>

## Available installations


|OpenCV version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.8.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`OpenCV/4.8.1-foss-2023a-contrib`|