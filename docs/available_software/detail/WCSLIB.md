---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The FITS "World Coordinate System" (WCS) standard defines keywords

    and usage that provide for the description of astronomical coordinate systems
    in a

    FITS image header.'
  license: Not confirmed
  name: WCSLIB
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
  softwareVersion: '[''7.11'']'
  url: https://www.atnf.csiro.au/people/mcalabre/WCS/
---
# WCSLIB


The FITS "World Coordinate System" (WCS) standard defines keywords
and usage that provide for the description of astronomical coordinate systems in a
FITS image header.

<small>homepage: </small><span class="software-link">[https://www.atnf.csiro.au/people/mcalabre/WCS/](https://www.atnf.csiro.au/people/mcalabre/WCS/)</span>

## Available installations


|WCSLIB version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.11|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`WCSLIB/7.11-GCC-13.2.0`|