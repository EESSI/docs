---
authors: [julianmorillo]
date: 2024-07-26
slug: extrae-now-available-in-EESSI 
---

# Extrae available in EESSI

Thanks to the work developed under [MultiXscale CoE](https://www.multixscale.eu/) we are proud to announce that as of 22 July 2024, [Extrae](https://tools.bsc.es/extrae) v4.2.0 is available in the EESSI production repository `software.eessi.io`, 
optimized for the [8 CPU targets](https://www.eessi.io/docs/software_layer/cpu_targets) that are fully supported by version 2023.06 of EESSI.
This allows using Extrae effortlessly on the EuroHPC systems where EESSI is already available,
like [Vega](https://doc.vega.izum.si) and [Karolina](https://docs.it4i.cz/karolina/introduction).

It is worth noting that from that date Extrae is also available in the EESSI RISC-V repository `risv.eessi.io`.

<!-- more -->

Extrae is a package developed at [BSC](https://www.bsc.es/es) devoted to generate [Paraver](https://tools.bsc.es/paraver) trace-files for a post-mortem analysis of applications performance. Extrae is a tool that uses different interposition mechanisms to inject probes into the target application so as to gather information regarding the application performance. It is one of the [tools](https://pop-coe.eu/partners/tools) used in the [POP3 CoE](https://pop-coe.eu/).

The work to incorporate Extrae into EESSI started early in May. It took quite some time and effort but has resulted in a number of updates, improvements and bug fixes for Extrae. The following sections explain the work done describing the issues encountered and the solutions adopted.

## Adapting EESSI software layer
During the first attempt to build Extrae (in this case `v4.0.6`) in the EESSI context, we found out two issues:

1. the `configure` script of Extrae was not able to find `binutils` in the location it is provided by the compat layer of EESSI, and
2. the `configure`/`make` files of Extrae make use of `which` command that does not work in our build container. 

Both problems were solved by adding a `pre_configure_hook` in the [`eb_hooks.py`](https://github.com/EESSI/software-layer/commit/41149ac060b7580f2b15d3e04908ffabe207e046) file of the EESSI software layer that:

- avoids the use of `which` during configuration and building processes by replacing it with `command -v` in the necessary files, and
- specifies the correct path to `binutils` in EESSI compat layer by passing `--with-binutils` option to the Extrae `configure` script.

## Moving to version 4.1.6
By the time we completed this work, `v4.1.6` of Extrae was available so we decided to switch to that version as v4.0.6 was throwing errors in the test suite provided by Extrae through the `make check`command. 

When first trying to build this new version, we noticed that there were still problems with `binutils` detection because the configure scripts of Extrae assume that the `binutils` libraries are under a `lib` directory in the provided `binutils` path while in the EESSI compat layer they are directly in the provided directory (i.e. without the `/lib`). This was solved with a [patch file](https://github.com/easybuilders/easybuild-easyconfigs/pull/20690/commits/e0bfd59cabd0bbb080c86073f179954486fe227e) committed to the [EasyBuild easyconfigs repository](https://github.com/easybuilders/easybuild-easyconfigs), that modifies both `configure` and `config/macros.m4` to make `binutils` detection more robust. This patch was also provided to Extrae developers to incorporate into future releases.

The next step was to submit a [Pull Request](https://github.com/easybuilders/easybuild-easyblocks/pull/3339) to the [EasyBuild easyblocks repository](https://github.com/easybuilders/easybuild-easyblocks) with some modifications to the `extrae.py` easyblock that:

- Removed configure options `--enable-xml` and `--with-dwarf` that were no longer available in Extrae starting from v4.1.0.
- Added `--with-xml` option to specify `libxml2` root dir.
- Added `--enable-posix-clock` configure option for RISCV64 (needed to build Extrae as no lower level clock seems to be available yet in RISC-V architectures).

With all of this in place, we managed to correctly build Extrae but found out that many tests failed to pass, including all 21 under the MPI directory. We reported this fact to Extrae developers who answered that there was a critical bug fix related to MPI tracing in version 4.1.7 so we switched to that version before continuing our work.

## Work with version 4.1.7
We tested the build of that version (of course including all the work done before for previous versions) and we still saw some errors in the `make check`phase. We focused first in the following 3:

* `FAIL: mpi_commranksize_f_1proc.sh`
* `FAIL: pthread.sh`
* `FAIL: check_Extrae_xml_envvar_counters.sh`

Regarding the first one, we found a bug in the Extrae test itself: the `mpi_comm_ranksize_f_1proc.sh` was invoking `trace-ldpreload.sh` instead of the Fortran version `trace-ldpreloadf.sh` and this caused the test to fail. We submitted a [Pull Request](https://github.com/bsc-performance-tools/extrae/pull/107) to the Extrae repository with the bugfix that has been already merged and incorporated into new releases.

Regarding the second one, it was reported to Extrae developers as an [issue](https://github.com/bsc-performance-tools/extrae/issues/104). They suggested commenting out a call at `src/tracer/wrappers/pthread/pthread_wrapper.c` at line 240: `//Backend_Flush_pThread (pthread_self());`. We reported that this fixed the issue so this change has also been incorporated into the Extrae main branch for future releases.

The last failing test was an issue related with the access to HW counters on the building/testing system. The problem was that the test assumed that Extrae (through [PAPI](https://icl.utk.edu/papi/)) can access HW counters (in this case, `PAPI_TOT_INS`). This might not be the case because this is very system-dependent (since it involves permissions, etc). As a solution, we committed a [patch](https://github.com/bsc-performance-tools/extrae/commit/3d8295cf45c4bf7068decd29c96bf755216a496f) to the Extrae repository which ensured that the test will not fail if `PAPI_TOT_CYC` is unavailable in the testing system. As this has not been incorporated yet into the Extrae repository, we also committed a [patch file](https://github.com/easybuilders/easybuild-easyconfigs/blob/develop/easybuild/easyconfigs/e/Extrae/Extrae-4.2.0-fix-hw-counters-checks.patch) to the EasyBuild easyconfigs repository that solves the problem with this specific test but also with others that suffered from this same issue.

## Finally, version 4.2.0
Due to the bugfixes mentioned in previous section that were incorporated into the Extrae repository, we switched again to an updated version of Extrae (in this case v4.2.0). With that updated version and the easyconfig (and patches) and easyblock modifications tests started to pass successfully in most of the testing platforms. 

We noticed, however, that Extrae produced segmentation faults when using [libunwind](https://www.nongnu.org/libunwind/) in ARM architectures. Our approach to that was to report the issue to Extrae developers and to make this dependency architecture specific (i.e. forcing `--without-unwind` when building for ARM while keeping the dependency for the rest of architectures). We did this in a [Pull Request](https://github.com/easybuilders/easybuild-easyconfigs/pull/21017) to the EasyBuild easyconfigs repository that is already merged. In this same [Pull Request](https://github.com/easybuilders/easybuild-easyconfigs/pull/21017) we added `zlib` as an explicit dependency in the easyconfig file for all architectures.

The last issue we encountered was similar to the previous one but in this case was seen on some RISC-V platforms and related to dynamic memory instrumentation. We adopted the same approach and reported the issue to Extrae developers and added `--disable-instrument-dynamic-memory` to the configure options in a [Pull Request](https://github.com/easybuilders/easybuild-easyconfigs/pull/20690/commits/a26b35cbc1dd6cf7129f866a5b2002febd289104) already merged into the EasyBuild-Easyconfigs repository.
 
With that, all tests passed in all platforms and we were able to incorporate Extrae to the list of software available in both the `software.eessi.io` and `riscv.eessi.io` repositories of EESSI.
    
