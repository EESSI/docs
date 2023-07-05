# Contribution policy

When [openining a pull request to add software to EESSI](adding_software.md), the following requirements must
be taken into account.

!!! note

    These requirements are subject to change, please check back regularly.

## Open source software

Only **open source software** can be added to the EESSI repository.

Make sure that you are aware of software license, and that redistribution is allowed.

For more information about a specific license, see the [SPDX license list](https://spdx.org/licenses/).

!!! note

    We intend to automatically verify that this requirement is met,
    by requiring that the [SPDX license identifier](https://spdx.dev/ids/) is provided for all software.

## Built by the bot

All software included in the EESSI repository *must* be built autonomously by [our bot :robot:](../bot.md),
see also the [semi-automatic software installation procedure](adding_software.md).

## Supported by EasyBuild

Currently, we require that all software being added to EESSI is supported by the *EasyBuild release* being used
to perform the installation.

That is, the easyconfig files used for the installation *must be included in the EasyBuild release*.

We do allow the use of [`--from-pr`](https://docs.easybuild.io/integration-with-github/#github_from_pr) and
[`--include-easyblocks-from-pr`](https://docs.easybuild.io/integration-with-github/#github_include_easyblocks_from_pr)
to pull in changes required to make the installation work correctly in the EESSI build environment,
but only if that is strictly required.

!!! note

    This restriction may be relaxed later to also allow adding software that is not supported yet in the latest
    EasyBuild release, or to allow for installing software with other tools.

## Supported compiler toolchains

A [compiler toolchain](https://docs.easybuild.io/terminology/#toolchains) that is still supported by the latest
EasyBuild must be used for building the software.

More information on deprecated toolchains in EasyBuild is available
[here](https://docs.easybuild.io/deprecated-easyconfigs/#deprecated_easyconfigs_toolchains).

## Supported CPU targets

The software *should* work on all [CPU targets supported by EESSI](cpu_targets.md).

Exceptions to this requirement are allowed if technical problems that can not be resolved with reasonable effort
prevent the installation of the software for specific CPU targets.

## Software versions & toolchains

Recent software versions and toolchains *should* be preferred,
although the installation of older versions of use of older toolchains is allowed if sufficiently motivated.

## Testing

We should be able to test the software installations via the [EESSI test suite](https://github.com/EESSI/test-suite)
being developed.

Ideally one or more tests are available that verify that the software is functionally correct,
and performs well.

It should be possible to run a minimal *smoke test*, for example using EasyBuild's `--sanity-check-only` feature.

!!! note

    The [EESSI test suite](https://github.com/EESSI/test-suite) is still in active development,
    and currently only has a minimal set of tests available.

    When the test suite is more mature, this requirement will be enforced more strictly.
