---
authors: [toine, timvc, boegel, ocaisa, darkless]
date: 2025-06-24
slug: rocm
---

# Building ROCm Support in EESSI

* an overview of what we're doing (adding ROCm support, previous blog post, etc)

<!-- more -->

## Our Goals: The ROCm Integration Roadmap

* main objective: full rocm support in EESSI
* milestones:
    * building core ROCm components (in EESSI)
    * driver support
    * validation suite / examples running

## Foundation Work: What We Did Before

* ecosystem mapping: ROCm overview (previous blog post)
* used these as a starting point (started on version 6.3.3)
    * https://github.com/bedroge/eb-rocm/tree/main (Bob)
    * https://github.com/Thyre/easybuild-custom/tree/support-passing-amdgcn/easybuild/easyconfigs/r (Jan)
* Davide got ROCm-LLVM to build with EasyBuild
    * https://github.com/easybuilders/easybuild-easyblocks/pull/3706
    * https://github.com/easybuilders/easybuild-easyblocks/pull/3781

## Current Progress: Building the Core Stack

* for version 6.4.0 the following can build with EasyBuild in the EESSI build container
    * ROCm-LLVM
    * rocminfo
    * rocm-cmake
    * HIP
    * amdsmi
    * roctracer
* currently testing/building on a VM without AMD GPU
    * some sanity checks are skipped

details:

* works in an EESSI build container/environment
* EasyBuild recipes created and tested
* some patches / workarounds / hooks used

limitations:

* no runtime validation yet
* skipped sanity checks (no GPU)

## Next Steps: Validating the Integration

high priority:

* add support for the driver/GPU
* finish adding support for the core components and validation suite / examples in EasyBuild
* run validation suite / examples to check that everything actually works
* test building with sanity checks enabled

lower priority:

* add support for more libraries and frameworks
* add support for popular scientific applications
* update ROCm overview with experience from building / running ROCm
* see about contributing overview back to AMD docs
