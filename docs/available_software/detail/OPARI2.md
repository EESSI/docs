---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n OPARI2, the successor of Forschungszentrum Juelich's OPARI, is\
    \ a\n source-to-source instrumentation tool for OpenMP and hybrid codes.\n It\
    \ surrounds OpenMP directives and runtime library calls with calls\n to the POMP2\
    \ measurement interface.\n"
  license: Not confirmed
  name: OPARI2
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
  softwareVersion: '[''2.0.9'', ''2.0.8'']'
  url: https://www.score-p.org
---
# OPARI2



 OPARI2, the successor of Forschungszentrum Juelich's OPARI, is a
 source-to-source instrumentation tool for OpenMP and hybrid codes.
 It surrounds OpenMP directives and runtime library calls with calls
 to the POMP2 measurement interface.


<small>homepage: </small><span class="software-link">[https://www.score-p.org](https://www.score-p.org)</span>

## Available installations


|OPARI2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`OPARI2/2.0.8-GCCcore-13.2.0`|
|2.0.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`OPARI2/2.0.9-GCCcore-14.2.0`|