---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "GNU Wget is a free software package for retrieving files using HTTP,\
    \ HTTPS and FTP,\n the most widely-used Internet protocols. It is a non-interactive\
    \ commandline tool,\n so it may easily be called from scripts, cron jobs, terminals\
    \ without X-Windows support, etc."
  license: Not confirmed
  name: wget
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
  softwareVersion: '[''1.24.5'', ''1.21.4'']'
  url: https://www.gnu.org/software/wget
---
# wget


GNU Wget is a free software package for retrieving files using HTTP, HTTPS and FTP,
 the most widely-used Internet protocols. It is a non-interactive commandline tool,
 so it may easily be called from scripts, cron jobs, terminals without X-Windows support, etc.

<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/wget](https://www.gnu.org/software/wget)</span>

## Available installations


|wget version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.21.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`wget/1.21.4-GCCcore-13.2.0`|
|1.24.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`wget/1.24.5-GCCcore-12.3.0`|