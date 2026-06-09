---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Libaec provides fast lossless compression of 1 up to 32 bit wide signed
    or unsigned integers

    (samples). The library achieves best results for low entropy data as often encountered
    in space imaging

    instrument data or numerical model output from weather or climate simulations.
    While floating point representations

    are not directly supported, they can also be efficiently coded by grouping exponents
    and mantissa.'
  license: Not confirmed
  name: libaec
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
  softwareVersion: '[''1.1.4'']'
  url: https://gitlab.dkrz.de/k202009/libaec
---
# libaec


Libaec provides fast lossless compression of 1 up to 32 bit wide signed or unsigned integers
(samples). The library achieves best results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate simulations. While floating point representations
are not directly supported, they can also be efficiently coded by grouping exponents and mantissa.

<small>homepage: </small><span class="software-link">[https://gitlab.dkrz.de/k202009/libaec](https://gitlab.dkrz.de/k202009/libaec)</span>

## Available installations


|libaec version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.1.4|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libaec/1.1.4-GCCcore-14.3.0`|