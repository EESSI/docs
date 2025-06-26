---
authors: [toine, timvc, boegel, ocaisa, darkless]
date: 2025-06-24
slug: rocm
---

# Building ROCm Support in EESSI

Following our [overview of the ROCm ecosystem](https://www.eessi.io/docs/rocm), we're excited to share our progress on the next phase of our ROCm initiative: actually building and integrating ROCm support into EESSI.
This work represents a significant step forward in making AMD GPU computing more accessible to the scientific computing community through our software stack.

<!-- more -->

Our previous blog post focused on understanding the ROCm landscape - mapping out the components, dependencies, and relationships within AMD's GPU computing ecosystem.
Now we're putting that knowledge into practice by systematically building ROCm support from the ground up.

## Our Goals: The ROCm Integration Roadmap

Our main objective is straightforward: achieve full ROCm support in EESSI that enables researchers and developers to leverage AMD GPUs seamlessly across diverse computing environments.
This means users should be able to access a complete, tested, and optimized ROCm stack without the complexity of building and managing these components themselves.

We've structured our approach around three key milestones:

**Building Core ROCm Components**: The foundation of our work involves successfully building all essential ROCm components within the EESSI environment using EasyBuild.
This includes the compiler stack (ROCm-LLVM), runtime libraries (HIP), development tools, and core utilities that form the backbone of AMD GPU computing.

**Driver Support Integration**: Moving beyond building components, we need to ensure proper integration with AMD GPU drivers and hardware detection.
This involves validating that our built components can successfully communicate with AMD GPUs and leverage their computational capabilities.

**Validation Suite and Examples**: The final milestone focuses on comprehensive testing through validation suites and real-world examples.
This ensures that our ROCm integration doesn't just build successfully, but actually works reliably for the diverse scientific computing workloads that EESSI users depend on.

## Foundation Work: What Was Done Before

Before diving into the technical implementation, we invested significant effort in understanding the ROCm ecosystem.
As detailed in our [previous blog post](https://www.eessi.io/docs/blog/2025/05/26/rocm/), we created an overview that maps out core components, programming models, libraries and frameworks, and the complex web of dependencies that connect them all.

Rather than starting from scratch, we leveraged existing community efforts as our foundation.
Specifically, we built upon excellent preliminary work from:

* [Bob Dröge](https://github.com/bedroge)'s ROCm EasyBuild configurations available [here](https://github.com/bedroge/eb-rocm/tree/main)
* [Jan André Reuter](https://github.com/Thyre)'s custom EasyBuild support for ROCm available [here](https://github.com/Thyre/easybuild-custom/tree/support-passing-amdgcn/easybuild/)

A crucial contribution came from [Davide Grassano](https://github.com/Crivella) who successfully got ROCm-LLVM to build with EasyBuild.
This involved significant technical work, including contributions back to the EasyBuild project through pull requests [#3706](https://github.com/easybuilders/easybuild-easyblocks/pull/3706) and [#3781](https://github.com/easybuilders/easybuild-easyblocks/pull/3781).
Getting ROCm-LLVM working was essential because it serves as the compiler foundation for the entire ROCm stack.

## Current Progress: Building and Testing the Core Stack

We've made substantial progress in building ROCm components for version 6.4.0 within the EESSI build environment.
The following core components now build successfully with EasyBuild in our EESSI build container: ROCm-LLVM, rocminfo, rocm-cmake, HIP, amdsmi, ROCTracer.

Initially, we conducted our building and testing on a virtual machine environment without physical AMD GPU hardware.
This approach allowed us to validate the build process and catch configuration issues, though it meant some sanity checks that require actual GPU hardware were necessarily skipped during the build process.

From a technical perspective, our work has focused on ensuring all components build reliably within the EESSI build container environment, guaranteeing reproducibility and consistency across different systems.
We've developed and tested EasyBuild recipes for each component, including some patches, build hooks, and workarounds to fix some issues.
Our work can be found [here](https://github.com/Timvnc/easyconfig-rocm/tree/master).

Recently we validated our ROCm builds with actual hardware.
The results were highly encouraging: `hip_device_query` executed successfully, properly detecting and reporting GPU information, and `amd-smi` worked correctly, providing detailed system monitoring capabilities.
We were also able to run a complete build with all sanity checks enabled and passing.

The successful hardware validation represents a significant milestone in our ROCm integration effort, demonstrating that our builds don't just compile correctly but actually function as expected with real AMD GPU hardware.

## Next Steps: Expanding the Integration

Looking ahead, we've identified clear priorities for completing our ROCm integration work.

Our high-priority next steps focus on validation and completeness.
We're working to finish adding support for remaining core components and extend our testing to cover AMD's [validation suite](https://github.com/ROCm/ROCmValidationSuite) and [examples](https://github.com/ROCm/rocm-examples) that demonstrate real-world functionality.
We also need to develop a mechanism to detect the host driver version and validate it against our ROCm build requirements, providing clear guidance to users when incompatibilities are detected.

Our lower-priority items, while still important, focus on expanding capabilities and improving documentation.
We plan to add support for additional libraries and frameworks beyond the core stack, integrate popular scientific applications that leverage ROCm, and update our ROCm overview document with practical insights gained from our building and testing experience.
We're also exploring the possibility of contributing our overview back to AMD's official documentation, which could benefit the broader community.
And finally, we will also provide feedback to AMD on our experience building ROCm, which likely will be useful for their new project [TheRock](https://github.com/ROCm/TheRock).

## Looking Forward

As we move forward, we'll continue sharing our progress, challenges, and solutions with the community.
The goal isn't just to build ROCm support for EESSI, but to contribute to the broader understanding and adoption of AMD GPU computing in scientific workflows.
