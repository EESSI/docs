---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Hypre is a library for solving large, sparse linear systems of equations\
    \ on massively\n parallel computers. The problems of interest arise in the simulation\
    \ codes being developed at LLNL\n and elsewhere to study physical phenomena in\
    \ the defense, environmental, energy, and biological sciences."
  license: Not confirmed
  name: Hypre
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
  softwareVersion: '[''2.33.0'', ''2.31.0'', ''2.29.0'']'
  url: https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods
---
# Hypre


Hypre is a library for solving large, sparse linear systems of equations on massively
 parallel computers. The problems of interest arise in the simulation codes being developed at LLNL
 and elsewhere to study physical phenomena in the defense, environmental, energy, and biological sciences.

<small>homepage: </small><span class="software-link">[https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods](https://computation.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods)</span>

## Available installations


|Hypre version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.29.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Hypre/2.29.0-foss-2023a`|
|2.31.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Hypre/2.31.0-foss-2023b`|
|2.33.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Hypre/2.33.0-foss-2025a`|