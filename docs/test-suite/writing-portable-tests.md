# Writing portable tests

This page is a tutorial on how to write a new test for the [EESSI test suite](https://github.com/EESSI/test-suite).

If you already know how to write regular ReFrame tests, we suggest you read the [High-level overview](#high-level-overview) and [Test requirements](#test-requirements) sections, then skip ahead to [Step 3: implementing as a portable ReFrame test](#as-portable-reframe-test).

## High-level overview

In this tutorial, you will learn how to write a test for the [EESSI test suite](https://www.eessi.io/docs/test-suite/). It is important to realize in which context the test suite will be run. Roughly speaking, there are three uses:

- Running tests for one (or a few) particular applications, as part of the [workflow of adding new software to EESSI](https://www.eessi.io/docs/adding_software/contribution_policy/#testing),  to validate the sanity of the (new) installation
- Regular (e.g. daily) runs, on a set of HPC clusters, to identify performance regressions
- By an end-user of EESSI, who runs either a specific test or the full test suite, to validate the functionality of EESSI (or a particular software in EESSI) on the end-user's system

The test suite will contain a combination of real-life use cases for end-user scientific software (e.g. tests for GROMACS, TensorFlow, CP2K, OpenFOAM, etc) and low level tests (e.g. OSU Microbenchmarks).

The tests in the EESSI test suite are developed using the [ReFrame HPC testing framework](https://reframe-hpc.readthedocs.io/en/stable/). Typically, ReFrame tests hardcode system specific information (core counts, performance references, etc) in the test definition. The EESSI test suite aims to be portable, and implements a series of standard [hooks](#REFERENCE_TO_HOOKS_API_DOCS) to replace information that is typically hardcoded. All system-specific information is then limited to the ReFrame configuration file. As an example: rather than hardcoding that a test should run with 128 tasks (i.e. because a system has 128 core nodes), the EESSI test suite has a hook that can define a test should be run on a "single, full node". The hook queries the ReFrame configuration file for the amount of cores per node, and specifies this number as the corresponding amount of tasks. Thus, on a 64-core node, this test would run with 64 tasks, while on a 128-core node, it would run 128 tasks.

## Test requirements

To be useful in the aforementioned scenarios, tests need to satisfy a number of requirements. 

- Tests are implemented in the [ReFrame HPC testing framework](https://reframe-hpc.readthedocs.io/en/stable/).
- Multiple test cases may be implemented for a single software package.
- Tests should run in a reasonable amount of time (less than 1 hour) for all the scales for which it is defined to be valid.
- There should be at least one light test case that can be run in less then ~5 minutes. This test should be marked with the 'CI' tag.
- Tests should only use a reasonable amount of memory, so that _most_ systems will be able to run them. For low core counts (1-4 cores), 8-16 GB is reasonable. For higher core counts, keeping a memory usage to less than 1 GB/core will ensure that _mosts_ systems will be able to run it.
- Tests should be portable, meaning they should not contain any system-specific information. If assumptions are made that might not be satisfied on every system (e.g. a test needs at least X cores to run), the test should check for it, and be skipped if the system does not satisfy the requirement.

## Step-by-step tutorial for writing a portable ReFrame test

In the next section, we will show how to write a test for the EESSI test suite by means of an example: we will create a test for [mpi4py](https://mpi4py.readthedocs.io/en/stable/) that executes an `MPI_REDUCE` to sum the ranks of all processes. If you're unfamiliar with MPI or `mpi4py`, or want to see the exact code this test will run, you may want to read [Background of the mpi4py test](#background-of-mpi4py-test) before proceeding. The complete test developed in this tutorial can be found in the `tutorials/mpi4py` directory in  of the [EESSI test suite](https://github.com/EESSI/test-suite/) repository.

### Step 1: writing job scripts to execute test
Although not strictly needed for the implementation of a ReFrame test, it is useful to try and write a job script for how you would want to run this test on a given system. For example, on a system with 128-core nodes, managed by SLURM, we might have the following job scripts to execute the `mpi4py_reduce.py` code.

To run on 2 cores:
```
#!/bin/bash
#SBATCH --ntasks=2  # 2 tasks, since 2 processes is the minimal size on which I can do a reduction
#SBATCH --cpus-per-task=1  # 1 core per task (this is a pure multiprocessing test, each process only uses 1 thread)
#SBATCH --time=5:00  # This test is very fast. It shouldn't need more than 5 minutes
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load mpi4py/3.1.5-gompi-2023b
mpirun -np 2 python3 mpi4py_reduce.py --n_iter 1000 --n_warmup 100
```
To run on one full node:
```
#!/bin/bash
#SBATCH --ntasks=128  # 2 tasks, since 2 processes is the minimal size on which I can do a reduction
#SBATCH --cpus-per-task=1  # 1 core per task (this is a pure multiprocessing test, each process only uses 1 thread)
#SBATCH --time=5:00  # This test is very fast. It shouldn't need more than 5 minutes
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load mpi4py/3.1.5-gompi-2023b
mpirun -np 128 python3 mpi4py_reduce.py --n_iter 1000 --n_warmup 100
```
To run on two full nodes
```
#!/bin/bash
#SBATCH --ntasks=256 # 2 tasks, since 2 processes is the minimal size on which I can do a reduction
#SBATCH --ntasks-per-node=128 
#SBATCH --cpus-per-task=1  # 1 core per task (this is a pure multiprocessing test, each process only uses 1 thread)
#SBATCH --time=5:00  # This test is very fast. It shouldn't need more than 5 minutes
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
module load mpi4py/3.1.5-gompi-2023b
mpirun -np 256 python3 mpi4py_reduce.py --n_iter 1000 --n_warmup 100
```

Clearly, such job scripts are not very portable: these only work on SLURM systems, we had to duplicate a lot to run on different scales, we would have to duplicate even more if we wanted to run test `mpi4py` versions, etc. This is where `ReFrame` comes in: it has support for different schedulers, and allows one to easily specify a range of parameters (such as the number of tasks in the above example) to create tests for.

### Step 2: implementing as a non-portable ReFrame test
First, let us implement this as a non-portable test in ReFrame. This code can be found under `tutorials/mpi4py/mpi4py_system_specific.py` in the [EESSI test suite](https://github.com/EESSI/test-suite/) repository. We will not elaborate on how to write ReFrame tests, it is well-documented in the official [ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/index.html). We have put extensive comments in the test definition below, to make it easier to understand when you have limited familiarity with ReFrame. Whenever the variables below have a specific meaning in ReFrame, we referenced the official documentation:

```python
"""
This module tests mpi4py's MPI_Reduce call
"""

import reframe as rfm
import reframe.utility.sanity as sn

from reframe.core.builtins import variable, parameter, run_after  # added only to make the linter happy

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
    valid_systems = ['my_cluster']

    # ReFrame will generate a test for each value of a parameter, in this case each module name
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.parameter
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.modules
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
        # Set the number of tasks per node to either be equal to the number of tasks, but at most 128, since we have 128-core nodes
        # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.num_tasks_per_node
        self.num_tasks_per_node = min(self.num_tasks, 128)

    # Now, we check if the pattern 'Sum of all ranks: X' with X the correct sum for the amount of ranks is found
    # in the standard output:
    # https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.builtins.sanity_function
    @sanity_function
    def validate(self):
        # Sum of 0, ..., N-1 is (N * (N-1) / 2)
        sum_of_ranks = round(self.num_tasks * ((self.num_tasks-1) / 2))
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

This test _works_, but is _not_ very portable. If we move to a system with 192 cores per node, the current `scale` parameter is a bit awkward. The test would still run, but we wouldn't have a test instance that just tests this on a full (single) node or a full two nodes. Furthermore, if we add a new `mpi4py` module in EESSI, we would have to alter the test to add the name to the list, since the module names are hardcoded in this test.

### Step 3: implementing as a portable ReFrame test { #as-portable-reframe-test }

In the previous section, there were several system-specific items in the test. In this section, we will show how we use the EESSI hooks to avoid hard-coding system specific information. We do this by replacing the system-specific parts of the test from Step 2 bit by bit. The full final test can be found under `tutorials/mpi4py/mpi4py_portable.py` in the [EESSI test suite](https://github.com/EESSI/test-suite/) repository.

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

the `SCALES` constant (TODO: API reference) contains a set of default scales at which we run all tests. For our `mpi4py` example, that is sufficient. 

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
from eessi.testsuite.constants import SCALES, COMPUTE_UNIT, CPU
    ...
    @run_after('init')
    def run_after_init(self):
        hooks.set_tag_scale(self)
        
    @run_after('setup')
    def set_num_tasks_per_node(self):
        """ Setting number of tasks per node and cpus per task in this function. This function sets num_cpus_per_task
        for 1 node and 2 node options where the request is for full nodes."""
        hooks.assign_tasks_per_compute_unit(self, COMPUTE_UNIT[CPU])
```

The first hook ([set_tag_scale](TODO: API reference)) sets a number of custom attributes for the current test, based on the scale (`self.num_nodes`, `self.default_num_cpus_per_node`, `self.default_num_gpus_per_node`, `self.node_part`). These are not used by ReFrame, but can be used by later hooks from the EESSI test suite. It also sets a ReFrame `tag` for convenience. These are useful for quick test selection, e.g. by running ReFrame with `--tag 1_node` one would only run the tests generated for the scale `1_node`. Calling this hook is mandatory for all tests, as it will ensure standardization of tag names based on the scales.

The second hook, `assign_tasks_per_compute_unit`, is used to set the task count. This hook sets the `self.num_tasks` and `self.num_tasks_per_node` we hardcoded before. In addition, it sets the `self.num_cpus_per_task`. In this case, we call it with the `COMPUTE_UNIT[CPU]` argument, which means one task will be launched per (physical) CPU available. Thus, for the `1_node` scale, this would run the `mpi4py` test with 128 tasks on a 128-core node, and with 192 tasks on a 192-core node. Check the [API reference](TODO) for other valid `COMPUTE_UNIT`'s.

#### Replacing hard-coded module names (mandatory)

If we write an `mpi4py` test, we typically want to run this for _all_ `mpi4py` modules that are currently on our `$MODULEPATH`. We do that by replacing

```python
    module_name = parameter(['mpi4py/3.1.4-gompi-2023a', 'mpi4py/3.1.5-gompi-2023b'])
```

by

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

This hook assumes that `self.module_name` has been set, but has the added advantage that a user running the EESSI test suite can overwrite the modules to load from the command line when running ReFrame (see [Overriding test parameters](https://www.eessi.io/docs/test-suite/usage/#overriding-test-parameters-advanced)).

#### Replacing hard-coded valid_systems (mandatory)

The `valid_systems` attribute is a mandatory attribute to specify in a ReFrame test. However, we can set it to match any system:

```python
valid_systems = [*]
```

Normally, `valid_systems` is used as a way of guaranteeing that a system has the necessary properties to run the test. E.g. if we know that `my_gpu_system` has NVIDIA GPUs, and I have a test written for NVIDIA GPUs. I would specify `valid_systems['my_gpu_system']` for that test. This, however, is a surrogate for declaring what my test _needs_: I'm saying it needs `my_gpu_system`, while in fact I could make the more general statement 'this test needs NVIDIA GPUs'.

To keep the test system-agnostic we _can_ declare what the test needs by using ReFrame's concept of partition `features` (a string) and/or `extras` (a key-value pair) [see valid_systems documentation](https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.valid_systems). E.g. a test could declare it _needs_ the `gpu` feature. Such a test will only be created by ReFrame for partitions that declare (in the ReFrame configuration file) that they have the `gpu` feature.

Since `features` and `extras` are full text fields, we standardize those in the EESSI test suite in the `eessi/testsuite/constants.py` file. For example, tests that require an NVIDIA GPU could specify

```python
from eessi.testsuite.constants import FEATURES, GPU, GPU_VENDOR, GPU_VENDORS, NVIDIA
...
valid_systems = f'+{FEATURES[GPU]} %{GPU_VENDOR}={GPU_VENDORS[NVIDIA]}'
```

which will make sure that a test instance is only generated for partitions in the ReFrame configuration file that specify that they _have_ the corresponding feature and extras:

```python
from eessi.testsuite.constants import FEATURES, GPU, GPU_VENDOR, GPU_VENDORS, NVIDIA
...
'features': [
     FEATURES[GPU],
],
'extras': {
    GPU_VENDOR: GPU_VENDORS[NVIDIA],
},
```

In practice, one will rarely hard-code this `valid_systems` string. Instead, we have a hook [filter_valid_systems_by_device_type](TODO API REF). It does the above, and a bit more: it also checks if the module that the test is generated for is CUDA-enabled (in case of a test for `NVIDIA` GPUs), and _only then_ will it generate a GPU-based test. Calling this hook is mandatory for all tests (even if just to declare they need a CPU to run).

Another aspect is that not all systems may be able to run tests of all of the standard `SCALES`. Thus, a test can also declare it needs a certain _scale_. I.e. a test for the `16_nodes` scale clearly needs a partition with at least 16 nodes. This is taken care of by the [filter_supported_scales](TODO API REF) hook. Calling this hook is also mandatory for all tests.

There may be other hooks that facilitate valid system selection for your tests, but please check the [API documentation](TODO: INSERT REFERENCE TO API DOCS) for a full list.

#### Requesting sufficient memory (mandatory)

When developing the test, we don't know how much memory the node will have on which it will run. However, we _do_ know how much our application _needs_.

We can declare this need using the `req_memory_per_node` hook. This hook is mandatory for all tests. If you are on a system with a scheduler that runs jobs within a cgroup, getting the memory consumption is easy. You can (temporarily) add the following to the class body of your test:

```python
   # Temporarily define postrun_cmds to make it easy to find out memory usage
    postrun_cmds = ['MAX_MEM_IN_BYTES=$(cat /sys/fs/cgroup/memory/$(</proc/self/cpuset)/memory.max_usage_in_bytes)', 'echo "MAX_MEM_IN_MIB=$(($MAX_MEM_IN_BYTES/1048576))"']
```

And define an additional `performance_function`:

```python
    @performance_function('MiB')
    def max_mem_in_mib(self):
        return sn.extractsingle(r'^MAX_MEM_IN_MIB=(?P<perf>\S+)', self.stdout, 'perf', int)
```

This results in the following output on 192-core nodes (we've omitted some output for readability):

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

We now have a pretty good idea how the memory per node scales: for our smallest process counts (1 core), it's about 200 MiB per process, while for our largest process counts (16 nodes, 16*192 processes), it's 22018 MiB per node (or about 115 MiB per process). If we wanted to do really well, we could define a linear function (with offset) and fit it through the data (and round up to be on the safe side, i.e. make sure there is _enough_ memory). Then, we could call the hook like this:

```python
@run_after('setup')
def request_mem(self):
    mem_required = self.num_tasks_per_node * mem_slope + mem_intercept
    hooks.req_memory_per_node(self, app_mem_req=mem_required)
```

In this case, however, the memory consumption is so low per process that we won't go through that effort, and simply request 256 MiB per task that is launched on a node. Thus, we call our hook using:

```python
@run_after('setup')
def request_mem(self):
    mem_required = self.num_tasks_per_node * 256
    hooks.req_memory_per_node(self, app_mem_req=mem_required)
```
Note that requesting too high an amount of memory means the test will be skipped on nodes that cannot meet that requirement (even if they might have been able to run it without _actually_ running out of memory). Requesting too little will risk nodes running out of memory while running the test. Note that many HPC systems have an amount memory of around 1-2 GB/core. It's good to ensure (if you can) that the memory requests for all valid `SCALES` for your test do not exceed the total amount of memory available on typical nodes.

#### Requesting task and/or process binding (optional)

Binding processes to a set of cores prevents the OS from migrating such processes to other cores. Especially on multi-socket systems, process migration can cause performance hits, especially if a process is moved to a CPU core on the other socket. Since this is controlled by the OS, and dependent on what other processes are running on the node, it may cause unpredictable performance: in some runs, processes might be migrated, while in others, they aren't.

Thus, it is typically better for reproducibility to bind processes to their respective set of cores. The `set_compact_process_binding` hook can do this for you:

```python
@run_after('setup')
def set_binding(self):
    hooks.set_compact_process_binding(self)
```

For pure MPI codes, it will bind rank 0 to core 0, rank 1 to core 1, etc. For hybrid codes (MPI + OpenMP, or otherwise codes that do both multiprocessing and multithreading at the same time), it will bind to consecuitive sets of cores. E.g. if a single process uses 4 cores, it will bind rank 0 to cores 0-3, rank 1 to cores 4-7, etc. 

To impose this binding, the hook sets environment variables that should be respected by the parallel launcher used to launch your application. Check the [TODO: API Documentation] to see which parallel launchers are currently supported. The use of this hook is optional, but generally recommended for all multiprocessing codes.

For multithreading codes, there `set_compact_thread_binding` hook is an equivalent hook that can do thread binding, if supported multithreading frameworks are used (e.g. Intel or GNU OpenMP, see the [TODO API documentation] for all supported frameworks):

```python
@run_after('setup')
def set_binding(self):
    hooks.set_compact_thread_binding(self)
```

The use of this hook is optional. Note that thread binding can sometimes cause unwanted behaviour: even if e.g. 8 cores are allocated to the process and 8 threads are launched, we have seen codes that bind all those threads to a single core (e.g. core 0) when core binding is enabled. Please verify that enabling core binding does not introduce any unwanted binding behaviour for your code.

#### Defining OMP_NUM_THREADS (optional)

The `set_omp_num_threads` hook sets the `OMP_NUM_THREADS` environment variable based on the number of `cpus_per_task` defined in the ReFrame test (which in turn is typically set by the `assign_tasks_per_compute_unit` hook). For OpenMP codes, it is generally recommended to call this hook, to ensure they launch the correct amount of threads.

### Skipping tests instances when required (optional)
Preferably, we prevent test instances from being generated (i.e. before ReFrame's `setup` phase) if we know that they cannot run on a certain system. However, sometimes we need information on the nodes that will run it, which is only available _after_ the `setup` phase. That is the case for anything where we need information from e.g. the [reframe.core.pipeline.RegressionTest.current_partition](https://reframe-hpc.readthedocs.io/en/stable/regression_test_api.html#reframe.core.pipeline.RegressionTest.current_partition). The `assign_tasks_per_compute_unit` hook for example needs uses this property to get the core count of a node, and thus needs to be executed after the `setup` phase.

For example, we might know that a test case only scales to around 300 tasks, and above that, execution time increases rapidly. In that case, we'd want to skip any test instance that results in a larger amount of tasks, but we only know this after `assign_tasks_per_compute_unit` has been called. E.g. the `2_nodes` scale would run fine on systems with 128 cores per node, but would exceed the task limit of 300 on systems with `192` cores per node.

We can skip any generated test instances using the `skip_if` function. E.g. to skip the test if the total task count exceeds 300, we'd need to call `skip_if` _after_ the task count has been set by `assign_tasks_per_compute_unit`:

```python
@run_after('setup')
    hooks.assign_tasks_per_compute_unit(test=self, compute_unit=COMPUTE_UNIT[CPU])

    max_tasks = 300
    self.skip_if(self.num_tasks > max_tasks,
                 f'Skipping test: more than {max_tasks} tasks are requested ({self.num_tasks})')
```

The `mpi4py` scales almost indefinitely, but if we were to set it for the sake of this example, one would see:
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

### Background of the mpi4py test { #background-of-mpi4py-test }
To understand what this test does, you need to know some basics of MPI. If you know about MPI, you can skip this section.

The MPI standard defines how to communicate between multiple processes that work on a common computational task. Each process that is part of the computational task gets a unique identifier (0 to N-1 for N processes), the MPI rank, which can e.g. be used to distribute a workload. The MPI standard defines communication between two given processes (so-called point-to-point communication), but also between a set of N processes (so-called collective communication).

An example of such a collective operation is the [MPI_REDUCE](https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report/node130.htm#Node130) call. It reduces data elements from multiple processes with a certain operation, e.g. it takes the sum of all elements or multiplication of all elements.

#### The mpi4py test
In this example, we will implement a test that does an `MPI_Reduce` on the rank, using the sum operation. This makes it easy to validate the result, as we know that for N processes, the theoretical sum of all ranks (0, 1, ... N-1) is `(N * (N-1) / 2)`.

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
    total = MPI.COMM_WORLD.reduce(rank)

# Actual reduction, multiple iterations for accuracy of timing
t1 = time.time()
for i in range(n_iter):
    total = MPI.COMM_WORLD.reduce(rank)
t2 = time.time()
total_time = (t2 - t1) / n_iter

if rank == 0:
    print(f"Total ranks: {size}")
    print(f"Sum of all ranks: {total}")  # Should be (size * (size-1) / 2)
    print(f"Time elapsed: {total_time:.3e}")
```

Assuming we have `mpi4py` available, we could run this manually using
```
$ mpirun -np 4 python3 mpi4py_reduce.py
Total ranks: 4
Sum of all ranks: 6
Time elapsed: 3.609e-06
```

This started 4 processes, with ranks 0, 1, 2, 3, and then summed all the ranks (`0+1+2+3=6`) on the process with rank 0, which finally printed all this output. The whole reduction operation is performed `n_iter` times, so that we get a more accurate timing.
