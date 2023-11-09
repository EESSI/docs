# Is EESSI accessible?

EESSI can be accessed via [a native (CernVM-FS) installation](native_installation.md),
or via [a container that includes CernVM-FS](eessi_container.md).

Before you look into these options, check if EESSI is already accessible on your system.

Run the following command:
``` { .bash .copy }
ls /cvmfs/pilot.eessi-hpc.org
```

!!! note

    This ``ls`` command may take a couple of seconds to finish, since CernVM-FS may need to download
    or update the metadata for that directory.

If you see output like shown below, **you already have access to EESSI on your system**. :tada:
```
host_injections  latest  versions
```

For starting to use EESSI, continue reading about
[Setting up environment](../using_eessi/setting_up_environment.md).

If you see an error message as shown below, **EESSI is not yet accessible on your
system**.
```
ls: /cvmfs/pilot.eessi-hpc.org: No such file or directory
```
No worries, you don't need to be a :mage: to get access to EESSI.

Continue reading about the [Native installation](native_installation.md) of EESSI,
or access via the [EESSI container](eessi_container.md).
