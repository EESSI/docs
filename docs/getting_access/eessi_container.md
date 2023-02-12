# EESSI container

This page provides all information and guides you through several examples
illustrating to access the EESSI software stack via a small container provided by
EESSI. The container only contains a minimal number tools such as the CernVM-FS
client and some configuration data.

### Prerequisites

- Singularity 3.7.x or newer _or_ Apptainer 1.0.0 or newer (any version with
  support for `--fusemount` should be sufficient)
- `git` available on your system

### Preparation

Clone the [`EESSI/software-layer`](https://github.com/EESSI/software-layer.git)
repository and change into the `software-layer` directory by running the commands
```bash
git clone https://github.com/EESSI/software-layer.git
cd software-layer
```

## Basic scenarios

### Getting access to EESSI

Simply run the command (from the directory you have changed into above)
```bash
./eessi_container.sh
```
!!! Note
    The first run may take a bit longer because the container image is
    downloaded and converted.

You should see output like
```
Using /tmp/eessi.RC6kYEjmSj as tmp storage (add '--resume /tmp/eessi.RC6kYEjmSj' to resume where this session ended).
Launching container with command (next line):
singularity shell --fusemount container:cvmfs2 pilot.eessi-hpc.org /cvmfs/pilot.eessi-hpc.org docker://ghcr.io/eessi/build-node:debian11
CernVM-FS: pre-mounted on file descriptor 3
Singularity> CernVM-FS: loading Fuse module... done
fuse: failed to clone device fd: Inappropriate ioctl for device
fuse: trying to continue without -o clone_fd.

Singularity>
```
!!! Note
    You may have to press enter to clearly see the prompt as some messages
    beginning with `CernVM-FS: ` have been printed after the first prompt
    `Singularity> ` was shown.

Read about [using EESSI](../../using_eessi) in a separate section or continue reading here
for additional features of the `eessi_container.sh` script.

To access the EESSI pilot stack run the command
```
source /cvmfs/pilot.eessi-hpc.org/latest/init/bash
```
This may take a while as data is downloaded from Stratum 1 server which is part of the
CernVM-FS infrastructure to distribute files. You should see the following (or
similar output depending on the CPU architecture of the machine you are accessing
EESSI).
```
Found EESSI pilot repo @ /cvmfs/pilot.eessi-hpc.org/versions/2021.12!
archspec says x86_64/intel/skylake_avx512
Using x86_64/intel/skylake_avx512 as software subdirectory.
Using /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/skylake_avx512/modules/all to $MODULEPATH...
Environment set up to use EESSI pilot software stack, have fun!
[EESSI pilot 2021.12] $ 
```
The last line is the prompt. Run `module avail` to see which modules and
extensions are available. Below is a short excerpt from `module avail`
showing 10 modules only.
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
Leave the container with `exit`.
### Reusing the previous session
You may have noted the following line in the output of `eessi_container.sh`
```
Using /tmp/eessi.RC6kYEjmSj as tmp storage (add '--resume /tmp/eessi.RC6kYEjmSj' to resume where this session ended).
```
!!! Note
    The parameter after `--resume` (`/tmp/eessi.RC6kYEjmSj`) *will* be different
    when you run `eessi_container.sh`. Scroll back and take note of it.
Try the following command to "resume" from the last session.
```
./eessi_container.sh --resume /tmp/eessi.RC6kYEjmSj
```
This should run much faster because the container image has been cached in the
temporary directory (`/tmp/eessi.RC6kYEjmSj` in the example above). You should
get to the prompt (`Singularity > ` or `Apptainer > `). Now you only have
to source again the EESSI init script by running
```
source /cvmfs/pilot.eessi-hpc.org/latest/init/bash
```
!!! Note
    The `/tmp/eessi...` directory contains a `home` directory which includes
    the saved history of your last session. Type `history` to see it. You should
    be able to access it as you would do in a normal terminal session.
### List available options for `eessi_container.sh`
Run `./eessi_container.sh --help` to see a list of available options.
```
./eessi_container.sh --help
usage: ./eessi_container.sh [OPTIONS] [SCRIPT]
 OPTIONS:
  -a | --access {ro,rw} - ro (read-only), rw (read & write) [default: ro]
  -c | --container IMG  - image file or URL defining the container to use
                          [default: docker://ghcr.io/eessi/build-node:debian11]
  -h | --help           - display this usage information [default: false]
  -g | --storage DIR    - directory space on host machine (used for
                          temporary data) [default: 1. TMPDIR, 2. /tmp]
  -m | --mode MODE      - with MODE==shell (launch interactive shell) or
                          MODE==run (run a script) [default: shell]
  -r | --repository CFG - configuration file or identifier defining the
                          repository to use [default: EESSI-pilot via
                          container configuration]
  -u | --resume DIR/TGZ - resume a previous run from a directory or tarball,
                          where DIR points to a previously used tmp directory
                          (check for output 'Using DIR as tmp ...' of a previous
                          run) and TGZ is the path to a tarball which is
                          unpacked the tmp dir stored on the local storage space
                          (see option --storage above) [default: not set]
  -s | --save DIR/TGZ   - save contents of tmp directory to a tarball in
                          directory DIR or provided with the fixed full path TGZ
                          when a directory is provided, the format of the
                          tarball's name will be {REPO_ID}-{TIMESTAMP}.tgz
                          [default: not set]
  -v | --verbose        - display more information [default: false]

 If value for --mode is 'run', the SCRIPT provided is executed.
```
## Running commands or scripts with the container
### Run a command
### Run a script
### Run EESSI demo scripts

## Build a package for `/cvmfs/pilot.eessi-hpc.org`

## Use EESSI in a compute job
