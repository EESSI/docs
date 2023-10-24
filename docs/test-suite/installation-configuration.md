# Installing and configuring the EESSI test suite

This page covers the installation and configuration of the [EESSI test suite](https://github.com/EESSI/test-suite).

For information on *using* the test suite, see [here](usage.md).


## Installation { #installation }

### Requirements { #requirements }

The EESSI test suite requires Python >= 3.6 and [ReFrame](https://reframe-hpc.readthedocs.io) v4.3.3 (or newer).

??? note "(for more details on the ReFrame version requirement, click here)"

    Two important bugs were resolved in ReFrame's CPU autodetect functionality [in version 4.3.3](https://github.com/reframe-hpc/reframe/pull/2978).

    _We strongly recommend you use `ReFrame >= 4.3.3`_.

    If you are using an older version of ReFrame, you may encounter some issues:

    * ReFrame will try to use the parallel launcher command configured for each partition (e.g. `mpirun`) when doing
      the remote autodetect. If there is no system-version of `mpirun` available, that will fail
      (see [ReFrame issue #2926](https://github.com/reframe-hpc/reframe/issues/2926)).
    * CPU autodetection only worked when using a clone of the ReFrame repository, _not_ when it was installed
      with `pip` or `EasyBuild` (as is also the case for the ReFrame shipped with EESSI)
      (see [ReFrame issue #2914](https://github.com/reframe-hpc/reframe/issues/2914)).
    

### Installing Reframe (incl. test library)

You need to make sure that [ReFrame](https://reframe-hpc.readthedocs.io) is available - that is, the `reframe` command should work:

```bash
reframe --version
```

General instructions for installing ReFrame are available in the [ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/started.html).

#### ReFrame test library (`hpctestlib`)

The EESSI test suite requires that the [ReFrame test library (`hpctestlib`)](https://reframe-hpc.readthedocs.io/en/stable/hpctestlib.html)
is available, which is currently not included in a standard installation of ReFrame.

We recommend installing ReFrame using [EasyBuild](https://easybuild.io/) (version 4.8.1, or newer),
or using a ReFrame installation that is available in EESSI (pilot version 2023.06, or newer).

For example (using EESSI):

```bash
source /cvmfs/pilot.eessi-hpc.org/versions/2023.06/init/bash
module load ReFrame/4.2.0
```

To check whether the ReFrame test library is available, try importing a submodule of the `hpctestlib` Python package:

```bash
python3 -c 'import hpctestlib.sciapps.gromacs'
```

### Installing the EESSI test suite

To install the EESSI test suite, you can either use `pip` or clone the GitHub repository directly:

#### Using `pip` { #pip-install }

```bash
pip install git+https://github.com/EESSI/test-suite.git
```

#### Cloning the repository

```bash
git clone https://github.com/EESSI/test-suite $HOME/EESSI-test-suite
cd EESSI-test-suite
export PYTHONPATH=$PWD:$PYTHONPATH
```

#### Verify installation

To check whether the EESSI test suite installed correctly,
try importing the `eessi.testsuite` Python package:

```bash
python3 -c 'import eessi.testsuite'
```


## Configuration

Before you can run the EESSI test suite, you need to create a configuration file for ReFrame that is specific to the system on which the tests will be run.

Example configuration files are available in the `config` subdirectory of the `EESSI/test-suite` GitHub repository](https://github.com/EESSI/test-suite/tree/main/config),
which you can use as a template to create your own.

### Configuring ReFrame environment variables

We recommend setting a couple of `$RFM_*` environment variables to configure ReFrame, to avoid needing to include particular options to the `reframe` command over and over again.

#### ReFrame configuration file (`$RFM_CONFIG_FILES`) { #RFM_CONFIG_FILES }

*(see also [`RFM_CONFIG_FILES` in ReFrame docs](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#envvar-RFM_CONFIG_FILES))*

Define the `$RFM_CONFIG_FILES` environment variable to instruct ReFrame which configuration file to use, for example:

```bash
export RFM_CONFIG_FILES=$HOME/EESSI-test-suite/config/example.py
```

Alternatively, you can use the `--config-file` (or `-C`) `reframe` option.

See the [section on the ReFrame configuration file](#reframe-config-file) below for more information.

#### Search path for tests (`$RFM_CHECK_SEARCH_PATH`)

*(see also [`RFM_CHECK_SEARCH_PATH` in ReFrame docs](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#envvar-RFM_CHECK_SEARCH_PATH))*

Define the `$RFM_CHECK_SEARCH_PATH` environment variable to tell ReFrame which directory to search for tests.

In addition, define `$RFM_CHECK_SEARCH_RECURSIVE` to ensure that ReFrame searches `$RFM_CHECK_SEARCH_PATH` recursively
(i.e. so that also tests in subdirectories are found).

For example:

```bash
export RFM_CHECK_SEARCH_PATH=$HOME/EESSI-test-suite/eessi/testsuite/tests
export RFM_CHECK_SEARCH_RECURSIVE=1
```

Alternatively, you can use the `--checkpath` (or `-c`) and `--recursive` (or `-R`) `reframe` options.

#### ReFrame prefix (`$RFM_PREFIX`) { #RFM_PREFIX }

*(see also [`RFM_PREFIX` in ReFrame docs](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#envvar-RFM_PREFIX))*

Define the `$RFM_PREFIX` environment variable to tell ReFrame where to store the files it produces. E.g.

```
export RFM_PREFIX=$HOME/reframe_runs
```

This involves:

* test output directories (which contain e.g. the job script, stderr and stdout for each of the test jobs)
* staging directories (unless otherwise specified by `staging`, see below);
* performance logs;

Note that the default is for ReFrame to use the current directory as prefix.
We recommend setting a prefix so that logs are not scattered around and nicely appended for each run.

If our [common logging configuration](#logging) is used, the regular ReFrame log file will
also end up in the location specified by `$RFM_PREFIX`.

!!! warning

    Using the `--prefix` option in your `reframe` command is *not* equivalent to setting `$RFM_PREFIX`,
    since our [common logging configuration](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/common_config.py)
    only picks up on the `$RFM_PREFIX` environment variable to determine the location for the ReFrame log file.

### ReFrame configuration file { #reframe-config-file }

In order for ReFrame to run tests on your system, it needs to know some properties about your system.
For example, it needs to know what kind of job scheduler you have, which partitions the system has,
how to submit to those partitions, etc.
All of this has to be described in a *ReFrame configuration file* (see also the [section on `$RFM_CONFIG_FILES` above](#RFM_CONFIG_FILES)).

The [official ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/configure.html) provides the full
description on configuring ReFrame for your site. However, there are some configuration settings that are specifically
required for the EESSI test suite. Also, there are a large amount of configuration settings available in ReFrame,
which makes the official documentation potentially a bit overwhelming.

Here, we will describe how to create a configuration file that works with the EESSI test suite, starting from an
[example configuration file `settings_example.py`](https://github.com/EESSI/test-suite/tree/main/config/settings_example.py),
which defines the most common configuration settings.

You can look at other example configurations in the [config directory](https://github.com/EESSI/test-suite/tree/main/config/) for more inspiration.

#### Python imports

The EESSI test suite standardizes a few string-based values as constants, as well as the logging format used by ReFrame.
Every ReFrame configuration file used for running the EESSI test suite should therefore start with the following import statements:

```python
from eessi.testsuite.common_config import common_logging_config
from eessi.testsuite.constants import *
```

#### High-level system info (`systems`)

First, we describe the system at its highest level through the
[`systems`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#systems) keyword.

You can define multiple systems in a single configuration file (`systems` is a Python list value).
We recommend defining just a single system in each configuration file, as it makes the configuration file a bit easier to digest (for humans).

An example of the `systems` section of the configuration file would be:

```python
site_configuration = {
    'systems': [
    # We could list multiple systems. Here, we just define one
        {
            'name': 'example',
            'descr': 'Example cluster',
            'modules_system': 'lmod',
            'hostnames': ['*'],
            'stagedir': f'/some/shared/dir/{os.environ.get("USER")}/reframe_output/staging',
            'partitions': [...],
        }
    ]
}
```

The most common configuration items defined at this level are:

- [`name`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.name):
  The name of the system. Pick whatever makes sense for you.
- [`descr`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.descr):
  Description of the system. Again, pick whatever you like.
- [`modules_system`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.modules_system):
  The modules system used on your system. EESSI provides modules in `lmod` format. There is no need to change this,
  unless you want to run tests from the EESSI test suite with non-EESSI modules.
- [`hostnames`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.hostnames):
  The names of the hosts on which you will run the ReFrame command, as regular expression. Using these names,
  ReFrame can automatically determine which of the listed configurations in the `systems` list to use, which is useful
  if you're defining multiple systems in a single configuration file. If you follow our recommendation to limit
  yourself to one system per configuration file, simply define `'hostnames': ['*']`.
- [`prefix`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.prefix):
  Prefix directory for a ReFrame run on this system. Any directories or files produced by ReFrame will use this prefix,
  if not specified otherwise.
  We recommend setting the `$RFM_PREFIX` environment variable rather than specifying `prefix` in
  your configuration file, so our [common logging configuration](#logging) can pick up on it
  (see also [`$RFM_PREFIX`](#RFM_PREFIX)).
- [`stagedir`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.stagedir): A shared directory that is available on all nodes that will execute ReFrame tests. This is used for storing (temporary) files related to the test. Typically, you want to set this to a path on a (shared) scratch filesystem. Defining this is optional: the default is a '`stage`' directory inside the `prefix` directory.
- [`partitions`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions): Details on system partitions, see below.



#### System partitions (`systems.partitions`) { #partitions }

The next step is to add the system partitions to the configuration files,
which is also specified as a Python list since a system can have multiple partitions.

The [`partitions`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions)
section of the configuration for a system with two [Slurm](https://slurm.schedmd.com/) partitions (one CPU partition,
and one GPU partition) could for example look something like this:

```python
site_configuration = {
    'systems': [
        {
            ...
            'partitions': [
                {
                    'name': 'cpu_partition',
                    'descr': 'CPU partition'
                    'scheduler': 'slurm',
                    'prepare_cmds': ['source /cvmfs/pilot.eessi-hpc.org/latest/init/bash'],
                    'launcher': 'mpirun',
                    'access':  ['-p cpu'],
                    'environs': ['default'],
                    'max_jobs': 4,
                    'features': [FEATURES[CPU]],
                },
                {
                    'name': 'gpu_partition',
                    'descr': 'GPU partition'
                    'scheduler': 'slurm',
                    'prepare_cmds': ['source /cvmfs/pilot.eessi-hpc.org/latest/init/bash'],
                    'launcher': 'mpirun',
                    'access':  ['-p gpu'],
                    'environs': ['default'],
                    'max_jobs': 4,
                    'resources': [
                        {
                            'name': '_rfm_gpu',
                            'options': ['--gpus-per-node={num_gpus_per_node}'],
                        }
                    ],
                    'devices': [
                        {
                            'type': DEVICE_TYPES[GPU],
                            'num_devices': 4,
                        }
                    ],
                    'features': [
                        FEATURES[CPU],
                        FEATURES[GPU],
                    ],
                    'extras': {
                        GPU_VENDOR: GPU_VENDORS[NVIDIA],
                    },
                },
            ]
        }
    ]
}
```

The most common configuration items defined at this level are:

- [`name`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.name):
  The name of the partition. Pick anything you like.
- [`descr`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.descr):
  Description of the partition. Again, pick whatever you like.
- [`scheduler`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.scheduler):
  The scheduler used to submit to this partition, for example `slurm`. All valid options can be found
  [in the ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.scheduler).
- [`launcher`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.launcher):
  The parallel launcher used on this partition, for example `mpirun` or `srun`. All valid options can be found
  [in the ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.launcher).
- [`access`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.access):
  A list of arguments that you would normally pass to the scheduler when submitting to this partition
  (for example '`-p cpu`' for submitting to a Slurm partition called `cpu`).
  If supported by your scheduler, we recommend to _not_ export the submission environment
  (for example by using '`--export=None`' with Slurm). This avoids test failures due to environment variables set
  in the submission environment that are passed down to submitted jobs.
- [`prepare_cmds`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.prepare_cmds):
  Commands to execute at the start of every job that runs a test. If your batch scheduler does not export
  the environment of the submit host, this is typically where you can initialize the EESSI environment.
- [`environs`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.environs):
  The names of the *programming environments* (to be defined later in the configuration file via [`environments`](#environments))
  that may be used on this partition. A programming environment is required for tests that are compiled first,
  before they can run. The EESSI test suite however only tests existing software installations, so no compilation
  (or specific programming environment) is needed. Simply specify `'environs': ['default']`,
  since ReFrame requires that *a* default environment is defined. 
- [`max_jobs`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.max_jobs):
  The maximum amount of jobs ReFrame is allowed to submit in parallel. Some batch systems limit how many jobs users
  are allowed to have in the queue. You can use this to make sure ReFrame doesn't exceed that limit.
- [`resources`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#custom-job-scheduler-resources):
  This field defines how additional resources can be requested in a batch job. Specifically, on a GPU partition,
  you have to define a resource with the name '`_rfm_gpu`'. The `options` field should then contain the argument to be
  passed to the batch scheduler in order to request a certain number of GPUs _per node_, which could be different for
  different batch schedulers. For example, when using Slurm you would specify:
  ```python
  'resources': [
    {
        'name': '_rfm_gpu',
        'options': ['--gpus-per-node={num_gpus_per_node}'],
    },
  ],
  ```
- [`processor`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.processor):
  We recommend to *NOT* define this field, unless [CPU autodetection](#cpu-auto-detection) is not working for you.
  The EESSI test suite relies on information about your processor topology to run. Using CPU autodetection is the
  easiest way to ensure that _all_ processor-related information needed by the EESSI test suite are defined.
  Only if CPU autodetection is failing for you do we advice you to set the `processor` in the partition configuration
  as an alternative. Although additional fields might be used by future EESSI tests, at this point you'll have to
  specify _at least_ the following fields:
  ```python
  'processor': {
      'num_cpus': 64,  # Total number of CPU cores in a node
      'num_sockets': 2,  # Number of sockets in a node
      'num_cpus_per_socket': 32,  # Number of CPU cores per socket
      'num_cpus_per_core': 1,  # Number of hardware threads per CPU core
  }                 
  ```
- [`features`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.features):
  The `features` field is used by the EESSI test suite to run tests _only_ on a partition if it supports a certain
  _feature_ (for example if GPUs are available). Feature names are standardized in the EESSI test suite in
  [`eessi.testsuite.constants.FEATURES`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py)
  dictionary.
  Typically, you want to define `features: [FEATURES[CPU]]` for CPU based partitions, and `features: [FEATURES[GPU]]`
  for GPU based partitions. The first tells the EESSI test suite that this partition can only run CPU-based tests,
  whereas second indicates that this partition can only run GPU-based tests.
  You _can_ define a single partition to have _both_ the CPU and GPU features (since `features` is a Python list).
  However, since the CPU-based tests will not ask your batch scheduler for GPU resources, this _may_ fail on batch
  systems that force you to ask for at least one GPU on GPU-based nodes. Also, running CPU-only code on a GPU node is
  typically considered bad practice, thus testing its functionality is typically not relevant.
- [`devices`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.devices): This field specifies information on devices (for example) present in the partition. Device types are standardized in the EESSI test suite in the [`eessi.testsuite.constants.DEVICE_TYPES`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py) dictionary. This is used by the EESSI test suite to determine how many of these devices it can/should use per node.
  Typically, there is no need to define `devices` for CPU partitions.
  For GPU partitions, you want to define something like:
  ```python
  'devices': {
      'type': DEVICE_TYPES[GPU],
      'num_devices': 4,  # or however many GPUs you have per node
  }
  ```
- [`extras`](https://reframe-hpc.readthedocs.io/en/stable/config_reference.html#config.systems.partitions.extras): This field specifies extra information on the partition, such as the GPU vendor. Valid fields for `extras` are standardized as constants in [`eessi.testsuite.constants`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py) (for example `GPU_VENDOR`). This is used by the EESSI test suite to decide if a partition can run a test that _specifically_ requires a certain brand of GPU.
  Typically, there is no need to define `extras` for CPU partitions.
  For GPU partitions, you typically want to specify the GPU vendor, for example:
  ```python
  'extras': {
      GPU_VENDOR: GPU_VENDORS[NVIDIA]
  }
  ```

Note that as more tests are added to the EESSI test suite, the use of `features`, `devices` and `extras` by the EESSI test suite may be extended, which may require an update of your configuration file to define newly recognized fields.

!!! note

    Keep in mind that ReFrame partitions are _virtual_ entities: they may or may not correspond to a partition as it is
    configured in your batch system. One might for example have a single partition in the batch system, but configure
    it as two separate partitions in the ReFrame configuration file based on additional constraints that are passed to
    the scheduler, see for example the [AWS CitC example configuration](https://github.com/EESSI/test-suite/blob/main/config/aws_citc.py).
    
    The EESSI test suite (and more generally, ReFrame) assumes the hardware _within_ a partition defined in the ReFrame configuration file is _homogeneous_.

#### Environments { #environments }

ReFrame needs a programming environment to be defined in its configuration file for tests that need to be compiled before they are run. While we don't have such tests in the EESSI test suite, ReFrame requires _some_ programming environment to be defined:

```python
site_configuration = {
    ...
    'environments': [
        {
            'name': 'default',  # Note: needs to match whatever we set for 'environs' in the partition
            'cc': 'cc',
            'cxx': '',
            'ftn': '',
        }
    ]
}
```

!!! note

    The `name` here needs to match whatever we specified for [the `environs` property of the partitions](#partitions).

#### Logging

ReFrame allows a large degree of control over what gets logged, and where. For convenience, we have created a common logging
configuration in [`eessi.testsuite.common_config`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/common_config.py)
that provides a reasonable default. It can be used by importing `common_logging_config` and calling it as a function
to define the '`logging` setting:
```python
from eessi.testsuite.common_config import common_logging_config

site_configuration = {
    ...
    'logging':  common_logging_config(),
}
```
When combined by setting the [`$RFM_PREFIX` environment variable](#RFM_PREFIX), the output, performance log, and
regular ReFrame logs will all end up in the directory specified by `$RFM_PREFIX`, which we recommend doing.

Alternatively, a prefix can be passed as an argument like `common_logging_config(prefix)`, which will control where
the regular ReFrame log ends up. Note that the performance logs do *not* respect this prefix: they will still end up
in the standard ReFrame prefix (by default the current directory, unless otherwise set with `$RFM_PREFIX` or `--prefix`).

#### Auto-detection of processor information { #cpu-auto-detection }

You can let ReFrame [auto-detect the processor information](https://reframe-hpc.readthedocs.io/en/stable/configure.html#proc-autodetection) for your system.

ReFrame will automatically use auto-detection when two conditions are met:

1. The [`partitions` section of you configuration file](#partitions) does *not* specify `processor` information for a
   particular partition (as per our recommendation [in the previous section](#partitions));
2. The `remote_detect` option is enabled in the `general` part of the configuration, as follows:
   ```python
   site_configuration = {
       'systems': ...
       'logging': ...
       'general': [
           {
               'remote_detect': True,
           }
       ]
   }
   ```

To trigger the auto-detection of processor information, it is sufficient to
let ReFrame list the available tests:

```
reframe --list
```

ReFrame will store the processor information for your system in `~/.reframe/topology/<system>-<partition>/processor.json`.

### Verifying your ReFrame configuration

To verify the ReFrame configuration, you can [query the configuration using `--show-config`](https://reframe-hpc.readthedocs.io/en/stable/configure.html#querying-configuration-options).

To see the full configuration, use:

```bash
reframe --show-config
```

To only show the configuration of a particular system partition, you can use the [`--system` option](https://reframe-hpc.readthedocs.io/en/stable/manpage.html#cmdoption-system).
To query a specific setting, you can pass an argument to `--show-config`.

For example, to show the configuration of the `gpu` partition of the `example` system:

```bash
reframe --system example:gpu --show-config systems/0/partitions
```

You can drill it down further to only show the value of a particular configuration setting.

For example, to only show the `launcher` value for the `gpu` partition of the `example` system:

```bash
reframe --system example:gpu --show-config systems/0/partitions/@gpu/launcher
```
