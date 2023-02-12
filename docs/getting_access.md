# Getting access to EESSI

EESSI can be accessed via a native installation and via a container. First,
verify if EESSI is already accessible on your system.
## Verify access to EESSI
Run the command _(Note, this may take a couple of seconds to finish.)_
``` { .bash .copy }
ls /cvmfs/pilot.eessi-hpc.org
```
If you see a message like
```
host_injections  latest  versions
```
you already have access to EESSI on your system. :tada:

For starting to use EESSI, continue reading about
[Setting up environment](../../using_eessi/setting_up_environment).

If you see a message such as
```
ls: /cvmfs/pilot.eessi-hpc.org: No such file or directory
```
EESSI is not yet accessible on your system. No worries, you don't need to be
a :mage: to get access to EESSI. Continue reading about the
[Native installation](native_installation) of EESSI or
access via the [EESSI container](eessi_container).
