---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Numerical surface area integrator for molecular inputs.

    This project is based on routines from xtb and dftb+.'
  license: Not confirmed
  name: numsa
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
  softwareVersion: '[''0.2.0'']'
  url: https://github.com/grimme-lab/CPCM-X
---
# numsa


Numerical surface area integrator for molecular inputs.
This project is based on routines from xtb and dftb+.

<small>homepage: </small><span class="software-link">[https://github.com/grimme-lab/CPCM-X](https://github.com/grimme-lab/CPCM-X)</span>

## Available installations


|numsa version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`numsa/0.2.0-gfbf-2025a`|