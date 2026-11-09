---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'MPICH is a high-performance and widely portable implementation

    of the Message Passing Interface (MPI) standard (MPI-1, MPI-2 and MPI-3).'
  license: Not confirmed
  name: MPICH
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
  softwareVersion: '[''5.0.1'']'
  url: https://www.mpich.org/
---
# MPICH


MPICH is a high-performance and widely portable implementation
of the Message Passing Interface (MPI) standard (MPI-1, MPI-2 and MPI-3).

<small>homepage: </small><span class="software-link">[https://www.mpich.org/](https://www.mpich.org/)</span>

## Available installations


|MPICH version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`MPICH/5.0.1-GCC-15.2.0`|