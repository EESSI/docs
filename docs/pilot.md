## Pilot software stack (2020.08)

### Caveats

The current EESSI pilot software stack (version 2020.08) is the first iteration,
and there are some known issues and limitations, please take these into account:

* First of all: the EESSI pilot software stack is **NOT READY FOR PRODUCTION!**

  Do not use it for production work, and be careful when testing it on production systems!

* The software is currently only installed for systems compatible with Intel Haswell processors.
  Installations tuned for other CPU architectures are not available yet (but are hopefully coming soon).

* There is no Lmod (spider) cache available yet for the environment module files included in the pilot repository,
  so `module` commands may be somewhat slow.

* The provided Open MPI installation (`OpenMPI/4.0.3-GCC-9.3.0` module) is not properly configured yet to use high-speed network interconnects.


### Accessing the EESSI pilot repository through Singularity

The easiest way to access the EESSI pilot repository is by using Singularity.
If Singularity is installed already, no admin privileges are required. No other software is needed either on the host.

A container image is available in Docker Hub (see https://hub.docker.com/r/eessi/client-pilot).
It only contains a minimal operating system + the necessary packages to access the EESSI pilot repository through CernVM-FS.

The container image can be used directly by Singularity (no prior download required), as follows:

* First, create some local directories in `/tmp/$USER` which will be bind mounted in the container:
  ```shell
  mkdir -p /tmp/$USER/{var-lib-cvmfs,var-run-cvmfs,home}
  ```
  These provides space for the CernVM-FS cache, and an empty home directory to use in the container.

* Set the `$SINGULARITY_BIND` and `$SINGULARITY_HOME` environment variables to configure Singularity:
  ```shell
  export SINGULARITY_BIND="/tmp/$USER/var-run-cvmfs:/var/run/cvmfs,/tmp/$USER/var-lib-cvmfs:/var/lib/cvmfs"
  export SINGULARITY_HOME="/tmp/$USER/home:/home/$USER"
  ```

* Start the container using `singularity shell`, using `--fusemount` to mount the EESSI config and pilot repositories
  (using the `cvmfs2` command that is included in the container image):
  ```shell
   export EESSI_CONFIG="container:cvmfs2 cvmfs-config.eessi-hpc.org /cvmfs/cvmfs-config.eessi-hpc.org"
   export EESSI_PILOT="container:cvmfs2 pilot.eessi-hpc.org /cvmfs/pilot.eessi-hpc.org"
   singularity shell --fusemount "$EESSI_CONFIG" --fusemount "$EESSI_PILOT" docker://eessi/client-pilot:centos7-2020.08
   ```

 * This should give you a shell in the container, where the EESSI config and pilot repositories are mounted:
   ```
   $ singularity shell --fusemount "$EESSI_CONFIG" --fusemount "$EESSI_PILOT" docker://eessi/client-pilot:centos7-2020.08
   INFO:    Using cached SIF image
   CernVM-FS: pre-mounted on file descriptor 3
   CernVM-FS: pre-mounted on file descriptor 3
   CernVM-FS: loading Fuse module... done
   CernVM-FS: loading Fuse module... done
   Singularity>
   ```
 * It is possible that you see some scary looking warnings, but those can be ignored for now.
   To verify that things are working, check the contents of the `/cvmfs/pilot.eessi-hpc.org/2020.08` directory:
   ```shell
   Singularity> ls /cvmfs/pilot.eessi-hpc.org/2020.08
   compat  init  software
   ```
### Setting up the EESSI environment

Once you have the EESSI pilot repository mounted, you can set up the environment by sourcing the provided init script:

```shell
source /cvmfs/pilot.eessi-hpc.org/2020.08/init/bash
```

If all goes well, you should see output like this:

```shell
Singularity> source /cvmfs/pilot.eessi-hpc.org/2020.08/init/bash

Found EESSI pilot repo @ /cvmfs/pilot.eessi-hpc.org/2020.08!
Derived subdirectory for software layer: x86_64/intel/haswell
Using x86_64/intel/haswell subdirectory for software layer (HARDCODED)
Initializing Lmod...
Prepending /cvmfs/pilot.eessi-hpc.org/2020.08/software/x86_64/intel/haswell/modules/all to $MODULEPATH...
Environment set up to use EESSI pilot software stack, have fun!

[EESSI pilot 2020.08] $
```

Now you're all set up! Go ahead and explore the software stack using "`module avail`", and go wild with testing the available software installations!

### Testing the EESSI pilot software stack

Please test the EESSI pilot software stack as you see fit: running simple commands, performing small calculations or running small benchmarks, etc.

Test scripts that have been verified to work correctly using the pilot software stack are available at https://github.com/EESSI/software-layer/tree/master/tests .

### Giving feedback or reporting problems

Any feedback is welcome, and questions or problems reports are welcome as well, through one of the EESSI communication channels:

* (**preferred!**) EESSI `software-layer` GitHub repository: https://github.com/EESSI/software-layer/issues 
* EESSI mailing list (`eessi@list.rug.nl`)
* EESSI Slack (https://eessi-hpc.slack.com, get an invite via https://www.eessi-hpc.org/join)
* EESSI `software-layer` GitHub repository: https://github.com/EESSI/software-layer/issues
* monthly EESSI meetings (first Thursday of the month at 2pm CEST)
