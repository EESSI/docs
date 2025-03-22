---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators
    thatcan be used with other COIN-OR packages that make use of cuts, such as, amongothers,
    the linear solver Clp or the mixed integer linear programming solversCbc or BCP.
    Cgl uses the abstract class OsiSolverInterface (see Osi) to use orcommunicate
    with a solver. It does not directly call a solver.
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
  softwareVersion: '[''Cgl/0.60.8-foss-2023a'']'
  url: https://github.com/coin-or/Cgl
---

Cgl
===


The COIN-OR Cut Generation Library (Cgl) is a collection of cut generators thatcan be used with other COIN-OR packages that make use of cuts, such as, amongothers, the linear solver Clp or the mixed integer linear programming solversCbc or BCP. Cgl uses the abstract class OsiSolverInterface (see Osi) to use orcommunicate with a solver. It does not directly call a solver.

https://github.com/coin-or/Cgl
# Available modules


The overview below shows which Cgl installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Cgl, load one of these modules using a `module load` command like:

```shell
module load Cgl/0.60.8-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Cgl/0.60.8-foss-2023a|x|x|x|-|x|x|x|x|x|x|x|
