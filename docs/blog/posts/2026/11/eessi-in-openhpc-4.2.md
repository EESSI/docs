---
authors: [adrianreber]
date: 2026-11-01
slug: eessi-in-openhpc-4.2
---

# EESSI in OpenHPC 4.2

<figure markdown="span">
![OpenHPC](ohpc_logo.png){width=50%}
</figure>

[OpenHPC](https://openhpc.community/) 4.2 was
[released on 1 November 2026](https://openhpc.community/news/2026/openhpc-v4-2-release-additional-provisioners-resource-managers-and-module-systems/).
Among the new material in the install guide is an optional section that sets up
[EESSI](../../../../index.md) on the cluster being built: the CernVM-FS client
on the head node and in the compute image, the `software.eessi.io` repository,
and a module that makes the EESSI software stack available through the usual
`module` commands.

<!-- more -->

## A long-standing connection

OpenHPC and the EasyBuild community have been in contact for a long time.
EasyBuild has been packaged in OpenHPC since late 2016 and is still part of
OpenHPC 4.2, alongside Spack, for sites that prefer to build their own
software. EESSI, in turn, grew out of that same community: its
[software layer](../../../../software_layer.md) is built with EasyBuild, and
the installations are exposed through Lmod.

The integration of EESSI in OpenHPC 4.2 is therefore not a first encounter
between two unrelated projects, but an existing connection becoming visible in
the install guide, where site administrators are likely to come across it.

It followed from several conversations over the past few years about bringing
the two projects closer together. While working on OpenHPC 4.2 I returned to
the idea, and integrating EESSI proved easier than expected. The section was
written on the OpenHPC side and reviewed by the EESSI project.

## What it does

Administrators who want EESSI on their cluster can enable the section when
preparing the installation. The recipe then installs the CernVM-FS client and
the EESSI configuration on the head node and in the compute image, and adds an
`eessi` module to the OpenHPC module hierarchy. From that point on, the
standard EESSI workflow applies:

```console
[test@sms ~]$ module load eessi
[test@sms ~]$ module avail EESSI

-------------------- /cvmfs/software.eessi.io/init/modules ---------------------
   EESSI/2023.06 (D)    EESSI/2025.06    EESSI/2026.06

  Where:
   D:  Default Module

[test@sms ~]$ module load EESSI/2026.06
[test@sms ~]$ module avail
```

The final `module avail` deserves attention. A freshly installed OpenHPC
cluster already provides a substantial set of packages, but EESSI adds
[more than 900 software projects](../../../../available_software/index.md) on
top of it, built for the CPU architecture of the node on which the job runs,
none of which has to be compiled at the site. For a cluster being set up today,
this removes a considerable amount of work before users can start.

The EESSI section is part of the recipe templates like every other section, and
the test matrix includes configurations with `enable_eessi` set, so it is
covered by the same integration testing as the rest of the guide. OpenHPC 4.2
was validated with 172,794 tests over 306 hours.

## Points to consider before enabling it

The section documents two constraints that are worth repeating here:

- **Lmod is required.** EESSI ships its initialization modules as Lua
  modulefiles, which only Lmod reads. OpenHPC 4.2 also offers Environment
  Modules 5.7 as an alternative module system, but with that selected the
  repository still mounts and its files remain usable directly, while the EESSI
  modules cannot be loaded. Support for Environment Modules is so far a
  [proposal](https://modules.readthedocs.io/en/latest/design/eessi.html) in the
  Environment Modules documentation rather than something EESSI provides.
- **A proxy is recommended in production.** The recipe configures clients with
  `CVMFS_USE_CDN=yes`, so that content is fetched through a CDN rather than
  directly from the EESSI mirror servers. This is adequate for a test cluster
  and keeps the load on those servers low, but a production cluster should run
  a local Squid proxy and point the clients at it with `CVMFS_HTTP_PROXY`. See
  the EESSI documentation on
  [native installation on clusters](../../../../getting_access/native_installation.md#native-install-on-clusters).

## Reading the section

OpenHPC 4.2 includes a
[Recipe Explorer](https://openhpc.github.io/ohpc/4.2/explorer/): after
selecting a base OS, architecture, provisioner and resource manager, and
enabling the optional features, it renders the corresponding install guide
together with a `recipe.sh` and an `input.local`. The EESSI section for an
AlmaLinux 10 / x86_64 / Warewulf / Slurm cluster is available
[here](https://openhpc.github.io/ohpc/4.2/explorer/#almalinux10-x86_64-warewulf-slurm?chapter=eessi);
for a different combination, enable EESSI in the options on the left and the
section appears in the table of contents.

## Questions

Questions about OpenHPC itself are best raised on the
[OpenHPC](https://github.com/openhpc/ohpc) issue tracker. Questions about EESSI,
such as missing software or problems with the CernVM-FS repository, should be
directed to the EESSI project through the channels listed on the
[support page](../../../../support.md).
