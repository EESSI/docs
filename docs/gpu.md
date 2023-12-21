# GPU support

!!! warning
    **The support for GPU software in EESSI is a work-in-progess.**

More information on the actions that must be performed to ensure that GPU software included in EESSI
can use the GPU in your system is available below.

[Please open a support issue](support.md) if you need help or have questions regarding GPU support.

This will be the docs page to replace https://www.eessi.io/docs/gpu/

## NVIDIA GPU support for EESSI on your system

EESSI supports running CUDA-enabled software. All CUDA-enabled modules are marked with the `(gpu)` feature when running `module avail`. However, for for CUDA-enabled software to run, it needs to be able to find the CUDA drivers of the host system. The challenge here is that CUDA drivers are not _always_ in a standard location. 

An additional requirement is necessary if someone wishes to compile new CUDA-enabled software via the CUDA module shipped with EESSI. This requires a full CUDA SDK, but the [CUDA SDK EULA](https://docs.nvidia.com/cuda/eula/index.html) does not allow for full redistribution of the SDK. We are only allowed to redistribute the files needed to _run_ CUDA code. Please note though: without a full CUDA SDK on the host system, you will still be able to run CUDA-enabled software from the EESSI stack, you just won't be able to compile new CUDA-enabled software.

Below, we describe how to make sure the EESSI software stack can find your CUDA drivers and (optionally) your full CUDA SDK.

### How it works: `host_injections`
In EESSI, a special directory has been prepared where host system administrators can install files which may be picked up by the EESSI shared software stack. This gives the ability to administrators to influence the behaviour (and capabilities) of the EESSI software stack.

This special directory is located in `/cvmfs/${EESSI_CVMFS_REPO}/host_injections`, and it is a CVMFS Variant Symlink: a symlink for which the target can be controlled by the CVMFS configuration on the client system (for more info, see ['Variant Symlinks' in the official CVMFS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#variant-symlinks)). Unless otherwise configured in the CVMFS client configuration for the EESSI repository, the `host_injections` symlink points to `/opt/eessi`.

As an example, let's imagine that we wish to use a architecture specific location on a shared filesystem as the target for the symlink. This has the advantage that one can make changes under `host_injections` that affect all nodes which share that CVMFS configuration. Configuring this in your CVMFS configuration would mean adding the following line in a CVMFS configuration file:

```
EESSI_HOST_INJECTIONS=/shared_fs/path
```

(After making a change to a CVMFS configuration file, you also need to reload the configuration with, e.g, `sudo cvmfs_config reload`) 

All CUDA-enabled software in EESSI expects the CUDA drivers to be in a specific subdirectory of this `host_injections` directory. Furthermore, all installations of the CUDA SDK in EESSI are stripped down to the files that we are allowed to redistribute. All other files are replaced to symlinks that point to another specific subdirectory of `host_injections`. If a full CUDA SDK is installed there, the CUDA module from EESSI can be used to build new CUDA software.


### Enabling GPU support for a native EESSI installation
Here, we describe the steps to enable GPU support when you have a native EESSI installation on your system, as described in [these docs](https://www.eessi.io/docs/getting_access/native_installation/).

!!! warning
    #### Requirements
    To enable GPU support for EESSI on your system, you will typically need to have system administration rights, since you need write permissions on the folder to the target directory of the `host_injections` symlink.

#### Enabling EESSI modules to find your GPU drivers

To install the symlinks to your GPU drivers in `host_injections`, run the script in `/cvmfs/${EESSI_PREFIX}/scripts/link_nvidia_host_libraries.sh`. This script uses `ldconfig` on your host system to locate your GPU drivers, and create symlinks to them in the correct location under `host_injections` directory. It also stores the CUDA version supported by the driver that the symlinks were created for.

You should re-run this script every time you update the drivers on the host system. Note that it is safe to re-run the script even if no driver updates were done: the script should detect that the current version of the drivers were already symlinked, and will exit.

#### Installing the CUDA SDK for integration with EESSI (optional)

To install the CUDA SDK under `host_injections`, run the script in `/cvmfs/${EESSI_PREFIX}/scripts/install_cuda_host_injections.sh`. 

As an example of executing this script, to install CUDA 12.1.1 in the `host_injections` directory, using `/path/to/tmpdir` as directory to store temporary files:
```
/cvmfs/${EESSI_PREFIX}/scripts/install_cuda_host_injections.sh --cuda-version 12.1.1 --temp-dir /path/to/tmpdir --accept-cuda-eula
```
You should choose the CUDA version you wish to install according to what CUDA versions are available as modules in the EESSI software stack.

You can run `/cvmfs/${EESSI_PREFIX}/scripts/install_cuda_host_injections.sh --help` to check all of the options.

Note that this script uses EasyBuild to install the CUDA SDK. For this to work, two requirements need to be satisfied: `module load EasyBuild` should work (or the `eb` command is already available in the environment), and the version of EasyBuild loaded/available should provide the requested version of the CUDA EasyConfig (in the example case: `CUDA-12.1.1.eb`). You can use the EasyBuild installation that comes with the EESSI software stack for this. Alternatively, you may load an EasyBuild module manually _before_ running the `install_cuda_host_injections.sh` script to make an `eb` command available.


### Enabling GPU support when using EESSI in a container

We focus here on the `apptainer`/`singularity` use case, and have only tested the `--nv` argument to enable GPU support within the container.

If you are using the [EESSI container](https://www.eessi.io/docs/getting_access/eessi_container/) to access the EESSI software, the procedure for enabling GPU support is slightly different and will be documented here eventually.

#### Enabling EESSI modules to find your GPU drivers

When using an `apptainer`/`singularity` container it is _not_ necessary to run the symlinking script since these containers use `LD_LIBRARY_PATH` internally in order to find GPU drivers.

The only scenario where this would be required is one where the `LD_LIBRARY_PATH` is modified/removed.
