# EESSI RISC-V development repository (`riscv.eessi.io`)

!!! note "Is `riscv.eessi.io` a webpage?"
    If you landed on this page because you typed `riscv.eessi.io` into your browser, then
    you may not know yet that this is not a URL/webpage but a [CernVM-FS repository](../filesystem_layer.md)
    that EESSI uses to distribute software.
 
    **See the [EESSI overview page](../overview.md) for a general introduction to EESSI.**

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

You can even source the initialization script of the [`software.eessi.io` production repository](software.eessi.io.md) now,
and it will automatically set up the RISC-V repository for you:
``` { .bash .copy }
$ source /cvmfs/software.eessi.io/versions/2023.06/init/bash 
RISC-V architecture detected, but there is no RISC-V support yet in the production repository.
Automatically switching to version 20240402 of the RISC-V development repository /cvmfs/riscv.eessi.io.
For more details about this repository, see https://www.eessi.io/docs/repositories/riscv.eessi.io/.

Found EESSI repo @ /cvmfs/riscv.eessi.io/versions/20240402!
archdetect says riscv64/generic
Using riscv64/generic as software subdirectory.
Found Lmod configuration file at /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/.lmod/lmodrc.lua
Found Lmod SitePackage.lua file at /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/.lmod/SitePackage.lua
Using /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/modules/all as the directory to be added to MODULEPATH.
Using /cvmfs/riscv.eessi.io/host_injections/20240402/software/linux/riscv64/generic/modules/all as the site extension directory to be added to MODULEPATH.
Initializing Lmod...
Prepending /cvmfs/riscv.eessi.io/versions/20240402/software/linux/riscv64/generic/modules/all to $MODULEPATH...
Prepending site path /cvmfs/riscv.eessi.io/host_injections/20240402/software/linux/riscv64/generic/modules/all to $MODULEPATH...
Environment set up to use EESSI (20240402), have fun!
{EESSI 20240402} $ 

```

Note that we currently only provide generic builds, hence `riscv64/generic` is being used for all RISC-V CPUs.

The amount of software is constantly increasing.
Besides having the `foss/2023b` toolchain available, applications like dlb, GROMACS, OSU Micro-Benchmarks, and R are already available as well.
Use `module avail` to get a full and up-to-date listing of available software.


## Infrastructure status

The status of the CernVM-FS infrastructure for this repository is shown at [https://status.eessi.io](https://status.eessi.io/).
