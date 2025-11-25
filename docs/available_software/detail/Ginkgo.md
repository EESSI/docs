---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Ginkgo is a high-performance numerical linear algebra library witha
    focus on the solution of sparse linear systems. It also has support for popular
    GPUs(NVIDIA, AMD and Intel) with their native programming models, aiming to maximize
    the attainableperformance. It also has distributed support with MPI and can be
    used to run solvers and preconditionerson large scale supercomputers. With a focus
    on sustainable software development, it has comprehensive unittests, usage examples
    and continuous integration setups to ensure robustness. It also has been integratedinto
    many popular applications such as MFEM, OpenCARP, deal.ii, OpenFOAM etc.
  license: Not confirmed
  name: Ginkgo
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
  softwareVersion: '[''Ginkgo/1.9.0-gompi-2023b'']'
  url: https://github.com/ginkgo-project/ginkgo
---

Ginkgo
======


Ginkgo is a high-performance numerical linear algebra library witha focus on the solution of sparse linear systems. It also has support for popular GPUs(NVIDIA, AMD and Intel) with their native programming models, aiming to maximize the attainableperformance. It also has distributed support with MPI and can be used to run solvers and preconditionerson large scale supercomputers. With a focus on sustainable software development, it has comprehensive unittests, usage examples and continuous integration setups to ensure robustness. It also has been integratedinto many popular applications such as MFEM, OpenCARP, deal.ii, OpenFOAM etc.

https://github.com/ginkgo-project/ginkgo
# Available modules


The overview below shows which Ginkgo installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Ginkgo, load one of these modules using a `module load` command like:

```shell
module load Ginkgo/1.9.0-gompi-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Ginkgo/1.9.0-gompi-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
