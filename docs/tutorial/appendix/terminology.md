!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# CernVM-FS Terminology

An overview of terms used in the context of CernVM-FS, in alphabetical order.

---

## Catalog { #catalog }

A **catalog** of a CernVM-FS [repository](#repository) is a table that lists files and directories along with the corresponding
metadata (sizes, timestamps, etc.).

Catalogs can be *nested*: subtrees of the [repository](#repository) may have their own catalog.

For more information on the *catalog* concept, see [the CernVM-FS
documentation](https://cvmfs.readthedocs.io/en/stable/cpt-details.html#file-catalog).

---

## CernVM { #cernvm }

**CernVM** is a virtual machine image based on CentOS combined with a custom, virtualization-friendly Linux kernel,
and which includes the [CernVM-FS](../cvmfs/what-is-cvmfs.md) client software.

It is used for the CERN [Large Hadron Collider (LHC)](https://home.cern/science/accelerators/large-hadron-collider)
experiment, and was created to remove a need for the installation of the experiment software and to minimize the
number of platforms (compiler-OS combinations) on which experiment software needs to be supported and tested.

While originally developed in conjunction, the [CernVM File System](#cvmfs) today is a product
that is completely independent from the CernVM virtual appliance.

For more information on CernVM, see the [website](https://cernvm.cern.ch/appliance/)
and [documentation](https://cernvm.readthedocs.io).

---

## CernVM-FS { #cvmfs }

*(see [What is CernVM-FS?](../cvmfs/what-is-cvmfs.md))*

---

## Client { #client }

A **client** in the context of CernVM-FS is a computer system on which a CernVM-FS [repository](#repository)
is being accessed, on which it will be presented as a [POSIX](https://en.wikipedia.org/wiki/POSIX)
read-only file system in a subdirectory of `/cvmfs`.

---

## Proxy { #proxy }

A **proxy**, also referred to as *squid proxy*, is a forward caching
[proxy server](https://en.wikipedia.org/wiki/Proxy_server) which acts as an intermediary between a CernVM-FS
[client](#client) and the [Stratum-1 replica servers](#stratum1).

It is used to improve the latency observed when accessing the contents of a [repository](#repository),
and to reduce the load on the [Stratum-1 replica servers](#stratum1).

A commonly used proxy is [Squid](http://www.squid-cache.org).

For more information on proxies, see the
[CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-squid.html).

---

## Publishing { #publishing }

**Publishing** is the process of adding more files to a CernVM-FS [repository](#repository),
which is done via a *transaction* mechanism, and is on possible on the [Stratum-0 server](#stratum0),
via a [publisher](https://cvmfs.readthedocs.io/en/stable/cpt-repository-gateway.html#publisher-configuration),
or via a [repository gateway](https://cvmfs.readthedocs.io/en/stable/cpt-repository-gateway.html#repository-gateway-configuration).

The workflow of publishing content is covered in detail in the
[CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-repository-gateway.html#publication-workflow).

---

## Repository { #repository }

A CernVM-FS **repository** is where the files and directories that you want to distribute via CernVM-FS are
stored, which usually correspond to a collection of software installations.

It is a form of [*content-addressable storage (CAS)*](https://en.wikipedia.org/wiki/Content-addressable_storage),
and is the single source of (new) data for the file system being presented as a subdirectory of `/cvmfs`
on [client](#client) systems that [mount](https://en.wikipedia.org/wiki/Mount_(computing)) the repository.

!!! note

    A CernVM-FS repository includes [**software installations**](#software-installations),
    not [*software packages*](https://en.wikipedia.org/wiki/Package_format) like RPMs.

---

## Software *installations* { #software-installations }

An important distinction for a CernVM-FS repository compared to the more traditional notion of a
[*software repository*](https://en.wikipedia.org/wiki/Software_repository) is that a CernVM-FS repository
provides access to the **individual files** that collectively form a particular software installation, as opposed to
housing a set of [*software packages*](https://en.wikipedia.org/wiki/Package_format) like RPMs,
each of which being a *collection of files* for a particular software installation that are *packed together*
in a single *package* to distribute as a whole.

!!! note

    This is an important distinction, since CernVM-FS enables only downloading the specific files that are
    required to perform a particular task with a software installation, which often is a small subset of all
    files that are part of that software installation.

---

## Stratum 0 server { #stratum0 }

A **Stratum 0 server**, often simply referred to a *Stratum 0* (Stratum Zero), is the central server
for one or more CernVM-FS [repositories](#repository).

It is the single source of (new) data, since it hosts the *master copy* of the repository contents.

Adding or updating files in a CernVM-FS repository ([publishing](#publishing)) can only be done on the Stratum 0 server,
either directly via the `cvmfs_server publish` command, or indirectory via a publisher server.

For more information, see the [CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html).

---

## Stratum 1 replica server { #stratum1 }

A **Stratum 1 replica server**, often simply referred to a *Stratum 1* (Stratum One), is a standard web server
that acts as a mirror server for one or more CernVM-FS [repositories](#repository).

It holds a complete copy of the data for each CernVM-FS repository it serves,
and automatically synchronises with the [Stratum 0](#stratum0).

There is typically a *network* of several Stratum 1 servers for a CernVM-FS repository,
which are geographically distributed.

[Clients](#client) can be configured to automatically connect to the closest Stratum 1 server by using
the CernVM-FS [GeoAPI](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#ordering-of-servers-according-to-geographic-proximity).

For more information, see the [CernVM-FS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-replica.html).
