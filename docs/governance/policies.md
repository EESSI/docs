<!--
# EESSI Policies
-->

<!--
No policies have been defined (yet) ==> see draft based on the thoughts below
-->

<!--
Should we have separate policies that Teams themselves can set? I.e. distinguish Project and Team policies, where project policies are set by the Steering Committee and Team policies by the respective Teams? Team policies could be ways to formalize concensus-based decisions. Clearly, if Team policies and Project policies contract, Project policy should come first.

EESSI Policies could be things like

- Should build for all architectures
  - If something isn't available for an architecture, the end-user should be informed at runtime, e.g. through an error printed by a modulefile
  - If something cannot be optimized for a micro-architecture, do we provide a less-optimized form (e.g. doesn't build for zen4 but does for zen3, so we provide zen3)?
- Something on the fact that we try to provide a full software Bill-of-Materials for all software we deploy?
- Acceptance of new software for the EESSI repository is "Yes, unless we can't" or "Yes, as long as it meets the Contribution Policy", i.e. we'll accept _anything_ that's reasonable?
- Rebuild policy: when do we rebuild?
- Removal policy: when do we remove?
- Something on optimization?
- Something on contributions _other_ than software for the EESSI repository (i.e. build logic, test suite, build bot). Should a requirement be that we can test it? Or is this too specific and should it be Team Policy?
- Include our current Contribution Policy? Or should that be separate? (it's maybe more a Team Policy?) https://www.eessi.io/docs/adding_software/contribution_policy/
- For security-critical roles (we should define which roles are security critical!), we only adopt new people that we (i.e. at least one person in that Team) knows _personally_.
- Whenever technical choices need to be made between (optimizing for) HPC, Cloud, or a PC, we prioritize HPC usage (?). I.e. if we can choose between two implementations, and one would break usage on HPC, and another would break Cloud usage, and there is no implementation that works on both, we prioritize HPC? Or do we NOT make this explicit? Or: do we only make it explicit for _optimization_ related stuff (but not for 'it works' vs 'it does not work')?
-->

# EESSI Project Policies

This document outlines project-wide policies that guide the development, deployment, and maintenance of the EESSI software stack. These policies are set by the Steering Committee and apply across all Teams and repositories. In case of conflict, Project Policies override Team Policies.

---

## 1. Policy Scope and Hierarchy

- **Project Policies** are defined and maintained by the Steering Committee.
- **Team Policies** may be defined by individual Teams to formalize consensus-based decisions within their scope.
- In case of conflict, **Project Policies take precedence** over Team Policies.

---

## 2. Build and Deployment Policies

### 2.1 Architecture Support

- EESSI aims to build and support software for all relevant hardware architectures.
- If a package is unavailable for a specific architecture, the system should provide a clear runtime message (e.g., via modulefile error).
- When optimization for a specific microarchitecture is not possible, a compatible fallback (e.g., zen3 for zen4) should be provided if available.

### 2.2 Rebuild Policy

- Software may be rebuilt in response to:
  - Security vulnerabilities
  - Dependency updates
  - Infrastructure changes
  - Community requests (subject to review)

### 2.3 Removal Policy

- Software may be removed if:
  - It violates licensing terms
  - It poses a security risk
  - It is deprecated or superseded
  - It is no longer maintainable or functional

### 2.4 Optimization Policy

- Optimization for performance is encouraged, especially for HPC environments.
- Where trade-offs are necessary, HPC compatibility and performance take precedence over Cloud or PC optimization.

---

## 3. Contribution Policies

### 3.1 Software Acceptance

- Contributions of new software are accepted as long as they meet the [Contribution Policy](https://www.eessi.io/docs/adding_software/contribution_policy/).
- The default stance is: **"Yes, unless we can't."**

### 3.2 Non-Software Contributions

- Contributions to build logic, test suites, or infrastructure must be testable and documented.
- Specific requirements may be defined by the relevant Team.

### 3.3 Security-Critical Roles

- Roles with elevated access (e.g., infrastructure maintainers, deployers) are considered security-critical.
- New members in these roles must be personally known and trusted by at least one existing Team member.

---

## 4. Transparency and Traceability

### 4.1 Software Bill of Materials (SBOM)

- EESSI is committed to providing a complete SBOM for all deployed software.
- The SBOM should include versioning, licensing, and dependency information.
- Preferred formats include SPDX or CycloneDX.

---

## 5. Platform Prioritization

- In cases where technical choices must be made between HPC, Cloud, or PC environments:
  - **HPC compatibility and performance are prioritized**, especially for optimization-related decisions.
  - This does not imply exclusion of other platforms, but reflects the project's primary use case.

---

_Last updated: [Insert Date]_
