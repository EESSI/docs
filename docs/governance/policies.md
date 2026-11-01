_Last updated: 08 August 2025_

# Policy Scope and Hierarchy

- **Project Policies** are defined and maintained by the Steering Committee.
- **Team Policies** may be defined by individual Teams to formalize consensus-based decisions within their scope.
- In case of conflict, **Project Policies take precedence** over Team Policies.

---

## EESSI Project Policies { #project-policies }

This document outlines project-wide policies that guide the development, deployment, and maintenance of the EESSI software stack.

These policies are set by the Steering Committee and apply across all Teams and repositories.

---

### 1. Security Policy { #security-policy }

The EESSI maintainers strive to swiftly mitigate known security issues that are relevant to EESSI.

No guarantees can be made on the time required to address security issues, as mitigations are implemented in a best effort manner.

#### 1.1 Prioritization { #security-issues-prioritization }

Known security issues will be prioritized based on risk, potential impact, and how commonly the software is assumed to be used.

The primary focus with respect to addressing security issues relevant for the [main production repository `software.eessi.io`](../repositories/software.eessi.io.md).

#### 1.2 Reporting security issues { #security-reports }

Reports of security issues relevant to EESSI can be sent via email to `security (at) eessi.io` .

We strive to respond to reported security issues within 2-3 working days. If your security issue is accepted, we will do what we can to fix it as soon as possible.

If fixing the issue would take us longer than a couple of days, we will discuss the expected timeline with you.

If you feel you need to escalate the reported security issue, please contact one or more members of the [EESSI Steering Committee](steering_committee.md).

---

### 2. Build and Deployment Policies { #build-deployment-policy }

#### 2.1 Architecture Support { #supported-architecures }

- EESSI aims to build and support software for a wide range of relevant hardware architectures. Currently supported CPU microarchitectures are listed [here](../software_layer/cpu_targets.md).
- If a package is unavailable for a specific CPU microarchitecture, a clear runtime message (e.g., via modulefile error) should be provided to the user.
- When optimization for a specific CPU microarchitecture is not possible, a compatible fallback (e.g., zen3 for zen4) should be provided if available. A clear runtime warning will be printed.

#### 2.2 Rebuild Policy { #rebuild }

Reproducibility is important in scientific computing. Thus, we exercise restraint in rebuilding software. A list of scenarios in which software may be rebuilt is:

- The software installation contained security vulnerabilities;
- There were updates to the (list of) dependencies, e.g. some optional dependency was missing which restricted functionality of the original installation;
- There were (unintended) differences between the software installations for different (micro)architectures;
- The original installation (or a substantial part thereof) was found to be broken. Note that this does _not_ apply to small bugs;
- Mistakes in the original installation prevent it from being used as a dependency for other software.

Additionally, software may be rebuilt for other reasons if there is sufficient consensus within the EESSI Community that this is beneficial.

In all cases, the value of rebuilding the software will be carefully weighed against the value of reproducibility.

#### 2.3 Deprecation Policy { #deprecation }

##### 2.3.1 Deprecation of EESSI software stack versions { #deprecation-EESSI-versions }

At any given time, we aim to have at least two EESSI software stack versions in production. When a new version of the EESSI software stack is introduced _and_ sufficiently populated, the oldest stack will be deprecated. A clear runtime warning will be printed when an end-user initializes a deprecated EESSI software stack.

##### 2.3.2 Deprecation of individual software installations { #deprecated-software-installations }

Installations of individual software packages in a (non-deprecated) EESSI software stack may be deprecated if they are no longer maintainable or functional. A clear runtime warning will be printed when an end-user tries to load a module for a deprecated software installation.

#### 2.4 Removal Policy { #removal }

##### 2.4.1 Removal of EESSI software stack versions { #removal-EESSI-versions }

Since CernVM-FS Stratum 1 servers have to fully mirror the repository, old EESSI software stack versions will have to be removed to keep the storage footprint within reasonable limits.

This will only be done after:

- The EESSI software stack version has been deprecated for at least 1 year
- The EESSI software stack version has been archived in _some_ form in which it can still be used by end-users (e.g. as a tarball, an exported CVMFS repository using CernVM-FS Shrinkwrap, or some other form).

A clear runtime error will be printed when an end-user tries to initialize a removed EESSI software stack.

##### 2.4.2 Removal of individual software installations { #removed-software-installations }

An individual software installation in EESSI may be removed if:

- It violates licensing terms
- It poses a security risk
- It is no longer maintainable or functional.

A clear runtime error will be printed when an end-user tries to load a module for a removed software installation.

#### 2.5 Optimization Policy { #optimization }

Optimization for performance is strongly encouraged. For compiled software, this means we aim to have the compiler optimize for the supported hardware targets.

---

### 3. Contribution Policies { #contribution-policy }

#### 3.1 Software Acceptance { #software-acceptance }

- Contributions of new software are accepted as long as they meet the [Contribution Policy](https://www.eessi.io/docs/adding_software/contribution_policy/).
- The default stance is: **"Yes, unless we can't."**

#### 3.2 Non-Software Contributions { #non-software-contributions }

- Contributions to build logic, test suites, or infrastructure should be testable and documented.
- Specific requirements may be defined by the relevant Team.

---

### 4. Transparency and Traceability { #transparency-traceability }

EESSI aims to be transparent regarding how software was built. A combination of the git history, EasyBuild logs, as well as the `easybuild` subdirectory within every installation (which provides the easyconfig and patch files, easyblock, and any hooks used at installation time) provide a detailed description of how software was configured and built.

---

### 5. Platform Prioritization { #platforms-prioritization }

**HPC compatibility and performance are prioritized**,
in cases where technical choices must be made between HPC, Cloud, or laptops & workstations,
especially for optimization-related decisions.

This does not imply exclusion of other platforms, but reflects the project's primary use case.

---

## EESSI Team Policies { #team-policies }

There are no Team Policies yet.

## Changelog { #changelog }

- 2 November 2026: Security policy added
- 4 August 2025: First version publishe§d
