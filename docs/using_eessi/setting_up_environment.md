# Setting up your environment

To set up the EESSI environment, simply run the command:

``` { .bash .copy }
source /cvmfs/pilot.eessi-hpc.org/latest/init/bash
```

This may take a while as data is downloaded from a Stratum 1 server which is
part of the CernVM-FS infrastructure to distribute files. You should see the
following output:

``` { .yaml .title="Output of source command" .no-copy }
Found EESSI pilot repo @ /cvmfs/pilot.eessi-hpc.org/versions/2021.12!
archspec says x86_64/intel/skylake_avx512 # (1)!
Using x86_64/intel/skylake_avx512 as software subdirectory.
Using /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/modules/all to $MODULEPATH...
Environment set up to use EESSI pilot software stack, have fun!
[EESSI pilot 2021.12] $ # (2)!
```

1.  What is reported here depends on the CPU architecture of the machine you are
    running the `source` command.
2.  This is the prompt indicating that you have access to the EESSI software
    stack.

The last line is the shell prompt.

:clap: Your environment is now set up, you are ready to start running software provided by EESSI!
