# Using EESSI

Using the software installations provided by the EESSI CernVM-FS repository `software.eessi.io`
is fairly straightforward.

Let's break it down step by step.

## 0) Is EESSI available?

First, check whether the EESSI [CernVM-FS](../cvmfs/what-is-cvmfs.md) repository is available on your system.

Try checking the contents of the `/cvmfs/software.eessi.io` directory with the `ls` command:

```bash
$ ls /cvmfs/software.eessi.io
README.eessi  host_injections  versions
```

If you see an error message like "`No such file or directory`", then either the CernVM-FS client
is not installed on your system, or the configuration for the EESSI repository is not available.
In that case, you may want to revisit the [Accessing a CernVM-FS repository](../access/index.md) section,
or go through the [Troubleshooting](../troubleshooting.md) section.

??? note "Don't be fooled by `autofs` *(click to expand)*"

    The `/cvmfs` directory may seem empty at first, because CernVM-FS repositories are automatically mounted
    as they are accessed via [`autofs`](https://www.kernel.org/doc/html/latest/filesystems/autofs.html).

    So rather than just using "`ls /cvmfs/`" to check which CernVM-FS repositories are available on your system,
    you should try to directly access a specific repository as shown above for EESSI with `ls /cvmfs/software.eessi.io` .

    For more information on various aspects of mounting of CernVM-FS repositories, [see the CernVM-FS documentation](
    https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#mounting).

## 1) Initialise shell environment {: #init }

If the EESSI repository is available, you can proceed to preparing your shell environment for using
a particular version of EESSI by *sourcing* the provided initialisation script by running the `source` command:

```shell
$ source /cvmfs/software.eessi.io/versions/2023.06/init/bash
Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
archdetect says x86_64/amd/zen2
Using x86_64/amd/zen2 as software subdirectory.
Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all as the directory to be added to MODULEPATH.
Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/.lmod/lmodrc.lua
Initializing Lmod...
Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all to $MODULEPATH...
Environment set up to use EESSI (2023.06), have fun!
```

??? note "Details on changes made to the shell environment *(click to expand)*"

    The initialisation script is a simple bash script that changes a couple of environment variables:

    * A set of `$EESSI_*` environment variables is defined;
    * The `$PS1` environment variable that specifies the [shell prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt)
      is updated to indicate that your shell session has been initialised for EESSI;
    * The location of the tools provided by the EESSI compatibility layer are prepended to the `$PATH` environment variable;
    * Lmod, which is included in the EESSI compatibility layer, is initialised to ensure that the `module` command is defined,
      and that the Lmod spider cache that is included in the EESSI software layer is picked up;
    * The location to the software installations that are optimised for the CPU microarchitecture of the client system
      is prepended to the `$MODULEPATH` environment variable by running a "`module use`" command.

Note how the CPU microarchitecture is being auto-detected, which determines which path that points to a set of
environment module files is used to update `$MODULEPATH`.

This ensures that the modules that will be loaded provide access to software installations from the EESSI software
layer that are *optimised* for the system you are using EESSI on.


## 2) Load module(s)

After initialising your shell environment for using EESSI, you can start exploring the EESSI software layer
using the `module` command.

Using `module avail` (or `ml av`), you can check which software is available.
Without extra arguments, `module avail` will produce an overview of *all* available software.
By passing an extra argument you can filter the results and search for specific software:

```shell
$ module avail tensorflow

----- /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all -----
    
    TensorFlow/2.13.0-foss-2023a
```

To start *using* software you should *load* the corresponding environment module files
using `module load` (or `ml`). For example:

```shell
$ module load TensorFlow/2.13.0-foss-2023a
```

A `module load` command usually does not produce any output, but it updates your shell environment
to make the software ready to use.

For more information on the `module` command, see the
[User Guide for Lmod](https://lmod.readthedocs.io/en/latest/010_user.html).

## 3) Use software

After loading a module, you should be able to use the corresponding software.

For example, after loading the `TensorFlow/2.13.0-foss-2023a` module, you can start a Python session
and play with the `tensorflow` Python package:

```python
$ python
>>> import tensorflow as tf
>>> tf.__version__
'2.13.0'
```

Keep in mind that you are using a Python installation provided by the EESSI software layer here,
*not* the Python version that may be provided by your client OS:

```shell
$ command -v python
/cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen2/software/Python/3.11.3-GCCcore-12.3.0/bin/python
```

??? note "Initial start-up delay *(click to expand)*"

    You may notice a bit of "lag" initially when starting to use software provided by the EESSI software layer.

    This is expected, since CernVM-FS may need to first download the files that are required
    to run the software you are using;
    see also [On-demand downloading of files and metadata](../cvmfs/what-is-cvmfs.md#features-ondemand).

    You should not observe any significant start-up delays anymore when running the same software shortly after,
    since then CernVM-FS will be able to serve the necessary files from the local client cache;
    see also [Multi-level caching](../cvmfs/what-is-cvmfs.md#features-caching).

---

*(next: [Getting support for EESSI](support.md))*
