# Using the EESSI test suite

This page covers the usage of the [EESSI test suite](https://github.com/EESSI/test-suite).

We assume you have already [installed and configured](installation-configuration.md) the EESSI test suite on your
system.

## Listing available tests

To list the tests that are available in the EESSI test suite,
use `reframe --list` (or `reframe -L` for short).

If you have properly [configured ReFrame](#Configuring-ReFrame), you should
see a (potentially long) list of checks in the output:

```
$ reframe --list
...
[List of matched checks]
- ...
Found 123 check(s)
```

!!! note
    When using `--list`, checks are only generated based on modules that are available in the system where the `reframe` command is invoked.

    The system partitions specified in your ReFrame configuration file are *not* taken into account when using `--list`.

    So, if `--list` produces an overview of 50 checks, and you have 4 system partitions in your configuration file,
    actually running the test suite may result in (up to) 200 checks being executed.

## Performing a dry run { #dry-run }

To perform a dry run of the EESSI test suite, use `reframe --dry-run`:

```
$ reframe --dry-run
...
[==========] Running 1234 check(s)

[----------] start processing checks
[ DRY      ] GROMACS_EESSI ...
...
[----------] all spawned checks have finished

[  PASSED  ] Ran 1234/1234 test case(s) from 1234 check(s) (0 failure(s), 0 skipped, 0 aborted)
```

!!! note

    When using `--dry-run`, the systems partitions listed in your ReFrame configuration file are also taken into
    account when generating checks, next to available modules and test parameters, which is *not* the case when using `--list`.

## Running the (full) test suite

To actually run the (full) EESSI test suite and let ReFrame
produce a performance report, use `reframe --run --performance-report`.

We strongly recommend filtering the checks that will be run by using additional options
like `--system`, `--name`, `--tag` (see the ['Filtering tests' section below](#filtering-tests)),
and doing a [dry run](#dry-run) first to make sure that the generated checks correspond to what you have in mind.

## ReFrame output and log files

ReFrame will generate various output and log files:

* a general ReFrame log file with debug logging on the ReFrame run (incl. selection of tests, generating checks,
  test results, etc.);
* stage directories for each generated check, in which the checks are run;
* output directories for each generated check, which include the test output;
* performance log files for each test, which include performance results for the test runs;

We strongly recommend controlling where these files go by using the [common logging configuration that
is provided by the EESSI test suite in your ReFrame configuration file](installation-configuration.md#logging)
and setting [`$RFM_PREFIX`](installation-configuration.md#RFM_PREFIX) (avoid using the cmd line option `--prefix`).

If you do, and if you use [ReFrame v4.3.3 or more newer](installation-configuration.md#requirements),
you should find the output and log files at:

* general ReFrame log file at `$RFM_PREFIX/logs/reframe_<datestamp>_<timestamp>.log`;
* stage directories in `$RFM_PREFIX/stage/<system>/<partition>/<environment>/`;
* output directories in `$RFM_PREFIX/output/<system>/<partition>/<environment>/`;
* performance log files in `$RFM_PREFIX/perflogs/<system>/<partition>/<environment>/`;

In the stage and output directories, there will be a subdirectory for each check that was run,
which are tagged with a unique hash (like `d3adb33f`) that is determined based on the specific parameters for that check
(see the [ReFrame documentation for more details on the test naming scheme](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#test-naming-scheme)).

## Filtering tests { #filtering-tests }

By default, ReFrame will automatically generate checks for each system partition,
based on the tests available in the EESSI test suite, available software modules,
and tags defined in the EESSI test suite.

To avoid being overwhelmed by checks, it is recommend to [apply filters](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#test-filtering)
so ReFrame only generates the checks you are interested in.

### Filtering by test name { #filter-name }

You can filter checks based on the full test name using the [`--name` option (or `-n`)](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-n),
which includes the value for all test parameters.

Here's an example of a full test name:

```
GROMACS_EESSI %benchmark_info=HECBioSim/Crambin %nb_impl=cpu %scale=1_node %module_name=GROMACS/2023.1-foss-2022a /d3adb33f @example:gpu+default
```

To let ReFrame only generate checks for GROMACS, you can use:

```bash
reframe --name GROMACS
```

To only run GROMACS checks with a particular version of GROMACS, you can use `--name` to only retain specific `GROMACS`
modules:

```bash
reframe --name %module_name=GROMACS/2023.1
```

Likewise, you can filter on any part of the test name.

You can also select one specific check using the corresponding [test hash](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#test-naming-scheme),
which is also part of the full test name (see `/d3adb33f` in the example above):
for example:

```bash
reframe --name /d3adb33f
```

The argument passed to `--name` is interpreted as a Python regular expression, so you can use wildcards like `.*`,
character ranges like `[0-9]`, use `^` to specify that the pattern should match from the start of the test name, etc.

Use `--list` or `--dry-run` to check the impact of using the `--name` option.

### Filtering by system (partition) { #filter-system-partition }

By default, ReFrame will generate checks for each system partition that is listed in your configuration file.

To only let ReFrame checks for a particular system or system partition,
you can use the [`--system` option](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-system).

For example:

* To let ReFrame only generate checks for the system named `example`, use:
  ```
  reframe --system example ...
  ```
* To let ReFrame only generate checks for the `gpu` partition of the system named `example`, use:
  ```
  reframe --system example:gpu ...
  ```

Use `--dry-run` to check the impact of using the `--system` option.


### Filtering by tags { #filter-tag }

To filter tests using one or more tags, you can use the [`--tag` option](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-0).

Using `--list-tags` you can get a list of known tags.

To check the impact of this on generated checks by ReFrame, use `--list` or `--dry-run`.

#### `CI` tag

For each software that is included in the EESSI test suite,
a small test is tagged with `CI` to indicate it can be used in a Continuous Integration (CI) environment.

Hence, you can use this tag to let ReFrame only generate checks for small test cases:

```
reframe --tag CI
```

For example:

```
$ reframe --name GROMACS --tag CI
...
```

#### `scale` tags

The EESSI test suite defines a set of custom tags that control the *scale* of
checks, which specify many cores/GPUs/nodes should be used for running a check.
The number of cores and GPUs serves as an upper limit; the actual count depends
on the specific configuration of cores, GPUs, and sockets within the node, as
well as the specific test being carried out.

| tag name | description |
|:--------:|-------------|
| `1_core` | using 1 CPU core 1 GPU |
| `2_cores` | using 2 CPU cores and 1 GPU |
| `4_cores` | using 4 CPU cores and 1 GPU |
| `1_cpn_2_nodes` | using 1 CPU core per node, 1 GPU per node, and 2 nodes |
| `1_cpn_4_nodes` | using 1 CPU core per node, 1 GPU per node, and 4 nodes |
| `1_8_node` | using 1/8th of a node (12.5% of available cores/GPUs, 1 at minimum) |
| `1_4_node` | using a quarter of a node (25% of available cores/GPUs, 1 at minimum) |
| `1_2_node` | using half of a node (50% of available cores/GPUs, 1 at minimum) |
| `1_node`   | using a full node (all available cores/GPUs) |
| `2_nodes` | using 2 full nodes |
| `4_nodes` | using 4 full nodes |
| `8_nodes` | using 8 full nodes |
| `16_nodes` | using 16 full nodes |

#### Using multiple tags

To filter tests using multiple tags, you can:

* use `|` as separator to indicate that *one* of the specified tags must match (logical OR, for example `--tag='1_core|2_cores'`);
* use the `--tag` option multiple times to indicate that *all* specified tags must match (logical AND, for example `--tag CI --tag 1_core`);

## Overriding test parameters *(advanced)*

You can override test parameters using the [`--setvar` option (or `-S`)](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-S).

This can be done either globally (for all tests), or only for specific tests (which is recommended when using `--setvar`).

For example, to run all GROMACS checks with a specific GROMACS module, you can use:

```
reframe --setvar GROMACS_EESSI.modules=GROMACS/2023.1-foss-2022a ...
```

!!! warning

    We do not recommend using `--setvar`, since it is quite easy to make unintended changes to test parameters
    this way that can result in broken checks.

    You should try filtering tests using the [`--name`](#filter-name) or [`--tag`](#filter-tag) options instead.


## Example commands

### Running all GROMACS tests on 4 cores on the `cpu` partition

```
reframe --run --system example:cpu --name GROMACS --tag 4_cores --performance-report
```

### List all checks for TensorFlow 2.11 using a single node

```
reframe --list --name %module_name=TensorFlow/2.11 --tag 1_node
```

### Dry run of TensorFlow CI checks on a quarter (1/4) of a node (on all system partitions)

```
reframe --dry-run --name 'TensorFlow.*CUDA' --tag 1_4_node --tag CI
```

## Available tests { #available-tests }

The EESSI test suite currently includes tests for:

* [GROMACS](#gromacs)
* [TensorFlow](#tensorflow)

For a complete overview of all available tests in the EESSI test suite, see the
[`eessi/testsuite/tests` subdirectory in the `EESSI/test-suite` GitHub repository](https://github.com/EESSI/test-suite/tree/main/eessi/testsuite/tests).

### GROMACS { #gromacs }

Several tests for [GROMACS](https://www.gromacs.org), a software package to perform molecular dynamics simulations,
are included, which use the systems included in the [HECBioSim benchmark suite](https://www.hecbiosim.ac.uk/access-hpc/benchmarks):

* `Crambin` (20K atom system)
* `Glutamine-Binding-Protein` (61K atom system)
- `hEGFRDimer` (465K atom system)
- `hEGFRDimerSmallerPL` (465K atom system, only 10k steps)
- `hEGFRDimerPair` (1.4M atom system)
- `hEGFRtetramerPair` (3M atom system)

It is implemented in [`tests/apps/gromacs.py`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/apps/gromacs.py),
on top of the GROMACS test that is included in the [ReFrame test library `hpctestlib`](https://reframe-hpc.readthedocs.io/en/stable/hpctestlib.html).

To run this GROMACS test with all HECBioSim systems, use:

```bash
reframe --run --name GROMACS
```

To run this GROMACS test only for a specific HECBioSim system, use for example:

```bash
reframe --run --name 'GROMACS.*HECBioSim/hEGFRDimerPair'
```

To run this GROMACS test with the smallest HECBioSim system (`Crambin`), you can use the `CI` tag:

```bash
reframe --run --name GROMACS --tag CI
```

### TensorFlow { #tensorflow }

A test for [TensorFlow](https://www.tensorflow.org), a machine learning framework, is included,
which is based on the ["Multi-worker training with Keras" TensorFlow tutorial](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras).

It is implemented in [`tests/apps/tensorflow/`](https://github.com/EESSI/test-suite/tree/main/eessi/testsuite/tests/apps/tensorflow).

!!! warning
    This test requires TensorFlow v2.11 or newer, using an older TensorFlow version will not work!

To run this TensorFlow test, use:

```bash
reframe --run --name TensorFlow
```
