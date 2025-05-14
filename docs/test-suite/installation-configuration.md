# Installing and configuring the EESSI test suite

This page covers the requirements, installation and configuration of the [EESSI test suite](https://github.com/EESSI/test-suite).



## Requirements { #requirements }

The EESSI test suite requires 

* Python >= 3.7
* [ReFrame](https://reframe-hpc.readthedocs.io) v4.3.3 (or newer)
* [ReFrame test library (`hpctestlib`)](https://reframe-hpc.readthedocs.io/en/stable/hpctestlib.html)

??? note "(If your system Python version is lower than the minimum required version, click here for some tips)

    * You can upgrade and manage python versions using `pyenv`. [Link](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
        * For installation follow the documentation in the repository using the link above.
        * Then follow the steps to install a new Python version and further change local paths to the new Python:

                pyenv install <python version number>
                pyenv local <python version number>

    * You can install a more recent version of Python on top of the GCC/GCCcore compiler.
    * You can install a ReFrame module with EasyBuild and a [ReFrame easyconfig](https://github.com/easybuilders/easybuild-easyconfigs/tree/develop/easybuild/easyconfigs/r/ReFrame) containing a more recent Python version.
    * Don't forget to set RFM_PURGE_ENVIRONMENT=1 if you use Python from a module. The ReFrame easyconfigs already do that for you.

#### Installing Reframe

General instructions for installing ReFrame are available in the [ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/started.html). To check if ReFrame is available, run the `reframe` command:

```bash
reframe --version
```

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
  

#### Installing ReFrame test library (`hpctestlib`)

The EESSI test suite requires that the ReFrame test library (`hpctestlib`) is available, which is currently not included in a standard installation of ReFrame.

We recommend installing ReFrame using [EasyBuild](https://easybuild.io/) (version 4.8.1, or newer), or using a ReFrame installation that is available in the EESSI repository (version 2023.06, or newer).

For example (using EESSI):

```bash
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load ReFrame/4.3.3
```

To check whether the ReFrame test library is available, try importing a submodule of the `hpctestlib` Python package:

```bash
python3 -c 'import hpctestlib.sciapps.gromacs'
```

## Installation { #installation }

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

See the [section on the ReFrame configuration file](ReFrame-configuration-file.md#reframe-config-file) for more information.

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

#### ReFrame prefix (`$RFM_PREFIX`) {: #RFM_PREFIX }

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

If our [common logging configuration](ReFrame-configuration-file.md#logging) is used, the regular ReFrame log file will
also end up in the location specified by `$RFM_PREFIX`.

!!! warning

    Using the `--prefix` option in your `reframe` command is *not* equivalent to setting `$RFM_PREFIX`,
    since our [common logging configuration](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/common_config.py)
    only picks up on the `$RFM_PREFIX` environment variable to determine the location for the ReFrame log file.

