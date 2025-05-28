---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GROMACS is a versatile package to perform molecular dynamics, i.e.
    simulate theNewtonian equations of motion for systems with hundreds to millions
    ofparticles.This is a CPU only build, containing both MPI and threadMPI binariesfor
    both single and double precision.It also contains the gmxapi extension for the
    single precision MPI build.
  license: Not confirmed
  name: GROMACS
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
  softwareVersion: '[''GROMACS/2024.1-foss-2023b'', ''GROMACS/2024.3-foss-2023b'',
    ''GROMACS/2024.4-foss-2023b'']'
  url: https://www.gromacs.org
---

GROMACS
=======


GROMACS is a versatile package to perform molecular dynamics, i.e. simulate theNewtonian equations of motion for systems with hundreds to millions ofparticles.This is a CPU only build, containing both MPI and threadMPI binariesfor both single and double precision.It also contains the gmxapi extension for the single precision MPI build.

https://www.gromacs.org
# Available modules


The overview below shows which GROMACS installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GROMACS, load one of these modules using a `module load` command like:

```shell
module load GROMACS/2024.4-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GROMACS/2024.4-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GROMACS/2024.3-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GROMACS/2024.1-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|


### GROMACS/2024.4-foss-2023b

This is a list of extensions included in the module:

gmxapi-0.4.2

### GROMACS/2024.3-foss-2023b

This is a list of extensions included in the module:

gmxapi-0.4.2

### GROMACS/2024.1-foss-2023b

This is a list of extensions included in the module:

gmxapi-0.5.0