---
authors: [toine, timvc]
date: 2025-05-26
slug: rocm
---

# Mapping the AMD ROCm Ecosystem

Within the EESSI community and Inuits, we're excited to share our latest contribution to the scientific computing community: a high-level overview of AMD's ROCm ecosystem.
This document is the result of our recent efforts to prepare for adding ROCm support to EESSI, and we believe it will serve as a valuable resource for anyone working with AMD GPUs in scientific computing environments.

The full overview document can be found at [**Overview of ROCm Ecosystem**](https://eessi.io/docs/rocm).

<!-- more -->

## Why we created this overview

When preparing to add ROCm support to EESSI, we needed a high-level overview of the ROCm ecosystem, but couldn't find one online.
While AMD's official [documentation](https://rocm.docs.amd.com/en/latest/) covers individual components thoroughly, we required a holistic view to understand how everything interconnects - from hardware architectures to high-level libraries and the dependencies between them.
This understanding was crucial for making informed decisions about which components to prioritize and how to handle compatibility across diverse scientific computing environments.

Rather than keep this knowledge internal, we decided to create the overview we wished had existed when we started.
We hope this document will save others the research time we invested in piecing together information from scattered sources.
Depending on community feedback and interest from AMD, we're also excited about the possibility of contributing portions or the entirety of this overview to the official ROCm documentation.

Once we are ready we will contribute it back to the ROCm documentation as described [here](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

## Scope

The document we've created offers a structured exploration of the ROCm ecosystem, including:

* AMD GPU microarchitectures (CDNA, RDNA, and earlier architectures)
* Core components of the ROCm stack
* Available programming models (HIP, OpenMP, OpenCL)
* The compiler ecosystem (ROCm-LLVM, AOCC, AOMP, hipcc)
* Developer tools for debugging and performance optimization
* Libraries and frameworks for various computational domains
* Compatibility policies
* AMD GPUs available in Azure cloud environments

We've also included dependency diagrams to help visualize the relationships between different components, making it easier to understand how everything fits together.

## A living document for and by the community

This overview is not meant to be a static document, we view it as a living resource that will evolve along with the ROCm ecosystem itself.
As AMD continues to develop and enhance ROCm, we hope to update this document with the latest information, dependency relationships, and best practices.

That's where you come in.
While we've worked diligently to ensure accuracy and comprehensiveness, we recognize that the collective knowledge of the community far exceeds our own.
We invite you to review the document, provide feedback, suggest additions, and point out any inaccuracies or omissions.

## How to contribute

We welcome contributions from the community to help improve and expand this overview.
You can help by:

* Reviewing the document for accuracy and identifying any outdated or incorrect information
* Suggesting missing components, libraries, or tools that should be included
* Providing insights on important details we may have overlooked
* Sharing your experiences with specific ROCm components or workflows
* Pointing out unclear explanations or areas that need better documentation

Please submit your feedback, suggestions, and corrections via the [EESSI support portal](https://eessi.io/docs/support).
We'll review all contributions and update the document accordingly to ensure it remains a valuable resource for the entire community.

## Looking forward

As we prepare to integrate ROCm support into EESSI, this overview serves as our roadmap.
We hope it will also guide others in the scientific computing community who are exploring AMD GPUs for their computational needs.

We look forward to your feedback and to continuing this collaborative effort to better understand and utilize the ROCm ecosystem for scientific computing.
