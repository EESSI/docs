---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Read, write and analyze MD trajectories with only a few lines of Python
    code.
  license: Not confirmed
  name: MDTraj
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
  softwareVersion: '[''1.11.0'']'
  url: https://mdtraj.org
---
# MDTraj


Read, write and analyze MD trajectories with only a few lines of Python code.

<small>homepage: </small><span class="software-link">[https://mdtraj.org](https://mdtraj.org)</span>

## Available installations


|MDTraj version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.11.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MDTraj/1.11.0-foss-2025b`|
|1.11.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MDTraj/1.11.0-foss-2025a`|

## Extensions

Overview of extensions included in MDTraj installations


### gsd


|`gsd` version|MDTraj modules that include it|
| --- | --- |
|4.2.0|`MDTraj/1.11.0-foss-2025b`|

### mdtraj


|`mdtraj` version|MDTraj modules that include it|
| --- | --- |
|1.11.0|`MDTraj/1.11.0-foss-2025b`<br/>`MDTraj/1.11.0-foss-2025a`|

### pyparsing


|`pyparsing` version|MDTraj modules that include it|
| --- | --- |
|3.2.5|`MDTraj/1.11.0-foss-2025b`|
|3.2.3|`MDTraj/1.11.0-foss-2025a`|

### pytest_rerunfailures


|`pytest_rerunfailures` version|MDTraj modules that include it|
| --- | --- |
|16.1|`MDTraj/1.11.0-foss-2025b`|