---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'PAW setups for the GPAW Density Functional Theory package.

    Users can install setups manually using ''gpaw install-data'' or use setups from
    this package.

    The versions of GPAW and gpaw-data can be intermixed.  This package replaces GPAW-SETUPS,
    but

    the latter can still be loaded instead of this package (this might change in future
    gpaw versions).

    '
  license: Not confirmed
  name: gpaw-data
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
  softwareVersion: '[''1.0.1'']'
  url: https://wiki.fysik.dtu.dk/gpaw/
---
# gpaw-data


PAW setups for the GPAW Density Functional Theory package.
Users can install setups manually using 'gpaw install-data' or use setups from this package.
The versions of GPAW and gpaw-data can be intermixed.  This package replaces GPAW-SETUPS, but
the latter can still be loaded instead of this package (this might change in future gpaw versions).


<small>homepage: </small><span class="software-link">[https://wiki.fysik.dtu.dk/gpaw/](https://wiki.fysik.dtu.dk/gpaw/)</span>

## Available installations


|gpaw-data version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`gpaw-data/1.0.1-GCCcore-14.2.0`|