# Using EESSI

There are different means to access EESSI depending on if and how it is set up on
your system.

### Determine whether EESSI is already set up on your system
If you run the command _(Note, this may take a while to finish.)_
```bash
ls /cvmfs/pilot.eessi-hpc.org
```
and see a message like
```
2021.06  host_injections  latest  versions
```
EESSI has been set up on your system already. :tada: Continue reading about using
EESSI via the [Native CernVM-FS client](cvmfs_client).

If you see a message such as
```
ls: /cvmfs/pilot.eessi-hpc.org: No such file or directory
```
EESSI has not been set up yet. No worries, you don't need to be a :mage: to get
access to EESSI. Continue reading about [Accessing EESSI via a
container](eessi_container).
