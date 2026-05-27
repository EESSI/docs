---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The NCO toolkit manipulates and analyzes data stored in netCDF-accessible
    formats,

    including DAP, HDF4, and HDF5.'
  license: Not confirmed
  name: NCO
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
  softwareVersion: '[''5.1.9'']'
  url: https://github.com/nco/nco
---
# NCO


The NCO toolkit manipulates and analyzes data stored in netCDF-accessible formats,
including DAP, HDF4, and HDF5.

<small>homepage: </small><span class="software-link">[https://github.com/nco/nco](https://github.com/nco/nco)</span>

## Available installations


|NCO version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.1.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`NCO/5.1.9-foss-2023a`|