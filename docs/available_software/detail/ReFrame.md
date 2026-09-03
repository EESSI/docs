---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: ReFrame is a framework for writing regression tests for HPC systems.
  license: Not confirmed
  name: ReFrame
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
  softwareVersion: '[''4.10.2'', ''4.7.4'', ''4.6.2'', ''4.3.3'']'
  url: https://github.com/reframe-hpc/reframe
---
# ReFrame


ReFrame is a framework for writing regression tests for HPC systems.

<small>homepage: </small><span class="software-link">[https://github.com/reframe-hpc/reframe](https://github.com/reframe-hpc/reframe)</span>

## Available installations


|ReFrame version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.10.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`ReFrame/4.10.2-GCCcore-15.2.0-no-analytics`|
|4.7.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`ReFrame/4.7.4`|
|4.6.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ReFrame/4.6.2`|
|4.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ReFrame/4.3.3`|

## Extensions

Overview of extensions included in ReFrame installations


### argcomplete


|`argcomplete` version|ReFrame modules that include it|
| --- | --- |
|3.7.2|`ReFrame/4.10.2-GCCcore-15.2.0-no-analytics`|

### ClusterShell


|`ClusterShell` version|ReFrame modules that include it|
| --- | --- |
|1.9.3|`ReFrame/4.10.2-GCCcore-15.2.0-no-analytics`|

### fasteners


|`fasteners` version|ReFrame modules that include it|
| --- | --- |
|0.20|`ReFrame/4.10.2-GCCcore-15.2.0-no-analytics`|

### pip


|`pip` version|ReFrame modules that include it|
| --- | --- |
|24.0|`ReFrame/4.7.4`<br/>`ReFrame/4.6.2`|
|21.3.1|`ReFrame/4.3.3`|

### reframe


|`reframe` version|ReFrame modules that include it|
| --- | --- |
|4.7.4|`ReFrame/4.7.4`|
|4.6.2|`ReFrame/4.6.2`|
|4.3.3|`ReFrame/4.3.3`|

### reframe-hpc


|`reframe-hpc` version|ReFrame modules that include it|
| --- | --- |
|4.10.2|`ReFrame/4.10.2-GCCcore-15.2.0-no-analytics`|

### semver


|`semver` version|ReFrame modules that include it|
| --- | --- |
|3.0.4|`ReFrame/4.10.2-GCCcore-15.2.0-no-analytics`|

### setuptools


|`setuptools` version|ReFrame modules that include it|
| --- | --- |
|68.0.0|`ReFrame/4.7.4`<br/>`ReFrame/4.6.2`|

### wheel


|`wheel` version|ReFrame modules that include it|
| --- | --- |
|0.42.0|`ReFrame/4.7.4`<br/>`ReFrame/4.6.2`|
|0.37.1|`ReFrame/4.3.3`|