---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The aim of VCFtools is to provide \n easily accessible methods for\
    \ working with complex \n genetic variation data in the form of VCF files."
  license: Not confirmed
  name: VCFtools
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
  softwareVersion: '[''0.1.16'']'
  url: https://vcftools.github.io
---
# VCFtools


The aim of VCFtools is to provide 
 easily accessible methods for working with complex 
 genetic variation data in the form of VCF files.

<small>homepage: </small><span class="software-link">[https://vcftools.github.io](https://vcftools.github.io)</span>

## Available installations


|VCFtools version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.1.16|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`VCFtools/0.1.16-GCC-12.2.0`|