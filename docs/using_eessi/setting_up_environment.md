# Setting up your environment
In Unix-like systems, _environment variables_ are used to configure the environment in which applications and scripts
run. To set up EESSI, you need to configure a specific set of environment variables so that your operating system is
aware that EESSI exists and is to be used. We have prepared a few automated approaches that do this for you: you can
either load an EESSI [environment module](https://lmod.readthedocs.io/en/latest/#overview) or `source` an
initialisation script for `bash`.

With any of the approaches below, the **first** time you use them they may seem to take a while as any necessary data
is downloaded in the background from a Stratum 1 server (which is part of the CernVM-FS infrastructure used to
distribute files for EESSI).

## Loading an EESSI environment module

There are a few different scenarios where you may want to set up the EESSI environment by loading an EESSI
_environment module_. The simplest scenario is one where you do not already have a environment module tool on your
system, in this case we configure the [Lmod module tool](https://lmod.readthedocs.io/en/latest/#) shipped with EESSI
and automatically load the EESSI environment module:
``` { .bash .copy }
source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
```
This command configures Lmod for your system and automatically loads the `EESSI` module so that EESSI is immediately
available to use. If you would like to see what environment variables the module sets, you can use `module show EESSI`.

:clap: Your environment is now set up, you are ready to start running software provided by EESSI!

??? tip "What if I don't use a `bash` shell?"

    The example above is shown for a `bash` shell but the environment module approach supports all the shells that Lmod
    itself supports (`bash`, `csh`, `fish`, `ksh`, `zsh`):
    ``` { .bash .copy }
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
    ```
    ``` { .csh .copy }
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/csh
    ```
    ``` { .fish .copy }
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/fish
    ```
    ``` { .ksh .copy }
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/ksh
    ```
    ``` { .zsh .copy }
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/zsh
    ```
    

??? tip "What if I already have Lmod installed or another module tool is available on the system?"

    You can check if the module command is already defined for your system and what version it has with
    ``` { .bash .copy }
    command -v module && module --version
    ```

    1.  If you are already using Lmod (modules based on Lua) with version >= 8.6:

        In this case, we _recommend_ resetting `$MODULEPATH`, because EESSI is not designed to mix modules coming from
        EESSI and from your system.

        ``` { .bash .copy }
        module unuse $MODULEPATH
        module use /cvmfs/software.eessi.io/init/modules
        module load EESSI/2023.06
        ```

        :clap: Your environment is now set up, you are ready to start running software provided by EESSI!

    2.  If you are using an Lmod with a version older than 8.6 or any other module tool utilizing `MODULEPATH` (e.g., 
        [Tcl-based Environment Modules](https://modules.sourceforge.net/)):

        It is recommended to unset `$MODULEPATH` to prevent Lmod from attempting to build a cache for your module tree
        (as this can be very slow if you have a lot of modules). Again, unsetting the `$MODULEPATH` should be
        considered as a good idea in general so you do not mix local and EESSI modules. You then will need to
        initialise a compatible version of Lmod, for example the one shipped with EESSI: 

        ``` { .bash .copy }
        unset MODULEPATH
        source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
        ```

        :clap: Your environment is now set up, you are ready to start running software provided by EESSI!
    
    !!! note "Why do we recommend to unset `MODULEPATH`?"

        Unsetting the `$MODULEPATH` environment variable, which tells Lmod in which directories environment module
        files are available, may be necessary. The underlying reason to suggest this is that EESSI and your system are
        most likely based on two different operating system distributions - EESSI uses it's
        [compatibility layer](../compatibility_layer.md "EESSI compatibility layer"), your system almost certainly uses
        some other Linux distribution. If you can find a way to ensure that the _software stacks_ from your site and
        EESSI do not mix (in particular when someone is building new software!), then this should be good enough.
    

## Sourcing the EESSI `bash` initialisation script

!!! warning "This is supported exclusively for `bash` shell users. If you're using a different shell, please use [the alternative approach](#loading-an-eessi-environment-module)"

    You can to see what your current shell is with the command `echo $SHELL`

You can initialise EESSI (in a non-reversible way) by running the command:

``` { .bash .copy }
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
```

You should see the following output:

``` { .bash .no-copy }
Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
archdetect says x86_64/amd/zen2  # (1)
archdetect could not detect any accelerators
Using x86_64/amd/zen2 as software subdirectory.
Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/lmodrc.lua
Found Lmod SitePackage.lua file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/SitePackage.lua
Using /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/amd/zen2 as the site extension directory for installations.
Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all as the directory to be added to MODULEPATH.
Using /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/amd/zen2/modules/all as the site extension directory to be added to MODULEPATH.
Found libcurl CAs file at RHEL location, setting CURL_CA_BUNDLE
Initializing Lmod...
Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Prepending site path /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Environment set up to use EESSI (2023.06), have fun!
{EESSI 2023.06} [user@system ~]$  # (2)!
```

What is reported at `(1)` depends on the CPU architecture of the machine you are running the `source` command.

At `(2)` is the prompt indicating that you have access to the EESSI software stack.

:clap: Your environment is now set up, you are ready to start running software provided by EESSI!

## Overriding the CPU or accelerator architecture

EESSI uses the custom bash script
[`eessi_archdetect.sh`](https://github.com/EESSI/software-layer-scripts/blob/main/init/eessi_archdetect.sh) to detect
the CPU and accelerator architectures of the host system.

This script listens to some environment variables that allow you to override the results it returns. If you set these
environment variables _before an EESSI version has been initialised_, you can thereby change the architecture target
of the software stack. 

### Overriding the CPU architecture

By default, [`eessi_archdetect.sh`](https://github.com/EESSI/software-layer-scripts/blob/main/init/eessi_archdetect.sh)
will return a best match between your system and the architectures it is aware of:
```bash
# Executed on an icelake system
$ ./eessi_archdetect.sh cpupath
x86_64/intel/icelake
```
(you can add a `-d` option to see debug output from the script).

It is also possible to list all the architectures that are compatible with your system:
```bash
# Executed on an icelake system
$ ./eessi_archdetect.sh -a cpupath
x86_64/intel/icelake:x86_64/intel/cascadelake:x86_64/intel/skylake_avx512:x86_64/intel/haswell:x86_64/generic
```

To override the returned CPU architecture, you can set the environment variable `EESSI_SOFTWARE_SUBDIR_OVERRIDE` to a
specific (expected) value:
```bash
export EESSI_SOFTWARE_SUBDIR_OVERRIDE="x86_64/intel/haswell"
# Executed on an icelake system
$ ./eessi_archdetect.sh cpupath
x86_64/intel/haswell
```
Note that the override value is not sanity checked, the end user is responsible for providing a valid value.

### Overriding the accelerator architecture

In a similar manner as for the CPU, you can override the accelerator detection of
[`eessi_archdetect.sh`](https://github.com/EESSI/software-layer-scripts/blob/main/init/eessi_archdetect.sh) with
`EESSI_ACCELERATOR_TARGET_OVERRIDE`:
```bash
$ export EESSI_ACCELERATOR_TARGET_OVERRIDE=accel/nvidia/cc70
# Executed on an icelake system with no GPU
$ ./eessi_archdetect.sh accelpath
accel/nvidia/cc70
```

To show the impact of this:
```bash
$ module av

--------------------------------------------------- /cvmfs/software.eessi.io/versions/2023.06/init/modules ---------------------------------------------------
   EESSI/2023.06

# ...

$ export EESSI_ACCELERATOR_TARGET_OVERRIDE=accel/nvidia/cc70
$ module load EESSI/2023.06
Module for EESSI/2023.06 loaded successfully

$ module av

------------------------ /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/icelake/accel/nvidia/cc70/modules/all -------------------------
   CUDA-Samples/12.1-GCC-12.3.0-CUDA-12.1.1 (g)      OSU-Micro-Benchmarks/7.2-gompi-2023a-CUDA-12.1.1 (g)
   CUDA/12.1.1                                       OSU-Micro-Benchmarks/7.5-gompi-2023b-CUDA-12.4.0 (g,D)
   CUDA/12.4.0                              (D)      UCC-CUDA/1.2.0-GCCcore-12.3.0-CUDA-12.1.1        (g)
   cuDNN/8.9.2.26-CUDA-12.1.1               (g)      UCC-CUDA/1.2.0-GCCcore-13.2.0-CUDA-12.4.0        (g,D)
   NCCL/2.18.3-GCCcore-12.3.0-CUDA-12.1.1   (g)      UCX-CUDA/1.14.1-GCCcore-12.3.0-CUDA-12.1.1       (g)
   NCCL/2.20.5-GCCcore-13.2.0-CUDA-12.4.0   (g,D)    UCX-CUDA/1.15.0-GCCcore-13.2.0-CUDA-12.4.0       (g,D)

--------------------------------- /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/icelake/modules/all ----------------------------------
   Abseil/20230125.2-GCCcore-12.2.0                   HDF/4.2.15-GCCcore-12.2.0                           OpenMPI/4.1.5-GCC-12.3.0

# ...
```

??? tip "Environment variables to consider while initializing EESSI"

    ### OVERRIDING variables

    | Environment variables | Description |
    |-----------------------|------------------------|
    | `EESSI_CVMFS_REPO_OVERRIDE` | Overrides the default CVMFS repository path (e.g. /cvmfs/software.eessi.io) used by init. |
    | `EESSI_VERSION_OVERRIDE` | Overrides the default EESSI version subdirectory (e.g. 2023.06) selected by init. |
    | `EESSI_SOFTWARE_SUBDIR_OVERRIDE` | Overrides detected CPU software subdir (e.g. linux/x86_64/intel/icelake) for the main stack. |
    | `EESSI_ACCELERATOR_TARGET_OVERRIDE` | Overrides detected accelerator target (e.g. accel/nvidia/cc70) regardless of local hardware. |
    | `EESSI_ARCHDETECT_OPTIONS_OVERRIDE` | Replaces any built-in archdetect options with the provided value. |

    ### Source-based Initialization

    | Environment variable | Description |
    |-----------------------|------------------------|
    | `EESSI_BASIC_ENV` | When set to 1, performs a minimal init only exporting essential  variables. |
    | `EESSI_SILENT` | When set to 1, suppresses non-error output during source-based init; errors still print. |
    | `EESSI_USE_ARCHDETECT` | When set to 0, disables automatic architecture detection using archdetect; otherwise detection is performed. |

    ### Module-based Initialization

    | Environment variable | Description |
    |-----------------------|------------------------|
    | `EESSI_DEBUG_INIT` | When set to 1, enables verbose debug output from init scripts to trace decisions and paths. |
    | `LMOD_SYSTEM_DEFAULT_MODULES` | List of modules Lmod auto-loads on shell start; can include EESSI/2023.06 to auto-enable. |
    | `EESSI_MODULE_FAMILY_NAME` | Name of the family applied to the EESSI module (default EESSI); affects family conflicts. |
    | `EESSI_MODULE_STICKY` | When set to 1, enables sticky behavior of the EESSI module. |


??? tip "The accelerator modules are visible but I can't load them"

    Do note that just because the accelerator modules are now visible doesn't mean you will be able to load them. EESSI
    has an additional check to ensure that the accelerator **drivers** are available since without access to the
    drivers any software typically cannot execute anyway. If you need to allow loading of the modules (for example
    because you wish to prepare the job execution environment from a login node where the accelerator is not
    available) you can set yet another environment variable `EESSI_OVERRIDE_GPU_CHECK=1`.

??? tip "I want to choose a different CPU architecture for the accelerator software"

    It is even possible to use a different CPU architecture for the accelerator software stack by setting the
    environment variable `EESSI_ACCEL_SOFTWARE_SUBDIR_OVERRIDE`. This environment variable is not listened to
    by the detection script, but does affect how EESSI is initialised.

    The use case for this scenario is expected to be extremely rare and is only tested for the relatively trivial
    context of making available and loading the software application modules for the specific architecture
    combination.
