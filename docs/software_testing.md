#Software testing

**WARNING: development of the software test suite has only just started and is a work in progress. This page describes how the test suite _will_ be designed, but not everything is implemented yet and the design may still change.**

##Description of the software test suite

###Framework
The EESSI project uses the [ReFrame framework](https://reframe-hpc.readthedocs.io/en/stable/index.html) for sofware testing. ReFrame is designed particularly for testing HPC software and thus has well integrated support for interacting with schedulers, as well as various launchers for MPI programs.

###Test variants
The EESSI software stack can be used in various ways, e.g. by using the [container](../pilot/#accessing-the-eessi-pilot-repository-through-singularity) or when the CVMFS software stack is mounted natively. This means the commands that need to be run to test an application are different in both cases. Similarly, systems may have different hardware (CPUs v.s. GPUs, system size, etc). Thus, tests - e.g. a GROMACS test - may have different variants: one designed to run on CPUs, one on GPUs, one designed to run through the container, etc.

The main goal of the EESSI test suite is to test the software stack on systems that have the EESSI CVMFS mounted natively. Some tests may also have variants that can run the same test through the container, but note that this setup is technically much more difficult. Thus, the main focus is on tests that run with a native CVMFS mount of the EESSI stack.

By default, ReFrame runs all test variants it find. Thus, in our test suite, we prespecify a number of tags that can be used to select an appropriate subset of tests for your system. We recognize the following tags:

- container: tests that use the EESSI container to run the software. E.g. one variant of our GROMACS test uses `singularity exec` to launch the EESSI container, load the GROMACS module, and run the GROMACS test. 
- `native`: tests that rely on the EESSI software stack being available through the modules system. E.g. one variant of the GROMACS test loads the GROMACS module and runs the GROMACS test.
- `singlecore`: tests designed to run on a single core
- `singlenode`: tests designed to run on a single (multicore) node (note: may still use MPI for multiprocessing)
- `small`: tests designed to run on 2-8 nodes.
- `large`: tests designed to run on >9 nodes.
- `cpu`: test designed to run on CPU.
- `gpu`, gpu_nvidia, gpu_amd: test designed to run on GPUs / nvidia GPUs / AMD GPUs.

##How to run the test suite

### General requirements

- A copy of the `tests` directory from [software repository](https://github.com/EESSI/software-layer)

### Requirements for container-based tests
Specifically for container-based tests, there are some requirements on the host system:

- An installation of ReFrame
- An MPI installation (to launch MPI tests) or PMIx-based launcher (e.g. SLURM compiled with PMIx support)
- Singularity

The container based tests will use a so-called shared alien CVMFS cache to store temporary data. In addition, they use a local CVMFS cache for speed. For this reason, the container tests need to be pointed to one directory that is shared between nodes on your system, and one directory that is node-specific (preferably a local disk). The `shared_alien_cache_minimal.sh` script that is part of the test suite defines these, and sets up the correct CVMFS configuration. You will have to adapt the `SHAREDSPACE` and `LOCALSPACE` variables in that script for your system, and point them to a shared and node-local directory.

### Setting up a ReFrame configuration file
Once the prerequisites have been met, you'll need to create a ReFrame configuration file that matches your system (see the [ReFrame documentation](https://reframe-hpc.readthedocs.io/en/stable/configure.html)). If you want to use the container-based tests, you *have* to define a partition programming environment called `container` and make sure it loads any modules needed to provide the MPI installation and singularity command. For an example configuration file, check the `tests/reframe/config/settings.py` in the [software-layer repository](https://github.com/EESSI/software-layer). Other than (potential) adaptations to the `container` environment, you should only really need to change the `systems` part.

### Adapting the tests to your system
For now, you will have to adapt the number of tasks specified in full-node tests to match the number of cores your machine has in a single node (in the future, you should be able to do this through the reframe configuration file). To do so, change all `self.num_tasks_per_node` you find in the various tests to that core count (unless they are 1, in which case the test specifically intended for only 1 process per node).


### An example run
In this example, we assume your current directory is the `tests/reframe` folder. To list e.g. all single node, cpu-based application tests on a system that has the EESSI software environment available natively, you execute:
```
reframe --config-file=config/settings.py --checkpath eessi-checks/applications/ -l -t native -t single -t cpu
```
(assuming you adapted the config file in `config/settings.py` for your system). This should list the tests that are selected based on the provided tags. To run the tests, change the `-l` argument into a `-r`:
```
reframe --config-file=config/settings.py --checkpath eessi-checks/applications/ -l -t native -t single -t cpu --performance-report
```
To run the same tests with using the EESSI container, run:
```
reframe --config-file=config/settings.py --checkpath eessi-checks/applications/ -l -t container -t single -t cpu --performance-report
```
Note that not all tests necessarily have implementations to run using the EESSI container: the primary focus of the test suite is for HPC sites to check the performance of their software suite. Such sites should have CVMFS mounted natively for optimal performance anyway.
