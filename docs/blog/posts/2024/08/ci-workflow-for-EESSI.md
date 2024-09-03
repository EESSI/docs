---
authors: [Neves-P]
date: 2024-08-19
slug: ci-workflow-for-EESSI 
---

# CI workflow for EESSI

EESSI is available via CI workflows both through GitHub Action and as GitLab CI/CD component. Enabling this is as simple as adding a few lines a workflow file, after which you will very quickly have access to access to the entire EESSI software stack optimized for the relevant CPU architecture(s). This can be very useful, for example, if you are developing an application that you would like to test over a number of systems. With the EESSI CI workflows you don't have to worry about figuring out how to set up and optimize build and runtime dependencies as these will be streamed seamlessly to your runner's environment.
