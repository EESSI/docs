---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Wayland is a project to define a protocol for a compositor to talk
    to its clients as well as a library implementation of the protocol.  The compositor
    can be a standalone display server running on Linux kernel modesetting and evdev
    input devices, an X application, or a wayland client itself.  The clients can
    be traditional applications, X servers (rootless or fullscreen) or other display
    servers.
  license: Not confirmed
  name: Wayland
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
  softwareVersion: '[''Wayland/1.22.0-GCCcore-12.3.0'', ''Wayland/1.22.0-GCCcore-13.2.0'']'
  url: https://wayland.freedesktop.org/
---

Wayland
=======


Wayland is a project to define a protocol for a compositor to talk to its clients as well as a library implementation of the protocol.  The compositor can be a standalone display server running on Linux kernel modesetting and evdev input devices, an X application, or a wayland client itself.  The clients can be traditional applications, X servers (rootless or fullscreen) or other display servers.

https://wayland.freedesktop.org/
# Available modules


The overview below shows which Wayland installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Wayland, load one of these modules using a `module load` command like:

```shell
module load Wayland/1.22.0-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Wayland/1.22.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Wayland/1.22.0-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
