---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Underworld is a Python API (Application Programming Interface) which provides

    functionality for the modelling of geodynamics processes, and is designed to

    work (almost) seamlessly across PC, cloud and HPC infrastructure. Primarily

    the API consists of a set of Python classes from which numerical geodynamics

    models may be constructed. The API also provides the tools required for inline

    analysis and data management. For scalability across multiprocessor platforms,

    MPI (Message Passing Interface) is leveraged, and for performant operation all

    heavy computations are executed within a statically typed layer.

    Note: This version does not come with badlands.

    '
  license: Not confirmed
  name: Underworld
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
  softwareVersion: '[''2.16.4'']'
  url: https://www.underworldcode.org
---
# Underworld



Underworld is a Python API (Application Programming Interface) which provides
functionality for the modelling of geodynamics processes, and is designed to
work (almost) seamlessly across PC, cloud and HPC infrastructure. Primarily
the API consists of a set of Python classes from which numerical geodynamics
models may be constructed. The API also provides the tools required for inline
analysis and data management. For scalability across multiprocessor platforms,
MPI (Message Passing Interface) is leveraged, and for performant operation all
heavy computations are executed within a statically typed layer.
Note: This version does not come with badlands.


<small>homepage: </small><span class="software-link">[https://www.underworldcode.org](https://www.underworldcode.org)</span>

## Available installations


|Underworld version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.16.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Underworld/2.16.4-foss-2023b-egl`|

## Extensions

Overview of extensions included in Underworld installations


### nbmake


|`nbmake` version|Underworld modules that include it|
| --- | --- |
|1.5.5|`Underworld/2.16.4-foss-2023b-egl`|

### underworld


|`underworld` version|Underworld modules that include it|
| --- | --- |
|2.16.4|`Underworld/2.16.4-foss-2023b-egl`|