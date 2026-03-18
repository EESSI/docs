---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Salmon is a wicked-fast program to produce a highly-accurate,\n transcript-level\
    \ quantification estimate from RNA-seq data."
  license: Not confirmed
  name: Salmon
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
  softwareVersion: '[''1.10.3'']'
  url: https://github.com/COMBINE-lab/salmon
---
# Salmon


Salmon is a wicked-fast program to produce a highly-accurate,
 transcript-level quantification estimate from RNA-seq data.

<small>homepage: </small><span class="software-link">[https://github.com/COMBINE-lab/salmon](https://github.com/COMBINE-lab/salmon)</span>

## Available installations


|Salmon version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.10.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Salmon/1.10.3-GCC-12.3.0`|