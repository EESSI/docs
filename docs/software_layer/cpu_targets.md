# CPU targets

In the 2023.06 version of the EESSI pilot repository, the following CPU microarchitectures are supported.

* `aarch64/generic`: fallback for Arm 64-bit CPUs (like Raspberri Pi, etc.)
* `aarch64/neoverse_n1`: AWS Graviton 2, Ampere Altra, ...
* `aarch64/neoverse_v1`: AWS Graviton 3
* `x86_64/generic`: fallback for older Intel + AMD CPUs (like Intel Sandy Bridge, ...)
* `x86_64/amd/zen2`: AMD Rome
* `x86_64/amd/zen3`: AMD Milan, AMD Milan X
* `x86_64/intel/haswell`: Intel Haswell, Broadwell
* `x86_64/intel/skylake_avx512`: Intel Skylake, Cascade Lake, Ice Lake, ...

The names of these CPU targets correspond to the names used by [archspec](https://github.com/archspec/archspec).
