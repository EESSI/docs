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
|1.9.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Ginkgo/1.9.0-gompi-2023b`|