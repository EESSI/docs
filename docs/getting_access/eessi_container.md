# EESSI container
The script `eessi_container.sh` provides a very easy and yet versatile means
to access EESSI. This page guides you through several example scenarios
illustrating the use of the script.

### Prerequisites
- Singularity 3.7.x / Apptainer 1.0.0 _or newer_ (support for `--fusemount` is
  required)
- `git`

### Preparation
Clone the [`EESSI/software-layer`](https://github.com/EESSI/software-layer.git)
repository and change into the `software-layer` directory by running the commands
``` { .bash .copy }
git clone https://github.com/EESSI/software-layer.git
cd software-layer
```

### Quickstart
Simply run the command (from the directory you have changed into above)
``` { .bash .copy }
./eessi_container.sh
```
!!! Note
    The first run may take a bit longer because the container image is
    downloaded and converted.

You should see output like
```
Using /tmp/eessi.EXAMPLE as tmp storage (add '--resume /tmp/eessi.EXAMPLE' to resume where this session ended).
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

To use EESSI, continue reading the section [Using EESSI](../../using_eessi).

## Viewing usage information for `eessi_container.sh`
The example in the [Quickstart](#quickstart) paragraph facilitates an
interactive session with read access to the EESSI pilot. It does so, because
the script `eessi_container.sh` uses some carefully chosen defaults. To view
all options of the script and its default values, run the command
``` { .bash .copy }
./eessi_container.sh --help
```
You should see the following output
```
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

So, the defaults are equal to running the command
``` { .bash .copy }
./eessi_container.sh --access ro --container docker://ghcr.io/eessi/build-node:debian11 --mode shell --repository EESSI-pilot
```
and it would either create a temporary directory under `${TMPDIR}` (if defined)
or `/tmp` (if `${TMPDIR}` is not defined).

## Reusing the previous session
You may have noted the following line in the output of `eessi_container.sh`
```
Using /tmp/eessi.EXAMPLE as tmp storage (add '--resume /tmp/eessi.EXAMPLE' to resume where this session ended).
```
!!! Note
    The parameter after `--resume` (`/tmp/eessi.EXAMPLE`) *will* be different
    when you run `eessi_container.sh`. Scroll back in your terminal and take
    note of it.
Try the following command to "resume" from the last session.
```
./eessi_container.sh --resume /tmp/eessi.EXAMPLE
```
This should run much faster because the container image has been cached in the
temporary directory (`/tmp/eessi.EXAMPLE` in the example above). You should
get to the prompt (`Singularity> ` or `Apptainer> `) and can use EESSI with
the _state_ where you left the previous session.
!!! Note
    The _state_ refers to what was stored on disk, not what was changed in
    memory. Particularly, any environment (variable) settings are not restored
    automatically.

    Because the `/tmp/eessi.EXAMPLE` directory contains a `home` directory which
    includes the saved history of your last session, you may easily restore
    the environment (variable) settings. Type `history` to see it. You should
    be able to access it as you would do in a normal terminal session.

## Running a simple command
## Running a script
## Running EESSI demo scripts
