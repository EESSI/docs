# Writing portable tests

This page is a tutorial on how to write a new test for the [EESSI test suite](https://github.com/EESSI/test-suite).

If you already know how to write regular ReFrame tests, we suggest you read the [High-level overview](#high-level-overview) and [Test requirements](#test-requirements) sections, then skip ahead to [Step 3: implementing as a portable ReFrame test](#as-portable-reframe-test).

## High-level overview

In this tutorial, you will learn how to write a test for the [EESSI test suite](https://www.eessi.io/docs/test-suite/). It is important to realize in which context the test suite will be run. Roughly speaking, there are three uses:

- Running tests for one (or a few) particular applications, as part of the [workflow of adding new software to EESSI](https://www.eessi.io/docs/adding_software/contribution_policy/#testing),  to validate the sanity of the (new) installation
- Regular (e.g. daily) runs, on a set of HPC clusters, to identify performance regressions
- By an end-user of EESSI, who runs either a specific test or the full test suite, to validate the functionality of EESSI (or a particular software in EESSI) on the end-user’s system

The test suite contains a combination of real-life use cases for end-user scientific software (e.g. tests for GROMACS, TensorFlow, CP2K, OpenFOAM, etc) and low level tests (e.g. OSU Microbenchmarks).

The tests in the EESSI test suite are developed using the [ReFrame HPC testing framework](https://reframe-hpc.readthedocs.io/en/stable/). Typically, ReFrame tests hardcode system specific information (core counts, performance references, etc) in the test definition. The EESSI test suite aims to be portable, and implements a [mixin class](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/eessi_mixin.py) that invokes a series of standard [hooks](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) to replace information that is typically hardcoded. All system-specific information is then limited to the ReFrame configuration file. As an example: rather than hardcoding that a test should run with 128 tasks (i.e. because a system has 128 core nodes), the EESSI test suite has a hook that can define a test should be run on a "single, full node". The hook queries the ReFrame configuration file for the amount of cores per node, and specifies this number as the corresponding amount of tasks. Thus, on a 64-core node, this test would run with 64 tasks, while on a 128-core node, it would run 128 tasks.

## Test requirements

To be useful in the aforementioned scenarios, tests need to satisfy a number of requirements. 

- Tests are implemented in the [ReFrame HPC testing framework](https://reframe-hpc.readthedocs.io/en/stable/).
- Multiple tests may be implemented for a single software package.
- Tests should run in a reasonable amount of time (less than 1 hour) for all the scales for which it is defined to be valid (on a recent CPU/GPU).
- There should be at least one light-weight (short, low-core, low-memory) test case. On a decently sized machine (in 2024, that means about 8 cores and 16 GB memory), this test case should run in less than 5 minutes. This test should be marked with the 'CI' tag.
- Tests should only use a reasonable amount of memory, so that _most_ systems will be able to run them. For low core counts (1-8 cores), 8-16 GB is reasonable. For higher core counts, keeping a memory usage to less than 1 GB/core will ensure that _mosts_ systems will be able to run it.
- Tests should be portable, meaning they should not contain any system-specific information. If assumptions are made that might not be satisfied on every system (e.g. a test needs at least X cores to run), the test should check for it, and be skipped if the system does not satisfy the requirement.

## Step-by-step tutorial for writing a portable ReFrame test

In the next section, we will show how to write a test for the EESSI test suite by means of an example: we will create a test for [mpi4py](https://mpi4py.readthedocs.io/en/stable/) that executes an `MPI_REDUCE` call to sum the ranks of all processes. If you’re unfamiliar with MPI or `mpi4py`, or want to see the exact code this test will run, you may want to read [Background of the mpi4py test](#background-of-mpi4py-test) before proceeding. The complete test developed in this tutorial can be found in the `tutorials/mpi4py` directory in  of the [EESSI test suite](https://github.com/EESSI/test-suite/) repository.

### Step 1: writing job scripts to execute tests
Although not strictly needed for the implementation of a ReFrame test, it is useful to try and write a job script for how you would want to run this test on a given system. For example, on a system with 128-core nodes, managed by SLURM, we might have the following job scripts to execute the `mpi4py_reduce.py` code.

To run on 2 cores:
```shell
#!/bin/bash
#SBATCH --ntasks=2  # 2 tasks, since 2 processes is the minimal size on which I can do a reduction
#SBATCH --cpus-per-task=1  # 1 core per task (this is a pure multiprocessing test, each process only uses 1 thread)
#SBATCH --time=5:00  # This test is very fast. It shouldn't need more than 5 minutes
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load mpi4py/3.1.5-gompi-2023b
mpirun -np 2 python3 mpi4py_reduce.py --n_iter 1000 --n_warmup 100
```
To run on one full node:
```shell
#!/bin/bash
#SBATCH --ntasks=128  # min. 2 tasks in total, since 2 processes is the minimal size on which I can do a reduction
#SBATCH --ntasks-per-node=128
#SBATCH --cpus-per-task=1  # 1 core per task (this is a pure multiprocessing test, each process only uses 1 thread)
#SBATCH --time=5:00  # This test is very fast. It shouldn't need more than 5 minutes
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load mpi4py/3.1.5-gompi-2023b
mpirun -np 128 python3 mpi4py_reduce.py --n_iter 1000 --n_warmup 100
```
To run on two full nodes
```shell
#!/bin/bash
#SBATCH --ntasks=256 # min. 2 tasks in total, since 2 processes is the minimal size on which I can do a reduction
#SBATCH --ntasks-per-node=128 
#SBATCH --cpus-per-task=1  # 1 core per task (this is a pure multiprocessing test, each process only uses 1 thread)
#SBATCH --time=5:00  # This test is very fast. It shouldn't need more than 5 minutes
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load mpi4py/3.1.5-gompi-2023b
mpirun -np 256 python3 mpi4py_reduce.py --n_iter 1000 --n_warmup 100
```

Clearly, such job scripts are not very portable: these only work on SLURM systems, we had to duplicate a lot to run on different scales, we would have to duplicate even more if we wanted to test multiple `mpi4py` versions, etc. This is where `ReFrame` comes in: it has support for different schedulers, and allows one to easily specify a range of parameters (such as the number of tasks in the above example) to create tests for.

### Step 2: implementing as a non-portable ReFrame test
First, let us implement this as a non-portable test in ReFrame. This code can be found under `tutorials/mpi4py/mpi4py_system_specific.py` in the [EESSI test suite](https://github.com/EESSI/test-suite/) repository. We will not elaborate on how to write ReFrame tests, it is well-documented in the official [ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/index.html). We have put extensive comments in the test definition below, to make it easier to understand when you have limited familiarity with ReFrame. Whenever the variables below have a specific meaning in ReFrame, we referenced the official documentation:

```python
"""
This module tests mpi4py's MPI_Reduce call
"""

import reframe as rfm
import reframe.utility.sanity as sn

# added only to make the linter happy
from reframe.core.builtins import variable, parameter, run_after, performance_function, sanity_function


# This python decorator indicates to ReFrame that this class defines a test
# Our class inherits from rfm.RunOnlyRegressionTest, since this test does not have a compilation stage
# https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RunOnlyRegressionTest
@rfm.simple_test
class EESSI_MPI4PY(rfm.RunOnlyRegressionTest):
    # Programming environments are only relevant for tests that compile something
    # Since we are testing existing modules, we typically don't compile anything and simply define
    # 'default' as the valid programming environment
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.valid_prog_environs
    valid_prog_environs = ['default']

    # Typically, we list here the name of our cluster as it is specified in our ReFrame configuration file
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.valid_systems
    valid_systems = ['snellius']

    # ReFrame will generate a test for each module
    # NOTE: each parameter adds a new dimension to the parametrization space. 
    # (EG 4 parameters with (3,3,2,2) possible values will result in 36 tests).
    # Be mindful of how many parameters you add to avoid the number of tests generated being excessive.
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.parameter
    module_name = parameter(['mpi4py/3.1.4-gompi-2023a', 'mpi4py/3.1.5-gompi-2023b'])

    # ReFrame will generate a test for each scale
    scale = parameter([2, 128, 256])

    # Our script has two arguments, --n_iter and --n_warmup. By defining these as ReFrame variables, we can
    # enable the end-user to overwrite their value on the command line when invoking ReFrame.
    # Note that we don't typically expose ALL variables, especially if a script has many - we expose
    # only those that we think an end-user might want to overwrite
    # Number of iterations to run (more iterations takes longer, but results in more accurate timing)
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.variable
    n_iterations = variable(int, value=1000)

    # Similar for the number of warmup iterations
    n_warmup = variable(int, value=100)

    # Define which executable to run
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.executable
    executable = 'python3'

    # Define which options to pass to the executable
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.executable_opts
    executable_opts = ['mpi4py_reduce.py', '--n_iter', f'{n_iterations}', '--n_warmup', f'{n_warmup}']

    # Define a time limit for the scheduler running this test
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.time_limit
    time_limit = '5m00s'

    # Using this decorator, we tell ReFrame to run this AFTER the init step of the test
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.run_after
    # See https://reframe-hpc.readthedocs.io/en/stable/pipeline.html for all steps in the pipeline
    # that reframe uses to execute tests. Note that after the init step, ReFrame has generated test instances for each
    # of the combinations of parameters above. Thus, now, there are 6 instances (2 module names * 3 scales). Here,
    # we set the modules to load equal to one of the module names
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.modules
    @run_after('init')
    def set_modules(self):
        self.modules = [self.module_name]

    # Similar for the scale, we now set the number of tasks equal to the scale for this instance
    @run_after('init')
    def define_task_count(self):
        # Set the number of tasks, self.scale is now a single number out of the parameter list
        # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.num_tasks
        self.num_tasks = self.scale
        # Set the number of tasks per node to either be equal to the number of tasks, but at most 128,
        # since we have 128-core nodes
        # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.num_tasks_per_node
        self.num_tasks_per_node = min(self.num_tasks, 128)

    # Now, we check if the pattern 'Sum of all ranks: X' with X the correct sum for the amount of ranks is found
    # in the standard output:
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.sanity_function
    @sanity_function
    def validate(self):
        # Sum of 0, ..., N-1 is (N * (N-1) / 2)
        sum_of_ranks = round(self.scale * ((self.scale - 1) / 2))
        # https://reframe-hpc.readthedocs.io/en/stable/deferrable_functions_reference.html#reframe.utility.sanity.assert_found
        return sn.assert_found(r'Sum of all ranks: %s' % sum_of_ranks, self.stdout)

    # Now, we define a pattern to extract a number that reflects the performance of this test
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.performance_function
    @performance_function('s')
    def time(self):
        # https://reframe-hpc.readthedocs.io/en/stable/deferrable_functions_reference.html#reframe.utility.sanity.extractsingle
        return sn.extractsingle(r'^Time elapsed:\s+(?P<perf>\S+)', self.stdout, 'perf', float)
```

This single test class will generate 6 test instances: tests with 2, 128 and 256 tasks for each of the two modules, respectively. It will check the sum of ranks produced at the end in the output, which is how ReFrame will validate that the test ran correctly. Finally, it will also print the performance number that was extracted by the `performance_function`.

This test _works_, but is _not_ very portable. If we move to a system with 192 cores per node, the current `scale` parameter is a bit awkward. The test would still run, but we wouldn’t have a test instance that just tests this on a full (single) node or two full nodes. Furthermore, if we add a new `mpi4py` module in EESSI, we would have to alter the test to add the name to the list, since the module names are hardcoded in this test.

### Step 3: implementing as a portable ReFrame test { #as-portable-reframe-test }

In step 2, there were several system-specific items in the test. In this section, we will show how we use inheritance from the `EESSI_Mixin` class to avoid hard-coding system specific information. The full final test can be found under `tutorials/mpi4py/mpi4py_portable_mixin.py` in the [EESSI test suite](https://github.com/EESSI/test-suite/) repository.

#### How EESSI_Mixin works

The `EESSI_Mixin` class provides standardized functionality that should be useful to all tests in the EESSI test-suite. One of its key functions is to make sure tests dynamically try to determine sensible values for the things that were system specific in Step 2. For example, instead of hard coding a task count, the test inheriting from `EESSI_Mixin` will determine this dynamically based on the amount of available cores per node, and a declaration from the inheriting test class about how you want to instantiate tasks.

To illustrate this, suppose you want to launch your test with one task per CPU core. In that case, your test (that inherits from `EESSI_Mixin`) only has to declare

```python
compute_unit = COMPUTE_UNITS.CPU
```

The `EESSI_Mixin` class then takes care of querying the ReFrame config file for the cpu topology of the node, and setting the correct number of tasks per node.

Another feature is that it sets defaults for a few items, such as the `valid_prog_environs = ['default']`. These will likely be the same for _most_ tests in the EESSI test suite, and when they _do_ need to be different, one can easily overwrite them in the child class.

Most of the functionality in the `EESSI_Mixin` class require certain class attributes (such as the `compute_unit` above) to be set by the child class, so that the `EESSI_Mixin` class can use those as input. It is important that these attributes are set _before_ the stage in which the `EESSI_Mixin` class needs them (see the stages of the [ReFrame regression pipeline](https://reframe-hpc.readthedocs.io/en/stable/pipeline.html)). To support test developers, the `EESSI_Mixin` class checks if these attributes are set, and gives verbose feedback in case any attributes are missing.

#### Inheriting from EESSI_Mixin

The first step is to actually inherit from the `EESSI_Mixin` class:

```python
from eessi.testsuite.eessi_mixin import EESSI_Mixin
...
@rfm.simple_test
class EESSI_MPI4PY(rfm.RunOnlyRegressionTest, EESSI_Mixin):
```

#### Removing hard-coded test scales

First, we remove 

```python
    # ReFrame will generate a test for each scale
    scale = parameter([2, 128, 256])
```
from the test. The `EESSI_Mixin` class will define the default set of scales on which this test will be run as
```python
from eessi.testsuite.constants import SCALES
...
    scale = parameter(SCALES.keys())
```

This ensures the test will run a test case for each of the default scales, as defined by the `SCALES` [constant](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py).

If, and only if, your test can not run on all of those scales should you overwrite this parameter in your child class. For example, if you have a test that does not support running on multiple nodes, you could define a filtering function outside of the class
```python
def filter_scales():
    return [
        k for (k,v) in SCALES.items()
        if v['num_nodes'] == 1
    ]
```
and then in the class body overwrite the scale parameter with a subset of items from the `SCALES` constant:
```python
    scale = parameter(filter_scales())
```

Next, we also remove

```python
   @run_after('init')
    def define_task_count(self):
        self.num_tasks = self.scale
        self.num_tasks_per_node = min(self.num_tasks, 128)
```

as `num_tasks` and and `num_tasks_per_node` will be set by the `assign_tasks_per_compute_unit` [hook](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py), which is invoked by the `EESSI_Mixin` class.

Instead, we only set the `compute_unit`. The number of launched tasks will be equal to the number of compute units. E.g.
```python
    compute_unit = COMPUTE_UNITS.CPU
```
will launch one task per (physical) CPU core. Other options are `COMPUTE_UNITS.HWTHREAD` (one task per hardware thread), `COMPUTE_UNITS.NUMA_NODE` (one task per numa node), `COMPUTE_UNITS.CPU_SOCKET` (one task per CPU socket), `COMPUTE_UNITS.GPU` (one task per GPU) and `COMPUTE_UNITS.NODE` (one task per node). Check the `COMPUTE_UNITS` [constant](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py) for the full list of valid compute units. The number of cores per task will automatically be set based on this as the ratio of the number of cores in a node to the number of tasks per node (rounded down). Additionally, the `EESSI_Mixin` class will set the `OMP_NUM_THREADS` environment variable equal to the number of cores per task.

!!! note
    `compute_unit` needs to be set before (or in) ReFrame’s `setup` phase. For the different phases of the pipeline, please see the [documentation on how ReFrame executes tests](https://reframe-hpc.readthedocs.io/en/stable/pipeline.html).

#### Replacing hard-coded module names
Instead of hard-coding a module name, we parameterize over all module names that match a certain regular expression. 

```python
from eessi.testsuite.utils import find_modules
...
    module_name = parameter(find_modules('mpi4py'))
```

This parameter generates all module names available on the current system matching the expression, and each test instance will load the respective module before running the test.

Furthermore, we remove the hook that sets `self.module`:
```python
@run_after('init')
def set_modules(self):
    self.modules = [self.module_name]
```
This is now taken care of by the `EESSI_Mixin` class.

!!! note
    `module_name` needs to be set before (or in) ReFrame’s `init` phase

#### Replacing hard-coded system names and programming environments
First, we remove the hard-coded system name and programming environment. I.e. we remove
```python
    valid_prog_environs = ['default']
    valid_systems = ['snellius']
```
The `EESSI_Mixin` class sets `valid_prog_environs = ['default']` by default, so that is no longer needed in the child class (but it can be overwritten if needed). The `valid_systems` is instead replaced by a declaration of what type of device type is needed. We’ll create an `mpi4py` test that runs on CPUs only:
```python
    device_type = DEVICE_TYPES.CPU
```
but note if we would have wanted to also generate test instances to test GPU <=> GPU communication, we could have defined this as a parameter:
```python
    device_type = parameter([DEVICE_TYPES.CPU, DEVICE_TYPES.GPU])
```

The device type that is set will be used by the `filter_valid_systems_by_device_type` hook to check in the ReFrame configuration file which of the current partitions contain the relevant device. Typically, we don’t set the `DEVICE_TYPES.CPU` on a GPU partition in the ReFrame configuration, so that we skip all CPU-only tests on GPU nodes. Check the `DEVICE_TYPES` [constant](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py) for the full list of valid compute units.

`EESSI_Mixin` also filters based on the supported scales, which can again be configured per partition in the ReFrame configuration file. This can e.g. be used to avoid running large-scale tests on partitions that don't have enough nodes to run them.

!!! note
    `device_type` needs to be set before (or in) ReFrame's `init` phase

#### Requesting sufficient RAM memory
To make sure you get an allocation with sufficient memory, your test should declare how much memory per node it needs by defining a `required_mem_per_node` function in your test class that returns the required memory per node (in MiB). Note that the amount of required memory generally depends on the amount of tasks that are launched per node (`self.num_tasks_per_node`).

Our `mpi4py` test takes around 200 MB when running with a single task, plus about 70 MB for every additional task. We round this up a little so that we can be sure the test won’t run out of memory if memory consumption is slightly different on a different system. Thus, we define:

```python
def required_mem_per_node(self):
    return self.num_tasks_per_node * 100 + 250
```

While rounding up is advisable, do keep your estimate realistic. Too high a memory request will mean the test will get skipped on systems that cannot satisfy that memory request. Most HPC systems have at least 1 GB per core, and most laptop/desktops have at least 8 GB total. Designing a test so that it fits within those memory constraints will ensure it can be run almost anywhere.

!!! note
    The easiest way to get the memory consumption of your test at various task counts is to execute it on a system which runs jobs in [cgroups](https://en.wikipedia.org/wiki/Cgroups), define `measure_memory_usage = True` in your class body, and make the `required_mem_per_node` function return a constant amount of memory equal to the available memory per node on your test system. This will cause the `EESSI_Mixin` class to read out the maximum memory usage of the cgroup (on the head node of your allocation, in case of multi-node tests) and report it as a performance number.

#### Process binding
The `EESSI_Mixin` class binds processes to their respective number of cores automatically using the `hooks.set_compact_process_binding` hook. E.g. for a pure MPI test like `mpi4py`, each task will be bound to a single core. For hybrid tests that do both multiprocessing and multithreading, tasks are bound to a sequential number of cores. E.g. on a node with 128 cores and a hybrid test with 64 tasks and 2 threads per task, the first task will be bound to core 0 and 1, second task to core 2 and 3, etc. To override this behaviour, one would have to overwrite the
```python
@run_after('setup')
def assign_tasks_per_compute_unit(self):
    ...
```
function. Note that this function also calls other hooks (such as `hooks.assign_task_per_compute_unit`) that you probably still want to invoke. Check the `EESSI_Mixin` [class definition](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/eessi_mixin.py) to see which hooks you still want to call.

#### CI Tag
As mentioned in the [Test requirements](#test-requirements), there should be at least one light-weight (short, low-core, low-memory) test case, which should be marked with the `CI` tag. If `is_ci_test` is set to `True` for a given test variant, the `EESSI_Mixin` class will automatically add the `CI` tag and add logging. The `mpi4py` test contains only one variant (which is very light-weight). In this case, it is sufficient to set it in the class body:
```python
is_ci_test = True
```

Suppose that our test has 2 variants, of which only `'variant1'` should be marked `CI`. In that case, we can define `test_variant` as a parameter:
```python
    test_variant = parameter(['variant1', 'variant2'])
```
Next, we can define a hook that does different things depending on the variant, and set `is_ci_test` for `'variant1'`, for example: 
```python
@run_after('init')
def do_something(self):
    if self.test_variant == 'variant1':
        do_this()
        is_ci_test = True
    elif self.test_variant == 'variant2':
        do_that()
```

#### Readonly files
To avoid excessive copying of test input files into each stage directory, it is
highly recommended to specify a list of files and/or dirs in `sourcesdir` that
are needed but not modified during the test, and thus can be symlinked into the
stage dirs. In this case, file `mpi4py_reduce.py` does not change during the
test, so it can be safely symlinked:
```
readonly_files = ['mpi4py_reduce.py']
```
We’ve made the `readonly_files` attribute mandatory for all tests to ensure it’s
not overlooked. If you are sure no files should be symlinked in your test, set
it to `['']`:
```
readonly_files = ['']
```

#### Thread binding (optional)
Thread binding is not done by default, but can be done by setting `thread_binding` in the class body:
```python
thread_binding = 'compact'
```

#### Skipping test instances when required (optional) { #skipping-test-instances }
Preferably, we prevent test instances from being generated (i.e. before ReFrame’s `setup` phase) if we know that they cannot run on a certain system. However, sometimes we need information on the nodes that will run it, which is only available _after_ the `setup` phase. That is the case for anything where we need information from e.g. the [reframe.core.pipeline.RegressionTest.current_partition](https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.current_partition).

For example, we might know that a test only scales to around 300 tasks, and above that, execution time increases rapidly. In that case, we’d want to skip any test instance that results in a larger amount of tasks, but we only know this after `assign_tasks_per_compute_unit` has been called (which is done by `EESSI_Mixin` in after the `setup` stage). For example, the `2_nodes` scale would run fine on systems with 128 cores per node, but would exceed the task limit of 300 on systems with `192` cores per node.

We can skip any generated test cases using the `skip_if` function. For example, to skip the test if the total task count exceeds 300, we’d need to call `skip_if` _after_ the `setup` stage (so that `self.num_tasks` is already set):

```python
@run_after('setup')
    hooks.assign_tasks_per_compute_unit(test=self, compute_unit=COMPUTE_UNITS.CPU)

    max_tasks = 300
    self.skip_if(self.num_tasks > max_tasks,
                 f'Skipping test: more than {max_tasks} tasks are requested ({self.num_tasks})')
```

The `mpi4py` test scales up to a very high core count, but if we were to set it for the sake of this example, one would see:
```bash
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=16_nodes /38aea144 @snellius:genoa+default
[     SKIP ] ( 1/13) Skipping test: more than 300 tasks are requested (3072)
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=8_nodes /bfc4d3d4 @snellius:genoa+default
[     SKIP ] ( 2/13) Skipping test: more than 300 tasks are requested (1536)
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=4_nodes /8de369bc @snellius:genoa+default
[     SKIP ] ( 3/13) Skipping test: more than 300 tasks are requested (768)
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=2_nodes /364146ba @snellius:genoa+default
[     SKIP ] ( 4/13) Skipping test: more than 300 tasks are requested (384)
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_node /8225edb3 @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_2_node /4acf483a @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_4_node /fc3d689b @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_8_node /73046a73 @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1cpn_4nodes /f08712a2 @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1cpn_2nodes /23cd550b @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=4_cores /bb8e1349 @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=2_cores /4c0c7c9e @snellius:genoa+default
[ RUN      ] EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_core /aa83ba9e @snellius:genoa+default

...
```
on a system with 192 cores per node. I.e. any test of 2 nodes (384 cores) or above would be skipped because it exceeds our max task count.

#### Setting a time limit (optional)
By default, the `EESSI_Mixin` class sets a time limit for jobs of 1 hour. You can overwrite this in your child class:
```python
time_limit = '5m00s'
```
For the appropriate string formatting, please check the [ReFrame documentation on time_limit](https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.time_limit). We already had this in the non-portable version of our `mpi4py` test and will keep it in the portable version: since this is a very quick test, specifying a lower time limit will help in getting the jobs scheduled more quickly.

Note that for the test to be portable, the time limit should be set such that it is sufficient _regardless of node architecture and scale_. It is pretty hard to guarantee this with a single, fixed time limit, without knowing upfront what architecture the test will be run on, and thus how many tasks will be launched. For strong scaling tests, you might want a higher time limit for low task counts, whereas for weak scaling tests you might want a higher time limit for higher task counts. To do so, you can consider setting the time limit after setup, and making it dependent on the task count.

Suppose we have a weak scaling test that takes 5 minutes with a single task, and 60 minutes with 10k tasks. We can set a time limit based on linear interpolation between those task counts:
```python
@run_after('setup')
def set_time_limit(self):
    # linearly interpolate between the single and 10k task count
    minutes = 5 + self.num_tasks * ((60-5) / 10000)
    self.time_limit = f'{minutes}m00s'
```
Note that this is typically an overestimate of how long the test will take for intermediate task counts, but that's ok: we'd rather overestimate than underestimate the runtime.

To be even safer, one could consider combining this with logic to [skip tests](#skipping-test-instances) if the 10k task count is exceeded.

#### Summary
To make the test portable, we added additional imports:
```python
from eessi.testsuite.eessi_mixin import EESSI_Mixin
from eessi.testsuite.constants import COMPUTE_UNITS, DEVICE_TYPES
from eessi.testsuite.utils import find_modules
```

Made sure the test inherits from `EESSI_Mixin`:
```python
@rfm.simple_test
class EESSI_MPI4PY(rfm.runOnlyRegressionTest, EESSI_Mixin):
```

Removed the following from the class body:
```python
valid_prog_environs = ['default']
valid_systems = ['snellius']

module_name = parameter(['mpi4py/3.1.4-gompi-2023a', 'mpi4py/3.1.5-gompi-2023b'])
scale = parameter([2, 128, 256])
```

Added the following to the class body:
```python
device_type = DEVICE_TYPES.CPU
compute_unit = COMPUTE_UNITS.CPU

module_name = parameter(find_modules('mpi4py'))
```

Defined the class method:
```python
def required_mem_per_node(self):
    return self.num_tasks_per_node * 100 + 250
```

Removed the ReFrame pipeline hook that sets `self.modules`:
```python
@run_after('init')
def set_modules(self):
     self.modules = [self.module_name]
```

Removed the ReFrame pipeline hook that sets the number of tasks and number of tasks per node:
```python
@run_after('init')
def define_task_count(self):
    # Set the number of tasks, self.scale is now a single number out of the parameter list
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.num_tasks
    self.num_tasks = self.scale
    # Set the number of tasks per node to either be equal to the number of tasks, but at most 128,
    # since we have 128-core nodes
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.num_tasks_per_node
    self.num_tasks_per_node = min(self.num_tasks, 128)
```

The final test is thus:
```python
"""
This module tests mpi4py's MPI_Reduce call
"""

import reframe as rfm
import reframe.utility.sanity as sn

from reframe.core.builtins import variable, parameter, run_after, performance_function, sanity_function

from eessi.testsuite.eessi_mixin import EESSI_Mixin
from eessi.testsuite.constants import COMPUTE_UNITS, DEVICE_TYPES
from eessi.testsuite.utils import find_modules

@rfm.simple_test
class EESSI_MPI4PY(rfm.RunOnlyRegressionTest, EESSI_Mixin):
    device_type = DEVICE_TYPES.CPU
    compute_unit = COMPUTE_UNITS.CPU

    module_name = parameter(find_modules('mpi4py'))

    n_iterations = variable(int, value=1000)
    n_warmup = variable(int, value=100)

    executable = 'python3'
    executable_opts = ['mpi4py_reduce.py', '--n_iter', f'{n_iterations}', '--n_warmup', f'{n_warmup}']

    time_limit = '5m00s'

    is_ci_test = True

    readonly_files = ['mpi4py_reduce.py']

    def required_mem_per_node(self):
        return self.num_tasks_per_node * 100 + 250

    @sanity_function
    def validate(self):
        sum_of_ranks = round(self.num_tasks * ((self.num_tasks - 1) / 2))
        return sn.assert_found(r'Sum of all ranks: %s' % sum_of_ranks, self.stdout)

    @performance_function('s')
    def time(self):
        return sn.extractsingle(r'^Time elapsed:\s+(?P<perf>\S+)', self.stdout, 'perf', float)
```

Note that with only 44 lines of code, this is now very quick and easy to write, because of the default behaviour from the `EESSI_Mixin` class.

### Background of the mpi4py test { #background-of-mpi4py-test }
To understand what this test does, you need to know some basics of MPI. If you know about MPI, you can skip this section.

The MPI standard defines how to communicate between multiple processes that work on a common computational task. Each process that is part of the computational task gets a unique identifier (0 to N-1 for N processes), the MPI rank, which can e.g. be used to distribute a workload. The MPI standard defines communication between two given processes (so-called point-to-point communication), but also between a set of N processes (so-called collective communication).

An example of such a collective operation is the [MPI_REDUCE](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node130.htm#Node130) call. It reduces data elements from multiple processes with a certain operation, e.g. it takes the sum of all elements or multiplication of all elements.

#### The mpi4py test
In this example, we will implement a test that does an `MPI_Reduce` on the rank, using the `MPI.SUM` operation. This makes it easy to validate the result, as we know that for N processes, the theoretical sum of all ranks (0, 1, ... N-1) is `(N * (N-1) / 2)`.

Our initial code is a python script `mpi4py_reduce.py`, which can be found in `tutorials/mpi4py/src/mpi4py_reduce.py` in the [EESSI test suite](https://github.com/EESSI/test-suite/) repository:
```python
#!/usr/bin/env python
"""
MPI_Reduce on MPI rank. This should result in a total of (size * (size - 1) / 2),
where size is the total number of ranks.
Prints the total number of ranks, the sum of all ranks, and the time elapsed for the reduction."
"""

import argparse
import time

from mpi4py import MPI

parser = argparse.ArgumentParser(description='mpi4py reduction benchmark',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--n_warmup', type=int, default=100,
                    help='Number of warmup iterations')
parser.add_argument('--n_iter', type=int, default=1000,
                    help='Number of benchmark iterations')
args = parser.parse_args()

n_warmup = args.n_warmup
n_iter = args.n_iter

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

# Warmup
t0 = time.time()
for i in range(n_warmup):
    total = MPI.COMM_WORLD.reduce(rank, op=MPI.SUM)

# Actual reduction, multiple iterations for accuracy of timing
t1 = time.time()
for i in range(n_iter):
    total = MPI.COMM_WORLD.reduce(rank, op=MPI.SUM)
t2 = time.time()
total_time = (t2 - t1) / n_iter

if rank == 0:
    print(f"Total ranks: {size}")
    print(f"Sum of all ranks: {total}")  # Should be (size * (size-1) / 2)
    print(f"Time elapsed: {total_time:.3e}")
```

Assuming we have `mpi4py` available, we could run this manually using
```bash
$ mpirun -np 4 python3 mpi4py_reduce.py
Total ranks: 4
Sum of all ranks: 6
Time elapsed: 3.609e-06
```

This started 4 processes, with ranks 0, 1, 2, 3, and then summed all the ranks (`0+1+2+3=6`) on the process with rank 0, which finally printed all this output. The whole reduction operation is performed `n_iter` times, so that we get a more reproducible timing.

### Step 3: implementing as a portable ReFrame test without using EESSI_Mixin { #as-portable-reframe-test-legacy }

The approach using inheritance from the `EESSI_Mixin` class, described above, is strongly preferred and recommended. There might be certain tests that do not fit the standardized approach of `EESSI_Mixin`, but usually that will be solvable by overwriting hooks set by `EESSI_Mixin` in the inheriting class. In the rare case that your test is so exotic that even this doesn’t provide a sensible solution, you can still invoke the hooks used by `EESSI_Mixin` manually. Note that this used to be the default way of writing tests for the EESSI test suite.

In step 2, there were several system-specific items in the test. In this section, we will show how we use the EESSI hooks to avoid hard-coding system specific information. We do this by replacing the system-specific parts of the test from Step 2 bit by bit. The full final test can be found under `tutorials/mpi4py/mpi4py_portable_legacy.py` in the [EESSI test suite](https://github.com/EESSI/test-suite/) repository.

#### Replacing hard-coded test scales (mandatory)

We replace the hard-coded

```python
    # ReFrame will generate a test for each scale
    scale = parameter([2, 128, 256])
```

by 

```python
from eessi.testsuite.constants import SCALES
...
    # ReFrame will generate a test for each scale
    scale = parameter(SCALES.keys())
```

the `SCALES` [constant](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/constants.py) contains a set of default scales at which we run all tests. For our `mpi4py` example, that is sufficient. 

!!! note
    It might be that particular tests do not make sense at certain scales. An example is code that only has multithreading, but no multiprocessing support, and is thus only able to run on a single node. In that case, we filter the set of `SCALES` down to only those where `num_nodes = 1`, and parameterize the test across those scales:

    ```python
    from eessi.testsuite.constants import SCALES
    def get_singlenode_scales():
        """
        Filtering function for single node tests
        """
        return [
            k for (k, v) in SCALES.items()
            if v['num_nodes'] == 1
        ]
       ...
       scale = parameter(get_singlenode_scales())
    ```

We also replace

```python
    @run_after('init')
    def define_task_count(self):
        self.num_tasks = self.scale
        self.num_tasks_per_node = min(self.num_tasks, 128)
```

by

```python
from eessi.testsuite import hooks
from eessi.testsuite.constants import SCALES, COMPUTE_UNITS
    ...
    @run_after('init')
    def run_after_init(self):
        hooks.set_tag_scale(self)
        
    @run_after('setup')
    def set_num_tasks_per_node(self):
        """ Setting number of tasks per node and cpus per task in this function. This function sets num_cpus_per_task
        for 1 node and 2 node options where the request is for full nodes."""
        hooks.assign_tasks_per_compute_unit(self, COMPUTE_UNITS.CPU)
```

The first [hook](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) (`set_tag_scale`) sets a number of custom attributes for the current test, based on the scale (`self.num_nodes`, `self.default_num_cpus_per_node`, `self.default_num_gpus_per_node`, `self.node_part`). These are not used by ReFrame, but can be used by later hooks from the EESSI test suite. It also sets a ReFrame scale `tag` for convenience. These scale `tag`s are useful for quick test selection, e.g. by running ReFrame with `--tag 1_node` one would only run the tests generated for the scale `1_node`. Calling this hook is mandatory for all tests, as it ensures standardization of tag names based on the scales.

The second hook, `assign_tasks_per_compute_unit`, is used to set the task count. This hook sets the `self.num_tasks` and `self.num_tasks_per_node` we hardcoded before. In addition, it sets the `self.num_cpus_per_task`. In this case, we call it with the `COMPUTE_UNITS.CPU` argument, which means one task will be launched per (physical) CPU available. Thus, for the `1_node` scale, this would run the `mpi4py` test with 128 tasks on a 128-core node, and with 192 tasks on a 192-core node. Check the [code](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) for other valid `COMPUTE_UNITS`.

#### Replacing hard-coded module names (mandatory)

If we write an `mpi4py` test, we typically want to run this for _all_ `mpi4py` modules that are available via our current `$MODULEPATH`. We do that by replacing

```python
    module_name = parameter(['mpi4py/3.1.4-gompi-2023a', 'mpi4py/3.1.5-gompi-2023b'])
```

by using the `find_modules` utility function:

```python
from eessi.testsuite.utils import find_modules
...
    module_name = parameter(find_modules('mpi4py'))
```

We also replace

```python
    @run_after('init')
    def set_modules(self):
        self.modules = [self.module_name]
```

by

```python
    @run_after('init')
    def set_modules(self):
        hooks.set_modules(self)
```

The `set_modules` hook assumes that `self.module_name` has been set, but has the added advantage that a user running the EESSI test suite can overwrite the modules to load from the command line when running ReFrame (see [Overriding test parameters](https://www.eessi.io/docs/test-suite/usage/#overriding-test-parameters-advanced)).

#### Replacing hard-coded valid_systems (mandatory)

The `valid_systems` attribute is a mandatory attribute to specify in a ReFrame test. However, we can set it to match any system:

```python
valid_systems = [*]
```

Normally, `valid_systems` is used as a way of guaranteeing that a system has the necessary properties to run the test. For example, if we know that `my_gpu_system` has NVIDIA GPUs and I have a test written for NVIDIA GPUs, I would specify `valid_systems['my_gpu_system']` for that test. This, however, is a surrogate for declaring what my test _needs_: I'm saying it needs `my_gpu_system`, while in fact I could make the more general statement 'this test needs NVIDIA GPUs'.

To keep the test system-agnostic we _can_ declare what the test needs by using ReFrame's concept of partition `features` (a string) and/or `extras` (a key-value pair); [see the ReFrame documentation on `valid_systems`](https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.valid_systems). For example, a test could declare it _needs_ the `gpu` feature. Such a test will only be created by ReFrame for partitions that declare (in the ReFrame configuration file) that they have the `gpu` feature.

Since `features` and `extras` are full text fields, we standardize those in the EESSI test suite in the `eessi/testsuite/constants.py` file. For example, tests that require an NVIDIA GPU could specify

```python
from eessi.testsuite.constants import EXTRAS, FEATURES, GPU_VENDORS
...
valid_systems = f'+{FEATURES.GPU} %{EXTRAS.GPU_VENDOR}={GPU_VENDORS.NVIDIA}'
```

which makes sure that a test instance is only generated for partitions (as defined in the ReFrame configuration file) that specify that they _have_ the corresponding feature and extras:

```python
from eessi.testsuite.constants import EXTRAS, FEATURES, GPU_VENDORS
...
'features': [
     FEATURES.GPU,
],
'extras': {
    EXTRAS.GPU_VENDOR: GPU_VENDORS.NVIDIA,
},
```

In practice, one will rarely hard-code this `valid_systems` string. Instead, we have a [hook](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) `filter_valid_systems_by_device_type`. It does the above, and a bit more: it also checks if the module that the test is generated for is CUDA-enabled (in case of a test for `NVIDIA` GPUs), and _only then_ will it generate a GPU-based test. Calling this hook is mandatory for all tests (even if just to declare they need a CPU to run).

Another aspect is that not all ReFrame partitions may be able to run tests of all of the standard `SCALES`. Each ReFrame partition must add the subset of `SCALES` it supports to its list of features.  A test case can declare it needs a certain scale. For example, a test case using the `16_nodes` scale needs a partition with at least 16 nodes. The `filter_supported_scales` [hook](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) then filters out all partitions that do not support running jobs on 16 nodes. Calling this hook is also mandatory for all tests.

There may be other hooks that facilitate valid system selection for your tests, but please check the [code](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) for a full list.

#### Requesting sufficient memory (mandatory)

When developing the test, we don’t know how much memory the node will have on which it will run. However, we _do_ know how much our application _needs_.

We can declare this need using the `req_memory_per_node` hook. This hook is mandatory for all tests. If you are on a system with a scheduler that runs jobs within a cgroup and where you can use `mpirun` or `srun` as the parallel launcher command in the ReFrame configuration, getting the memory consumption is easy. You can (temporarily) add a `postrun_cmds` the following to the class body of your test that extracts the maximum memory that was used within your cgroup. For cgroups v1, the syntax would be:

```python
   # Temporarily define postrun_cmds to make it easy to find out memory usage
    postrun_cmds = ['MAX_MEM_IN_BYTES=$(</sys/fs/cgroup/memory/$(</proc/self/cpuset)/../memory.max_usage_in_bytes)', 'echo "MAX_MEM_IN_MIB=$(($MAX_MEM_IN_BYTES/1048576))"']
```

For cgroups v2, the syntax would be:

```python
   # Temporarily define postrun_cmds to make it easy to find out memory usage
   postrun_cmds = ['MAX_MEM_IN_BYTES=$(</sys/fs/cgroup/$(</proc/self/cpuset)/../../../memory.peak)', 'echo "MAX_MEM_IN_MIB=$(($MAX_MEM_IN_BYTES/1048576))"']
```

And define an additional `performance_function`:

```python
    @performance_function('MiB')
    def max_mem_in_mib(self):
        return sn.extractsingle(r'^MAX_MEM_IN_MIB=(?P<perf>\S+)', self.stdout, 'perf', int)
```

This results in the following output on 192-core nodes (we’ve omitted some output for readability):

```bash
[----------] start processing checks
[       OK ] ( 1/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=16_nodes /38aea144 @snellius:genoa+default
P: max_mem_in_mib: 22018 MiB (r:0, l:None, u:None)
[       OK ] ( 2/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=8_nodes /bfc4d3d4 @snellius:genoa+default
P: max_mem_in_mib: 21845 MiB (r:0, l:None, u:None)
[       OK ] ( 3/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=4_nodes /8de369bc @snellius:genoa+default
P: max_mem_in_mib: 21873 MiB (r:0, l:None, u:None)
[       OK ] ( 4/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=2_nodes /364146ba @snellius:genoa+default
P: max_mem_in_mib: 21800 MiB (r:0, l:None, u:None)
[       OK ] ( 5/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_node /8225edb3 @snellius:genoa+default
P: max_mem_in_mib: 21666 MiB (r:0, l:None, u:None)
[       OK ] ( 6/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_2_node /4acf483a @snellius:genoa+default
P: max_mem_in_mib: 10768 MiB (r:0, l:None, u:None)
[       OK ] ( 7/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_4_node /fc3d689b @snellius:genoa+default
P: max_mem_in_mib: 5363 MiB (r:0, l:None, u:None)
[       OK ] ( 8/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_8_node /73046a73 @snellius:genoa+default
P: max_mem_in_mib: 2674 MiB (r:0, l:None, u:None)
[       OK ] ( 9/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1cpn_4nodes /f08712a2 @snellius:genoa+default
P: max_mem_in_mib: 210 MiB (r:0, l:None, u:None)
[       OK ] (10/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1cpn_2nodes /23cd550b @snellius:genoa+default
P: max_mem_in_mib: 209 MiB (r:0, l:None, u:None)
[       OK ] (11/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=4_cores /bb8e1349 @snellius:genoa+default
P: max_mem_in_mib: 753 MiB (r:0, l:None, u:None)
[       OK ] (12/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=2_cores /4c0c7c9e @snellius:genoa+default
P: max_mem_in_mib: 403 MiB (r:0, l:None, u:None)
[       OK ] (13/13) EESSI_MPI4PY %module_name=mpi4py/3.1.5-gompi-2023b %scale=1_core /aa83ba9e @snellius:genoa+default
P: max_mem_in_mib: 195 MiB (r:0, l:None, u:None)
```

If you are _not_ on a system where your scheduler runs jobs in cgroups, you will have to figure out the memory consumption in another way (e.g. by checking memory usage in `top` while running the test).

We now have a pretty good idea how the memory per node scales: for our smallest process count (1 core), it’s about 200 MiB per process, while for our largest process count (16 nodes, 16 * 192 processes), it’s 22018 MiB per node (or about 115 MiB per process). If we wanted to do really well, we could define a linear function (with offset) and fit it through the data (and round up to be on the safe side, i.e. make sure there is _enough_ memory). Then, we could call the hook like this:

```python
@run_after('setup')
def request_mem(self):
    mem_required = self.num_tasks_per_node * mem_slope + mem_intercept
    hooks.req_memory_per_node(self, app_mem_req=mem_required)
```

In this case, however, the memory consumption per process is low enough that we don’t have go through that effort, and generously request 256 MiB per task that is launched on a node. Thus, we call our hook using:

```python
@run_after('setup')
def request_mem(self):
    mem_required = self.num_tasks_per_node * 256
    hooks.req_memory_per_node(self, app_mem_req=mem_required)
```
Note that requesting too high an amount of memory means the test will be skipped on nodes that cannot meet that requirement (even if they might have been able to run it without _actually_ running out of memory). Requesting too little will risk nodes running out of memory while running the test. Note that many HPC systems have an amount memory of around 1-2 GB/core. It’s good to ensure (if you can) that the memory requests for all valid `SCALES` for your test do not exceed the total amount of memory available on typical nodes.

#### Requesting task/process/thread binding (recommended)

Binding processes to a set of cores prevents the OS from migrating such processes to other cores. Especially on multi-socket systems, process migration can cause performance hits, especially if a process is moved to a CPU core on the other socket. Since this is controlled by the OS, and dependent on what other processes are running on the node, it may cause unpredictable performance: in some runs, processes might be migrated, while in others, they aren’t.

Thus, it is typically better for reproducibility to bind processes to their respective set of cores. The `set_compact_process_binding` hook can do this for you:

```python
@run_after('setup')
def set_binding(self):
    hooks.set_compact_process_binding(self)
```

For pure MPI codes, it will bind rank 0 to core 0, rank 1 to core 1, etc. For hybrid codes (MPI + OpenMP, or otherwise codes that do both multiprocessing and multithreading at the same time), it will bind to consecuitive sets of cores. E.g. if a single process uses 4 cores, it will bind rank 0 to cores 0-3, rank 1 to cores 4-7, etc. 

To impose this binding, the hook sets environment variables that should be respected by the parallel launcher used to launch your application. Check the [code](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) to see which parallel launchers are currently supported. The use of this hook is optional, but generally recommended for all multiprocessing codes.

For multithreading codes, there `set_compact_thread_binding` hook is an equivalent hook that can do thread binding, if supported multithreading frameworks are used (e.g. Intel or GNU OpenMP, see the [code](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/hooks.py) for all supported frameworks):

```python
@run_after('setup')
def set_binding(self):
    hooks.set_compact_thread_binding(self)
```

The use of this hook is optional but recommended in most cases. Note that thread binding can sometimes cause unwanted behaviour: even if e.g. 8 cores are allocated to the process and 8 threads are launched, we have seen codes that bind all those threads to a single core (e.g. core 0) when core binding is enabled. Please verify that enabling core binding does not introduce any unwanted binding behaviour for your code.

#### Defining OMP_NUM_THREADS (recommended)

The `set_omp_num_threads` hook sets the `$OMP_NUM_THREADS` environment variable based on the number of `cpus_per_task` defined in the ReFrame test (which in turn is typically set by the `assign_tasks_per_compute_unit` hook). For OpenMP codes, it is generally recommended to call this hook, to ensure they launch the correct amount of threads.



