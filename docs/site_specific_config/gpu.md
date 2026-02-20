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

### Configuring runtime support {: #nvidia_drivers}

For CUDA-enabled software to run, it needs to be able to find the **NVIDIA GPU drivers** of the host system.
The challenge here is that the NVIDIA GPU drivers are not _always_ in a standard system location, and that we
can not install the GPU drivers in EESSI (since they are too closely tied to the client OS and GPU hardware).

#### Enabling runtime support for a native EESSI installation (using the helper script) {: #nvidia_eessi_native }

To get runtime support, we need to ensure that the EESSI runtime linker can find the drivers. To do this, we symlink the drivers
in a predictable location that is searched by the EESSI runtime linker.

*Step 1:* [initialize a version of EESSI](../using_eessi/setting_up_environment.md).

*Step 2 (EESSI 2025.06 and newer, mandatory):* define the `EESSI_NVIDIA_OVERRIDE_DEFAULT` variable in your local CernVM-FS configuration to point to a directory where you want
to store the symlinks to the drivers. For example, to store these under `/opt/eessi/nvidia`, one would run:

```{ .bash .copy }
sudo bash -c "echo 'EESSI_NVIDIA_OVERRIDE_DEFAULT=/opt/eessi/nvidia' >> /etc/cvmfs/default.local"
```

*Step 2 (EESSI 2023.06, optional):* Change the location in which the symlinks will end up by configuring `EESSI_HOST_INJECTIONS` explicitly (default: `/opt/eessi`):

```{ .bash copy }
sudo bash -c "echo 'EESSI_HOST_INJECTIONS=/desired/path/to/host/injections' >> /etc/cvmfs/default.local"
```

*Step 3:* To actually reconfigure the variant symlinks, reload the updated CernVM-FS configuration using:
```{ .bash copy }
sudo cvmfs_config reload software.eessi.io
```

*Step 4:* Run the helper script:

```{ .bash .copy }
/cvmfs/software.eessi.io/versions/${EESSI_VERSION}/scripts/gpu_support/nvidia/link_nvidia_host_libraries.sh
```

!!! tip "Rerun script after each driver update"
    You should re-run this script every time you update the NVIDIA GPU drivers on the host system, as it may expose libraries that are new to your driver version.
    Note that it is safe to re-run the script even if no driver updates were done: the script should detect that the current version of the drivers were already symlinked.

!!! tip "Maintaining different driver versions for each EESSI version"
    The standard approach for EESSI >= 2025.06 means that the drivers may be found by any EESSI version. If you prefer to create one set of symlinks per EESSI
    version, instead of defining a single location through EESSI_NVIDIA_OVERRIDE_DEFAULT, you can define one per EESSI version, by setting EESSI_<VERSION>_NVIDIA_OVERRIDE.
    For example:
    ```{ .bash .copy}
    sudo bash -c "echo 'EESSI_202506_NVIDIA_OVERRIDE=/opt/eessi/2025.06/nvidia' >> /etc/cvmfs/default.local"
    ```

