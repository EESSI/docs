---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "ecCodes is a package developed by ECMWF which provides an application\
    \ programming interface and\n a set of tools for decoding and encoding messages\
    \ in the following formats: WMO FM-92 GRIB edition 1 and edition 2,\n WMO FM-94\
    \ BUFR edition 3 and edition 4, WMO GTS abbreviated header (only decoding)."
  license: Not confirmed
  name: ecCodes
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
  softwareVersion: '[''2.31.0'']'
  url: https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home
---
# ecCodes


ecCodes is a package developed by ECMWF which provides an application programming interface and
 a set of tools for decoding and encoding messages in the following formats: WMO FM-92 GRIB edition 1 and edition 2,
 WMO FM-94 BUFR edition 3 and edition 4, WMO GTS abbreviated header (only decoding).

<small>homepage: </small><span class="software-link">[https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home](https://software.ecmwf.int/wiki/display/ECC/ecCodes+Home)</span>

## Available installations


|ecCodes version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.31.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ecCodes/2.31.0-gompi-2023a`|
|2.31.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ecCodes/2.31.0-gompi-2023b`|