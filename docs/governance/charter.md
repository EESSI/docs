<!-- 
A project charter discusses _what it is and why it exists_, a governance discusses _how it operates_.

Examples

https://docs.clearlydefined.io/docs/community/charter
https://openssf.org/about/charter/
https://github.com/cncf/foundation/blob/main/charter.md
https://github.com/mochajs/mocha/blob/main/PROJECT_CHARTER.md
https://github.com/nodejs/TSC/blob/main/TSC-Charter.md
Combined charter - governance https://github.com/camaraproject/Governance/blob/main/ProjectCharter.md
blog about charters https://opensource.org/blog/what-is-open-governance-drafting-a-charter-for-an-open-source-project
-->

# Project Charter

## 1. Mission
<!-- Describe the project's purpose and the problem it addresses. Include a short mission statement. -->
The [European Environment for Scientific Software Installations](https://www.eessi.io/docs/) (EESSI) project aims to build a common software stack that is

- Cross-platform (laptop, Cloud VM, HPC Cluster)
- Ready-to-use (served over the internet, just mount-and-go)
- Optimized for a wide range of hardware architectures (CPU, GPU, interconnects)
- Easily extendable with additional local installations
- Customizable (e.g. site-specific Lmod hooks, injecting a local MPI library, etc.)

and can be used on any Linux (virtual) machine.

## 2. Scope
<!-- Define what is within the scope of the project and what is explicitly out of scope. -->
EESSI focusses on creating a [CernVM-FS repository](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html) of software installations (`software.eessi.io`).

This requires:

- Source code to automate the process of building and deploying additional software installations in `software.eessi.io`
- Source code to provide a user-friendy interface on end-user systems
- Infrastructure to build new software for `software.eessi.io`
- Infrastructure to host the CernVM-FS repository for `software.eessi.io`

All of these (both code and infrastructure itself) are considered 'in scope' for the project.

There are additional CernVM-FS repositories under the eessi.io namespace, such as dev.eessi.io and riscv.eessi.io. All code and infrastructure related to those repositories (and any other CernVM-FS repositories under the eessi.io namespace) are also considered part of the EESSI project.

## 3. Membership
<!-- Who can join or participate? Are there any requirements (e.g., code contributions, voting eligibility)? -->
There is currently no membership. Any individual or institution may participate by using EESSI, contributing to EESSI, making EESSI available on systems managed by them, etc.

## 4. Review and Amendment
Changes to the charter require approval by the Steering Committee. See the [relevant section of the Governance](governance.md#voting-by-the-steering-committee).
