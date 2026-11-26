---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This is an fully open source solvation model, based on the

    original conductor like screening model for realistic solvation (COSMO-RS)

    model by Klamt et al. in combination with the universal solvation model

    based on solute electron density (SMD) by Marenich, Cramer and Truhlar.'
  license: Not confirmed
  name: CPCM-X
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
  softwareVersion: '[''1.1.0'']'
  url: https://github.com/grimme-lab/CPCM-X
---
# CPCM-X


This is an fully open source solvation model, based on the
original conductor like screening model for realistic solvation (COSMO-RS)
model by Klamt et al. in combination with the universal solvation model
based on solute electron density (SMD) by Marenich, Cramer and Truhlar.

<small>homepage: </small><span class="software-link">[https://github.com/grimme-lab/CPCM-X](https://github.com/grimme-lab/CPCM-X)</span>

## Available installations


|CPCM-X version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`CPCM-X/1.1.0-gfbf-2025a`|