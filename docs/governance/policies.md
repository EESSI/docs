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

# Policy Scope and Hierarchy

- **Project Policies** are defined and maintained by the Steering Committee.
- **Team Policies** may be defined by individual Teams to formalize consensus-based decisions within their scope.
- In case of conflict, **Project Policies take precedence** over Team Policies.

---

# EESSI Project Policies

This document outlines project-wide policies that guide the development, deployment, and maintenance of the EESSI software stack. These policies are set by the Steering Committee and apply across all Teams and repositories.

---

## 2. Build and Deployment Policies

### 2.1 Architecture Support

- EESSI aims to build and support software for a wide range of relevant hardware architectures. Currently supported architectures are listed [here](../software-layer/cpu_targets.md).
- If a package is unavailable for a specific architecture, a clear runtime message (e.g., via modulefile error) should be provided to the user.
- When optimization for a specific microarchitecture is not possible, a compatible fallback (e.g., zen3 for zen4) should be provided if available. A clear runtime warning will be printed.

### 2.2 Rebuild Policy

Reproducibility is important in scientific computing. Thus, we exercise restraint in rebuilding software. A list of scenarios in which software may be rebuilt is:

- The software contained security vulnerabilities
- There were updates to the (list of) dependencies, e.g. some optional dependency was missing which restricted functionality of the original installation
- There were (unintended) differences between the software installations for different (micro)architectures
- The original installation (or a substantial part thereof) was found to be broken. Not that this does _not_ apply to small bugs.
- Mistakes in the original installation prevent it from being used as a dependency for other software

Additionally, software may be rebuilt for other reasons if there is sufficient consensus within the EESSI Community that this is beneficial.

In all cases, the value of rebuilding the software will be carefully weighed against the value of reproducibility.

### 2.3 Deprecation Policy

#### 2.3.1 Deprecation of EESSI software stack versions
At any given time, we aim to have at least two EESSI software stack versions in production. When a new version of the EESSI software stack is introduced _and_ sufficiently populated, the oldest stack will be deprecated. A clear runtime warning will be printed when an end-user initializes a deprecated EESSI software stack.

#### 2.3.2 Deprecation of individual software installations

Installations of individual software packages in a (non-deprecated) EESSI software stack may be deprecated if they are no longer maintainable or functional. A clear runtime warning will be printed when an end-user tries to load a module for a deprecated software installation.

### 2.4 Removal Policy

#### 2.4.1 Removal of EESSI software stack versions

Since CernVM-FS Stratum 1 servers have to fully mirror the repository, old EESSI software stack versions will have to be removed to keep the storage footprint within reasonable limits. This will only be done after:
- The EESSI software stack version has been deprecated for at least 1 year
- The EESSI software stack version has been archived in _some_ form in which it can still be used by end-users (e.g. as a tarball, an exported CVMFS repository using CernVM-FS Shrinkwrap, or some other form).

A clear runtime error will be printed when an end-user tries to initialize a removed EESSI software stack.

#### 2.4.2 Removal of individual software installations

An individual software installation in EESSI may be removed if:
- It violates licensing terms
- It poses a security risk
- It is no longer maintainable or functional.

A clear runtime error will be printed when an end-user tries to load a module for a removed software installation.

### 2.5 Optimization Policy

Optimization for performance is strongly encouraged. For compiled software, this means we aim to have the compiler optimize for the supported hardware targets.

---

## 3. Contribution Policies

### 3.1 Software Acceptance

- Contributions of new software are accepted as long as they meet the [Contribution Policy](https://www.eessi.io/docs/adding_software/contribution_policy/).
- The default stance is: **"Yes, unless we can't."**

### 3.2 Non-Software Contributions

- Contributions to build logic, test suites, or infrastructure must be testable and documented.
- Specific requirements may be defined by the relevant Team.

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

# EESSI Team Policies

There are currently no Team Policies yet.

_Last updated: [Insert Date]_
