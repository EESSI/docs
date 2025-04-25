---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Generic PCI access library.
  license: Not confirmed
  name: libpciaccess
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
  softwareVersion: '[''libpciaccess/0.17-GCCcore-12.2.0'', ''libpciaccess/0.17-GCCcore-12.3.0'',
    ''libpciaccess/0.17-GCCcore-13.2.0'']'
  url: https://cgit.freedesktop.org/xorg/lib/libpciaccess/
---

libpciaccess
============


Generic PCI access library.

https://cgit.freedesktop.org/xorg/lib/libpciaccess/
# Available modules


The overview below shows which libpciaccess installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libpciaccess, load one of these modules using a `module load` command like:

```shell
module load libpciaccess/0.17-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|libpciaccess/0.17-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
|libpciaccess/0.17-GCCcore-12.3.0|x|x|x|-|x|x|x|x|x|x|x|x|
|libpciaccess/0.17-GCCcore-12.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
