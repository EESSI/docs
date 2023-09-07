# EESSI test suite

[toc]

## Installation

### Requirements

The EESSI test suite requires Python >= 3.6 and [ReFrame](https://reframe-hpc.readthedocs.io).

### Installing Reframe (incl. `hpctestlib`)

You need to make sure that [ReFrame](https://reframe-hpc.readthedocs.io) is available - that is, the `reframe` command should work:

```bash
reframe --version
```

General instructions for installing ReFrame are available in the [ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/started.html).
The EESSI test suite requires ReFrame v4.0 or newer.

#### `hpctestlib` ReFrame component

The EESSI test suite requires the [`hpctestlib`](https://github.com/reframe-hpc/reframe/tree/develop/hpctestlib) component of ReFrame,
which is currently not included in a standard installation.

We recommend installing ReFrame using [EasyBuild](https://easybuild.io/),
or using a ReFrame installation that is available in EESSI (pilot version 2023.06, or newer).

For example:

```bash
source /cvmfs/pilot.eessi-hpc.org/versions/2023.06/init/bash
module load ReFrame/4.2.0
```

To check whether the `hpctestlib` component of ReFrame is available,
try importing the Python package:

```bash
python3 -c 'import hpctestlib'
```

### Installing the EESSI test suite

To install the EESSI test suite, you can either use `pip` or clone the GitHub repository directly:

#### Using `pip`

```bash
pip install git+https://github.com/EESSI/test-suite.git
```

#### Cloning the repository

```bash
git clone https://github.com/EESSI/test-suite EESSI-test-suite
cd EESSI-test-suite
export PYTHONPATH=$PWD:$PYTHONPATH
```

#### Check installation

To check whether the EESSI test suite installed correctly,
try importing the `eessi.testsuite` Python package:

```bash
python3 -c 'import eessi.testsuite'
```

## Configuration

Before you can run the EESSI test suite, you need to create a configuration file for ReFrame that is specific to the system on which the tests will be run.

Example configuration files are available [in the `EESSI/test-suite` GitHub repository in the `config` subdirectory](https://github.com/EESSI/test-suite/tree/main/config), which you can use as a template to create your own.

### Configuring ReFrame

We recommend configuring ReFrame by setting a couple of `$RFM_*` environment variables, to avoid that you need to include particular options to the `reframe` command over and over again.

#### ReFrame configuration file (`$RFM_CONFIG_FILES`)

*(see also [ReFrame docs](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#envvar-RFM_CONFIG_FILES))*

```
export RFM_CONFIG_FILES=$HOME/EESSI-test-suite/config/example.py
```

#### Search path for tests (`$RFM_CHECK_SEARCH_PATH`)

*(see also [ReFrame docs](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#envvar-RFM_CHECK_SEARCH_PATH))*

```
export RFM_CHECK_SEARCH_PATH=$HOME/EESSI-test-suite/eessi/testsuite/tests
export RFM_CHECK_SEARCH_RECURSIVE=1
```

**FIXME** explain why recursive needs to be enabled

### System configuration file

**FIXME** see Vega as reference example?

* partitions (incl. features, access, launcher, scheduler, name + partition (cfr. `--system`))

### Auto-detection of processor information

You can let ReFrame [auto-detect the processor information](https://reframe-hpc.readthedocs.io/en/stable/configure.html#proc-autodetection) for your system.

ReFrame will automatically use auto-detection if the `partitions` section
of you configuration file does not specify `processor` information for a
particular partition, and `remote_detect` is enabled.

To trigger the auto-detection of processor information, it is sufficient to
let ReFrame list the available tests:

```
reframe --list
```

ReFrame will store the processor information for your system in `~/.reframe/topology/<system>-<partition>/processor.json`.

#### Note

If you are using Slurm, you may need to temporarily change the launcher to `srun` in your configuration for auto-detection of processor information to work correctly.

See the [example AWS configuration file](https://github.com/EESSI/test-suite/blob/main/config/aws_citc.py), and [ReFrame issue #2926](https://github.com/reframe-hpc/reframe/issues/2926) for more information.

In addition, auto-detection does not work if ReFrame was installed directly
from PyPI, see [ReFrame issue #2914](https://github.com/reframe-hpc/reframe/issues/2914).
**FIXME** auto-detection also doesn't work with installation in EasyBuild/EESSI

## Running tests

### Listing available tests

To list the tests that are available in the EESSI test suite,
use `reframe --list` (or `reframe -L` for short).

If you have properly [configured ReFrame](#Configuring-ReFrame), you should
see a (potentially long) list of checks in the output:

```
$ reframe --list
...
[List of matched checks]
- ...
Found 1234 tests
```

**FIXME Kenneth** checks are only generated for available modules

### Performing a dry-run

To perform a dry run of the EESSI test suite, use `reframe --dry-run`:

```
$ reframe --dry-run
...
[==========] Running 1234 check(s)

[----------] start processing checks
[ DRY      ] GROMACS_EESSI ...
```

**FIXME Kenneth** explain why this can be useful, contrast with `--list` (which doesn't take into account partitions)

### Running the (full) test suite

To actually run the (full) EESSI test suite and let ReFrame
produce a performance report, use `reframe --run --performance-report`.

We recommend filtering the tests that will be run however, [see below](#Filtering-tests).

### ReFrame output and log files

**FIXME**

- `--prefix` to control where output goes
- 
- relation with common logging setup
- ReFrame log, perf log, output dirs, staging dirs, ...

### Filtering tests

By default, ReFrame will automatically generate checks for each system partition,
based on the tests available in the EESSI test suite, available software modules, and tags defined in the EESSI test suite.

To avoid being overwhelmed by checks, it is recommend to
[apply filters](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#test-filtering) so ReFrame only generates the checks you are interested in.

#### Filtering by test name

**FIXME** `--name`

#### Filtering by system (partition)

**FIXME** Cover both for specific system/partition

By default, ReFrame will generate checks for each system partition
that is listed in your configuration file.

To only let ReFrame checks for a particular system partition,
you can use the [`--system` option](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-system).

For example, to let ReFrame only generate checks for the `part_one` partition
of the system named `example`, use:

```
reframe --system example:part_one ...
```

Use the `--dry-run` option to check the impact of this.

#### Filtering by tags

To filter tests using one or more tags, you can use the [`--tag` option](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-0).

Using `--list-tags` you can get a list of known tags.

To check the impact of this on generated checks by ReFrame, use `--list`.

##### `CI` tag

For each software that is supported by the test suite,
a small test is tagged with `CI` to indicate it can be used in a Continuous Integration (CI) environment.

Hence, you can use this tag to let ReFrame only generate checks for small test cases:

```
reframe --tag CI
```

For example:

```
$ reframe --name GROMACS --tag CI
...
FIXME OUTPUT
```

##### `scale` tags

The EESSI test suite defines a set of custom tags that control the *scale*
of tests, that is how many resources will be used for running it.

| tag name | description |
|:--------:|-------------|
| `1_core` | using a single CPU core, or single GPU |
| `2_cores` | using 2 CPU cores, or 2 GPUs |
| `4_cores` | using 4 CPU cores, or 4 GPUs |
| `1_8_node` | using 1/8th of a node (12.5% of available cores/GPUs, 1 at minimum) |
| `1_4_node` | using a quarter of a node (25% of available cores/GPUs, 1 at minimum) |
| `1_2_node` | using half of a node (50% of available cores/GPUs, 1 at minimum) |
| `1_node`   | using a full node (all available cores/GPUs) |
| `2_nodes` | using 2 full nodes |
| `4_nodes` | using 4 full nodes |
| `8_nodes` | using 8 full nodes |
| `16_nodes` | using 16 full nodes |

##### Using multiple tags

To filter tests using multiple tags, you can:

* use `|` as separator to indicate that one of the specified tags must match (logical OR, for example `--tag='1_core|2_cores'`);
* use the `--tag` option multiple times to indicate that all specified tags must match (logical AND, for example `--tag CI --tag 1_core`);

#### Filtering by modules

**FIXME** This is not really filtering, but overriding default behaviour (see also https://github.com/EESSI/test-suite#changing-the-default-test-behavior-on-the-cmd-line), should use `--name` instead - add warning that this is advanced usage

By default, ReFrame will generate checks for each available software module
that can be used to run a particular test (for example, all available GROMACS modules will be used once to run each GROMACS test).

To only run the tests with specific modules, use the `--setvar modules=...` option.

You can use the `--list` option to check the impact on checks that ReFrame generates.

For example:

```
reframe --setvar modules=GROMACS/2021.3-foss-2021a --list
```

### Example commands

#### Running all GROMACS tests on 4 cores

```
reframe --name GROMACS --tag 4_cores --run
```

#### Running all GROMACS tests using a specific GROMACS module

```
reframe --setvar modules=GROMACS/2021.3-foss-2021a --run
```

## Available tests

The EESSI test suite currently includes tests for:

* [GROMACS](#GROMACS)
* [TensorFlow](#TensorFlow)

For a complete overview of all available tests in the EESSI test suite, see <https://github.com/EESSI/test-suite/tree/main/eessi/testsuite/tests>.

### GROMACS

using GROMACS test in ReFrame test library <link>

https://www.hecbiosim.ac.uk/access-hpc/benchmarks

Example run:


### TensorFlow

Example run:

```
[ReFrame Setup]
  version:           4.2.0
  command:           '/readonly/dodrio/apps/RHEL8/zen2-ib/software/ReFrame/4.2.0/bin/reframe --config-file config/vsc_hortense.py --checkpath eessi/testsuite/tests/apps/tensorflow --name TensorFlow/2.11 --tag 1_core --system hortense:cpu_rome_512gb --run --performance-report'
  launched by:       vsc46128@login55.dodrio.os
  working directory: '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite'
  settings files:    '<builtin>', 'config/vsc_hortense.py'
  check search path: '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/eessi/testsuite/tests/apps/tensorflow'
  stage directory:   '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/stage'
  output directory:  '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/output'
  log files:         '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/reframe_20230828_101237.log', '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/reframe_20230828_101237.out'

[==========] Running 1 check(s)
[==========] Started on Mon Aug 28 10:12:38 2023 

[----------] start processing checks
[ [32mRUN     [0m ] TENSORFLOW_EESSI %scale=1_core %module_name=TensorFlow/2.11.0-foss-2022a %device_type=cpu /af8226d5 @hortense:cpu_rome_512gb+default
[ [32m      OK[0m ] (1/1) TENSORFLOW_EESSI %scale=1_core %module_name=TensorFlow/2.11.0-foss-2022a %device_type=cpu /af8226d5 @hortense:cpu_rome_512gb+default
P: perf: 2770.757396498742 img/s (r:0, l:None, u:None)
[----------] all spawned checks have finished

[ [32m PASSED [0m ] Ran 1/1 test case(s) from 1 check(s) (0 failure(s), 0 skipped, 0 aborted)
[==========] Finished on Mon Aug 28 10:16:32 2023 

=========================================================================================================================================================
PERFORMANCE REPORT
---------------------------------------------------------------------------------------------------------------------------------------------------------
[TENSORFLOW_EESSI %scale=1_core %module_name=TensorFlow/2.11.0-foss-2022a %device_type=cpu /af8226d5 @hortense:cpu_rome_512gb:default]
  num_cpus_per_task: 1
  num_tasks_per_node: 1
  num_tasks: 1
  performance:
    - perf: 2770.757396498742 img/s (r: 0 img/s l: -inf% u: +inf%)
---------------------------------------------------------------------------------------------------------------------------------------------------------
Log file(s) saved in '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/reframe_20230828_101237.log', '/dodrio/scratch/projects/gadminforever/vsc46128/test-suite/reframe_20230828_101237.out'
```

## Release notes

v0.1.0
- ...
