# GPU support

More information on the actions that must be performed to ensure that GPU software included in EESSI
can use the GPU in your system is available below.

[Please open a support issue](../support.md) if you need help or have questions regarding GPU support.

!!! tip "Make sure the `${EESSI_VERSION}` version placeholder is defined!"
    In this page, we use `${EESSI_VERSION}` as a placeholder for the version of the EESSI repository,
    for example:
    ```{ .bash .copy }
    /cvmfs/software.eessi.io/versions/${EESSI_VERSION}
    ```

    Before inspecting paths, or executing any of the specified commands, you should define `$EESSI_VERSION` first,
    for example with:
    ```{ .bash .copy }
    export EESSI_VERSION=2023.06
    ```

## Support for using NVIDIA GPUs {: #nvidia }

EESSI supports running CUDA-enabled software. All CUDA-enabled modules are marked with the `(gpu)` feature,
which is visible in the output produced by `module avail`.

### NVIDIA GPU drivers {: #nvidia_drivers }

For CUDA-enabled software to run, it needs to be able to find the **NVIDIA GPU drivers** of the host system.
The challenge here is that the NVIDIA GPU drivers are not _always_ in a standard system location, and that we
can not install the GPU drivers in EESSI (since they are too closely tied to the client OS and GPU hardware).

### Compiling CUDA software {: #cuda_sdk }

An additional requirement is necessary if you want to be able to compile CUDA-enabled software using a CUDA installation included in EESSI. This requires a *full* CUDA SDK, but the [CUDA SDK End User License Agreement (EULA)](https://docs.nvidia.com/cuda/eula/index.html) does not allow for full redistribution. In EESSI, we are (currently) only allowed to redistribute the files needed to *run* CUDA software.

!!! note "Full CUDA SDK only needed to *compile* CUDA software"
    Without a full CUDA SDK on the host system, you will still be able to *run* CUDA-enabled software from the EESSI stack,
    you just won't be able to *compile* additional CUDA software.

Below, we describe how to make sure that the EESSI software stack can find your NVIDIA GPU drivers and (optionally) full installations of the CUDA SDK.

### Configuring CUDA driver location {: #driver_location }

All CUDA-enabled software in EESSI expects the CUDA drivers to be available in a specific subdirectory of this `host_injections` directory.
In addition, installations of the CUDA SDK included EESSI are stripped down to the files that we are allowed to redistribute;
all other files are replaced by symbolic links that point to another specific subdirectory of `host_injections`. For example:
```
$ ls -l /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen3/software/CUDA/12.1.1/bin/nvcc
lrwxrwxrwx 1 cvmfs cvmfs 109 Dec 21 14:49 /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen3/software/CUDA/12.1.1/bin/nvcc -> /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/amd/zen3/software/CUDA/12.1.1/bin/nvcc
```

If the corresponding full installation of the CUDA SDK is available there, the CUDA installation included in EESSI can be used to build CUDA software.


### Using NVIDIA GPUs via a native EESSI installation {: #nvidia_eessi_native }

Here, we describe the steps to enable GPU support when you have a [native EESSI installation](../getting_access/native_installation.md) on your system.

!!! warning "Required permissions"
    To enable GPU support for EESSI on your system, you will typically need to have system administration rights, since you need write permissions on the folder to the target directory of the `host_injections` symlink.

#### Exposing NVIDIA GPU drivers

To install the symlinks to your GPU drivers in `host_injections`, run the `link_nvidia_host_libraries.sh` script that is included in EESSI:

```{ .bash .copy }
/cvmfs/software.eessi.io/versions/${EESSI_VERSION}/scripts/gpu_support/nvidia/link_nvidia_host_libraries.sh
```

This script uses `ldconfig` on your host system to locate your GPU drivers, and creates symbolic links to them in the correct location under `host_injections` directory. It also stores the CUDA version supported by the driver that the symlinks were created for.

!!! tip "Re-run `link_nvidia_host_libraries.sh` after NVIDIA GPU driver update"
    You should re-run this script every time you update the NVIDIA GPU drivers on the host system.

    Note that it is safe to re-run the script even if no driver updates were done: the script should detect that the current version of the drivers were already symlinked.

#### Installing full CUDA SDK (optional)

To install a full CUDA SDK under `host_injections`, use the `install_cuda_host_injections.sh` script that is included in EESSI:

```{ .bash .copy }
/cvmfs/software.eessi.io/versions/${EESSI_VERSION}/scripts/gpu_support/nvidia/install_cuda_host_injections.sh
```

For example, to install CUDA 12.1.1 in the directory that the [`host_injections` variant symlink](host_injections.md) points to,
using `/tmp/$USER/EESSI` as directory to store temporary files:
```
/cvmfs/software.eessi.io/versions/${EESSI_VERSION}/scripts/gpu_support/nvidia/install_cuda_host_injections.sh --cuda-version 12.1.1 --temp-dir /tmp/$USER/EESSI --accept-cuda-eula
```
You should choose the CUDA version you wish to install according to what CUDA versions are included in EESSI;
see the output of `module avail CUDA/` after [setting up your environment for using
EESSI](../using_eessi/setting_up_environment.md).

You can run `/cvmfs/software.eessi.io/scripts/install_cuda_host_injections.sh --help` to check all of the options.

!!! tip

    This script uses EasyBuild to install the CUDA SDK. For this to work, two requirements need to be satisfied:

    * `module load EasyBuild` should work (or the `eb` command is already available in the environment);
    * The version of EasyBuild being used should provide the requested version of the CUDA easyconfig file
      (in the example case above, that's `CUDA-12.1.1.eb`).

    You can rely on the EasyBuild installation that is included in EESSI for this.

    Alternatively, you may load an EasyBuild module manually _before_ running the `install_cuda_host_injections.sh`
    script to make an `eb` command available.


### Using NVIDIA GPUs via EESSI in a container {: #nvidia_eessi_container }

We focus here on the [Apptainer](https://apptainer.org/)/[Singularity](https://sylabs.io/singularity) use case,
and have only tested the [`--nv` option](https://apptainer.org/docs/user/latest/gpu.html#nvidia-gpus-cuda-standard)
to enable access to GPUs from within the container.

If you are using the [EESSI container](../getting_access/eessi_container.md) to access the EESSI software,
the procedure for enabling GPU support is slightly different and will be documented here eventually.

#### Exposing NVIDIA GPU drivers

When running a container with `apptainer` or `singularity` it is _not_ necessary to run the `install_cuda_host_injections.sh`
script since both these tools use `$LD_LIBRARY_PATH` internally in order to make the host GPU drivers available
in the container.

The only scenario where this would be required is if `$LD_LIBRARY_PATH` is modified or undefined.

### Testing the GPU support {: #gpu_cuda_testing }

The quickest way to test if software installations included in  EESSI can access and use your GPU is to run the
`deviceQuery` executable that is part of the `CUDA-Samples` module:
```
module load CUDA-Samples
deviceQuery
```
If both are successful, you should see information about your GPU printed to your terminal.
