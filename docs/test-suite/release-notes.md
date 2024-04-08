# Release notes for EESSI test suite

## 0.2.0 (7 march 2024)

This is a minor release of the EESSI test-suite

It includes:

* Implement the CI for regular runs on a system (#93)
* Add OSU tests and update the hooks and configs to make the tests portable (#54, #95, #96, #97, #110, #116, #117, #118, #121)
* Add extra scales to filter tests(#94)
* add new hook to filter out invalid scales based on features in the config (#111)
* unify test names (#108)
* updates to CI workflow ((#102, #103, #104, #105)
* Update common_config (#114)
* Add common config item to redirect the report file to the same directory as e.g. the perflog (#122)
* Fix code formatting + enforce it in CI workflow  (#120)

Bug fixes:

* Fix hook _assign_num_tasks_per_node (#98)
* fix import common-config vsc_hortense (#99)
* fix typo in partition names in configuration file for vsc_hortense (#106)


## 0.1.0 (5 Oktober 2023)

Version 0.1.0 is the first release of the EESSI test suite.

It includes:

* A well-structured `eessi.testsuite` Python package that provides [constants](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py),
  [utilities](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/utils.py),
  [hooks](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py),
  and [tests](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/),
  which can be [installed with "`pip install`"](installation-configuration.md#pip-install).
* Tests for [GROMACS](usage.md#gromacs) and [TensorFlow](usage.md#tensorflow) in [`eessi.testsuite.tests.apps`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/apps)
  that leverage the functionality provided by `eessi.testsuite.*`.
* Examples of [ReFrame configuration files](installation-configuration.md#reframe-config-file) for various systems in
  the [`config` subdirectory](https://github.com/EESSI/test-suite/tree/main/config).
* A [`common_logging_config()`](installation-configuration.md#logging) function to facilitate the ReFrame logging configuration.
* A set of standard *device types* and *features* that can be used in the [`partitions` section of the ReFrame configuration file](installation-configuration.md#partitions).
* A set of [*tags* (`CI` + `scale`) that can be used to filter checks](usage.md#filter-tag).
* [Scripts](https://github.com/EESSI/test-suite/tree/main/scripts) that show how to run the test suite.
