---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Python is a programming language that lets you work more quickly and\
    \ integrate your systems\n more effectively."
  license: Not confirmed
  name: Python
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
  softwareVersion: '[''3.13.5'', ''3.13.1'', ''3.12.3'', ''3.11.5'', ''3.11.3'']'
  url: https://python.org/
---
# Python


Python is a programming language that lets you work more quickly and integrate your systems
 more effectively.

<small>homepage: </small><span class="software-link">[https://python.org/](https://python.org/)</span>

## Available installations


|Python version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.13.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Python/3.13.5-GCCcore-14.3.0`|
|3.13.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Python/3.13.1-GCCcore-14.2.0`|
|3.12.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Python/3.12.3-GCCcore-13.3.0`|
|3.11.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Python/3.11.5-GCCcore-13.2.0`|
|3.11.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Python/3.11.3-GCCcore-12.3.0`|

## Extensions

Overview of extensions included in Python installations


### flit_core


|`flit_core` version|Python modules that include it|
| --- | --- |
|3.12.0|`Python/3.13.5-GCCcore-14.3.0`|
|3.10.1|`Python/3.13.1-GCCcore-14.2.0`|
|3.9.0|`Python/3.12.3-GCCcore-13.3.0`<br/>`Python/3.11.5-GCCcore-13.2.0`<br/>`Python/3.11.3-GCCcore-12.3.0`|

### packaging


|`packaging` version|Python modules that include it|
| --- | --- |
|25.0|`Python/3.13.5-GCCcore-14.3.0`|
|24.2|`Python/3.13.1-GCCcore-14.2.0`|
|24.0|`Python/3.12.3-GCCcore-13.3.0`|
|23.2|`Python/3.11.5-GCCcore-13.2.0`|
|23.1|`Python/3.11.3-GCCcore-12.3.0`|

### pip


|`pip` version|Python modules that include it|
| --- | --- |
|25.1.1|`Python/3.13.5-GCCcore-14.3.0`|
|24.3.1|`Python/3.13.1-GCCcore-14.2.0`|
|24.0|`Python/3.12.3-GCCcore-13.3.0`|
|23.2.1|`Python/3.11.5-GCCcore-13.2.0`|
|23.1.2|`Python/3.11.3-GCCcore-12.3.0`|

### setuptools


|`setuptools` version|Python modules that include it|
| --- | --- |
|80.9.0|`Python/3.13.5-GCCcore-14.3.0`|
|75.6.0|`Python/3.13.1-GCCcore-14.2.0`|
|70.0.0|`Python/3.12.3-GCCcore-13.3.0`|
|68.2.2|`Python/3.11.5-GCCcore-13.2.0`|
|67.7.2|`Python/3.11.3-GCCcore-12.3.0`|

### setuptools-scm


|`setuptools-scm` version|Python modules that include it|
| --- | --- |
|8.0.4|`Python/3.11.5-GCCcore-13.2.0`|

### setuptools_scm


|`setuptools_scm` version|Python modules that include it|
| --- | --- |
|8.3.1|`Python/3.13.5-GCCcore-14.3.0`|
|8.1.0|`Python/3.13.1-GCCcore-14.2.0`<br/>`Python/3.12.3-GCCcore-13.3.0`|
|7.1.0|`Python/3.11.3-GCCcore-12.3.0`|

### tomli


|`tomli` version|Python modules that include it|
| --- | --- |
|2.2.1|`Python/3.13.5-GCCcore-14.3.0`<br/>`Python/3.13.1-GCCcore-14.2.0`|
|2.0.1|`Python/3.12.3-GCCcore-13.3.0`<br/>`Python/3.11.5-GCCcore-13.2.0`<br/>`Python/3.11.3-GCCcore-12.3.0`|

### typing_extensions


|`typing_extensions` version|Python modules that include it|
| --- | --- |
|4.14.0|`Python/3.13.5-GCCcore-14.3.0`|
|4.12.2|`Python/3.13.1-GCCcore-14.2.0`|
|4.11.0|`Python/3.12.3-GCCcore-13.3.0`|
|4.8.0|`Python/3.11.5-GCCcore-13.2.0`|
|4.6.3|`Python/3.11.3-GCCcore-12.3.0`|

### wheel


|`wheel` version|Python modules that include it|
| --- | --- |
|0.45.1|`Python/3.13.5-GCCcore-14.3.0`<br/>`Python/3.13.1-GCCcore-14.2.0`|
|0.43.0|`Python/3.12.3-GCCcore-13.3.0`|
|0.41.2|`Python/3.11.5-GCCcore-13.2.0`|
|0.40.0|`Python/3.11.3-GCCcore-12.3.0`|