# Building software on top of EESSI

## Building software on top of EESSI with EasyBuild
Building on top of EESSI with EasyBuild is relatively straightforward. One crucial feature is that EasyBuild supports building against operating system libraries that are _not_ in a standard prefix (such as `/usr/lib`). This is required when building against EESSI, since all of the software in EESSI is build against the [compatibility layer](../compatibility_layer.md).

### Starting the EESSI software environment
Start your environment as described [here](../using_eessi/setting_up_environment.md)

### Configure EasyBuild
To configure EasyBuild, first, check out the [EESSI software-layer repository](https://github.com/EESSI/software-layer.git). We advise you to check out the branch corresponding to the version of EESSI you would like to use.

If you are unsure which version you are using, you can run
```
echo ${EESSI_PILOT_VERSION}
```
to check it.

To build on top of e.g. version `2023.06` of the EESSI software stack, we check it out, and go into that directory:

```
git clone https://github.com/EESSI/software-layer/ --branch 2023.06
cd software-layer
```
Then, you have to pick a working directory (that you have write access to) where EasyBuild can do the build, and an install directory (with sufficient storage space), where EasyBuild can install it. In this example, we create a temporary directory in `/tmp/` as our working directory, and use `$HOME/.local/easybuild` as our installpath:
```
export WORKDIR=$(mktemp --directory --tmpdir=/tmp  -t eessi-build.XXXXXXXXXX)
export EASYBUILD_INSTALLPATH="${HOME}/.local/easybuild"
source configure_easybuild
```
Next, you load the EasyBuild module that you want to use, e.g. 
```
module load EasyBuild/4.8.1
```
Finally, you can check the current configuration for EasyBuild using
```
eb --show-config
```

!!! Note
    We use EasyBuild's default behaviour in optimizing for the host architecture. Since the EESSI initialization script also loads the EESSI stack that is optimized for your host architecture, this matches nicely. However, if you work on a cluster with heterogeneous node types, you have to realize you can only use these builds on the same architecture as where you build them. You can use different `EASYBUILD_INSTALLPATH`s if you want to build for different host architectures. For example, when you are on a system that has a mix of `AMD zen3` and `AMD zen4` nodes, you might want to use `EASYBUILD_INSTALLPATH=$HOME/.local/easybuild/zen3` when building on a `zen3` node, `EASYBUILD_INSTALLPATH=$HOME/.local/easybuild/zen4` when building on a `zen4` node. Then, in the step beloww, instead of the `module use` command listed there, you can use `module use $HOME/.local/easybuild/zen3/modules/all` when you want to run on a `zen3` node and `module use $HOME/.local/easybuild/zen4/modules/all` when you want to run on a `zen4` node.

### Building
Now, you are ready to build. For example, at the time of writing, `netCDF-4.9.0-gompi-2022a.eb` was not in the EESSI environment yet, so you can build it yourself:
```
eb netCDF-4.9.0-gompi-2022a.eb
```

!!! Note
    If this netCDF module is available by the time you are trying, you can force a local rebuild by adding the `--force` argument in order to experiment with building locally, or pick a different EasyConfig to build.

### Using the newly build module
First, you'll need to add the subdirectory of the `EASYBUILD_INSTALLPATH` that contains the modules to the `MODULEPATH`. You can do that using:

```
module use ${EASYBUILD_INSTALLPATH}/modules/all
```

you may want to do this as part of your `.bashrc`.

!!! Note
    Be careful adding to the `MODULEPATH` in your `.bashrc` if you are on a cluster with heterogeneous architectures. You don't want to pick up on a module that was not compiled for the correct architectures accidentally.

Since your module is build on top of the EESSI environment, that needs to be loaded first (as described [here](../using_eessi/setting_up_environment.md)), if you haven't already done so.

Finally, you should be able to load our newly build module:
```
module load netCDF/4.9.0-gompi-2022a
```

## Manually building software op top of EESSI
Building software on top of EESSI would require your linker to use the same system-dependencies as the software in EESSI does. In other words: it requires you to link against libraries from the compatibility layer, instead of from your host OS.

While we plan to support this in the future, manually building on top of EESSI is not supported yet.
