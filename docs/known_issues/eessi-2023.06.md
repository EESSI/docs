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
</div>

### `Bug in EESSI initialization and priority mechanisms: site OpenMPI or UCX not loaded`
<div style="padding-left: 30px;">

<p>This error may occur when bugs resolving or site-specific tuning is needed for OpenMPI or UCX.</p>

<p>There is an issue on this problem opened with EESSI software layer repository.
See: https://github.com/EESSI/software-layer/issues/456</p>

<b>Workarounds</b>

<p>The workaround is to specify site properties and allow defining lmod hooks in host injections (see https://github.com/EESSI/software-layer/pull/525).
</div>

