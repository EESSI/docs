---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "MPI for Python (mpi4py) provides bindings of the Message Passing Interface\
    \ (MPI) standard for\n the Python programming language, allowing any Python program\
    \ to exploit multiple processors."
  license: Not confirmed
  name: mpi4py
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
  softwareVersion: '[''4.1.0'']'
  url: https://github.com/mpi4py/mpi4py
---
# mpi4py


MPI for Python (mpi4py) provides bindings of the Message Passing Interface (MPI) standard for
 the Python programming language, allowing any Python program to exploit multiple processors.

<small>homepage: </small><span class="software-link">[https://github.com/mpi4py/mpi4py](https://github.com/mpi4py/mpi4py)</span>

## Available installations


|mpi4py version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.1.0|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`mpi4py/4.1.0-gompi-2025b`|

## Extensions

Overview of extensions included in mpi4py installations


### mpi4py


|`mpi4py` version|mpi4py modules that include it|
| --- | --- |
|4.1.0|`mpi4py/4.1.0-gompi-2025b`|