!!! tip "Use a EESSI-specific CernVM-FS configuration file to configure the variant symlinks"
    Instead of using `/etc/cvmfs/default.local` you can also put the symlink configuration in a local configuration file that is specific to the `software.eessi.io` repository
    or to the `eessi.io` domain.
    For the first you can use `/etc/cvmfs/config.d/software.eessi.io.local`, while for the latter you can use `/etc/cvmfs/domain.d/eessi.io.local`.
    For more details about the different configuration files, 
    see [the configuration hierarchy section of our CernVM-FS tutorial](https://www.eessi.io/docs/training-events/2025/tutorial-best-practices-cvmfs-hpc/access/client/#configuration_hierarchy).

!!! note "How does EESSI find the linked drivers?"

    The runtime linker provided by the EESSI [compatibility layer](../compatibility_layer.md) is configured to search an
    additional directory (run `ld.so --help | grep -A 10 "Shared library search path"` after initializing EESSI).
    For `EESSI/2025.06` and later, that is: `/cvmfs/software.eessi.io/versions/<EESSI_VERSION>/compat/<OS>/<ARCH>/lib/nvidia`).
    This directory is special, since it is a CernVM-FS [Variant Symlink](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#variant-symlinks).
    The target of this symlink is what you configure in your local CernVM-FS configuration.

#### Enabling runtime support for a native EESSI installation (using manual symlinking)
If, for some reason, the helper script is unable to locate the drivers on your system you _can_ link them manually.
To do so, grab the list of libraries that need to be symlinked from [here](https://raw.githubusercontent.com/apptainer/apptainer/main/etc/nvliblist.conf).
Then, change to the correct directory:
- For EESSI 2025.06 and later: `/cvmfs/software.eessi.io/versions/${EESSI_VERSION}>/compat/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/lib/nvidia`,
- For EESSI 2023.06: `/cvmfs/software.eessi.io/host_injections/${EESSI_VERSION}/compat/${EESSI_OS_TYPE}/${EESSI_CPU_FAMILY}/lib`
Then, manually create the symlinks for each of the files in the aforementioned list (if they exist on your system) to the current directory.

#### Runtime support when using EESSI in a container {: #nvidia_eessi_container } 

If you are running your own [Apptainer](https://apptainer.org/)/[Singularity](https://sylabs.io/singularity) container,
it is sufficient to use the [`--nv` option](https://apptainer.org/docs/user/latest/gpu.html#nvidia-gpus-cuda-standard)
to enable access to GPUs from within the container. This will ensure the container runtime exposes the drivers through
the `$LD_LIBRARY_PATH`.

If you are using the [EESSI container](../getting_access/eessi_container.md) to access the EESSI software,
simply pass `--nvidia run` or `--nvidia all` to enable nvidia GPU runtime support.

### Configuring compile time support {: #cuda_sdk }

To compile new CUDA software using dependencies from EESSI, additional configuration is needed.

The [CUDA license](https://docs.nvidia.com/cuda/eula/index.html) and [cuDNN license](https://docs.nvidia.com/deeplearning/cudnn/latest/reference/eula.html)
only allow redistribution of their _runtime_ libraries. Thus, the installations of CUDA and cuDNN that come with EESSI have been stripped down to contain
only the runtime libraries. A local installation of CUDA and cuDNN is required to compile new software.

!!! note "A full CUDA SDK or cuDNN SDK is only needed to *compile* CUDA or cuDNN software"
    Without a full CUDA SDK or cuDNN SDK on the host system, you will still
    be able to *run* CUDA-enabled or cuDNN-enabled software from the EESSI stack
    (provided the required configuration for runtime support was done - see above),
    you just won't be able to *compile* additional CUDA or cuDNN software.

First, [initialize a version of EESSI](../using_eessi/setting_up_environment.md).

Second, (optionally) define the `EESSI_HOST_INJECTIONS` variable in your local CernVM-FS configuration to point to a directory where you want to
store the local installations of CUDA and cuDNN (the default location is `/opt/eessi`):

```{ .bash .copy }
sudo bash -c "echo 'EESSI_HOST_INJECTIONS=/my/custom/prefix' >> /etc/cvmfs/default.local"
```

Third, run the helper script to install the CUDA and cuDNN versions that are used _in that version of EESSI_.

```{ .bash .copy }
/cvmfs/software.eessi.io/versions/${EESSI_VERSION}/scripts/gpu_support/nvidia/install_cuda_and_libraries.sh
```

Note that this script uses EasyBuild in order to install CUDA and cuDNN - and EasyBuild does not allow running as root by default. 
The recommended approach is to change ownership of the `host_injections` directory to a non-root user, and perform the installation with
that user. Alternatively (but not recommended), you can override EasyBuild's behaviour and install as root by setting 
`export EASYBUILD_ALLOW_USE_AS_ROOT_AND_ACCEPT_CONSEQUENCES=1` before running `install_cuda_and_libraries.sh`.

The script searches `/cvmfs/software.eessi.io/versions/${EESSI_VERSION}/scripts/gpu_support/nvidia/easystacks` for any file
named `eessi-*CUDA*.yml`, and installs all CUDA and cuDNN versions defined in those files.

Thus, you may want to periodically run this script to pick up on new CUDA and cuDNN versions that get added to EESSI over time.

!!! note "How does EESSI find the local installation of CUDA/cuDNN?"
    The non-redistributable components of CUDA/cuDNN in EESSI have been replaced by symlinks that point to a specific directory
    in the `/cvmfs/software.eessi.io/host_injections` prefix. For example, the `nvcc` compiler can not be redistributed, so it
    is replaced in EESSI with a symlink:
    ```
    $ ls -l /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen3/software/CUDA/12.1.1/bin/nvcc
    lrwxrwxrwx 1 cvmfs cvmfs 109 Dec 21 14:49 /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/amd/zen3/software/CUDA/12.1.1/bin/nvcc -> /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/amd/zen3/software/CUDA/12.1.1/bin/nvcc
    ```
    the `/cvmfs/software.eessi.io/host_injections` directory is special, since it is not part of the actual EESSI repository:
    it is a CernVM-FS [Variant Symlink](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#variant-symlinks) that points to
    a directory on the local system (`/opt/eessi` by default).
    The `install_cuda_and_libraries.sh` script installs CUDA and cuDNN in this local directory, thus un-breaking the symlinks.
    This means that from an end-user point of view, the EESSI CUDA module now 'just works', all while adhering to the EULA
    (e.g. not redistributing the compiler through EESSI itself).


### Testing the GPU support {: #gpu_cuda_testing }

The quickest way to test if software installations included in EESSI can access and use your GPU is to run the
`deviceQuery` executable that is part of the `CUDA-Samples` module:
```
module load CUDA-Samples
deviceQuery
```
If both are successful, you should see information about your GPU printed to your terminal.

## Support for using AMD GPUs {: #amd }

*(last update: May 2025)*

ROCm (Radeon Open Compute) support in EESSI is currently under development to enable GPU-accelerated computing on AMD hardware.

### Current status

ROCm support is not yet available in EESSI.
We are actively working on integrating AMD's ROCm ecosystem to provide GPU computing capabilities for AMD GPUs alongside our existing CUDA support for NVIDIA hardware.

For the latest updates join the #amd-rocm channel in the [EESSI Slack](https://app.slack.com/client/TP0103C4C/C0780BEV9JN).

### Overview of ROCm ecosystem

To prepare for ROCm integration, we have created a comprehensive overview of the entire ROCm ecosystem.
This document maps out AMD GPU architectures, core ROCm components, programming models, libraries, and the dependencies between them.

For a detailed understanding of the ROCm ecosystem that will inform our implementation, see [Overview of ROCm Ecosystem](rocm.md).

We also have a blog post about this [here](http://eessi.io/docs/blog/2025/05/26/rocm/).

### Future plans

Our ROCm integration will focus on providing:

* The ROCm core components
* ROCm-enabled scientific computing libraries
* Support for HIP, OpenMP, and OpenCL programming models
* GPU-accelerated frameworks and applications

### Community input

We welcome feedback from the community on ROCm support priorities and use cases.
If you have specific ROCm software requirements or insights to share, please [contact us](../support.md).
