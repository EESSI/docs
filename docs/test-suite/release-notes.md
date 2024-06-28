# Release notes for EESSI test suite

## 0.3.0 (27 june 2024)

This is a minor release of the EESSI test-suite

It includes:

* Update config AWS MC cluster to use `software.eessi.io` (#126)
* Add test for QuantumESPRESSO (pw.x) (#128)
* Fix compact process binding for OpenMPI mpirun (#137)
* Use compact process binding for GROMACS (#139)
* Rename scale tags 1_cpn_2_nodes and 1_cpn_4_nodes (#140)
* Set SRUN_CPUS_PER_TASK for srun launcher (#141)
* Fix for "Failed to modify UD QP to INIT on mlx5_0" on Karolina CI runs (#142)
* Reduce the iteration count to make the OSU tests run faster, especially on slower interconnects (#143)
* Add test for ESPResSo (P3M) (#144)
* Use software.eessi.io repo in CI (#146)
* Add notes on release management to README (#148)
* Fix memory_per_node for Hortense (#151)
* Use MiB units for memory per node (#152)
* Added / updated memory for various systems in MiB units (#153)
* Add additional test for ESPRESSO (LJ) (#155)
* Bump default version used in CI (#157)

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


## 0.1.0 (5 October 2023)

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
