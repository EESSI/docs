*(Tue Jan 19th 2021)*

EESSI "behind the scenes" presentation by Kenneth Hoste (@boegel) and Bob Dröge (@bedroge),
prepared with the help from Terje Kvernes (@terjekv).

* [slides](EESSI-behind-the-scenes-20210119.pdf)
* [recording @ YouTube](https://www.youtube.com/watch?v=WAOP6-sCfG0) (unlisted)

## Q&A

(questions collected via Zoom chat + hackmd.io, answered during presentation by Alan, Bob, Kenneth)

* Q: In one video on YouTube, Kenneth(?) says that Compute Canada made some design decisions that made him not want to use their software stack. What was that decision and are we sure that our design does not suffer from such a problem?
  * A: We discussed early on the possibility to join forces with ComputeCanada on their software stack, but eventually we both agreed it was not a good way to go forward.
    It would be difficult for ComputeCanada to "open up" their software stack for others to add software into it. There are also some (historic) design decisions that may
    not agree with what we have in mind (for example using a hierarchical module naming scheme).
 
    In the EESSI project, we're also a bit more ambitious, for example by trying to also support macOS, or additional CPU families like Arm 64-bit, POWER, etc.

* Q: Would it make sense to embed Gentoo Prefix (compat layer) inside a (Singularity) container image ?
  * A: In a container image, you're already in full control of the operating system, so there's no need to use Gentoo Prefix.

    You could consider rsync'ing the parts of the EESSI repository into a container image (compat layer + parts of software layer) to avoid relying on CernVM-FS,
    but then you again end up with a container image that's specific to a particular CPU microarchitecture (for example, Intel Haswell).

    CernVM-FS has a tracing option that could facilitate this; see https://cvmfs.readthedocs.io/en/stable/cpt-tracer.html .
    Another option would be to pre-populate a CernVM-FS alien cache inside the container image with only the things you need.

* Q: Can the CernVM-FS cache be warmed up, with part of the EasyBuild tree that admins know in advance to be required, Instead of doing it on initial load?
  * A: Yes, you can have a multi-level cache which can include a pre-loaded alien cache (see https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#alien-cache and https://github.com/EESSI/filesystem-layer/issues/37 which leverages this approach).

* Q: What is the planned scope of EESSI? One Stratum 0 for each site/county/state/...? who would run it?
  * There's only 1 Stratum 0 server (the central server).

    It makes sense to have a Stratum 1 per "large" setup (like a cloud region, HPC sites, etc.), but that's not strictly required.
    The more Stratum 1 servers we have, the better w.r.t. reliability of the network, performance (the closest Stratum 1 is picked automatically by CernVM-FS).
    
    We will not force anybody to set up a Stratum 1, that's up to each site to decide for themselves.
    There's a bit a maintenance implied, like keeping up with CernVM-FS version updates, etc.
    Required resources are fairly minimal (2-core VM, couple of GBs of RAM, ~1TB of disk should be sufficient).

* Q: What if someone needs software compiled slightly differently (compiler flags,etc)?
  * The installations included in EESSI are "common", and are typically done such that they're useful to most sites.
    It's easy to build addiotional software (or customized installations) on top of what EESSI provides, like a custom configuration of GROMACS, etc.
  
    Alan did this last week in a container, to leverage the stack you just need a few EasyBuild settings and then you can install what you want how you want with EasyBuild (https://github.com/EESSI/software-layer/issues/59). It would also be reasonably easy to provide a build environment module (that sets up rpathing, CC, CXX etc.) for general use since this is what EasyBuild is doing internally anyway.

* Multi-part question:
  * Q1:  What is the typical expected installation for an HPC provider? Consume EESSI software along with custom local set of software?
    * HPC sites can determine themselves how they leverage EESSI.
      
      Minimal thing to do is just mount the EESSI CernVM-FS repository.
      Ideally also a Stratum 1 + one or more proxies (and make them publicly accessible), but this is not required.
      
      If sites want to provide additional software on top, they can, but that's up to them.
      
  * Q2: Would that local set need to be build using the same framework as EESSI?
    * See question above about compiling differently. The goal of the test was exactly that, to see how hard it is to use EESSI as a baseline installation.
     
      For example, you might just want to take everything to the GCCcore level and this would be possible by leveraging the new easystack file support (still WIP, see https://github.com/easybuilders/easybuild-framework/issues/3468) and building your own module tree somewhere (which point to the EESSI installations).

  * Q3: What about licensed software, I expect they would fit the later?
    * A: ComputeCanada has a separate CVMFS repository with licensed software, which is not publicly accessible.

      That would be harder to set up in EESSI, since it involves making sure all sites have the necessary licenses, etc.
      
      So likely commercial/licensed software will still need to be handled by each site as local installations
      (unless we can come to some kind of agreement with the software vendor).

* Q: I saw quite a bit of load from CVMFS when populating the cache, are there any recommendations for a cache size to control this?
  * A: Different aspects to this: size of the cache (big enough to avoid lots of cache misses), cache should be on a fast filesystem (local SSD or /dev/shm, NOT something like NFS).

    It's also helpful to have a "local" proxy in the network, which has a big cache, to avoid that you're downloading the same files multiple times.

* Q: W.r.t. automatic deployment of for example the CVMFS configuration repo: how will you ensure that no malicious party manages to make changes there that are then automatically picked up by all clients?
  * A: (question answered on stream, see recording)

    We should ask the CVMFS developers about this too (see also https://cvmfs.readthedocs.io/en/stable/apx-security.html).

* Q: LTS for Gentoo? Lifetime? Major upgrade -> EasyBuild complete rebuild? How long can we re-use the previous "trees"?
  * A: (question answered on stream, see recording).
       Short answer: we haven't decided this yet.

* Q: did you do a comparison with other packaging-deploying tools like Spack or [GuixHPC](https://hpc.guix.info) ?
  * A: There have been plenty of comparisons between EasyBuild and Spack (see https://youtu.be/Uaw5-L7BMtM for example for an independent view). This is also covered in the EasyBuild Tutorial https://easybuilders.github.io/easybuild-tutorial/comparison_other_tools/
  
    See also recent E4S webinar https://www.youtube.com/watch?v=uFkFwUvgrAI which is perhaps a comparable project to EESSI, but a different approach 

* Q: Would it be hard to add non optimised distribution? https://sbgrid.org// 
  * A: We already provide generic installations for both x86_64 and aarch64.
  
    It looks like software included in SBGrid *must* be installed under `/opt/sbgrid` (see https://sbgrid.org/wiki/client_install#pre-installation), which can't be done in EESSI (we only control stuff under `/cvmfs`).
