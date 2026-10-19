---
authors: [hmeiland]
date: 2026-07-12
slug: risc-v-x60-openblas-hpl
hide:
  - toc
---

# Chasing a NaN: correct RVV HPL on a RISC-V SpaceMiT X60, through EESSI

*A fresh-install, end-to-end walkthrough on an Orange Pi RV2: reproduce a silent **NaN
failure** in the stock EESSI HPL, trace it to one RISC-V vector kernel, and fix it —
correct results — with a single `eb --from-pr`.*

<!-- more -->

## TL;DR

- The Orange Pi RV2 (SpaceMiT **K1**, eight **X60** cores) is a vector RISC-V board:
  **RVV 1.0, VLEN=256**. Unlike the scalar SiFive U74, its OpenBLAS *already* has a mature
  RVV GEMM kernel (`RISCV64_ZVL256B`), and the stock EESSI OpenBLAS 0.3.30 is a
  `DYNAMIC_ARCH` build that **does** dispatch it on this chip.
- So RVV is engaged out of the box — but the result is **wrong**: stock EESSI **HPL fails
  with residual `nan`** on the X60. The run even reports a healthy-looking ~8.5 GFLOP/s;
  only the residual check reveals the answer is garbage.
- The cause is a one-kernel bug in OpenBLAS **0.3.30**'s RVV `gemv_n` (it zeroes an
  **uninitialized** vector register). It was fixed upstream in **v0.3.31**
  ([OpenMathLib/OpenBLAS#5408]). Backporting that single kernel restores correctness:
  **HPL passes** (residual ~4e-03).
- The fix is packaged for EESSI as an EasyBuild easyconfig + patch
  ([easybuilders/easybuild-easyconfigs#26444]). This post reproduces the whole thing from
  a clean CVMFS stack: see the NaN, build the fix straight from the PR, swap it in with
  FlexiBLAS, and watch HPL pass — **without recompiling HPL**.

Everything below was run on a real Orange Pi RV2, entirely from the EESSI CVMFS stack.

## The board

The [Orange Pi RV2](http://www.orangepi.org/) (~$50) is built on the SpaceMiT **K1**:
eight **SpaceMiT X60** cores at ~1.6 GHz, `rv64gcv` (RVA22-class), **RVV 1.0 with a 256-bit
vector length** (`Zvl256b`), 8 GB RAM. It's one of the first affordable multi-core RISC-V
boards with a *ratified-vector* unit — which makes it a natural target for a vectorized
BLAS.

That is the key difference from the scalar U74 story: here we don't need to *write* a
kernel. OpenBLAS already ships a good RVV DGEMM micro-kernel for `RISCV64_ZVL256B`, and —
as we'll see — EESSI's OpenBLAS already selects it on this board. The problem is not
*whether* RVV runs; it's that the shipped version runs **incorrectly**.

## What you need

- A SpaceMiT X60 / K1 board (Orange Pi RV2 here; Banana Pi BPI-F3 and Milk-V Jupiter are
  the same SoC), 8 GB RAM.
- [CVMFS](https://cvmfs.readthedocs.io/) + the [EESSI](https://www.eessi.io/) software
  stack, specifically the RISC-V development repository [`dev.eessi.io/riscv`][eessi-riscv].

No compilers, MPI, or BLAS installed by hand — EESSI provides the entire stack.

## Step 0 — Get EESSI

If CVMFS + EESSI aren't already present, install them once. A CVMFS client for RISC-V is
still experimental — tracked in [cvmfs/cvmfs#3441][cvmfs-riscv-issue], with Ubuntu/riscv64
test `.deb`s published at [`vavolkl/cvmfs-riscv`][cvmfs-riscv-rel]:

```bash
# CVMFS RISC-V client — experimental test packages (see cvmfs/cvmfs#3441)
rel=https://github.com/vavolkl/cvmfs-riscv/releases/download/cvmfs-2.14.0-riscv-test
wget $rel/cvmfs_2.14.0+ubuntu24.04_riscv64.deb \
     $rel/cvmfs-libs_2.14.0+ubuntu24.04_riscv64.deb \
     $rel/cvmfs-fuse3_2.14.0+ubuntu24.04_riscv64.deb \
     $rel/cvmfs-config-default_2.2_all.deb
sudo apt install -y ./cvmfs*.deb
sudo dpkg -i cvmfs-config-eessi_*_all.deb     # EESSI config (architecture-independent)
sudo cvmfs_config setup
```

Initialize the EESSI environment (the RISC-V stack lives under a version override):

```bash
export EESSI_VERSION_OVERRIDE=2025.06-001
source /cvmfs/software.eessi.io/versions/2025.06/init/lmod/bash
```

You should land in the EESSI environment, targeting `riscv64/generic`:

```
$ echo $EESSI_SOFTWARE_SUBDIR
riscv64/generic
```

Everything from here is `module load` — the whole toolchain, MPI, and BLAS come from CVMFS.

## Step 1 — Run HPL with the stock stack → a NaN

EESSI ships a ready-to-run HPL; loading it pulls in HPL, OpenMPI, and FlexiBLAS (whose
default backend is the stock OpenBLAS 0.3.30):

```bash
module load HPL/2.3-foss-2025b
```

Confirm every binary comes from CVMFS:

```
$ command -v xhpl
/cvmfs/dev.eessi.io/riscv/versions/2025.06-001/software/linux/riscv64/generic/software/HPL/2.3-foss-2025b/bin/xhpl
```

Run a small problem (N=8000, NB=256, 1×8 grid, one MPI rank per core):

```bash
mkdir -p ~/hpl-run && cd ~/hpl-run
# HPL.dat: N=8000, NB=256, P=1, Q=8
OMP_NUM_THREADS=1 mpirun -np 8 xhpl
```

```
T/V                N    NB     P     Q               Time                 Gflops
--------------------------------------------------------------------------------
WR11C2R4        8000   256     1     8              40.05             8.5251e+00
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=              nan ...... FAILED
--------------------------------------------------------------------------------
              0 tests completed and passed residual checks,
              1 tests completed and failed residual checks,
```

**`nan` — FAILED.** Note the trap: HPL reports **8.53 GFLOP/s**, a perfectly plausible
number — the vector kernel *is* running fast — but the linear system was solved to
garbage. Without the residual check you might never notice.

Why is RVV even running? Because the stock CVMFS OpenBLAS is a **`DYNAMIC_ARCH`** build.
Its LP64 `libopenblas.so` carries three cores — you can see them in the binary:

```bash
strings $EBROOTOPENBLAS/lib/libopenblas.so | grep -oE '_k_RISCV64_(GENERIC|ZVL128B|ZVL256B)' | sort -u
# _k_RISCV64_GENERIC
# _k_RISCV64_ZVL128B
# _k_RISCV64_ZVL256B
```

At runtime it detects the X60's VLEN=256 and dispatches the **`ZVL256B`** RVV kernels. Good
— except one of those kernels is broken in 0.3.30.

> A subtlety worth recording: the *ILP64* `libopenblas64_p.so` in the same install is
> `RISCV64_GENERIC` (scalar) only — the vector cores are compiled into the **LP64** library.
> HPL uses LP64, so it gets RVV. (If you ever inspect the ILP64 lib and conclude "EESSI has
> no RVV kernels", that's why it looks that way — check the LP64 lib.)

## Step 2 — The root cause: one RVV `gemv_n` kernel

HPL's panel factorization leans heavily on **`dgemv`** (matrix–vector). In OpenBLAS 0.3.30,
`kernel/riscv64/gemv_n_vector.c` initializes its vector accumulator by *subtracting a
register from itself* (`vfsub_vv(v, v)`) — but on an **uninitialized** vector register. If
that register happens to hold NaN bits, `NaN − NaN = NaN`, and `dgemv` returns all-NaN. The
DGEMM path uses a different (correct) kernel, so a standalone GEMM benchmark looks fine —
which is exactly why the failure only surfaces in a full solve like HPL.

The kernel was rewritten upstream right after 0.3.30 (first released in **v0.3.31**):
[OpenMathLib/OpenBLAS#5408] (the NaN-init fix) and [#5476][openblas-5476] (a cache-friendly
`f64m4`→`f64m8` rewrite). EESSI currently ships 0.3.30, so the bug is live. The fix is to
**backport that one kernel**.

## Step 3 — Build the fixed OpenBLAS straight from the PR

The fixed, X60-targeted OpenBLAS lives in easyconfigs PR **#26444** — an easyconfig plus
the backported `gemv_n` patch. `eb --from-pr` builds directly from it.

Set up an **EESSI-extend** user installation so the module lands in your home directory
while reusing the CVMFS stack:

```bash
module load EasyBuild/5.3.0
mkdir -p $HOME/eessi-x60                  # must exist BEFORE loading EESSI-extend
export EESSI_USER_INSTALL=$HOME/eessi-x60
module load EESSI-extend/2025.06-easybuild

# The dev.eessi.io/riscv toolchain needs a valid RVV -march pinned (see note below):
export EASYBUILD_OPTARCH='-march=rv64imafdcv_zvl256b'

eb --from-pr 26444 --robot
```

`--from-pr` fetches `OpenBLAS-0.3.30-GCC-14.3.0-x60.eb` **and** its patches, applies the
`gemv_n` fix, and builds with `TARGET=RISCV64_ZVL256B DYNAMIC_ARCH=0` — a single-target RVV
library. It reuses the CVMFS GCC/14.3.0 toolchain and installs the module
`OpenBLAS/0.3.30-GCC-14.3.0-x60` under `$EESSI_USER_INSTALL`.

This is a *full* build with **no shortcuts** — it runs the BLAS test suite **and** the
complete netlib LAPACK test suite for each interface (LP64 + ILP64). On the 1.6 GHz X60
that took ~15 h and completed with zero failures; the SBC is the bottleneck, not the build.

> **Note for the experimental `dev.eessi.io/riscv` toolchain.** GCC 14.3.0's auto-optarch
> can emit a canonical-expanded `-march` (`…zaamo_zalrsc…`) that the same compiler then
> rejects, breaking OpenBLAS's `getarch`. Pinning a valid `-march` via `EASYBUILD_OPTARCH`
> (above) avoids it. It's a quirk of that experimental toolchain, not of the easyconfig —
> and note this **keeps EESSI's own build hooks**, so don't override `--hooks`.

## Step 4 — Swap it in via FlexiBLAS and re-run → PASSED

HPL was built against **FlexiBLAS**, so we switch the BLAS backend at *runtime* — no HPL
rebuild. Make the user module visible, load it, and register it as a FlexiBLAS backend:

```bash
module use $EESSI_USER_INSTALL/versions/2025.06-001/software/linux/riscv64/generic/modules/all
module load OpenBLAS/0.3.30-GCC-14.3.0-x60

flexiblas add x60 $EBROOTOPENBLAS/lib/libopenblas.so
flexiblas default x60
```

> A caveat (the answer to an obvious question): swapping the OpenBLAS *module* is not
> enough — EESSI binaries are linked with **RPATH**, and FlexiBLAS's default backend has an
> RPATH-pinned `libopenblas.so.0`. Loading a different module only changes compile-time
> paths. Register the backend with FlexiBLAS (above), or point at it explicitly per-run:
> ```bash
> FLEXIBLAS=$EBROOTOPENBLAS/lib/libopenblas.so OMP_NUM_THREADS=1 mpirun -np 8 xhpl
> ```

Re-run the **exact same** `xhpl`, same input, same command:

```
WR11C2R4        8000   256     1     8              44.50             7.6719e+00
||Ax-b||_oo/(eps*(||A||_oo*||x||_oo+||b||_oo)*N)=   4.04326757e-03 ...... PASSED
              1 tests completed and passed residual checks,
```

**PASSED**, residual `4.04e-03`. Only the BLAS backend changed: the same CVMFS HPL and
OpenMPI, now with a *correct* RVV `gemv_n`.

## Results

**Correctness** (N=8000, NB=256, 1×8 — identical HPL binary and input, only the BLAS
backend changes):

| BLAS backend                                          | HPL residual        |
|-------------------------------------------------------|---------------------|
| Stock EESSI CVMFS OpenBLAS 0.3.30 (RVV, unpatched)    | **`nan` — FAILED**  |
| Fixed RVV OpenBLAS — PR #26444 (backported `gemv_n`)  | **4.04e-03 — PASSED** |

**Performance.** With the fix in place, the *vector* path does real work. On eight X60
cores (pure CVMFS HPL, fixed RVV backend, NB=256) HPL reaches **~10.5 GFLOP/s** — and the
process grid matters as much as the problem size:

| Problem / grid   | HPL (8 cores)     | residual |
|------------------|-------------------|----------|
| N=16000, 1×8     | 9.74 GFLOP/s      | PASSED   |
| N=16000, 2×4     | 10.00 GFLOP/s     | PASSED   |
| **N=20000, 2×4** | **10.53 GFLOP/s** | PASSED   |

A square-ish **2×4** grid beats 1×8, and throughput is still climbing at N=20000. Every run
passes its residual check — the whole point. One caveat worth knowing: this is OpenBLAS
**0.3.30**'s RVV kernel; a newer OpenBLAS (≥ 0.3.34) is both faster *and* carries this fix
natively (see below).

## Why this matters

- **It's a real bug in the shipped stack, not a synthetic demo.** The stock EESSI HPL on
  this board fails its own residual check. Reproducing it takes only CVMFS + `module load`,
  and the fix is a reviewable EasyBuild PR — no hand-built BLAS, no `LD_PRELOAD`.
- **Correctness first.** A fast NaN is worthless — a valid residual is the whole point.
  This walkthrough restores the *correct* RVV path.
- **Runtime-swappable.** FlexiBLAS lets one HPL (or NumPy, SciPy, …) switch backends — set
  the fixed library as your default with `flexiblas default`, or per-run with one
  environment variable.
- **On a path to "just works".** OpenBLAS ≥ 0.3.31 already carries the gemv_n fix, and its
  newer RVV kernels are *faster* than 0.3.30's — so a future EESSI bump to OpenBLAS **≥ 0.3.34**
  (0.3.34 also clears a separate RISC-V/K1 DGEMM regression that affects 0.3.31–0.3.33) makes
  the NaN disappear with no patch **and** raises the performance ceiling. A future
  `riscv64/…/x60`-style software subdirectory could then ship a pre-selected RVV build so an
  Orange Pi RV2 user gets correct, vectorized BLAS from `module load` alone. This post is the
  manual version of what should become transparent.

## Links

- EasyBuild easyconfig PR (the fix this post builds): <https://github.com/easybuilders/easybuild-easyconfigs/pull/26444>
- Upstream OpenBLAS `gemv_n` fix (first in v0.3.31): <https://github.com/OpenMathLib/OpenBLAS/pull/5408> and <https://github.com/OpenMathLib/OpenBLAS/pull/5476>
- EESSI RISC-V dev repository: <https://www.eessi.io/docs/repositories/dev.eessi.io-riscv/>

---

*Reproduced end-to-end on an Orange Pi RV2 (SpaceMiT K1, 8× X60 @ ~1.6 GHz, RVV 1.0
VLEN=256, 8 GB) using EESSI `2025.06-001`, entirely from the CVMFS stack. The easyconfig,
patch, and the diagnosis were produced with AI assistance — an OpenCode agent driving
Claude Opus 4.8, running on Microsoft GitHub Copilot — with a human directing the work,
operating the hardware, and validating every result, per the
[EasyBuild AI policy](https://docs.easybuild.io/policies/ai/).*

[OpenMathLib/OpenBLAS#5408]: https://github.com/OpenMathLib/OpenBLAS/pull/5408
[openblas-5476]: https://github.com/OpenMathLib/OpenBLAS/pull/5476
[easybuilders/easybuild-easyconfigs#26444]: https://github.com/easybuilders/easybuild-easyconfigs/pull/26444
[eessi-riscv]: https://www.eessi.io/docs/repositories/dev.eessi.io-riscv/
[cvmfs-riscv-issue]: https://github.com/cvmfs/cvmfs/issues/3441
[cvmfs-riscv-rel]: https://github.com/vavolkl/cvmfs-riscv/releases/tag/cvmfs-2.14.0-riscv-test
