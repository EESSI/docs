---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Ghostscript is a versatile processor for PostScript data with the ability
    to render PostScript to different targets. It used to be part of the cups printing
    stack, but is no longer used for that.
  license: Not confirmed
  name: Ghostscript
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
  softwareVersion: '[''Ghostscript/10.0.0-GCCcore-12.2.0'', ''Ghostscript/10.01.2-GCCcore-12.3.0'',
    ''Ghostscript/10.02.1-GCCcore-13.2.0'']'
  url: https://ghostscript.com
---

Ghostscript
===========


Ghostscript is a versatile processor for PostScript data with the ability to render PostScript to different targets. It used to be part of the cups printing stack, but is no longer used for that.

https://ghostscript.com
# Available modules


The overview below shows which Ghostscript installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Ghostscript, load one of these modules using a `module load` command like:

```shell
module load Ghostscript/10.02.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Ghostscript/10.02.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|Ghostscript/10.01.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|Ghostscript/10.0.0-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
