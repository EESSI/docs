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
The EESSI project aims to build a common software stack that is:
- Cross-platform (laptop, Cloud VM, HPC Cluster)
- Ready-to-use (served over the internet, just mount-and-go)
- optimized for a wide range of hardware architectures (CPU, GPU, interconnects)

## 2. Scope
<!-- Define what is within the scope of the project and what is explicitly out of scope. -->
EESSI will focus on creating a repository of software installations. This requires:
- code to build and deploy new software into the repository
- code to make EESSI work on end-user systems
- infrastructure to build new software for software.eessi.io
- infrastructure to host the repository for software.eessi.io

All of these (both code and infrastructure itself) are considered 'in scope' for the project. <!-- sould mention explicitely here that there are other repos, and that the CODE for those repos is part of EESSI, but the infrastructure itself is NOT, or maybe make subsection on repo's and state what is  in and out of scope -->

<!-- I know we discussed potentially separating infrastructure. For now, I've included it. Infrastructure maintainers is also a role in the current governance.  -->

## 3. Membership
<!-- Who can join or participate? Are there any requirements (e.g., code contributions, voting eligibility)? -->
There is currently no membership. Any individual or instution may participate by using the EESSI software stack, contributing to the EESSI software stack, making the EESSI software stack available on systems managed by them, etc.

## 4. Review and Amendment
Changes to the charter require approval by the Steering Committee
