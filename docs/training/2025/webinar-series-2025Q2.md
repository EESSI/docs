# EESSI webinar series (May-June 2025)

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

**In you have any questions regarding these webinars, please send an email to `support@eessi.io`.**

## Sessions

- Monday 5 May 2025 (13:30-15:30 CEST): **Introduction to EESSI**
- Monday 12 May 2025 (13:30-15:30 CEST): **Introduction to CernVM-FS**
- Monday 19 May 2025 (13:30-15:30 CEST): **Introduction to EasyBuild** (incl. EasyBuild 5.0.0)
- Monday 26 May 2025 (13:30-15:30 CEST): **EESSI for CI/CD**
- Monday 2 June 2025 (13:30-15:30 CEST): **Using EESSI as the base for a system stack**

## Format

- Online webinars (via Zoom)
- Mix of presentation & hands-on demos: ~1.5h of content, ~30min for Q&A

## Registration

Attendance is free of cost, but registration is required.

**Register via [https://event.ugent.be/registration/eessi202505](https://event.ugent.be/registration/eessi202505)**

## Q&A via Slack

For posting questions or comments during the webinar, we strongly prefer that you post them
in the **`#webinar-series-2025q2` channel in the EESSI Slack** ([direct link to that channel](https://eessi-hpc.slack.com/archives/C068DV7GY3V)).

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

- Monday 5 May 2025, 13:30-15:30 CEST (Zoom webinar)
- speakers:
    - Richard Topuchain (University of Bergen)
    - Helena Vela (Do IT Now)
- moderators:
    - Thomas Röblitz (University of Bergen)
    - Kenneth Hoste (Ghent University)

#### Outline

Discover how EESSI (European Environment for Scientific Software Installation) is transforming
the way scientific software is deployed and shared across HPC systems, cloud platforms, and even laptops.

In this session, we'll introduce the motivation behind EESSI, its architecture, and how you can start using
a fully pre-built, modular software environment — no matter where you compute. Whether you're an HPC user,
sysadmin, or developer, this webinar will show how EESSI can help you save time, improve reproducibility,
and simplify your scientific workflows.

#### Materials

- [slides (PDF)](EESSI-webinars-MayJune-2025-001-Introduction-to-EESSI-20250505.pdf)
- [recording (YouTube)](https://www.youtube.com/watch?v=FvVbzKLn-C8)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/FvVbzKLn-C8?si=WSTP8vw51zcpdtRB" title="YouTube video player"
frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

### Introduction to CernVM-FS

- Monday 12 May 2025, 13:30-15:30 CEST (Zoom webinar)
- speakers:
    - Valentin Volkl (CERN)
    - Kenneth Hoste (Ghent University)

#### Outline

CernVM-FS, the CernVM File System a.k.a. CVMFS (https://cernvm.cern.ch/fs), is a file distribution service
that is particularly well suited to distribute software installations across a large number of systems world-wide
in an efficient way.

In this webinar, we will introduce you to CernVM-FS, show how to access existing CernVM-FS repositories (like [EESSI](https://eessi.io),
cover some aspects specific to using CernVM-FS on HPC systems.

It is intended for people who are interested in CernVM-FS (system administrators, support team members, researchers, etc.),
no specific prior knowledge or experience with it is required.

#### Materials

- [slides (PDF)](EESSI-webinars-MayJune-2025-001-Introduction-to-CernVM-FS-20250512.pdf)
- [recording (YouTube)](https://www.youtube.com/watch?v=5-IYnxCz_aQ)

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/5-IYnxCz_aQ?si=zqgYBiZCdY5islK8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

### Introduction to EasyBuild

- Monday 19 May 2025, 13:30-15:30 CEST
- speakers:
    - Kenneth Hoste (Ghent University)

#### Outline

EasyBuild (https://easybuild.io) is an open-source software installation tool written in Python that aims to support
the various installation procedures used by the vast collection of software packages that are typically installed from source code
in an HPC environment.

In this webinar, we will introduce you to EasyBuild, show how to install and configure it, and present basic usage through
hands-on demos. We will also cover some new capabilities that are supported by the recently released [EasyBuild v5.0.0](https://docs.easybuild.io/easybuild-v5/).

---

### EESSI for CI/CD

- Monday 26 May 2025, 13:30-15:30 CEST
- speakers:
    - Alan O'Cais (CECAM, University of Barcelona)

#### Outline

*(more info soon)*

---

### Using EESSI as the base for a system stack

- Monday 2 June 2025, 13:30-15:30 CEST
- speakers:
    - Bob Dröge (University of Groningen)
    - Pedro Santos Neves (University of Groningen)

#### Outline

Despite being very open to community contributions, EESSI is unlikely to provide all the software you want to offer
on your system as an HPC site. For instance, it will never be able to provide proprietary software due to license constraints.

This session focuses on how you can use EESSI as the base for a system software stack, and easily build additional software on top
and add it to your local software share. A recommended setup using CernVM-FS will be shown, but pointers for using any other (shared)
filesystem will also be given. Finally, we will show how the EESSI build workflow (using a build bot and pull requests) can be adopted
for your local software installations.

This webinar is particularly intended for system administrators or support team members that maintain the central software stack
for the users of their HPC infrastructure, but it can also be useful for end users who want to install additional software.

---

!!! tip
    Attending these sessions is free, but you must be registered to get an invitation to join the Zoom webinar sessions!

    See also [Registration](#registration).
