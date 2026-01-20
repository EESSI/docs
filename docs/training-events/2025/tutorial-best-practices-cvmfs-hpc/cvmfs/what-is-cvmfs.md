# What is CernVM-FS?

<div align="center">
<img src="../../img/logos/CernVM-FS_logo_with_name.png" alt="CernVM-FS logo" width="50%"/></br>
</div>

[CernVM-FS](https://cernvm.cern.ch/fs/), the CernVM File System (also known as *CVMFS*),
is a *file distribution service* that is particularly well suited to distribute *software installations*
across a large number of systems world-wide in an efficient way.

From an end user perspective, files in a CernVM-FS [repository](../appendix/terminology.md#repository) are available
*read-only* via a subdirectory in `/cvmfs`, with a user experience similar to that of an *on-demand streaming service*
for music or video, but then (mainly) applied to software installations.


## Primary use case

The primary use case of CernVM-FS is **distributing software**, and it provides several interesting features that
support this, including:

* [on-demand downloading](#features-ondemand) and [updating](#features-updating) of repository contents;
* [multi-level caching](#features-caching);
* [de-duplication of files](#features-deduplication);
* [compression of data](#features-compression);
* [verification of data integrity](#features-data-integrity);

CernVM-FS has been proven to scale to *billions* of files and *tens of thousands* of [clients](../appendix/terminology.md#client).

It was originally developed at [CERN](https://home.cern/) to let High Energy Physics (HEP) collaborations
like the experiments at the [Large Hadron Collider (LHC)](https://home.cern/science/accelerators/large-hadron-collider)
deploy software on the [Worldwide LHC Computing Grid (WLCG)](https://wlcg.web.cern.ch/) infrastructure that is used to
run data processing applications.

The primary use case of distributing software is a particular one, since software often comprises many small files that
are frequently opened and read as a whole, and frequent look-ups for files in multiple directories are
triggered when search paths are examined.

In certain cases, the CernVM-FS has also been used to
[distribute large *data* repositories](https://cvmfs.readthedocs.io/en/stable/cpt-large-scale.html).


## Features

### On-demand downloading of files and metadata { #features-ondemand }

The metadata and content of files included in a CernVM-FS repository are **automatically downloaded on-demand**
as files and directories are being accessed, which is akin to *streaming* services for music, movies, and TV series.

This happens fully transparently, all the contents of a repository are exposed by CernVM-FS as if they were
a local (read-only) file system. Hence, clients that access a CernVM-FS repository typically do not
have a local copy of all the files included in that repository, but only have a limited set of files and
metadata directly available: those which were most recently accessed.


### Automatic updates { #features-updating }

CernVM-FS clients **automatically pull in updates** to the contents of a repository as they are
[published](../appendix/terminology.md#publishing) server-side.
This happens in *transactions*, to ensure that clients observe a consistent state of the repository.

Once a CernVM-FS repository is accessible on a client system, no subsequent actions must be taken
to keep clients up-to-date other than updating CernVM-FS itself on a regular basis.

This significantly limits the maintenance burden, since no action is required on client systems
to update the software stack that is provided through a CernVM-FS repository, since the updates are
*streamed in* automatically by CernVM-FS.

Only the CernVM-FS client should be updated on a regular basis on client systems.

For more elaborate setups that involve [proxies](../appendix/terminology.md#proxy) or
[CernVM-FS replica (mirror) servers](../appendix/terminology.md#stratum1), additional maintenance is necessary,
but again only to update the CernVM-FS components themselves.


### Multi-level caching { #features-caching }

CernVM-FS uses a **multi-level caching** hierarchy to reduce the latency observed when accessing repository contents.
Caching is an essential part of CernVM-FS, since the contents of a CernVM-FS repository are
[downloaded on-demand](#features-ondemand) as they are accessed.

The caching mechanism employed by CernVM-FS goes way beyond the standard (in-memory) Linux kernel file system cache,
and consists of a *local client cache*,
an optional [forward proxy server](../appendix/terminology.md#proxy) that acts as an intermediary cache level, and a distributed
network of [mirror servers](../appendix/terminology.md#stratum1) that support the CernVM-FS repository being accessed.

When a part of the repository is being accessed that is not available yet in the local client cache,
CernVM-FS will traverse the multi-level cache hierarchy to obtain the necessary data and update the local client
cache with it, so the files being accessed can be served with low latency.

Proxy and mirror servers scale horizontally: the CernVM-FS client makes automatic use of
multiple deployed service instances for load-balancing and high-availability.

We will explore this multi-level caching mechanism in more detail in this tutorial.

See [here](technical-details.md#caching) more technical details on CernVM-FS caching.


### De-duplication of files {: #features-deduplication }

CernVM-FS **stores the contents of a file only once**, even when it is included multiple times
in a particular repository at different paths.

This can result in a significant reduction in storage capacity that is required to host a large software stack,
especially when identical files are spread out across the repository,
as often happens with particular files like example data files across multiple versions of the same software.

For the CernVM-FS client, data de-duplication will also happen across repositories when the local client cached is shared across all repositories (the default).


### Compression of data { #features-compression }

CernVM-FS [**stores file content compressed**](https://cvmfs.readthedocs.io/en/stable/cpt-repo.html#compression-and-hash-algorithms)
on the server, which not only further reduces required storage space but also significantly limits the
network bandwidth that is required to download (and serve) the contents of a repository.

On the client side, the data is transparently decompressed when the files included in a CernVM-FS repository
are presented under `/cvmfs` as a normal (read-only) file system.


### Verification of data integrity { #features-data-integrity }

The integrity of data provided by a CernVM-FS server is ensured on a client system by verifying a cryptographic
hash, which is again a direct result of content-addressable storage mechanism that is used by CernVM-FS.
This is an essential security aspect since CernVM-FS uses (possibly untrusted) caches and HTTP connections
to distribute the contents of a repository.

---

*(next: [Technical details of CernVM-FS](technical-details.md))*
