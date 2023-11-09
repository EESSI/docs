# Contribution policy

*(version v0.1.0 - updated 9 Nov 2023)*

!!! note

    This policy is subject to change, please check back regularly.

## Purpose

The purpose of this contribution policy is to provide guidelines for [adding software](opening_pr.md) to EESSI.

It informs about what requirements must be met in order for software to be eligible for inclusion
in the EESSI software layer.

## Requirements

The following requirements must be taken into account when adding software to EESSI.

Note that additional restrictions may apply in specific cases that are currently not covered explicitly by this policy.

---

### i) Open source software { #open_source_software }

Only **freely redistributable software** can be added to the EESSI repository,
and we strongly prefer including only **open source software** in EESSI.

Make sure that you are aware of the relevant software licenses,
and that redistribution of the software you want to add to EESSI is allowed.

For more information about a specific software license,
see the [SPDX license list](https://spdx.org/licenses/).

!!! note

    We intend to automatically verify that this requirement is met,
    by requiring that the [SPDX license identifier](https://spdx.dev/ids/) is provided
    for all software included in EESSI.


---

### ii) Built by the bot { #built_by_bot }

All software included in the EESSI repository *must* be **built autonomously** by [our bot :robot:](../bot.md).

For more information, see our [semi-automatic software installation procedure](building_software.md).


---

### iii) Built and installed with EasyBuild { #easybuild }

We currently require that all software installations in EESSI are
**built and installed using EasyBuild**.

We strongly prefer that the [*latest release of EasyBuild*](https://pypi.org/project/easybuild/)
that is available at the time is used to add software to EESSI.

The use of [`--from-pr`](https://docs.easybuild.io/integration-with-github/#github_from_pr) and
[`--include-easyblocks-from-pr`](https://docs.easybuild.io/integration-with-github/#github_include_easyblocks_from_pr)
to pull in changes to EasyBuild that are required to make the installation work correctly
in EESSI is allowed, but only if that is strictly required
(that is, if those changes are not included yet in the latest EasyBuild release).


---

### iv) Supported compiler toolchain { #supported_toolchain }

A **[compiler toolchain](https://docs.easybuild.io/terminology/#toolchains) that is still supported**
by the latest EasyBuild release *must* be used for building the software.

For more information on supported toolchains,
see the [EasyBuild toolchain support policy](https://docs.easybuild.io/policies/toolchains).


---

### v) Recent toolchain versions { #recent_toolchains }

We strongly prefer adding software to EESSI that was built with a **recent compiler toolchain**.

When adding software to a particular version of EESSI,
you should *use a toolchain version that is already installed*.

If you would like to see an additional toolchain version being added to a particular version of EESSI,
please [open a support request](../support.md) for this, and motivate your request.

---

### vi) Recent software versions { #recent_software_versions }

We strongly prefer adding sufficiently **recent software versions** to EESSI.

If you would like to add older software versions, please clearly motivate the need for this
in your contribution.


---

### vii) CPU targets { #cpu_targets }

Software that is added to EESSI *should* **work on all [supported CPU targets](../software_layer/cpu_targets.md)**.

Exceptions to this requirement are allowed if technical problems that can not be resolved with reasonable effort
prevent the installation of the software for specific CPU targets.


---

### viii) Testing { #testing }

We should be able to test the software installations via the [EESSI test suite](../test-suite/index.md),
in particular for software applications and user-facing tools.

Ideally one or more tests are available that verify that the software is functionally correct,
and that it (still) performs well.

Tests that are run during the software installation procedure as performed by EasyBuild *must* pass.
Exceptions can made if only a small subset of tests fail for specific CPU targets,
as long as these exceptions are tracked and an effort is made to assess the impact of those failing tests.

It should be possible to run a minimal *smoke test* for the software included in EESSI,
for example using EasyBuild's `--sanity-check-only` feature.

!!! note

    The [EESSI test suite](https://github.com/EESSI/test-suite) is still in active development,
    and currently only has a minimal set of tests available.

    When the test suite is more mature, this requirement will be enforced more strictly.

---

## Changelog

### v0.1.0 (9 Nov 2023)

- initial contribution policy
