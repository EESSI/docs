# Known issues

## EESSI Production Repository (v2023.06)

### `Failed to modify UD QP to INIT on mlx5_0: Operation not permitted`
<div style="padding-left: 30px;">

<p>This is an error that occurs with OpenMPI after updating to OFED 23.10.</p>

<p>There is an upstream issue on this problem opened with EasyBuild.
See: https://github.com/easybuilders/easybuild-easyconfigs/issues/20233</p>

<b>Workarounds</b>

<p>You can instruct OpenMPI to not use libfabric and turn off `uct`(see https://openucx.readthedocs.io/en/master/running.html#running-mpi) by passing the following options to `mpirun`:</p>

```
mpirun -mca pml ucx -mca btl '^uct,ofi' -mca mtl '^ofi'
```

Or equivalently, you can set the following environment variables:

```
export OMPI_MCA_btl='^uct,ofi'
export OMPI_MCA_pml='ucx'
export OMPI_MCA_mtl='^ofi'
```

You may also set these additional environment variables via site-specific Lmod hooks:
```
require("strict")
local hook=require("Hook")

-- Fix Failed to modify UD QP to INIT on mlx5_0: Operation not permitted
function fix_ud_qp_init_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('OMPI_MCA_btl', '^uct,ofi')
        setenv('OMPI_MCA_pml', 'ucx')
        setenv('OMPI_MCA_mtl', '^ofi')
    end
end

local function combined_load_hook(t)
    if eessi_load_hook ~= nil then
        eessi_load_hook(t)
    end
    fix_ud_qp_init_openmpi(t)
end

hook.register("load", combined_load_hook)
```
 For more information about how to write and implement site-specific Lmod hooks, please check  [EESSI Site Specific Configuration LMOD Hooks](site_specific_config/lmod_hooks.md)
</div>

### GCC-12.2.0 and foss-2022b based modules cannot be loaded on `zen4` architecture

The `zen4` architecture was released late 2022. As a result, the compilers and BLAS libraries that are part of the 2022b toolchain generation do not yet (fully) support this architecture. Concretely, it was found [in this pr](https://github.com/EESSI/software-layer/pull/567) that unit tests in the OpenBLAS version that is part of the foss-2022b toolchain were failing. As a result, it was decided that we would not support this toolchain-generation at all on the `zen4` architecture.
