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
