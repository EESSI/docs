---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'A python extension, written in C, for quick access to bigBed

    files and access to and creation of bigWig files.'
  license: Not confirmed
  name: pyBigWig
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
  softwareVersion: '[''0.3.24'']'
  url: https://github.com/deeptools/pyBigWig
---
# pyBigWig


A python extension, written in C, for quick access to bigBed
files and access to and creation of bigWig files.

<small>homepage: </small><span class="software-link">[https://github.com/deeptools/pyBigWig](https://github.com/deeptools/pyBigWig)</span>

## Available installations


|pyBigWig version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.3.24|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`pyBigWig/0.3.24-gfbf-2024a`|