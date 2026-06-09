---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'FFmpeg nvidia headers. Adds support for nvenc and nvdec. Requires
    Nvidia GPU and drivers to be present

    (picked up dynamically).'
  license: Not confirmed
  name: ffnvcodec
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
  softwareVersion: '[''13.0.19.0'']'
  url: https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
---
# ffnvcodec


FFmpeg nvidia headers. Adds support for nvenc and nvdec. Requires Nvidia GPU and drivers to be present
(picked up dynamically).

<small>homepage: </small><span class="software-link">[https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git](https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git)</span>

## Available installations


|ffnvcodec version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|13.0.19.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ffnvcodec/13.0.19.0`|