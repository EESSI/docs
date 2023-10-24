# Contribution policy

*(version v0.1.0 - updated 24 Oct 2023)*

!!! note

    This policy is subject to change, please check back regularly.

## Purpose

The purpose of this contribution policy is to provide guidelines for [adding software](software_layer/adding_software.md) to EESSI.

It informs about what requirements must be met in order for software to be eligible for inclusion
in the EESSI software layer.

## Requirements

The following requirements must be taken into account when adding software to EESSI.

---

### a) Open source software { #open_source_software }

Only **open source software** can be added to the EESSI repository.

Make sure that you are aware of relevant software license, and that redistribution is allowed.

For more information about a specific license, see the [SPDX license list](https://spdx.org/licenses/).

!!! note

    We intend to automatically verify that this requirement is met,
    by requiring that the [SPDX license identifier](https://spdx.dev/ids/) is provided for all software.


---

### b) Built by the bot { #built_by_bot }

All software included in the EESSI repository *must* be built autonomously by [our bot :robot:](bot.md),
see also the [semi-automatic software installation procedure](software_layer/adding_software.md).


---

### c) Supported by EasyBuild { #supported_by_easybuild }

Currently, we require that all software being added to EESSI is supported by the *EasyBuild release* being used
to perform the installation.

That is, the easyconfig files used for the installation *must be included in the EasyBuild release*.

We do allow the use of [`--from-pr`](https://docs.easybuild.io/integration-with-github/#github_from_pr) and
[`--include-easyblocks-from-pr`](https://docs.easybuild.io/integration-with-github/#github_include_easyblocks_from_pr)
to pull in changes required to make the installation work correctly in the EESSI build environment,
but only if that is strictly required.


---

### d) Compiler toolchain { #compiler_toolchain }

A [compiler toolchain](https://docs.easybuild.io/terminology/#toolchains) that is still supported by the latest
EasyBuild must be used for building the software.

More information on supported toolchains in EasyBuild is available [here](https://docs.easybuild.io/policies/toolchains).


---

### e) CPU targets { #cpu_targets }

The software *should* work on all [CPU targets supported by EESSI](software_layer/cpu_targets.md).

Exceptions to this requirement are allowed if technical problems that can not be resolved with reasonable effort
prevent the installation of the software for specific CPU targets.


---

### f) Versions & toolchains { #versions_toolchains }

Recent software versions and toolchains *should* be preferred,
although the installation of older software versions and toolchains is allowed if sufficiently motivated.


---

### g) Testing { #testing }

We should be able to test the software installations via the [EESSI test suite](https://github.com/EESSI/test-suite)
being developed.

Ideally one or more tests are available that verify that the software is functionally correct,
and performs well.

It should be possible to run a minimal *smoke test*, for example using EasyBuild's `--sanity-check-only` feature.

!!! note

    The [EESSI test suite](https://github.com/EESSI/test-suite) is still in active development,
    and currently only has a minimal set of tests available.

    When the test suite is more mature, this requirement will be enforced more strictly.

---

## Changelog

### v0.1.0 (24 Oct 2023)

- initial contribution policy
