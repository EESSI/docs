---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    PDAL is Point Data Abstraction Library. It is a C/C++ open source library and
    applications for

    translating and processing point cloud data. It is not limited to LiDAR data,

    although the focus and impetus for many of the tools in the library have their
    origins in LiDAR.'
  license: Not confirmed
  name: PDAL
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
  softwareVersion: '[''2.8.2'']'
  url: https://pdal.io/
---
# PDAL



PDAL is Point Data Abstraction Library. It is a C/C++ open source library and applications for
translating and processing point cloud data. It is not limited to LiDAR data,
although the focus and impetus for many of the tools in the library have their origins in LiDAR.

<small>homepage: </small><span class="software-link">[https://pdal.io/](https://pdal.io/)</span>

## Available installations


|PDAL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.8.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`PDAL/2.8.2-foss-2023a`|