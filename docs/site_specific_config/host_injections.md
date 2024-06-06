# How to configure EESSI

## The `host_injections` variant symlink

While the EESSI software stack aims to work 'out of the box', one cannot avoid some degree of site-specific configuration for certain functionality and/or performance tuning. For example, GPU drivers may be in different locations on different systems. Also, a site might want to tune the OpenMPI installation that comes with EESSI for optimal performance on the local hardware.

To allow such site-specific configuration, the EESSI repository includes a special directory where system administrations can install files that can be picked up by the software installations included in EESSI. This special directory is located in `/cvmfs/software.eessi.io/host_injections`, and it is a *CernVM-FS Variant Symlink*:
a symbolic link for which the target can be controlled by the CernVM-FS client configuration (for more info, see ['Variant Symlinks' in the official CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#variant-symlinks)).

!!! info "Default target for `host_injections` variant symlink"

    Unless otherwise configured in the CernVM-FS client configuration for the EESSI repository, the `host_injections` symlink points to `/opt/eessi` on the client system:
    ```
    $ ls -l /cvmfs/software.eessi.io/host_injections
    lrwxrwxrwx 1 cvmfs cvmfs 10 Oct  3 13:51 /cvmfs/software.eessi.io/host_injections -> /opt/eessi
    ```

The target for this symlink can be controlled by setting the `EESSI_HOST_INJECTIONS` variable in your local CVMFS configuration for EESSI. E.g.
```{bash}
sudo bash -c "echo 'EESSI_HOST_INJECTIONS=/shared_fs/path/to/host/injections/' > /etc/cvmfs/domain.d/eessi.io.local"

```

!!! note "Don't forget to reload the CernVM-FS configuration"
    After making a change to a CernVM-FS configuration file, you also need to reload the configuration:
    ```{ .bash .copy }
    sudo cvmfs_config reload
    ```

On a heterogeneous system, you may want to use different targets for the variant symlink for different node types. For example, you might have two types of GPU nodes (`gpu1` and `gpu2`) for which the GPU drivers are _not_ in the same location, or not of the same version. Since those are both things we configure under `host_injections`, you'll need separate `host_injections` directories for each node type. That can easily be achieved by putting e.g.

```{bash}
sudo bash -c "echo 'EESSI_HOST_INJECTIONS=/shared_fs/path/to/host/injections/gpu1/' > /etc/cvmfs/domain.d/eessi.io.local"

```

in the CVMFS config on the `gpu1` nodes, and

```{bash}
sudo bash -c "echo 'EESSI_HOST_INJECTIONS=/shared_fs/path/to/host/injections/gpu2/' > /etc/cvmfs/domain.d/eessi.io.local"

```
in the CVMFS config on the `gpu2` nodes.
