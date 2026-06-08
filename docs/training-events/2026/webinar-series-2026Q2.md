# EESSI webinar series (April-May 2026)

_provided by [EuroHPC CoE MultiXscale](https://www.multixscale.eu)_

!!! tip
    Attending these sessions is free, but you must be registered to get an invitation to join the Zoom webinar sessions!

    See also [Registration](#registration).

**What if you no longer have to install a broad range of scientific software from
scratch on every laptop, HPC cluster, or cloud instance you use or maintain,
without compromising on performance?**

The European Environment for Scientific Software Installations (EESSI, [https://eessi.io](https://eessi.io)) comes to the rescue!

In this webinar series we will provide a comprehensive overview of EESSI: why we started it, how it works, how you can use it, ...

You can register for the sessions listed below (either all of them, or selected ones).

All sessions will be recorded. Recordings, slides, and materials used will be made publicly available shortly after each session via this page.

**If you have any questions regarding these webinars, please send an email to `support@eessi.io`.**

## Sessions

- Monday 27 April 2026 (14:00-16:00 CEST): **Introduction to EESSI**
- Monday 4 May 2026 (14:00-16:00 CEST): **Building software on top of EESSI + contributing to EESSI**
- Monday 11 May 2026 (14:00-16:00 CEST): **Using EESSI for Continuous Integration**
- Monday 18 May 2026 (14:00-16:00 CEST): **Introduction to CernVM-FS**
- Monday 1 June 2026 (14:00-16:00 CEST): **Using EESSI as a base for a central software stack**

[YouTube playlist with recordings](https://www.youtube.com/watch?v=I-KUy023I2Q&list=PL6_PkP_6pUtZu-Er2Xi2W2eJ-KugM-Btr)

## Format

- Online webinars (via Zoom)
- Mix of presentation & hands-on demos: ~1.5h of content, ~30min for Q&A

## Registration {: #registration }

Attendance is free of cost, but registration is required.

**Register via [https://event.ugent.be/registration/eessiwebinarsspring2026](https://event.ugent.be/registration/eessiwebinarsspring2026)**

## Q&A via Slack

For posting questions or comments during the webinar, we strongly prefer that you post them
in the **`#webinar-series-2026q2` channel in the EESSI Slack** ([direct link to that channel](https://eessi-hpc.slack.com/archives/C0AP84QKU05)).

If you haven't joined the EESSI Slack yet, first use the "`Slack channel`" link on the [EESSI website (https://eessi.io)](https://eessi.io).

There will also be an opportunity at the end of the webinar to ask questions directly to the speakers, should you wish to do so.

## Useful links

- EESSI website: [https://eessi.io](https://eessi.io)
- EESSI documentation: [https://eessi.io/docs](https://eessi.io/docs)
- CernVM-FS website: [https://cernvm.cern.ch/fs](https://cernvm.cern.ch/fs)
- CernVM-FS documentation: [https://cvmfs.readthedocs.io](https://cvmfs.readthedocs.io)
- EasyBuild website: [https://easybuild.io](https://easybuild.io)
- EasyBuild documentation: [https://docs.easybuild.io](https://docs.easybuild.io)
- MultiXscale website: [https://www.multixscale.eu](https://www.multixscale.eu)

---

## Session details

### Introduction to EESSI

- Monday 27 April 2026, 14:00-16:00 CEST (Zoom webinar)
- speaker: Helena Vela (Do IT Now)
- [slides (PDF)](EESSI-webinars-spring-2026-introduction-to-EESSI-2026-04-27.pdf)
- [recording (YouTube)](https://www.youtube.com/watch?v=I-KUy023I2Q)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/I-KUy023I2Q?si=c4pGvPCMU-8QPLQX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Outline

The European Environment for Scientific Software Installation (EESSI) is a collaborative initiative aimed at streamlining how scientific software is deployed and shared across diverse infrastructures, from high-performance computing (HPC) clusters and cloud platforms to local workstations. By providing a fully pre-built, modular software environment, EESSI addresses the challenges of performance and reproducibility, allowing users to access the same optimized software regardless of their specific hardware.

This session will provide an overview of the current status of EESSI and the progress made in expanding its capabilities. We will highlight broader support for modern computing technologies, including the addition of new CPU and GPU targets, as well as a significantly grown software ecosystem that now features over 750 unique software projects—or over 3,000 when including individual Python packages and R libraries.

The presentation will cover EESSI's architecture, its integration with established tools like Spack and Open OnDemand, and how it has evolved into a key service for managing software across varied infrastructures. Through a live hands-on demo, we will showcase how EESSI is utilized in real-world HPC and cloud environments. Finally, we will discuss the future direction of the platform, outlining upcoming features and improvements designed to support scientific software management in Europe and beyond.

---

### Building software on top of EESSI + contributing to EESSI

- Monday 4 May 2026, 14:00-16:00 CEST (Zoom webinar)
- speakers:
    - Lara Peeters (Ghent University)
    - Kenneth Hoste (Ghent University)
- [slides (PDF)](EESSI-webinars-spring-2026-building-contributing-2026-05-04.pdf)
- [recording (YouTube)](https://youtu.be/ZDzxDujSg0w)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/ZDzxDujSg0w?si=rBAk59xv-aSoIuL8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Outline

- A detailed look at the EESSI software layer
- Building software on top of EESSI
  - Using EasyBuild, via `EESSI-extend`
  - Manually, with the help of `buildenv`
  - Using Spack on top of EESSI
- Contributing software to EESSI

---

### Using EESSI for Continuous Integration (CI)

- Monday 11 May 2026, 14:00-16:00 CEST (Zoom webinar)
- speaker: Alan O'Cais (freelancer w/ Ghent University)
- [slides (PDF)](EESSI-webinars-spring-2026-EESSI-CI-CD-2026-05-11.pdf)
- [recording (YouTube)](https://youtu.be/Tcjubkc43Hg)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Tcjubkc43Hg?si=lBsXfq6baR3MueAg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Outline

- Introducing Continuous Integration (CI)
- Navigating EESSI to build my project
- Building my project with the EESSI GitHub Action
- Navigating EasyBuild to build with EESSI-extend
- Building with EESSI-extend and the EESSI GitHub Action
- Building my project with the EESSI GitLab Component
- CI with EESSI + Spack
- Continuous Deployment and what EESSI can offer there

---


### Introduction to CernVM-FS

- Monday 18 May 2026, 14:00-16:00 CEST (Zoom webinar)
- speaker: Valentin Volkl (CERN)
- [slides (PDF)](EESSI-webinars-spring-2026-EESSI-CVMFS-2026-05-18.pdf)
- [recording (YouTube)](https://youtu.be/jsnGDWkASnI)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/jsnGDWkASnI?si=JGejcahXMq9mK-yd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Outline

- What is CernVM-FS?
- Quick introduction to EESSI (example CernVM-FS repository)
- CernVM-FS client installation + configuration
- CernVM-FS on large-scale systems: proxy, Stratum 1
- Alternative access mechanisms for CernVM-FS repos 
- Monitoring CernVM-FS
- Troubleshooting CernVM-FS
- Creating your own CernVM-FS repository
- Software startup performance

---

### Using EESSI as a base for a central software stack

- Monday 1 June 2026, 14:00-16:00 CEST (Zoom webinar)
- speakers:
    - Caspar van Leeuwen (SURF)
    - Bob Dröge (University of Groningen)
- [slides (PDF)](EESSI-webinars-spring-2026-EESSI-as-a-base-stack-2026-06-01.pdf)
- [recording (YouTube)](https://youtu.be/WCQ2vEnQon4)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/WCQ2vEnQon4?si=9I_s31nOD1s2jZE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Outline

- Building on top of EESSI overview and motivation
- Site builds on top of EESSI in a shared file system
- Leveraging all of EESSI for site-builds
- Special cases: software rebuilds, licensed software
- Site configuration
- Discussion / Future work


#### Materials {: #materials-cvmfs }

---

!!! tip
    Attending these sessions is free, but you must be registered to get an invitation to join the Zoom webinar sessions!

    See also [Registration](#registration).
