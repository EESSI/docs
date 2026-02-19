# Short-term roadmap for EESSI

*(approved by EESSI steering committee: 19-02-2026; valid until: 18-02-2027; to be revised by: 18-12-2026; questions/suggestions: support@eessi.io)*

The purpose of this roadmap is to focus the collective effort of the EESSI
community on the specific goals we aim to achieve together in the coming year.

## Core Infrastructure, Operations & Policy
### Lifecycle & Governance Policies
- Version Lifecycle: Define clear policies for "Active" vs. "Archived" versions (e.g., how long to add software to EESSI/2023.06)
- Development Policy: Establish lifetime policies for experimental installations on `dev.eessi.io`
- Cadence: Formalise the yearly release cycle (targeting pre-summer releases)
### Build System Modernisation
- Diversify Build Sites: Enhance reliability by spreading build operations
- Bot Modernisation: Upgrade infrastructure; implement tarball analysis to simplify ingestion and track differences
- Maintainer Support: Leverage the EESSI bot to assist EasyBuild maintainers
### Quality Assurance & Compliance
- Automated License Checks: Towards automatic mandatory license checks for the next EESSI version (2026.x)
- Monitoring: Establish regular use of regression tests & status dashboard
- Performance: Assess performance of end-user applications
### Compatibility Layer
- Release the next EESSI version (2026.x): next version bundled with upcoming toolchains (update of Gentoo Prefix)
## Software Stack & Hardware Targets
### Hardware Enablement
- NVIDIA: Support for Blackwell GPUs
- AMD: Support for Zen5 and ROCm stack (AMD GPUs)
- ARM: Support for AWS Graviton 4+5
### Software Portfolio
- AI/ML Focus: Extend GPU software (PyTorch, TensorFlow, AlphaFold)
- Volume Goal: Reach 1,000 unique software packages
- Toolchains: Integration of `lfoss/2025b` (in EESSI 2025.06) and `foss/2026*` (in EESSI 2026.x) toolchains
## User Experience & Integration
### Direct User Interaction
- CLI: Prototype an EESSI Command Line Interface (CLI) to provide an interface beyondmodules
- Discovery: Create a dynamic software overview
### Feedback & Transparency
- Software Wishlist: Implement mechanism (e.g., anonymous forms) for users to request software and trigger documentation PRs
- Work-in-Progress (WIP) View: Create dashboard/overview of WIP PRs, so users can see upcoming software
### Workflow Integration
- Tools: Prototype Nextflow & Spack integration
- CI/CD: Promote EESSI usage in CI/CD pipelines
- Scientific Compliance: Enhance FAIRness of software installations
## Community, Outreach & Sustainability
### Governance & Future
- Sustainability: Advance steps towards joining Linux Foundation (LF) & HPSF
### Community Engagement
- Events: Continue "Happy Hours", hackathons (focus on documentation/cleanup), and training
- Feedback: Conduct an annual User Survey
- Adoption: Track and map systems/sites that have adopted EESSI
### Dissemination & Marketing
- Content: Maintain a standard slide deck, elevator pitch, monthly blog/social updates
- Conference: FOSDEM, EuroHPC Summit, ISC, EUM, and EuroHPC User Days, etc
