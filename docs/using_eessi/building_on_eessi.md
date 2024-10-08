# Building software on top of EESSI

## Building software on top of EESSI with EasyBuild
Building on top of EESSI with EasyBuild is relatively straightforward. One crucial feature is that EasyBuild supports building against operating system libraries that are _not_ in a standard prefix (such as `/usr/lib`). This is required when building against EESSI, since all of the software in EESSI is built against the [compatibility layer](../compatibility_layer.md).

### Starting the EESSI software environment
Start your environment as described [here](../using_eessi/setting_up_environment.md)

### Using the EESSI-extend module
The `EESSI-extend` module facilitates building on top of EESSI using EasyBuild. It does a few key things:

1. It configures EasyBuild to match how the rest of the EESSI software is built
2. It configures EasyBuild to use a certain installation path (e.g. in your homedir), taking into account the hardware architecture you are building on
3. It adds the relevant subdirectory from your installation path to your `MODULEPATH`, to make sure your newly installed modules are available
4. It loads the EasyBuild module

The `EESSI-extend` module recognizes a few environment variables. To print an up-to-date list, check the module itself
```
module help EESSI-extend/2023.06-easybuild
```

The installation prefix is determined by `EESSI-extend` through the following logic:
1. If `EESSI_CVMFS_INSTALL` is set, software is installed in `EESSI_SOFTWARE_PATH`. This variable shouldn't be used by users and would only be used by CVMFS administrators of the EESSI repository.
2. If `EESSI_SITE_INSTALL` is set and the EESSI site installation prefix (`/cvmfs/software.eessi.io/host_injections/...`) is writeable, this prefix will be used. This is typically where sites hosting a system that has EESSI deployed would install additional software on top of EESSI and make it available to all their users.
3. If `EESSI_PROJECT_INSTALL` is set (and `EESSI_USER_INSTALL` is not set), this prefix will be used. You should use this if you want to install additional software on top of EESSI that should also be usable by your project partners on the same system.
4. If `EESSI_USER_INSTALL` is set, this prefix will be used. You should use this if yo uwant to install additional software on top of EESSI just for your own user.
If none of the above apply, the default is a user installation in `$HOME/EESSI` (i.e. effectively the same as setting `EESSI_USER_INSTALL=$HOME/EESSI`).

Here, we assume you are just an end-user, not having set any of the above environment variables, and loading the `EESSI-extend` module with the default installation prefix:

```
module load EESSI-extend/2023.06-easybuild
```

Now, if we check the EasyBuild configuration


```
eb --show-config
allow-loaded-modules (E) = EasyBuild, EESSI-extend
buildpath            (E) = /tmp/<user>/easybuild/build
containerpath        (E) = /tmp/<user>/easybuild/containers
debug                (E) = True
experimental         (E) = True
filter-deps          (E) = Autoconf, Automake, Autotools, binutils, bzip2, DBus, flex, gettext, gperf, help2man, intltool, libreadline, libtool, M4, makeinfo, ncurses, util-linux, XZ, zlib
filter-env-vars      (E) = LD_LIBRARY_PATH
hooks                (E) = /cvmfs/software.eessi.io/versions/2023.06/init/easybuild/eb_hooks.py
ignore-osdeps        (E) = True
installpath          (E) = /home/<user>/eessi/versions/2023.06/software/linux/x86_64/amd/zen2
module-extensions    (E) = True
packagepath          (E) = /tmp/<user>/easybuild/packages
prefix               (E) = /tmp/<user>/easybuild
read-only-installdir (E) = True
repositorypath       (E) = /tmp/<user>/easybuild/ebfiles_repo
robot-paths          (D) = /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/software/EasyBuild/4.9.4/easybuild/easyconfigs
rpath                (E) = True
sourcepath           (E) = /tmp/<user>/easybuild/sources
sticky-bit           (E) = True
sysroot              (E) = /cvmfs/software.eessi.io/versions/2023.06/compat/linux/x86_64
trace                (E) = True
umask                (E) = 077
zip-logs             (E) = bzip2
```

Apart from the `installpath`, this is exactly how EasyBuild is configured when software is built for EESSI itself.

!!! note
    Be aware that `EESSI-extend` will optimize the installation for your current hardware architecture, and the `installpath` also contains this architecture in it's directory structure (just like regular EESSI installations do). This means you should run the installation on the node type on which you also want to use the software. If you want the installation to be present for multiple node types, you can simply run it once on each type of node.

And, if we check our `MODULEPATH`, we see that the `installpath` that EasyBuild will use here is prepended
```
$ echo $MODULEPATH
/home/<user>/eessi/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all:...
```

### Building
Now, you are ready to build. For example, suppose you want to install `netcdf4-python-1.6.5-foss-2023b.eb` (which is not present at the time of writing), you run:

```
eb netcdf4-python-1.6.5-foss-2023b.eb
```

!!! Note
    If this netCDF for python module is available by the time you are trying, you can force a local rebuild by adding the `--rebuild` argument in order to experiment with building locally, or pick a different EasyConfig to build.

### Using the newly built module

If the installation was done in the site installation path (i.e. `EESSI_SITE_INSTALL` was set, and things were installed in `/cvmfs/software.eessi.io/host_injections/...`), the modules are available by default to anyone who has initialized the EESSI software environment.

If the installation through `EESSI-extend` was done in a `EESSI_PROJECT_INSTALL` or `EESSI_USER_INSTALL` location, one has to make sure to load the `EESSI-extend` module before loading the module of interest, since this adds those prefixes to the `MODULEPATH`.

If we don't have the `EESSI-extend` module loaded, it will not find any modules installed in the `EESSI_PROJECT_INSTALL` or `EESSI_USER_INSTALL` locations:
```
$ module unload EESSI-extend
$ module av netcdf4-python/1.6.5-foss-2023b
No module(s) or extension(s) found!
```

But, if we load `EESSI-extend` first:

```
$ module load EESSI-extend/2023.06-easybuild
$ module av netcdf4-python/1.6.5-foss-2023b

---- /home/<user>/eessi/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all ----
   netcdf4-python/1.6.5-foss-2023b
```


This means you'll _always_ need to load the `EESSI-extend` module if you want to use these modules (also, and particularly when you want to use them in a job script).

## Manually building software op top of EESSI
Building software on top of EESSI would require your linker to use the same system-dependencies as the software in EESSI does. In other words: it requires you to link against libraries from the compatibility layer, instead of from your host OS.

While we plan to support this in the future, manually building on top of EESSI is currently not supported yet in a trivial way.
