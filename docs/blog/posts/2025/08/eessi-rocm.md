---
authors: [toine, boegel, ocaisa]
date: 2025-08-04
slug: rocm
---

# ROCm Integration Progress: Core Components Ready for EasyBuild Release

Following our previous posts on [mapping the ROCm ecosystem](https://www.eessi.io/docs/blog/2025/05/26/rocm) and [building ROCm support in EESSI](https://www.eessi.io/docs/blog/2025/06/30/rocm), we're excited to share a significant milestone in our ROCm integration journey.
Our core ROCm components are now hardware-validated and nearly ready for inclusion in the next EasyBuild release, marking substantial progress toward making AMD GPU computing more accessible through EESSI.

<!-- more -->

## Major Milestone: Core Components Production-Ready

We've successfully reached a crucial milestone in our ROCm integration roadmap.
Our `ROCm-LLVM` toolchain, `ROCmInfo`, and `AMD SMI` components have been tested on actual AMD GPU hardware and are performing as expected.
More importantly, these components are now ready to be submitted to the official EasyBuild repository, which means the broader scientific computing community will soon have access to reliable, tested ROCm builds.

Having a working ROCm-LLVM toolchain provides the compiler foundation that (nearly) every other ROCm component depends on.
Combined with `ROCmInfo` for GPU discovery and `AMD SMI` for system monitoring, we now have the essential building blocks for AMD GPU computing in place.

## Hardware Validation Success

Our recent hardware testing confirmed that our builds don't just compile correctly, they function reliably with real AMD GPU hardware.
One particularly encouraging discovery during our hardware validation was that **the AMDGPU driver required no special handling in our EasyBuild configurations**.
This contrasts favorably with NVIDIA CUDA driver integration, where additional complexity is often required.
The AMDGPU driver integration worked seamlessly out of the box, which should significantly simplify deployment for EESSI users.

## EasyBuild Integration: Ready for Community Access

Our work is now formalized in [EasyBuild pull request #23542](https://github.com/easybuilders/easybuild-easyconfigs/pull/23542), which adds comprehensive ROCm support to the EasyBuild ecosystem.
This PR includes:

* **ROCm-LLVM toolchain**: The compiler foundation for AMD GPU computing
* **Essential dependencies**: Previously missing components now properly packaged
* **Core utilities**: ROCmInfo, AMDSMI, and HIP runtime with all necessary dependencies
* **Validation suite groundwork**: Initial components for the ROCm Validation Suite

The PR builds upon significant framework enhancements, including support for AMD GPU compute capabilities (similar to CUDA's compute capabilities), a new LLVM-based toolchain implementation, and specialized EasyBlocks for ROCm components.
Special thanks to [Jan André Reuter](https://github.com/Thyre) and [Bob Dröge](https://github.com/bedroge) for their parts in this.

## Current Challenge: ROCm Validation Suite

While celebrating our core component success, we must acknowledge the challenge that has prevented us from completing our original goal of full ROCm Validation Suite support.
We encountered compilation issues with `hipBLASLt` (documented in [ROCm issue #316](https://github.com/ROCm/rocm-libraries/issues/316)), which is a dependency for the complete validation suite.

**[UPDATE MARKER: Check hipBLASLt workaround status before publication]**

We're currently exploring potential workarounds for the `hipBLASLt` compilation issue.
If successful, we may be able to include full validation suite support in this EasyBuild release.
Otherwise, this will remain a priority for the next development cycle.

## Outstanding Work: Driver Compatibility Checking

One important piece of functionality we still need to implement is automatic compatibility checking between the host AMDGPU driver version and our ROCm builds.
While our current builds work correctly with compatible drivers, we want to provide clear guidance to users when incompatibilities are detected, similar to what's available in the CUDA ecosystem.

## What's Next: Expanding the Stack

With our core components ready for release, our focus shifts to expanding ROCm support in several key areas:

**Immediate priorities:**

* Resolving the `hipBLASLt` compilation issue to enable full validation suite support
* Implementing driver compatibility detection and user guidance

**Medium-term goals:**

* Expanding library support beyond the core stack
* Integrating popular scientific applications that leverage ROCm
* Update our ROCm overview to incorporate what we've learned

**Long-term goals:**

* Contributing our ROCm ecosystem overview to AMD's official documentation
* Providing feedback to AMD's TheRock project based on our integration experience

## Community Impact and Looking Forward

As we approach the EasyBuild release containing our ROCm components, we're excited about the possibilities this opens for the scientific computing community.
AMD GPUs offer compelling alternatives to traditional computing architectures, and our work is helping remove the barriers that have historically made them challenging to deploy and manage.

We'll continue sharing our progress as we work toward complete ROCm integration in EESSI.
The goal remains unchanged: making high-performance AMD GPU computing as accessible and reliable as possible for researchers and developers worldwide.
