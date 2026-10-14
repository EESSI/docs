---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Ginkgo is a high-performance numerical linear algebra library with

    a focus on the solution of sparse linear systems. It also has support for popular
    GPUs

    (NVIDIA, AMD and Intel) with their native programming models, aiming to maximize
    the attainable

    performance. It also has distributed support with MPI and can be used to run solvers
    and preconditioners

    on large scale supercomputers. With a focus on sustainable software development,
    it has comprehensive unit

    tests, usage examples and continuous integration setups to ensure robustness.
    It also has been integrated

    into many popular applications such as MFEM, OpenCARP, deal.ii, OpenFOAM etc.'
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
  softwareVersion: '[''1.9.0'']'
  url: https://github.com/ginkgo-project/ginkgo
---
# Ginkgo


Ginkgo is a high-performance numerical linear algebra library with
a focus on the solution of sparse linear systems. It also has support for popular GPUs
(NVIDIA, AMD and Intel) with their native programming models, aiming to maximize the attainable
performance. It also has distributed support with MPI and can be used to run solvers and preconditioners
on large scale supercomputers. With a focus on sustainable software development, it has comprehensive unit
tests, usage examples and continuous integration setups to ensure robustness. It also has been integrated
into many popular applications such as MFEM, OpenCARP, deal.ii, OpenFOAM etc.

<small>homepage: </small><span class="software-link">[https://github.com/ginkgo-project/ginkgo](https://github.com/ginkgo-project/ginkgo)</span>

## Available installations


|Ginkgo version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.9.0|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Ginkgo/1.9.0-gompi-2023b`|