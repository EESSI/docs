---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'FlexiBLAS is a wrapper library that enables the exchange of the BLAS
    and LAPACK implementation

    used by a program without recompiling or relinking it.'
  license: Not confirmed
  name: FlexiBLAS
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
  softwareVersion: '[''3.4.5'']'
  url: https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release
---
# FlexiBLAS


FlexiBLAS is a wrapper library that enables the exchange of the BLAS and LAPACK implementation
used by a program without recompiling or relinking it.

<small>homepage: </small><span class="software-link">[https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release](https://gitlab.mpi-magdeburg.mpg.de/software/flexiblas-release)</span>

## Available installations


|FlexiBLAS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.4.5|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.5-GCC-14.3.0`|
|3.4.5|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.5-GCC-14.2.0`|
|3.4.5|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FlexiBLAS/3.4.5-llvm-compilers-20.1.8`|

## Extensions

Overview of extensions included in FlexiBLAS installations


### FlexiBLAS


|`FlexiBLAS` version|FlexiBLAS modules that include it|
| --- | --- |
|3.4.5|`FlexiBLAS/3.4.5-GCC-14.3.0`<br/>`FlexiBLAS/3.4.5-GCC-14.2.0`<br/>`FlexiBLAS/3.4.5-llvm-compilers-20.1.8`|

### LAPACK


|`LAPACK` version|FlexiBLAS modules that include it|
| --- | --- |
|3.12.1|`FlexiBLAS/3.4.5-GCC-14.3.0`<br/>`FlexiBLAS/3.4.5-llvm-compilers-20.1.8`|
|3.12.0|`FlexiBLAS/3.4.5-GCC-14.2.0`|