---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Environ is a computational library aimed at introducing environment

    effects into atomistic first-principles simulations, in particular for

    applications in surface science and materials design.


    A hierarchical, multi-scale, strategy is at the base of the different

    methods implemented: while the atomistic and electronic details of the

    system of interest are fully preserved, the degrees of freedom of the

    surrounding environment (being it a liquid solution of a more complex

    embedding) are treated using simplified approaches. By reducing the

    number of degrees of freedom and by exploiting intrinsic or faster

    statistical averaging, the implemented methods allow the systematic

    un-expensive study of large systems.

    '
  license: Not confirmed
  name: Environ
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
  softwareVersion: '[''3.1.1'']'
  url: http://www.quantum-environ.org/
---
# Environ



Environ is a computational library aimed at introducing environment
effects into atomistic first-principles simulations, in particular for
applications in surface science and materials design.

A hierarchical, multi-scale, strategy is at the base of the different
methods implemented: while the atomistic and electronic details of the
system of interest are fully preserved, the degrees of freedom of the
surrounding environment (being it a liquid solution of a more complex
embedding) are treated using simplified approaches. By reducing the
number of degrees of freedom and by exploiting intrinsic or faster
statistical averaging, the implemented methods allow the systematic
un-expensive study of large systems.


<small>homepage: </small><span class="software-link">[http://www.quantum-environ.org/](http://www.quantum-environ.org/)</span>

## Available installations


|Environ version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Environ/3.1.1-foss-2025b`|