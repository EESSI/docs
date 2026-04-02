---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'LAMMPS is a classical molecular dynamics code, and an acronym

    for Large-scale Atomic/Molecular Massively Parallel Simulator. LAMMPS has

    potentials for solid-state materials (metals, semiconductors) and soft matter

    (biomolecules, polymers) and coarse-grained or mesoscopic systems. It can be

    used to model atoms or, more generically, as a parallel particle simulator at

    the atomic, meso, or continuum scale. LAMMPS runs on single processors or in

    parallel using message-passing techniques and a spatial-decomposition of the

    simulation domain. The code is designed to be easy to modify or extend with new

    functionality.

    '
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
  softwareVersion: '[''2Aug2023_update2'', ''29Aug2024'', ''22Jul2025'']'
  url: https://www.lammps.org
---
# LAMMPS


LAMMPS is a classical molecular dynamics code, and an acronym
for Large-scale Atomic/Molecular Massively Parallel Simulator. LAMMPS has
potentials for solid-state materials (metals, semiconductors) and soft matter
(biomolecules, polymers) and coarse-grained or mesoscopic systems. It can be
used to model atoms or, more generically, as a parallel particle simulator at
the atomic, meso, or continuum scale. LAMMPS runs on single processors or in
parallel using message-passing techniques and a spatial-decomposition of the
simulation domain. The code is designed to be easy to modify or extend with new
functionality.


<small>homepage: </small><span class="software-link">[https://www.lammps.org](https://www.lammps.org)</span>

## Available installations


|LAMMPS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|22Jul2025|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`LAMMPS/22Jul2025-foss-2024a-kokkos`|
|29Aug2024|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`LAMMPS/29Aug2024-foss-2023b-kokkos`|
|2Aug2023_update2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|<span class="software-gpu-nvidia">NVIDIA</span>: `cc70`, `cc80`, `cc90`<br/>|<span class="software-eessi-version-202306">2023.06</span>|`LAMMPS/2Aug2023_update2-foss-2023a-kokkos-CUDA-12.1.1`|
|2Aug2023_update2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`LAMMPS/2Aug2023_update2-foss-2023a-kokkos`|