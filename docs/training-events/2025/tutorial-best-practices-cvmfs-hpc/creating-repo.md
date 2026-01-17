# Creating a CernVM-FS repository

Although creating a new CernVM-FS repository and making it available to the world is not in scope for this
tutorial, we do want to give a (very) brief overview of what that entails.

For more information on starting with CernVM-FS from scratch to create your own CernVM-FS repository,
see the [introductory tutorial to the CernVM-FS](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021)
that was organised at the [6th EasyBuild User Meeting](https://easybuild.io/eum21) (Jan'21).

## Stratum 0 + creating repository

To create a new CernVM-FS repository, you will need to **set up a [Stratum 0 server](appendix/terminology.md#stratum0)**,
or find an existing one that is willing to host your repository.

On a Stratum 0 server, a new repository can be created with:

```{ .bash .copy }
sudo cvmfs_server mkfs example.domain.tld
```

For more information on this, see [the CernVM-FS documentation](
https://cvmfs.readthedocs.io/en/stable/cpt-repo.html),
or the [second section of the CernVM-FS introductory tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/02_stratum0_client/).

## Publishing content

After creating the repository, you should add some content to it via the update procedure
that is documented [here](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#repository-update),
which involves starting a *transaction*, making changes, and then *publishing* those changes.

## Managing repository

To optimize metadata access for client systems, you may need to look into creating [nested catalogs](
https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#managing-nested-catalogs).

If files are frequently removed from the repository, you should consider enabling [garbage
collection](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#repository-garbage-collection).

## Public Stratum 1 replica servers

To distribute your repository, you should set up one or more public [Stratum 1 replica
servers](appendix/terminology.md#stratum1), much like we also did in this tutorial (see the
[Accessing repositories - Private Stratum 1 replica server](access/stratum1.md) section).

More information on this is available [in the CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-replica.html) as well.

---

*(next: [Appendix: Terminology](appendix/terminology.md))*
