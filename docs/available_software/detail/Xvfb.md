---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Xvfb is an X server that can run on machines with no display hardware
    and no physical input devices. It emulates a dumb framebuffer using virtual memory.
  license: Not confirmed
  name: Xvfb
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
  softwareVersion: '[''Xvfb/21.1.6-GCCcore-12.2.0'', ''Xvfb/21.1.8-GCCcore-12.3.0'',
    ''Xvfb/21.1.9-GCCcore-13.2.0'']'
  url: https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml
---

Xvfb
====


Xvfb is an X server that can run on machines with no display hardware and no physical input devices. It emulates a dumb framebuffer using virtual memory.

https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml
# Available modules


The overview below shows which Xvfb installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Xvfb, load one of these modules using a `module load` command like:

```shell
module load Xvfb/21.1.9-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Xvfb/21.1.9-GCCcore-13.2.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
|Xvfb/21.1.8-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|Xvfb/21.1.6-GCCcore-12.2.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
