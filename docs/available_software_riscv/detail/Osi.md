---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Osi (Open Solver Interface) provides an abstract base class to a generic
    linear

    programming (LP) solver, along with derived classes for specific solvers. Many

    applications may be able to use the Osi to insulate themselves from a specific

    LP solver. That is, programs written to the OSI standard may be linked to any

    solver with an OSI interface and should produce correct results. The OSI has

    been significantly extended compared to its first incarnation. Currently, the

    OSI supports linear programming solvers and has rudimentary support for integer

    programming.'
  license: Not confirmed
  name: Osi
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
  softwareVersion: '[''0.108.11'']'
  url: https://github.com/coin-or/Osi
---
# Osi


Osi (Open Solver Interface) provides an abstract base class to a generic linear
programming (LP) solver, along with derived classes for specific solvers. Many
applications may be able to use the Osi to insulate themselves from a specific
LP solver. That is, programs written to the OSI standard may be linked to any
solver with an OSI interface and should produce correct results. The OSI has
been significantly extended compared to its first incarnation. Currently, the
OSI supports linear programming solvers and has rudimentary support for integer
programming.

<small>homepage: </small><span class="software-link">[https://github.com/coin-or/Osi](https://github.com/coin-or/Osi)</span>

## Available installations


|Osi version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.108.11|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Osi/0.108.11-GCC-14.3.0`|