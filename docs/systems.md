# Systems on which EESSI is available natively

This page lists the [HPC](https://en.wikipedia.org/wiki/High-performance_computing "High-Performance Computing") systems (that we know of) on which EESSI is available system-wide.

On these systems, you should be able to initialise your session environment for using EESSI as documented [here](using_eessi/setting_up_environment.md),
and you can try [running our demos](using_eessi/eessi_demos.md).

!!! info "Please report additional systems on which EESSI is available"
    If you know of one or more systems on which EESSI is available system-wide that are not listed here yet,
    **please let us know by [contacting the EESSI support team](support.md)**,
    so we can update this page (or [open a pull request](https://github.com/EESSI/docs)).

!!! example "What if EESSI is not available system-wide yet?"
    If EESSI is not available yet on the HPC system(s) that you use,
    **contact the corresponding support team** and submit a request to make it available.
    
    You can point them to our documentation:

    * [How to install and configure CernVM-FS to provide native access to EESSI](https://www.eessi.io/docs/getting_access/native_installation/);
    * [*Best Practices for CernVM-FS in HPC* tutorial](https://multixscale.github.io/cvmfs-tutorial-hpc-best-practices/);

    If they have any questions, please suggest to [**contact the EESSI support team**](support.md).

    In the meantime, you can try using one of the alternative ways of accessing EESSI,
    like [using a container](getting_access/eessi_container.md).

---

## EuroHPC JU systems

EESSI is available on several of the [EuroHPC JU supercomputers](https://eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en).

### Karolina (Czech Republic)

Karolina is the EuroHPC JU supercomputer hosted by [IT4Innovations](https://www.it4i.cz/en).

* [General documentation](https://docs.it4i.cz/karolina/introduction)
* [EESSI @ Karolina](https://docs.it4i.cz/software/eessi)

### Vega (Slovenia)

Vega is the EuroHPC JU supercomputer hosted by the [Institute for Information Science (IZUM)](https://izum.si/en/home).

* [General documentation](https://doc.vega.izum.si)
* [EESSI @ Vega](https://doc.vega.izum.si/eessi)

### Deucalion (Portugal)

Deucalion is the EuroHPC JU supercomputer hosted by the [Minho Advanced Computing Center (MACC)](https://www.macc.fccn.pt/).
EESSI is supported in the ARM and GPU-accelerated partitions of Deucalion with plans to expand to the non-accelerated x86 partition soon.

* [General documentation](https://docs.deucalion.macc.fccn.pt/)
* [EESSI @ Deucalion](https://docs.deucalion.macc.fccn.pt/jobs/eessi/)

### MareNostrum 5 (Spain)

MareNostrum 5 is the EuroHPC JU supercomputer hosted by the [Barcelona Supercomputing Center (BSC](https://www.bsc.es/).

* [General documentation](https://www.bsc.es/supportkc/)

---

## Other European systems


### Belgium

#### Ghent University

* Tier-2 clusters: [General documentation](https://docs.hpc.ugent.be)
* VSC Tier-1 Hortense: [General documentation](https://docs.vscentrum.be/gent/tier1_hortense.html)

#### Vrije Universiteit Brussel

* Hydra: [General documentation](https://hpc.vub.be/docs/) | [EESSI @ Hydra](https://hpc.vub.be/docs/software/modules/#european-environment-for-scientific-software-installations)


### Germany

#### EMBL Heidelberg

* HPC cluster: [General documentation](https://www.embl.org/about/info/it-services/it-infrastructure)

#### Jülich Supercomputing Centre

* JUSUF: [General documentation](https://apps.fz-juelich.de/jsc/hps/jusuf/index.html)

#### University of Stuttgart

* Ant: [General documentation](https://www2.icp.uni-stuttgart.de/~jgrad/hpc/_pages/_hpc_facilities/ant.html)

### Greece

#### Aristotle University of Thessaloniki

* Aristotle: [General documentation](https://hpc.it.auth.gr/nodes-summary_en/) | [EESSI @ Aristotle](https://hpc.it.auth.gr/software/eessi/)

### Luxembourg

#### University of Luxembourg

* ULHPC platform: [General documentation](https://hpc-docs.uni.lu/) | [EESSI @ ULHPC](https://hpc-docs.uni.lu/software/eessi/)

### Netherlands

#### SURF

* Snellius: [General documentation](https://servicedesk.surf.nl/wiki/display/WIKI/Snellius) | [EESSI @ Snellius](https://servicedesk.surf.nl/wiki/display/WIKI/EESSI+software+environment)
* Spider: [General documentation](https://doc.spider.surfsara.nl/en/latest/index.html) | [EESSI @ Spider](https://doc.spider.surfsara.nl/en/latest/Pages/software/eessi.html)
* Research Cloud: [General documentation](https://servicedesk.surf.nl/wiki/display/WIKI/SURF+Research+Cloud) | [EESSI @ Research Cloud](https://servicedesk.surf.nl/wiki/display/WIKI/RC+component+EESSI+Client)

#### University of Groningen

* Hábrók: [General documentation](https://wiki.hpc.rug.nl/habrok/introduction/cluster_description)
* Managed Linux workspace (LWP): [General documentation](https://lwpwiki.webhosting.rug.nl/) | [EESSI @ LWP](https://lwpwiki.webhosting.rug.nl/index.php/EESSI)

### Norway

#### Sigma2 AS / Norwegian Research Infrastructure Services

* Betzy: [General documentation](https://documentation.sigma2.no/hpc_machines/betzy.html#betzy) | [EESSI @ Betzy](https://documentation.sigma2.no/software/eessi.html)
* Fram: [General documentation](https://documentation.sigma2.no/hpc_machines/fram.html#fram) | [EESSI @ Fram](https://documentation.sigma2.no/software/eessi.html)
* Saga: [General documentation](https://documentation.sigma2.no/hpc_machines/saga.html#saga) | [EESSI @ Saga](https://documentation.sigma2.no/software/eessi.html)
* [Norwegian AI Cloud](https://www.naic.no/) - Offers a provisioning system for virtual machines (VM) with preconfigured access to EESSI. Users can launch VMs on a local OpenStack-based cloud and on the commercial clouds Google and Azure.

### Spain

#### Barcelona Supercomputing Center

* thunder
* arriesgado-fedora37: [General documentation](https://repo.hca.bsc.es/gitlab/epi-public/risc-v-vector-simulation-environment/-/wikis/HCA-RISC%E2%80%90V-clusters-user-guide)
This is a RISC-V cluster that uses [riscv.eessi.io](https://www.eessi.io/docs/repositories/riscv.eessi.io/)
* arriesgado-hirsute: [General documentation](https://repo.hca.bsc.es/gitlab/epi-public/risc-v-vector-simulation-environment/-/wikis/HCA-RISC%E2%80%90V-clusters-user-guide)
This is a RISC-V cluster that uses [riscv.eessi.io](https://www.eessi.io/docs/repositories/riscv.eessi.io/)

#### Galicia Supercomputing Center (CESGA)

* FinisTerrae III: [General documentation](https://cesga-docs.gitlab.io/ft3-user-guide/overview.html) | [EESSI @ FinisTerrae III](https://cesga-docs.gitlab.io/ft3-user-guide/compilers_and_dev_tools.html#eessi)

---

## Systems outside of Europe

### United States of America

#### Michigan State University

* Institute for Cyber-Enabled Research (ICER): [General documentation](https://icer.msu.edu/)

---

## Other infrastructures

### AWS

* AWS ParallelCluster [General documentation](https://docs.aws.amazon.com/parallelcluster/) | [EESSI @ AWS ParallelCluster](https://github.com/aws-samples/aws-hpc-recipes/tree/main/recipes/env/eessi)
