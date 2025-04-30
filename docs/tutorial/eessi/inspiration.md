!!! danger "Work in progress"

    *(30 April 2025)*

    The contents of this tutorial are currently being reworked to be up-to-date with recent developments in CernVM-FS,
    and to be well integrated in the EESSI documentation.

    It is based on the *"Best Practices for CernVM-FS in HPC"* tutorial that was held on
    4 Dec 2023, see also https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices.


# Inspiration for EESSI

The EESSI concept is heavily inspired by software stack provided by the
[Digital Research Alliance of Canada](https://alliancecan.ca/en/about/alliance) (a.k.a. The Alliance, formerly known as *Compute Canada*), which is a shared software stack used on all
[national host sites for Advanced Research Computing in Canada](
https://alliancecan.ca/en/services/advanced-research-computing/federation/national-host-sites)
that is distributed across Canada (and beyond) using [CernVM-FS](../cvmfs/what-is-cvmfs.md);
see also [here](../cvmfs/flagship-repositories.md#the-alliance).

EESSI is significantly more ambitious in its goals however, in various ways.

It intends to support a **broader range of system architectures** than what is currently supported by the
Compute Canada software stack, like Arm 64-bit microprocessors, accelerators beyond NVIDIA GPUs, etc.

In addition, EESSI is set up to be a **community project**, by setting up services and infrastructure to automate the
software build and installation process as much as possible, providing extensive [documentation](https://eessi.io/docs/)
*and* [support](https://www.eessi.io/docs/support/) to end users, user support teams, and system administrators
who want to employ EESSI, and allowing contributors to [propose
additions](https://www.eessi.io/docs/adding_software/overview/) to the software stack.

The design of the Compute Canada software stack is discussed in detail in the
[PEARC'19 paper *"Providing a Unified Software Environment for Canada’s National Advanced Computing Centers"*](
https://dl.acm.org/doi/10.1145/3332186.3332210).

It has also been presented at the 5th [EasyBuild User Meeting](https://easybuild.io/eum), see
[slides](https://easybuild.io/eum23/eum23_008_Digital-Research-Alliance-Canada.pdf) and
[talk recording](https://www.youtube.com/watch?v=gRNYp4gQKls).

More information on the Compute Canada software stack is available in
[their documentation](https://docs.alliancecan.ca/wiki/Accessing_CVMFS/en),
and in their [overview of available software](https://docs.alliancecan.ca/wiki/Available_software).


---

*(next: [High-level Overview of EESSI](high-level-design.md))*
