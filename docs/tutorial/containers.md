!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Containers and CernVM-FS

CernVM-FS can also be used to distribute container images, providing many of the same benefits that come with any CernVM-FS installation. Especially the on-demand download of accessed files means that containers start nearly instantly, and are more efficient for large images when only a fraction of the files are read, which is typically the case.

Any CernVM-FS repository can be used to distribute container images (although often, dedicated repositories are used, like [`/cvmfs/unpacked.cern.ch`](cvmfs/flagship-repositories.md#unpacked-containers)).

In order to provide [de-duplication](cvmfs/what-is-cvmfs.md#features-deduplication) and [on-demand download](cvmfs/what-is-cvmfs.md#features-ondemand), images must be stored *unpacked*. This requires some dedicated tools, provided by CernVM-FS itself - see the section "[Ingesting container images](#ingesting)" below.

## Accessing containers hosted in CernVM-FS via Apptainer

[Apptainer](https://apptainer.org) is the recommended way to run containers from CernVM-FS, as it can start a container directly from an unpacked root file system, which is ideal for CernVM-FS.

[Docker](https://www.docker.com) can be used as well but the setup is more complicated, requiring the [CernVM-FS graphdriver plugin](https://cvmfs.readthedocs.io/en/stable/cpt-graphdriver.html).

For example, to run the [`tensorflow/tensorflow:2.15.0-jupyter`](https://hub.docker.com/layers/tensorflow/tensorflow/2.15.0-jupyter/images/sha256-3bf17d6d5f2ed968543238936cca0725ca664d24729c537778b1333a315036d7?context=explore) image from [Docker Hub](https://hub.docker.com/) that has been unpacked in `/cvmfs/unpacked.cern.ch`, use the following commands:

```{ .bash .copy }
container="registry.hub.docker.com/tensorflow/tensorflow:2.15.0-jupyter"
python_code="import tensorflow as tf; print(tf.__version__)"
apptainer run /cvmfs/unpacked.cern.ch/${container} python -c "${python_code}"
```

This directory just contains the root file system of the image:

```{ .bash .copy }
ls /cvmfs/unpacked.cern.ch/registry.hub.docker.com/tensorflow/tensorflow:2.15.0-jupyter
```



## Ingesting container images {: #ingesting }

CernVM-FS provides a suite of container unpacking tools called `cvmfs_ducc` (provided by the `cvmfs-ducc` package). This can be used to unpack and ingest container images by simply running

```{ .bash .copy }
cvmfs_ducc convert recipe.yaml 
```
where `recipe.yaml` is a 'wishlist' of container images available in external registries that should be made available:

```yaml
version: 1
user: cvmfsunpacker
cvmfs_repo: 'unpacked.repo.tld'
input:
    - 'https://registry.hub.docker.com/tensorflow/tensorflow:2.15.0-jupyter'
    ...
```

For more information, [see the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-ducc.html).


## Using `/cvmfs` inside containers

The easiest way to access CernVM-FS repositories from a container is to set it up on the host and bind-mount it inside the container:

```{ .bash .copy }
docker run -it --volume /cvmfs:/cvmfs:shared ubuntu ls -lna /cvmfs/atlas.cern.ch
```

For Apptainer, the same can be done by setting the `$SINGULARITY_BIND` (or `$APPTAINER_BIND`) environment variable: 

```{ .bash .copy }
export SINGULARITY_BIND="/cvmfs"
```

---

*(next: [Creating a CernVM-FS repository](creating-repo.md))*
