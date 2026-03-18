---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The DWARF Debugging Information Format is of interest to programmers
    working on compilers

    and debuggers (and anyone interested in reading or writing DWARF information))'
  license: Not confirmed
  name: libdwarf
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
  softwareVersion: '[''0.9.2'']'
  url: https://www.prevanders.net/dwarf.html
---
# libdwarf


The DWARF Debugging Information Format is of interest to programmers working on compilers
and debuggers (and anyone interested in reading or writing DWARF information))

<small>homepage: </small><span class="software-link">[https://www.prevanders.net/dwarf.html](https://www.prevanders.net/dwarf.html)</span>

## Available installations


|libdwarf version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.9.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libdwarf/0.9.2-GCCcore-13.2.0`|