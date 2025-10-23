---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: PuLP is an LP modeler written in Python. PuLP can generate MPS or LP
    files andcall GLPK, COIN-OR CLP/CBC, CPLEX, GUROBI, MOSEK, XPRESS, CHOCO, MIPCL,
    SCIP tosolve linear problems.
  license: Not confirmed
  name: PuLP
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
  softwareVersion: '[''PuLP/2.8.0-foss-2023a'', ''PuLP/2.8.0-foss-2023b'']'
  url: https://github.com/coin-or/pulp
---

PuLP
====


PuLP is an LP modeler written in Python. PuLP can generate MPS or LP files andcall GLPK, COIN-OR CLP/CBC, CPLEX, GUROBI, MOSEK, XPRESS, CHOCO, MIPCL, SCIP tosolve linear problems.

https://github.com/coin-or/pulp
# Available modules


The overview below shows which PuLP installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PuLP, load one of these modules using a `module load` command like:

```shell
module load PuLP/2.8.0-foss-2023b
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PuLP/2.8.0-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|PuLP/2.8.0-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
