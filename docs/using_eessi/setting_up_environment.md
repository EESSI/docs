# Setting up your environment

To set up the EESSI environment, simply run the command:

``` { .bash .copy }
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
```

This may take a while as data is downloaded from a Stratum 1 server which is
part of the CernVM-FS infrastructure to distribute files. You should see the
following output:

``` { .yaml .no-copy }
Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
archdetect says x86_64/amd/zen2
Using x86_64/amd/zen2 as software subdirectory.
Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Environment set up to use EESSI (2023.06), have fun!
{EESSI 2023.06} [user@system ~]$ # (2)!
```

1.  What is reported here depends on the CPU architecture of the machine you are
    running the `source` command.
2.  This is the prompt indicating that you have access to the EESSI software
    stack.

The last line is the shell prompt.

:clap: Your environment is now set up, you are ready to start running software provided by EESSI!
