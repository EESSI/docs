# Flagship CernVM-FS repositories

Here we list a couple of flagship CernVM-FS repositories, all of which are **publicly available**.

## LHC experiments

CernVM-FS repositories are used to distribute the software required to analyse the data produced by the
[Large Hadron Collider (LHC)](https://home.cern/science/accelerators/large-hadron-collider) at each of the
[LHC experiments](https://home.cern/science/experiments).

Examples include *(click to browse repository contents)*:

* [`/cvmfs/alice.cern.ch`](https://cvmfs-monitor-frontend.web.cern.ch/browse/alice.cern.ch): software for [ALICE](https://home.cern/science/experiments/alice) experiment
* [`/cvmfs/atlas.cern.ch`](https://cvmfs-monitor-frontend.web.cern.ch/browse/atlas.cern.ch): software for [ATLAS](https://home.cern/science/experiments/atlas) experiment
* [`/cvmfs/cms.cern.ch`](https://cvmfs-monitor-frontend.web.cern.ch/browse/cms.cern.ch): software for [CMS](https://home.cern/science/experiments/cms) experiment
* [`/cvmfs/lhcb.cern.ch`](https://cvmfs-monitor-frontend.web.cern.ch/browse/lhcb.cern.ch): software for [LHCb](https://home.cern/science/experiments/lhcb) experiment
* [`/cvmfs/sft.cern.ch`](https://cvmfs-monitor-frontend.web.cern.ch/browse/sft.cern.ch): LCG Software Stacks

## LCG Releases

The [LCG Software Stacks](https://lcginfo.cern.ch/) which is distributed via the CernVM-FS repository
`/cvmfs/sft.cern.ch` contains in total over 800 external packages as well as HEP-specific tools and generators.

Software installations included often come with a script that updates your shell environment
for using them by sourcing it. In addition, through so-called *views* a complete software stack
can be made available in your shell environment.

For example, loading software for the specific view [*LCG_107*](https://lcginfo.cern.ch/release/107/) for RHEL9 can be dona via:
```
source /cvmfs/sft.cern.ch/lcg/views/LCG_107/x86_64-el9-gcc14-opt/setup.sh
```


## The Alliance

The [Digital Research Alliance of Canada](https://alliancecan.ca/en/about/alliance), a.k.a. *The Alliance* and formerly
known as *Compute Canada*, uses CernVM-FS to distribute the software stack for the Canadian national compute clusters.

Documentation on using their CernVM-FS repository `/cvmfs/soft.computecanada.ca` can be found
[here](https://docs.alliancecan.ca/wiki/Accessing_CVMFS/en), and an overview of all available software can be found
[here](https://docs.alliancecan.ca/wiki/Available_software).

## Unpacked containers

CernVM-FS repositories can be used to provide an efficient way to access container images,
by serving unpacked container images that can be consumed by container runtimes such as [Apptainer](https://apptainer.org).

Examples include:

* [`/cvmfs/unpacked.cern.ch`](https://cvmfs-monitor-frontend.web.cern.ch/browse/unpacked.cern.ch)
* `/cvmfs/singularity.opensciencegrid.org`

More information on `unpacked.cern.ch` is available in the CernVM-FS documentation:

* [Container Images and CernVM-FS](https://cvmfs.readthedocs.io/en/stable/cpt-containers.html)
* [Working with DUCC and Docker Images](https://cvmfs.readthedocs.io/en/stable/cpt-ducc.html)

## EESSI

The [*European Environment for Scientific Software Installations (EESSI)*](https://eessi.io) provides optimized installations
of scientific software for `x86_64` (Intel + AMD) and `aarch64` (64-bit Arm) systems that work on any Linux
distribution via the CernVM-FS repository `/cvmfs/software.eessi.io`.

We will use EESSI as an example CernVM-FS repository throughout this tutorial.


---

*(next: [What is EESSI?](../eessi/what-is-eessi.md))*
