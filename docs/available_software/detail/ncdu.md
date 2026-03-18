---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Ncdu is a disk usage analyzer with an ncurses interface. It is designed\
    \ to find space hogs on a\n remote server where you don't have an entire graphical\
    \ setup available, but it is a useful tool even on regular\n desktop systems.\
    \ Ncdu aims to be fast, simple and easy to use, and should be able to run in any\
    \ minimal POSIX-like\n environment with ncurses installed."
  license: Not confirmed
  name: ncdu
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
  softwareVersion: '[''1.18'']'
  url: https://dev.yorhel.nl/ncdu
---
# ncdu


Ncdu is a disk usage analyzer with an ncurses interface. It is designed to find space hogs on a
 remote server where you don't have an entire graphical setup available, but it is a useful tool even on regular
 desktop systems. Ncdu aims to be fast, simple and easy to use, and should be able to run in any minimal POSIX-like
 environment with ncurses installed.

<small>homepage: </small><span class="software-link">[https://dev.yorhel.nl/ncdu](https://dev.yorhel.nl/ncdu)</span>

## Available installations


|ncdu version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.18|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ncdu/1.18-GCC-12.3.0`|