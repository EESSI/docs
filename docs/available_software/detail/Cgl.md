---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators
    that

    can be used with other COIN-OR packages that make use of cuts, such as, among

    others, the linear solver Clp or the mixed integer linear programming solvers

    Cbc or BCP. Cgl uses the abstract class OsiSolverInterface (see Osi) to use or

    communicate with a solver. It does not directly call a solver.'
  license: Not confirmed
  name: Cgl
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
  softwareVersion: '[''0.60.8'']'
  url: https://github.com/coin-or/Cgl
---
# Cgl


The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators that
can be used with other COIN-OR packages that make use of cuts, such as, among
others, the linear solver Clp or the mixed integer linear programming solvers
Cbc or BCP. Cgl uses the abstract class OsiSolverInterface (see Osi) to use or
communicate with a solver. It does not directly call a solver.

<small>homepage: </small><span class="software-link">[https://github.com/coin-or/Cgl](https://github.com/coin-or/Cgl)</span>

## Available installations


|Cgl version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.60.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Cgl/0.60.8-foss-2023a`|
|0.60.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Cgl/0.60.8-foss-2023b`|
|0.60.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Cgl/0.60.8-foss-2024a`|