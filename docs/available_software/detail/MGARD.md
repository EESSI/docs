---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'MGARD (MultiGrid Adaptive Reduction of Data) is a technique for multilevel
    lossy compression and

    refactoring of scientific data based on the theory of multigrid methods'
  license: Not confirmed
  name: MGARD
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
  softwareVersion: '[''1.6.0'']'
  url: https://github.com/CODARcode/MGARD
---
# MGARD


MGARD (MultiGrid Adaptive Reduction of Data) is a technique for multilevel lossy compression and
refactoring of scientific data based on the theory of multigrid methods

<small>homepage: </small><span class="software-link">[https://github.com/CODARcode/MGARD](https://github.com/CODARcode/MGARD)</span>

## Available installations


|MGARD version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.6.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MGARD/1.6.0-GCC-14.3.0`|