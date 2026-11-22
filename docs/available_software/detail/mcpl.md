---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: MCPL (Monte Carlo Particle Lists) is library and a file format for
    storing Monte Carlo particles to be used with a range of particle transport packages,
    such as MCNP, OpenMC, PHITS, McStas, McXtrace, as well as supporting tools such
    as KDSource
  license: Not confirmed
  name: mcpl
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
  softwareVersion: '[''2.2.8'']'
  url: https://mctools.github.io/mcpl
---
# mcpl


MCPL (Monte Carlo Particle Lists) is library and a file format for storing Monte Carlo particles to be used with a range of particle transport packages, such as MCNP, OpenMC, PHITS, McStas, McXtrace, as well as supporting tools such as KDSource

<small>homepage: </small><span class="software-link">[https://mctools.github.io/mcpl](https://mctools.github.io/mcpl)</span>

## Available installations


|mcpl version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.2.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`mcpl/2.2.8-foss-2025b`|