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

## Help for `eessi_container.sh`
The example in the [Quickstart](#quickstart) paragraph facilitates an
interactive session with read access to the EESSI pilot software stack. It
does not require any command-line arguments, because the script
`eessi_container.sh` uses some carefully chosen defaults. To view
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

The remainder of this page will demonstrate different scenarios using some of
the command-line arguments used for read-only access. Other arguments will be
discussed in a yet-to-be written section covering adding software to the EESSI
stack.

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
``` { .bash .copy }
./eessi_container.sh --resume /tmp/eessi.EXAMPLE
```
This should run much faster because the container image has been cached in the
temporary directory (`/tmp/eessi.EXAMPLE`). You should
get to the prompt (`Singularity> ` or `Apptainer> `) and can use EESSI with
the _state_ where you left the previous session.
!!! Note
    The _state_ refers to what was stored on disk, not what was changed in
    memory. Particularly, any environment (variable) settings are not restored
    automatically.

    Because the `/tmp/eessi.EXAMPLE` directory contains a `home` directory which
    includes the saved history of your last session, you may easily restore
    the environment (variable) settings. Type `history` to see which commands
    you ran. You should be able to access the history as you would do in a
    normal terminal session.

## Running a simple command
We run the command `ls /cvmfs/pilot.eessi-hpc.org` through the script
`eessi_container.sh` to verify if the CernVM-FS repository of
the EESSI pilot is accessible.
``` { .bash .copy }
./eessi_container.sh --mode run ls /cvmfs/pilot.eessi-hpc.org
```
You should see an output such as
```
Using /tmp/eessi.EXAMPLE as tmp storage (add '--resume /tmp/eessi.EXAMPLE' to resume where this session ended).$
Launching container with command (next line):
singularity run --fusemount container:cvmfs2 pilot.eessi-hpc.org /cvmfs/pilot.eessi-hpc.org docker://ghcr.io/eessi/build-node:debian11 ls /cvmfs/pilot.eessi-hpc.org
CernVM-FS: pre-mounted on file descriptor 3
CernVM-FS: loading Fuse module... done
host_injections  latest  versions
```
After the script has run you are now back in the session where you ran
`eessi_container.sh` not inside the container. This is because of the
command-line argument `--mode run`.

!!! Note
    The last line is the contents of the directory
    `/cvmfs/pilot.eessi-hpc.org`.

    Also, not that there is not container prompt (`Singularity>` or
    `Apptainer>`).

Alternatively to specify the command as we did above, you can also do the
following.
``` { .bash .copy }
RUN_CMD_FROM_VARIABLE="ls -l /cvmfs/pilot.eessi-hpc.org"
./eessi_container.sh --mode shell <<< ${RUN_CMD_FROM_VARIABLE}
```

!!! Note
    We changed the mode from `run` to `shell` because we use a different method
    to let the script run _our_ command.

Because `shell` is the default value for `--mode` we can also omit this and
simply run
``` { .bash .copy }
RUN_CMD_FROM_VARIABLE="ls -l /cvmfs/pilot.eessi-hpc.org"
./eessi_container.sh <<< ${RUN_CMD_FROM_VARIABLE}
```

## Running a script
While running simple command can be sufficient in some cases, you often want
to run scripts containing many commands. To run the script
`eessi_architectures.sh` shown below (create it in your current directory, then
make it executable with `chmod +x eessi_architectures.sh`)
``` { .bash .copy }
#!/usr/bin/env bash
# This script determines which architectures are included in the
# latest EESSI pilot version. It makes use of the specifc directory
# structure in the EESSI pilot repository.
#
# determine which OS types
BASE=${EESSI_CVMFS_REPO:-/cvmfs/pilot.eessi-hpc.org}/latest/software
cd ${BASE}
for os_type in $(ls -d *)
do
    # determine architecture families
    OS_BASE=${BASE}/${os_type}
    cd ${OS_BASE}
    for arch_family in $(ls -d *)
    do
        # determine CPU microarchitectures
        OS_ARCH_BASE=${BASE}/${os_type}/${arch_family}
        cd ${OS_ARCH_BASE}
        for microarch in $(ls -d *)
        do
            case ${microarch} in
                amd | intel )
                    for sub in $(ls ${microarch})
                    do
                        echo "${os_type}/${arch_family}/${microarch}/${sub}"
                    done
                    ;;
                * )
                    echo "${os_type}/${arch_family}/${microarch}"
                    ;;
            esac
        done
    done
done
```
Run the script as follows
``` { .bash .copy }
./eessi_container.sh --mode shell < eessi_architectures.sh
```
The output should be similar to
``` { .yaml linenums="1" }
Using /tmp/eessi.EXAMPLE as tmp storage (add '--resume /tmp/eessi.EXAMPLE' to resume where this session ended).$
Launching container with command (next line):
singularity shell --fusemount container:cvmfs2 pilot.eessi-hpc.org /cvmfs/pilot.eessi-hpc.org docker://ghcr.io/eessi/build-node:debian11
CernVM-FS: pre-mounted on file descriptor 3
CernVM-FS: loading Fuse module... done
linux/aarch64/generic
linux/aarch64/graviton2
linux/aarch64/graviton3
linux/ppc64le/generic
linux/ppc64le/power9le
linux/x86_64/amd/zen2
linux/x86_64/amd/zen3
linux/x86_64/generic
linux/x86_64/intel/haswell
linux/x86_64/intel/skylake_avx512
```
Lines 6 to 16 show the output of the script `eessi_architectures.sh`.

If you want to use the mode `run`, you have to make the script's location
available inside the container. You can do that by mapping the current directory
(which contains `eessi_architectures.sh`) to any not-yet existing directory
inside the container using the `SINGULARITY_BIND` or
`APPTAINER_BIND` variable. For example,
``` { .bash .copy }
SINGULARITY_BIND=${PWD}:/scripts ./eessi_container.sh --mode run /scripts/eessi_container.sh
```

## Running EESSI demos
If you want to run some more complex scripts using software provided through
EESSI, continue reading about [Running EESSI demos](../../using_eessi/eessi_demos).
