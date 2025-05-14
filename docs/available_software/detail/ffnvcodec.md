---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: FFmpeg nvidia headers. Adds support for nvenc and nvdec. Requires Nvidia
    GPU and drivers to be present(picked up dynamically).
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
  softwareVersion: '[''ffnvcodec/11.1.5.2'', ''ffnvcodec/12.0.16.0'', ''ffnvcodec/12.1.14.0'']'
  url: https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
---

ffnvcodec
=========


FFmpeg nvidia headers. Adds support for nvenc and nvdec. Requires Nvidia GPU and drivers to be present(picked up dynamically).

https://git.videolan.org/?p=ffmpeg/nv-codec-headers.git
# Available modules


The overview below shows which ffnvcodec installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ffnvcodec, load one of these modules using a `module load` command like:

```shell
module load ffnvcodec/12.1.14.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ffnvcodec/12.1.14.0|x|x|x|x|x|x|x|x|x|x|x|
|ffnvcodec/12.0.16.0|x|x|x|x|x|x|x|x|x|x|x|
|ffnvcodec/11.1.5.2|x|x|x|x|x|x|x|x|x|x|x|
