---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Extrae is the package devoted to generate Paraver trace-files for
    a post-mortem analysis.

    Extrae is a tool that uses different interposition mechanisms to inject probes
    into the target application

    so as to gather information regarding the application performance.'
  license: Not confirmed
  name: Extrae
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
  softwareVersion: '[''4.2.0'']'
  url: https://tools.bsc.es/extrae
---
# Extrae


Extrae is the package devoted to generate Paraver trace-files for a post-mortem analysis.
Extrae is a tool that uses different interposition mechanisms to inject probes into the target application
so as to gather information regarding the application performance.

<small>homepage: </small><span class="software-link">[https://tools.bsc.es/extrae](https://tools.bsc.es/extrae)</span>

## Available installations


|Extrae version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Extrae/4.2.0-gompi-2023b`|