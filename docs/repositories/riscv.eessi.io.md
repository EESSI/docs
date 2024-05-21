# EESSI RISC-V development repository (`riscv.eessi.io`)

This repository contains development versions of an EESSI RISC-V software stack.
Note that versions may be added, modified, or deleted at any time.

## Accessing the RISC-V repository

See [Getting access](../getting_access/is_eessi_accessible.md);
by making the EESSI CVMFS domain available, you will automatically have access to `riscv.eessi.io` as well.

## Using `riscv.eessi.io`

This repository currently offers one version (20240402), and this contains both a compatibility layer and a software layer.
Furthermore, initialization scripts are in place to set up the repository:


``` { .bash .copy }
$ source /cvmfs/riscv.eessi.io/versions/20240402/init/bash
Found EESSI repo @ /cvmfs/riscv.eessi.io/versions/20240402!
archdetect says riscv64/generic
Using riscv64/generic as software subdirectory.
Found Lmod configuration file at /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/.lmod/lmodrc.lua
Found Lmod SitePackage.lua file at /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/.lmod/SitePackage.lua
Using /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/modules/all as the directory to be added to MODULEPATH.
Initializing Lmod...
Prepending /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/modules/all to $MODULEPATH...
Environment set up to use EESSI (20240402), have fun!
{EESSI 20240402} $
```

Note that we currently only provide generic builds, hence `riscv64/generic` is being used for all RISC-V CPUs.

The amount of software is constantly increasing.
Besides having the `foss/2023b` toolchain available, applications like dlb, GROMACS, OSU Micro-Benchmarks, and R are already available as well.
Use `module avail` to get a full and up-to-date listing of available software.


## Infrastructure status

The status of the CernVM-FS infrastructure for this repository is shown at [https://status.eessi.io](https://status.eessi.io/).
