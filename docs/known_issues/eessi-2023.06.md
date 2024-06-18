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

You may also set these additional environment variables via site-specific Lmod hooks. For more information about how to write and implement site-specific Lmod hooks, please check  [EESSI Site Specific Configuration LMOD Hooks](site_specific_config/lmod_hooks.md)
</div>

