---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the

    Newtonian equations of motion for systems with hundreds to millions of

    particles.


    This is a CPU only build, containing both MPI and threadMPI binaries

    for both single and double precision.


    It also contains the gmxapi extension for the single precision MPI build.

    '
  license: Not confirmed
  name: GROMACS
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
  softwareVersion: '[''2026.2'']'
  url: https://www.gromacs.org
---
# GROMACS



GROMACS is a versatile package to perform molecular dynamics, i.e. simulate the
Newtonian equations of motion for systems with hundreds to millions of
particles.

This is a CPU only build, containing both MPI and threadMPI binaries
for both single and double precision.

It also contains the gmxapi extension for the single precision MPI build.


<small>homepage: </small><span class="software-link">[https://www.gromacs.org](https://www.gromacs.org)</span>

## Available installations


|GROMACS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2026.2|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`GROMACS/2026.2-foss-2025b`|

## Extensions

Overview of extensions included in GROMACS installations


### gmxapi


|`gmxapi` version|GROMACS modules that include it|
| --- | --- |
|0.5.0a1|`GROMACS/2026.2-foss-2025b`|