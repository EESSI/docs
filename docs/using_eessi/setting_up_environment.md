# Setting up your environment

To set up the EESSI environment, you can either load an EESSI module with Lmod or source a bash initialisation script.

## Loading an EESSI module with Lmod

There are a few different scenarios where you may want to set up the EESSI environment by loading an EESSI module with Lmod:

1.  You are already using Lmod with version >= 8.6

    In this case, we recommend unsetting the `MODULEPATH`, because EESSI is not designed to mix modules coming from EESSI and from your system.
    The underlying reason is that very likely EESSI and your system are based on two different operating system distributions - EESSI uses Gentoo, your system likely uses some other distribution. Note, unsetting `MODULEPATH` may not be possible at some sites, and some compromise may be necessary:

    ``` { .bash .copy }
    unset MODULEPATH
    export MODULEPATH=/cvmfs/software.eessi.io/init/modules
    module load EESSI/2023.06
    ```

    :clap: Your environment is now set up, you are ready to start running software provided by EESSI!

2.  You are using an Lmod with a version older than 8.6 or any other tool utilizing `MODULEPATH` (Tmod, etc.)

    You should unset MODULEPATH to prevent Lmod from attempting to build a cache for your module tree (as this can be very slow if you have
    a lot of modules). Again, unsetting the MODULEPATH should be considered as a good idea in general so you do not mix local and EESSI
    modules: 

    ``` { .bash .copy }
    unset MODULEPATH
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
    ```

    :clap: Your environment is now set up, you are ready to start running software provided by EESSI!

3.  Should Lmod be unavailable and `MODULEPATH` not utilized, you can initialise EESSI via an Lmod module by directly sourcing the Lmod initialisation script (this script automatically loads the EESSI module):

    ``` { .bash .copy }
    source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
    ```

    :clap: Your environment is now set up, you are ready to start running software provided by EESSI!

## Sourcing the EESSI `bash` initialisation script

You can initialise EESSI (in a non-reversible way) by running the command:

``` { .bash .copy }
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
```

This may take a while as data is downloaded from a Stratum 1 server which is
part of the CernVM-FS infrastructure to distribute files. You should see the
following output:

``` { .bash .no-copy }
Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
archdetect says x86_64/amd/zen2  # (1)
Using x86_64/amd/zen2 as software subdirectory.
Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Environment set up to use EESSI (2023.06), have fun!
{EESSI 2023.06} [user@system ~]$  # (2)!
```

What is reported at `(1)` depends on the CPU architecture of the machine you are running the `source` command.

At `(2)` is the prompt indicating that you have access to the EESSI software stack.

:clap: Your environment is now set up, you are ready to start running software provided by EESSI!
