# Site builds on top of a shared file system

For this approach we use a shared file system for doing site installations on top of EESSI.

The setup for this approach is very simple, and it allows you to quickly get started with making additional installations available to the users of your infrastructure.

## Requirements

The following setup is needed, and we assume this is already in place:

- EESSI is available on your build nodes (note that you still need to build on every CPU type that you want to support)
  - See the [native installation page](../getting_access/native_installation.md) for instructions
- A shared file system to make the software installations available on all your nodes
- A user account with write access to the shared file system
- Optionally: Singularity or Apptainer to do the builds in a controlled and isolated environment

Ideally, you already have some workflow or automation in place to build software for your different node types.
It should be straightforward to adapt these for building on top of EESSI.

## Initialize EESSI and EESSI-extend

To get started, we need to initialize EESSI and load EESSI-extend on a build node, and we configure the EESSI environment for site installations.
This ensures that the installation directories will become world-readable.
By default, site installations will end up in the EESSI [host injections directory](../site_specific_config/host_injections.md).
If you have not configured this directory yet, it will point to `/opt/eessi`, meaning that your software installations will end up there as well.
Often you would want to use the host injections directory for node-specific files like GPU drivers,
while we would like the software installations to end up on the shared file system.
By setting the environment variable `$EESSI_SITE_SOFTWARE_PREFIX` before loading EESSI and EESSI-extend,
we can adjust the site software installation prefix and point it to the shared file system:

``` { .bash .copy }
export EESSI_SITE_INSTALL=1
export EESSI_SITE_SOFTWARE_PREFIX=/sharedfs/eessi
module load EESSI/2025.06
module load EESSI-extend
```

!!! note

    Note that we have to pick a specific EESSI version here, depending on the toolchain of the software that we want to install.
    See [EESSI versions](../repositories/versions/) for more information about the different EESSI versions.

## Start building

The environment should now be configured for doing site installations to the chosen prefix.
The `EESSI-extend` module automatically loads `EasyBuild`, and to be sure you can check its configuration:
``` { .bash .copy }
$ eb --show-config

#
# Current EasyBuild configuration
# (C: command line argument, D: default value, E: environment variable, F: configuration file)
#
allow-loaded-modules                     (E) = EasyBuild, EESSI-extend
buildpath                                (E) = /tmp/user/easybuild/build
bwrap-installpath                        (E) = /tmp/user/easybuild/bwrap
containerpath                            (E) = /tmp/user/easybuild/containers
cuda-sanity-check-error-on-failed-checks (E) = True
debug                                    (E) = True
experimental                             (E) = True
fail-on-mod-files-gcccore                (E) = True
filter-deps                              (E) = binutils, bzip2, DBus, flex, gettext, gperf, help2man, intltool, libreadline, makeinfo, ncurses, NVPL, ParMETIS, util-linux, XZ, zlib
filter-env-vars                          (E) = LD_LIBRARY_PATH
hooks                                    (E) = /cvmfs/software.eessi.io/versions/2025.06/init/easybuild/eb_hooks.py
ignore-osdeps                            (E) = True
installpath                              (E) = /sharedfs/eessi/versions/2025.06/software/linux/x86_64/amd/zen3
...
```

Now, we can start building, e.g.:

``` { .bash .copy }
eb -r attr-2.5.2-GCCcore-14.3.0.eb
eb -r cowsay-3.04.eb
```

When the installation has completed, the software should be available in your prefix.

## Container

Instead of doing the builds on the host system itself, you could consider doing them in a container.
Using a minimal build container minimizes the risk of accidentally picking up host libraries (instead of the ones provided by EESSI),
and a container also provides a controlled and isolated environment.

In principle you could use any container, as long as you make sure that both the EESSI CVMFS repository and your shared file system are available in the container.
Assuming both are available on the build host, you can simply bind mount both of them into the container.

You can also use the [`eessi_container.sh` script](https://github.com/EESSI/software-layer-scripts/blob/main/eessi_container.sh), provided by EESSI,
which mounts the EESSI CVMFS repository inside the EESSI build container. In order to also bind mount your shared file system, you can use:
``` { .bash .copy }
eessi_container.sh -b $EESSI_SITE_SOFTWARE_PREFIX
```

In the container you can then use the same build procedure as described before.


## Using the software
The EESSI module should make sure that site installations are automatically picked up by the module environment,
as long as you make sure that `$EESSI_SITE_SOFTWARE_PREFIX` is always set to your prefix before loading the `EESSI` module:

``` { .bash .copy }
export EESSI_SITE_SOFTWARE_PREFIX=/sharedfs/eessi
module load EESSI/2025.06
module avail
```
This should show something like:
``` { .bash .copy }
---- /sharedfs/eessi/versions/2025.06/software/linux/x86_64/amd/zen3/modules/all ----
   attr/2.5.2-GCCcore-14.3.0    cowsay/3.04

---- /cvmfs/software.eessi.io/versions/2025.06/software/linux/x86_64/amd/zen3/modules/all ----
   Abseil/20240722.0-GCCcore-13.3.0
   absl-py/2.1.0-GCCcore-13.3.0
   ...
```

As you can see, EESSI installed it into a CPU-specific directory under the chosen prefix.
This allows you to redo the installation on other CPU types that you want to support,
such that each of them has access to an optimized installation.
Every time the EESSI module gets loaded, it will detect the CPU of that node and use the corresponding subtree in your prefix.

You can now simply load the software using:

``` { .bash .copy }
module load cowsay/3.04 
cowsay "EESSI keeps the clusters moo-ving."
 ____________________________________ 
< EESSI keeps the clusters moo-ving. >
 ------------------------------------ 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

```

