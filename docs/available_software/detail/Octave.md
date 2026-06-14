---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GNU Octave is a high-level interpreted language, primarily intended
    for numerical computations.
  license: Not confirmed
  name: Octave
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
  softwareVersion: '[''10.3.0'', ''10.1.0'']'
  url: https://www.gnu.org/software/octave/
---
# Octave


GNU Octave is a high-level interpreted language, primarily intended for numerical computations.

<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/octave/](https://www.gnu.org/software/octave/)</span>

## Available installations


|Octave version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|10.3.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Octave/10.3.0-foss-2025a`|
|10.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Octave/10.1.0-foss-2023a`|

## Extensions

Overview of extensions included in Octave installations


### datatypes


|`datatypes` version|Octave modules that include it|
| --- | --- |
|1.1.5|`Octave/10.3.0-foss-2025a`|

### general


|`general` version|Octave modules that include it|
| --- | --- |
|2.1.3|`Octave/10.3.0-foss-2025a`<br/>`Octave/10.1.0-foss-2023a`|

### io


|`io` version|Octave modules that include it|
| --- | --- |
|2.7.0|`Octave/10.3.0-foss-2025a`|
|2.6.4|`Octave/10.1.0-foss-2023a`|

### optim


|`optim` version|Octave modules that include it|
| --- | --- |
|1.6.2|`Octave/10.3.0-foss-2025a`<br/>`Octave/10.1.0-foss-2023a`|

### statistics


|`statistics` version|Octave modules that include it|
| --- | --- |
|1.8.0|`Octave/10.3.0-foss-2025a`|
|1.6.6|`Octave/10.1.0-foss-2023a`|

### struct


|`struct` version|Octave modules that include it|
| --- | --- |
|1.0.18|`Octave/10.3.0-foss-2025a`<br/>`Octave/10.1.0-foss-2023a`|