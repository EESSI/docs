---
hide:
  - toc
---
{% set eessi_202306 = '<span class="software-eessi-version-202306">2023.06</span>' %}
{% set eessi_202506 = '<span class="software-eessi-version-202506">2025.06</span>' %}

# CPU targets

The following table lists the CPU microarchitectures that are natively supported by the different versions of the EESSI repository.

| CPU target                    | Description                                                        | Supported in EESSI version                            |
| ----------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------- |
| `aarch64/generic`             | fallback for Arm 64-bit CPUs (like Raspberri Pi, etc.)             | {{ eessi_202306 }} {{ eessi_202506 }} |
| `aarch64/a64fx`               | Fujitsu A64FX                                                      | {{ eessi_202306 }} {{ eessi_202506 }} |
| `aarch64/neoverse_n1`         | AWS Graviton 2, Ampere Altra, ...                                  | {{ eessi_202306 }} {{ eessi_202506 }} |
| `aarch64/neoverse_v1`         | AWS Graviton 3                                                     | {{ eessi_202306 }} {{ eessi_202506 }} |
| `aarch64/nvidia/grace`        | NVIDIA Grace                                                       | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/generic`              | fallback for older Intel + AMD CPUs (like Intel Sandy Bridge, ...) | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/amd/zen2`             | AMD Rome                                                           | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/amd/zen3`             | AMD Milan, Milan-X                                                 | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/amd/zen4`             | AMD Genoa, Genoa-X, Bergamo, Siena                                 | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/amd/zen5`             | AMD Turin                                                          | {{ eessi_202506 }}                            |
| `x86_64/intel/haswell`        | Intel Haswell, Broadwell                                           | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/intel/skylake_avx512` | Intel Skylake                                                      | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/intel/cascadelake`    | Intel Cascade Lake, Cooper Lake                                    | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/intel/icelake`        | Intel Ice Lake                                                     | {{ eessi_202306 }} {{ eessi_202506 }} |
| `x86_64/intel/sapphirerapids` | Intel Sapphire Rapids, Emerald Rapids                              | {{ eessi_202306 }} {{ eessi_202506 }} |

The names of these CPU targets correspond to the names used by [archspec](https://github.com/archspec/archspec).

!!! info "What does native support mean?"
    Native support means that the software has been built on, and has been optimized for, this specific CPU type.
    That does not mean that CPUs that are not listed here are not supported:
    EESSI's CPU autodetection scripts will simply fall back to the stack of the best matching CPU type in terms of supported CPU instructions.
    For instance, on an Intel Broadwell CPU you will get the stack optimized for Intel Haswell, and for an AMD Zen 5 CPU you would get the Zen 4 stack in EESSI 2023.06.
