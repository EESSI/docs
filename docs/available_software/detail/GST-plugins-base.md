---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GStreamer is a library for constructing graphs of media-handling components.
    The applications it supports range from simple Ogg/Vorbis playback, audio/video
    streaming to complex audio (mixing) and video (non-linear editing) processing.
  license: Not confirmed
  name: GST-plugins-base
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
  softwareVersion: '[''GST-plugins-base/1.22.1-GCC-12.2.0'', ''GST-plugins-base/1.22.5-GCC-12.3.0'',
    ''GST-plugins-base/1.24.8-GCC-13.2.0'']'
  url: https://gstreamer.freedesktop.org/
---

GST-plugins-base
================


GStreamer is a library for constructing graphs of media-handling components. The applications it supports range from simple Ogg/Vorbis playback, audio/video streaming to complex audio (mixing) and video (non-linear editing) processing.

https://gstreamer.freedesktop.org/
# Available modules


The overview below shows which GST-plugins-base installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GST-plugins-base, load one of these modules using a `module load` command like:

```shell
module load GST-plugins-base/1.24.8-GCC-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GST-plugins-base/1.24.8-GCC-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GST-plugins-base/1.22.5-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GST-plugins-base/1.22.1-GCC-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
