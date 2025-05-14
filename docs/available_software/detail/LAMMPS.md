---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: LAMMPS is a classical molecular dynamics code, and an acronymfor Large-scale
    Atomic/Molecular Massively Parallel Simulator. LAMMPS haspotentials for solid-state
    materials (metals, semiconductors) and soft matter(biomolecules, polymers) and
    coarse-grained or mesoscopic systems. It can beused to model atoms or, more generically,
    as a parallel particle simulator atthe atomic, meso, or continuum scale. LAMMPS
    runs on single processors or inparallel using message-passing techniques and a
    spatial-decomposition of thesimulation domain. The code is designed to be easy
    to modify or extend with newfunctionality.
  license: Not confirmed
  name: LAMMPS
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
  softwareVersion: '[''LAMMPS/2Aug2023_update2-foss-2023a-kokkos'', ''LAMMPS/29Aug2024-foss-2023b-kokkos'']'
  url: https://www.lammps.org
---

LAMMPS
======


LAMMPS is a classical molecular dynamics code, and an acronymfor Large-scale Atomic/Molecular Massively Parallel Simulator. LAMMPS haspotentials for solid-state materials (metals, semiconductors) and soft matter(biomolecules, polymers) and coarse-grained or mesoscopic systems. It can beused to model atoms or, more generically, as a parallel particle simulator atthe atomic, meso, or continuum scale. LAMMPS runs on single processors or inparallel using message-passing techniques and a spatial-decomposition of thesimulation domain. The code is designed to be easy to modify or extend with newfunctionality.

https://www.lammps.org
# Available modules


The overview below shows which LAMMPS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using LAMMPS, load one of these modules using a `module load` command like:

```shell
module load LAMMPS/29Aug2024-foss-2023b-kokkos
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|LAMMPS/29Aug2024-foss-2023b-kokkos|x|x|x|x|x|x|x|x|x|x|x|
|LAMMPS/2Aug2023_update2-foss-2023a-kokkos|x|x|x|x|x|x|x|x|x|x|x|
