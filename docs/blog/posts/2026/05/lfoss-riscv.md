---
authors: [julianmorillo]
date: 2026-05-12
slug: lfoss-riscv
---

# `lfoss/2025b` now available in the EESSI RISC-V stack

The EESSI RISC-V software stack available through the `dev.eessi.io/riscv` repository 
now includes the `lfoss/2025b` toolchain.

This is an important milestone for the RISC-V enablement work in EESSI, since it brings a 
modern LLVM-based software toolchain to the growing collection of software available for 
RISC-V systems through EESSI.

<!-- more -->

The RISC-V software stack is distributed through the EESSI development repository 
infrastructure and is intended for experimentation, testing, and early adoption of RISC-V
support in EESSI.

## What is `lfoss`

`lfoss` is the LLVM-based counterpart to the widely used `foss` toolchain in EESSI and 
EasyBuild ecosystems.

Where `foss` is centered around GCC, the `lfoss` family uses LLVM/Clang while still 
providing the familiar scientific software stack components such as MPI, BLAS/LAPACK, FFT 
libraries, and related HPC tooling.

The availability of `lfoss/2025b` on RISC-V is particularly relevant because LLVM's RISC-V 
backend has matured significantly in recent years, making it increasingly viable for HPC 
and scientific computing workloads.

## Why this matters

Adding `lfoss/2025b` to the EESSI RISC-V stack provides several benefits:
 
+ access to a modern LLVM/Clang-based compiler environment on RISC-V;
+ broader compiler coverage for portability testing;
+ improved support for projects already using LLVM toolchains;
+ additional opportunities to validate and improve RISC-V support in HPC software
ecosystems.

This also helps align the RISC-V stack more closely with the software offerings already
available on x86\_64 and AArch64 platforms in EESSI.

## Accessing the RISC-V stack

The RISC-V stack is currently provided through the dedicated RISC-V development
repository. To access it, just:

```
$ export EESSI_VERSION_OVERRIDE=2025.06-001
$ source /cvmfs/software.eessi.io/versions/2025.06/init/lmod/bash
This EESSI production version only provides a RISC-V compatibility layer,
software installations are provided by the EESSI development repository at /cvmfs/dev.eessi.io/riscv.

Module for EESSI/2025.06 loaded successfully
EESSI has selected riscv64/generic as the compatible CPU target for EESSI/2025.06
EESSI did not identify an accelerator on the system
(for debug information when loading the EESSI module, set the environment variable EESSI_MODULE_DEBUG_INIT)
```

On a RISC-V system, this will initialize the RISC-V software stack environment.

You can then verify that the new toolchain is available:

```
module avail lfoss
```

and load it via:

```
module load lfoss/2025
```

## Availability in `dev.eessi.io/riscv`

The RISC-V stack is currently hosted in the EESSI development infrastructure, which is
intended for pre-release and experimental software deployments.

As with the rest of the RISC-V repository:

+ software availability is still evolving;
+ builds may be updated or replaced;
+ the stack currently focuses on generic RISC-V targets.

The RISC-V repository already contains a growing collection of scientific software and toolchains.

## Looking ahead

The addition of `lfoss/2025b` in another step toward broader and more mature RISC-V 
support within EESSI.

Future work will include:

+ expanding software coverage built with LLVM-based toolchains;
+ improving validation and CI coverage for RISC-V;
+ enabling additional optimized RISC-V targets as the ecosystem matures;
+ continuing collaboration with the broader RISC-V and HPC communities.

RISC-V remains an exciting and rapidly developing architecture for HPC and scientific
computing, and EESSI aims to make portable, reproducible software stacks readily 
available for emerging platforms.

## Learn more

+ [EESSI RISC-V repository documentation](https://www.eessi.io/docs/repositories/dev.eessi.io-riscv/)
+ [dev.eessi.io documentation](https://www.eessi.io/docs/repositories/dev.eessi.io/)
+ [Available software in EESSI](https://www.eessi.io/docs/available_software/)
+ [foss toolchain documentation](https://www.eessi.io/docs/available_software/detail/foss)

