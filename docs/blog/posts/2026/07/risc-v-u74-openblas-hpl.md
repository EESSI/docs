---
authors: [hmeiland]
date: 2026-07-11
slug: risc-v-u74-openblas-hpl
hide:
  - toc
---

# A 1.7× faster HPL on a RISC-V SiFive U74, delivered through EESSI

*A fresh-install, end-to-end walkthrough: from a bare VisionFive 2 to a ~1.7× faster
High-Performance Linpack run, using nothing but EESSI and a single `eb --from-pr`.*

<!-- more -->

## TL;DR

- The StarFive VisionFive 2 (SiFive **U74**, `rv64gc`) runs stock OpenBLAS at roughly
  **3 GFLOP/s** on HPL — it falls back to a generic C GEMM kernel.
- A hand-tuned scalar **4×4 DGEMM micro-kernel** for the U74 lifts that to **~5.3 GFLOP/s
  (~1.7× on HPL**; the raw DGEMM kernel itself is roughly **2×** faster).
- The kernel is upstreamed to OpenBLAS ([OpenMathLib/OpenBLAS#5903]) and packaged for
  EESSI as an EasyBuild easyconfig ([easybuilders/easybuild-easyconfigs#26436]).
- This post reproduces the **whole thing from a clean machine**: set up EESSI, measure a
  baseline HPL, build the optimized OpenBLAS straight from the PR with `eb --from-pr`,
  load it as a module, and re-run HPL — **without recompiling HPL**.

Everything below was run on a real VisionFive 2. Total wall-clock: a few minutes of
commands plus one longer `eb` build.

## The board and the gap

The [VisionFive 2](https://www.starfive.tech/en/site/boards) is a ~$70 single-board
computer built on the StarFive **JH7110**: four **SiFive U74** cores at 1.5 GHz,
`rv64gc` (RVA20-class, scalar — *no* vector extension), 8 GB RAM, running Ubuntu 24.04.

Out of the box, OpenBLAS has no U74-specific GEMM kernel, so it selects the generic
`RISCV64_GENERIC` path — a portable C `2×2` kernel. It works, but it leaves a lot of the
(admittedly modest) FP throughput on the table. On HPL that lands around **3 GFLOP/s**
across the four cores.

The optimization is a classic register-blocked GEMM micro-kernel, written in RV64
assembly and tuned specifically for the U74's in-order, single-FP-pipe, one-load-port
pipeline: a software-pipelined **4×4** inner kernel with operand double-buffering and
load-before-FMA scheduling. On this core it lifts single-core DGEMM from ~1.4 to
**1.77 GFLOP/s** and, combined with a re-tuned block size, lifts HPL by **~1.7×** (the raw
4-core DGEMM rate is ~2× the generic kernel). (The full design write-up is in the
companion paper; this post is purely about *reproducing the result*.)

The interesting part for practitioners isn't just the kernel — it's that you can get it
onto a machine through the **normal scientific-software supply chain**: EESSI provides the
stack, and EasyBuild pulls the not-yet-released kernel straight from a pull request.

## What you need

- A SiFive U74 / `rv64gc` RISC-V board (VisionFive 2 here), ~8 GB RAM, Ubuntu 24.04.
- [CVMFS](https://cvmfs.readthedocs.io/) + the [EESSI](https://www.eessi.io/) software
  stack, specifically the RISC-V development repository
  [`dev.eessi.io/riscv`][eessi-riscv].

That's it — no compilers, no MPI, no BLAS to install by hand. EESSI provides all of it.

## Step 0 — Get EESSI

If CVMFS + EESSI aren't already on the box, install them once. A CVMFS client for RISC-V is still
experimental — it's tracked in [cvmfs/cvmfs#3441][cvmfs-riscv-issue], with Ubuntu/riscv64 test
`.deb`s published at [`vavolkl/cvmfs-riscv`][cvmfs-riscv-rel] (release `cvmfs-2.14.0-riscv-test`).
Fetch the riscv64 client packages from there, add EESSI's architecture-independent config, and set up:

```bash
# CVMFS RISC-V client — experimental test packages (see cvmfs/cvmfs#3441)
rel=https://github.com/vavolkl/cvmfs-riscv/releases/download/cvmfs-2.14.0-riscv-test
wget $rel/cvmfs_2.14.0+ubuntu24.04_riscv64.deb \
     $rel/cvmfs-libs_2.14.0+ubuntu24.04_riscv64.deb \
     $rel/cvmfs-fuse3_2.14.0+ubuntu24.04_riscv64.deb \
     $rel/cvmfs-config-default_2.2_all.deb
sudo apt install -y ./cvmfs*.deb
# EESSI CVMFS configuration (architecture-independent, from EESSI):
sudo dpkg -i cvmfs-config-eessi_*_all.deb
sudo cvmfs_config setup
```

Then initialize the EESSI environment. The RISC-V stack currently lives under a version
override:

```bash
export EESSI_VERSION_OVERRIDE=2025.06-001
source /cvmfs/software.eessi.io/versions/2025.06/init/lmod/bash
```

You should now be in the EESSI environment, targeting `riscv64/generic`:

```
$ echo $EESSI_SOFTWARE_SUBDIR
riscv64/generic
```

Everything from here on is `module load` + EasyBuild.

## Step 1 — Baseline HPL with the stock stack

EESSI ships a ready-to-run HPL. Load it — this pulls in HPL, OpenMPI, and FlexiBLAS
(whose default backend is the generic OpenBLAS 0.3.30):

```bash
module load HPL/2.3-foss-2025b
```

Create a small problem (N=10000, NB=192, 2×2 process grid — one MPI rank per core):

```bash
mkdir -p ~/hpl-run && cd ~/hpl-run
# HPL.dat: 1 problem size N=10000, NB=192, P=2, Q=2  (see the HPL docs for the full file)
```

Run it as pure MPI (one thread per rank):

```bash
OMP_NUM_THREADS=1 mpirun -np 4 xhpl | grep -A1 '^WR'
```

On the VisionFive 2 this yields the baseline:

```
================================================================================
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4       10000   192     2     2             213.34             3.1257e+00
================================================================================
```

**~3.13 GFLOP/s** — the generic-kernel starting point. (`WR…` = the residual check
passed.)

## Step 2 — Build the U74-optimized OpenBLAS *straight from the PR*

Here's the payoff of doing this through EasyBuild: the optimized OpenBLAS isn't released
yet, but it lives in easyconfigs PR **#26436**, and `eb --from-pr` builds directly from it.

Load EasyBuild, and set up an **EESSI-extend** user installation so the new module lands
in your home directory alongside (and reusing) the CVMFS stack:

```bash
module load EasyBuild/5.3.0

mkdir -p $HOME/eessi-u74                 # must exist BEFORE loading EESSI-extend
export EESSI_USER_INSTALL=$HOME/eessi-u74
module load EESSI-extend/2025.06-easybuild
```

Now build the easyconfig from the PR:

```bash
eb --from-pr 26436 --robot
```

`--from-pr` fetches `OpenBLAS-0.3.30-GCC-14.3.0-U74.eb` **and** its source patch from the
pull request, applies the patch (which adds the `U74` target and the 4×4 kernel to the
OpenBLAS source tree), and builds with `TARGET=U74 DYNAMIC_ARCH=0`. It reuses the
GCC/14.3.0 toolchain, Python, etc. already in CVMFS, and installs the result as the module
`OpenBLAS/0.3.30-GCC-14.3.0-U74` under `$EESSI_USER_INSTALL`.

> **Note for the `dev.eessi.io/riscv` stack.** On that experimental stack, GCC 14.3.0's
> auto-optarch can emit a canonical-expanded `-march` (`…zaamo_zalrsc…`) that the very same
> compiler then rejects, breaking OpenBLAS's `getarch` check. It's a quirk of that
> experimental toolchain, *not* of the easyconfig or patch. Fix it by pinning a valid
> `-march` via `EASYBUILD_OPTARCH`:
>
> ```bash
> export EASYBUILD_OPTARCH='-march=rv64imafdc_zba_zbb'   # valid scalar march for the U74
> eb --from-pr 26436 --robot
> ```

## Step 3 — Load the module and re-run HPL (no HPL rebuild!)

This is the neat trick. HPL was built against **FlexiBLAS**, which lets you switch the
BLAS backend at *runtime* — so we don't rebuild HPL at all.

First, make the user-installed module visible and load it (module system, no hard-coded
paths):

```bash
module use $EESSI_USER_INSTALL/versions/2025.06-001/software/linux/riscv64/generic/modules/all
module load OpenBLAS/0.3.30-GCC-14.3.0-U74
```

Lmod recognizes the OpenBLAS family and swaps the stock module out of the way:

```
OpenBLAS/0.3.30-GCC-14.3.0 => OpenBLAS/0.3.30-GCC-14.3.0-U74
```

**A caveat worth knowing** (and the answer to an obvious question): swapping the OpenBLAS
*module* is **not** enough for HPL to pick up the new library. EESSI binaries are linked
with **RPATH**, not `LD_LIBRARY_PATH`, and FlexiBLAS's `OPENBLAS` backend has an RPATH that
hard-pins the stock `libopenblas.so.0`. Loading a different OpenBLAS module only changes
`LIBRARY_PATH` (used at *compile* time) — it doesn't change what FlexiBLAS `dlopen`s at
runtime. So you have to point FlexiBLAS at the new backend explicitly.

The clean way — and it means you never type a library path at run time — is to register
the module's library as a FlexiBLAS backend **once**, using the module's own
`$EBROOTOPENBLAS`, and make it your default:

```bash
flexiblas add U74 $EBROOTOPENBLAS/lib/libopenblas.so
flexiblas default U74          # writes ~/.flexiblasrc
```

From here on, every FlexiBLAS-linked program — HPL, but also NumPy, SciPy, … — uses the
U74 library by default. Re-run the *exact same* `xhpl`, with **no environment variable and
no path**:

```bash
cd ~/hpl-run
OMP_NUM_THREADS=1 mpirun -np 4 xhpl | grep -A1 '^WR'
```

```
WR11C2R4       10000   192     2     2             126.19             5.2841e+00
```

**5.28 GFLOP/s** — same binary, same input, same command; only the registered BLAS backend
changed.

> Prefer not to touch `~/.flexiblasrc`? Select the backend per-invocation instead — still
> via the module, not a hard-coded path:
> ```bash
> FLEXIBLAS=$EBROOTOPENBLAS/lib/libopenblas.so OMP_NUM_THREADS=1 mpirun -np 4 xhpl
> ```

## Results

| Configuration                                  | HPL (N=10000, 4 cores) | Speedup |
|------------------------------------------------|------------------------|---------|
| Stock EESSI OpenBLAS 0.3.30 (generic `rv64gc`) | 3.13 GFLOP/s (213 s)   | 1.00×   |
| U74-optimized OpenBLAS (PR #26436)             | 5.28 GFLOP/s (126 s)   | 1.69×   |

For reference, raw DGEMM on the installed U74 module: **1.77 GFLOP/s** single-core,
**6.31 GFLOP/s** on 4 cores — versus ~1.4 single-core for the generic kernel. (HPL sits
below peak DGEMM because of its non-GEMM work — panel factorization, pivoting,
communication — so the ~1.7× end-to-end gain trails the ~2× raw-kernel gain.)

The only thing that changed between the two HPL runs is which `libopenblas.so` FlexiBLAS
loaded. That's the whole point of shipping the kernel through EESSI/EasyBuild: it drops
into an existing, unmodified toolchain.

## Why this matters

- **Reproducible.** No hand-built BLAS, no `LD_PRELOAD` gymnastics, no patched HPL. The
  optimized library is a first-class EasyBuild module built from a reviewable PR.
- **Runtime-swappable.** FlexiBLAS means one HPL (or NumPy, or any FlexiBLAS-linked app)
  can switch between the stock and tuned backends — set once as your default with
  `flexiblas default`, or per-run with a single environment variable.
- **On a path to "just works".** Once [OpenMathLib/OpenBLAS#5903] merges and ships in an
  OpenBLAS release, the interim source patch disappears — a stock version-bump easyconfig
  will build the U74 target with nothing but `buildopts`, and `eb --from-pr` won't be
  needed at all.
- **Eventually, pre-optimized by default.** The bigger prize is for `U74` to become a
  recognized **CPU target** in its own right: once the target is upstream in OpenBLAS and
  the kernel matures, EESSI could detect a SiFive U74 (a `riscv64/sifive/u74`-style
  software subdirectory, the way it already distinguishes x86-64 microarchitectures) and
  **ship a pre-optimized OpenBLAS build automatically**. At that point a VisionFive 2 user
  gets the tuned library from `module load` alone — no `TARGET`, no patch, no
  `--from-pr`, no FlexiBLAS backend juggling. This walkthrough is the manual version of
  what should eventually be transparent.

## Links

- OpenBLAS source PR (the U74 target + kernel): <https://github.com/OpenMathLib/OpenBLAS/pull/5903>
- EasyBuild easyconfig PR (what this post builds): <https://github.com/easybuilders/easybuild-easyconfigs/pull/26436>
- EESSI RISC-V dev repository: <https://www.eessi.io/docs/repositories/dev.eessi.io-riscv/>

---

*Reproduced end-to-end on a StarFive VisionFive 2 (JH7110, 4× SiFive U74 @ 1.5 GHz,
Ubuntu 24.04) using EESSI `2025.06-001`. The kernel, patch, and easyconfig were produced
with AI assistance — an OpenCode agent driving Claude Opus 4.8, running on Microsoft
GitHub Copilot — with a human directing the work, operating the hardware, and validating
every result, per the [EasyBuild AI policy](https://docs.easybuild.io/policies/ai/).*

[OpenMathLib/OpenBLAS#5903]: https://github.com/OpenMathLib/OpenBLAS/pull/5903
[easybuilders/easybuild-easyconfigs#26436]: https://github.com/easybuilders/easybuild-easyconfigs/pull/26436
[eessi-riscv]: https://www.eessi.io/docs/repositories/dev.eessi.io-riscv/
[cvmfs-riscv-issue]: https://github.com/cvmfs/cvmfs/issues/3441
[cvmfs-riscv-rel]: https://github.com/vavolkl/cvmfs-riscv/releases/tag/cvmfs-2.14.0-riscv-test
