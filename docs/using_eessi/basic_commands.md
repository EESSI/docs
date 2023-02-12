## Basic commands to access software provided via EESSI

EESSI provides software in modules and extensions. To see which modules and
extensions are available run
``` { .bash .copy }
module avail
```
Below is a short excerpt from `module avail` showing 10 modules only.
```
   PyYAML/5.3-GCCcore-9.3.0
   Qt5/5.14.1-GCCcore-9.3.0
   Qt5/5.15.2-GCCcore-10.3.0                               (D)
   QuantumESPRESSO/6.6-foss-2020a
   R-bundle-Bioconductor/3.11-foss-2020a-R-4.0.0
   R/4.0.0-foss-2020a
   R/4.1.0-foss-2021a                                      (D)
   re2c/1.3-GCCcore-9.3.0
   re2c/2.1.1-GCCcore-10.3.0                               (D)
   RStudio-Server/1.3.1093-foss-2020a-Java-11-R-4.0.0
```
Load modules with `module load package/version`, e.g.,
`module load R/4.1.0-foss-2021a`, and try out the software. See below for a short
session
```
[EESSI pilot 2021.12] $ module load R/4.1.0-foss-2021a
[EESSI pilot 2021.12] $ which R
/cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/software/R/4.1.0-foss-2021a/bin/R
[EESSI pilot 2021.12] $ R --version
R version 4.1.0 (2021-05-18) -- "Camp Pontanezen"
Copyright (C) 2021 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under the terms of the
GNU General Public License versions 2 or 3.
For more information about these matters see
https://www.gnu.org/licenses/.
```
