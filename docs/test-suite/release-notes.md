# Release notes for EESSI test suite

## 0.1.0

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
