---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'f90wrap is a tool to automatically generate Python extension modules
    which

    interface to Fortran code that makes use of derived types. It builds on the

    capabilities of the popular f2py utility by generating a simpler Fortran 90

    interface to the original Fortran code which is then suitable for wrapping with

    f2py, together with a higher-level Pythonic wrapper that makes the existance of

    an additional layer transparent to the final user.'
  license: Not confirmed
  name: f90wrap
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
  softwareVersion: '[''0.2.13'']'
  url: https://github.com/jameskermode/f90wrap
---
# f90wrap


f90wrap is a tool to automatically generate Python extension modules which
interface to Fortran code that makes use of derived types. It builds on the
capabilities of the popular f2py utility by generating a simpler Fortran 90
interface to the original Fortran code which is then suitable for wrapping with
f2py, together with a higher-level Pythonic wrapper that makes the existance of
an additional layer transparent to the final user.

<small>homepage: </small><span class="software-link">[https://github.com/jameskermode/f90wrap](https://github.com/jameskermode/f90wrap)</span>

## Available installations


|f90wrap version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.2.13|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`f90wrap/0.2.13-foss-2023a`|