# EESSI RISC-V development repository (`dev.eessi.io/riscv`)

!!! note "Is `dev.eessi.io` a webpage?"
    If you landed on this page because you typed `dev.eessi.io` into your browser, then
    you may not know yet that this is not a URL/webpage but a [CernVM-FS repository](../filesystem_layer.md)
    that EESSI uses to distribute software.
 
    **See the [EESSI overview page](../overview.md) for a general introduction to EESSI.**

This repository contains development versions of an EESSI RISC-V software stack
and replaces the older [`riscv.eessi.io`](riscv.eessi.io.md) repository, which is now deprecated.
Note that versions may be added, modified, or deleted at any time.

## Accessing the RISC-V repository

See [Getting access](../getting_access/is_eessi_accessible.md);
by making the EESSI CVMFS domain available, you will automatically have access to `dev.eessi.io/riscv` as well.

## Using `dev.eessi.io/riscv`

This repository currently offers one version (2025.06-001), which is built on top of the
RISC-V compatibility layer of EESSI version 2025.06 in the production repository `software.eessi.io`.
New versions may be added later, and will be named similarly.

You can use this version by running the following commands on a RISC-V machine:

``` { .bash .copy }
$ export EESSI_VERSION_OVERRIDE=2025.06-001
$ source /cvmfs/software.eessi.io/versions/2025.06/init/lmod/bash
This EESSI production version only provides a RISC-V compatibility layer,
software installations are provided by the EESSI development repository at /cvmfs/dev.eessi.io/riscv.

Module for EESSI/2025.06 loaded successfully
EESSI has selected riscv64/generic as the compatible CPU target for EESSI/2025.06
EESSI did not identify an accelerator on the system
(for debug information when loading the EESSI module, set the environment variable EESSI_MODULE_DEBUG_INIT)
```

Note that we currently only provide generic builds, hence `riscv64/generic` is being used for all RISC-V CPUs.
We are currently working on support for builds that are optimized for specific RISC-V CPUs.

The amount of software is constantly increasing.
Besides having the `foss/2025a` and `foss/2025b` toolchains available, several applications are already available as well.
Use `module avail` to get a full and up-to-date listing of available software.


## Infrastructure status

The status of the CernVM-FS infrastructure for this repository is shown at [https://status.eessi.io](https://status.eessi.io/).
