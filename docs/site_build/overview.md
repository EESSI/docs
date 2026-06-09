# Introduction
This documentation is aimed at HPC sites or other facilities that make EESSI available on their system, but would like to offer additional installations that are performed 'on top' of EESSI (i.e. using dependencies provided by EESSI).

There are several reasons why, as a site, you may want to offer additional software on top of EESSI. For example:
1. You want to offer software that does is not suitable for upstream deployment in EESSI (e.g. because it is proprietary, or because it is a development build / otherwise very specific build that is not useful for a general audience).
2. You need to make software available on (very) short notice to your users, and cannot wait for it to be deployed in upstream EESSI.
3. You want to retain full autonomy over what gets deployed

While all of these are valid arguments, note that there is also one major downside to deploying things locally: you loose one of the core benefits of EESSI, namely that it provides _the same software on every system_. The more site-specific installations you have, the more difficult it will be for your users to move their workflows from e.g. their own development machine/cloud environment to your cluster, or scale up to larger clusters. If you're doing site-builds to make software available to your users on short notice, we highly encourage you to _also_ contribute the same software installation in upstream EESSI. This way, once accepted upstream, users that rely on that software retain their 'mobility'.

# Choosing your approach
There are two approaches to doing site builds, each with their own advantages and disadvantages.

1. Perform site builds using EESSI-extend on a shared filesystem.
2. Leverage EESSI's build procedure for site builds. In this approach, you use the EESSI build bot (`EESSI/eessi-bot-software-layer`), together with the EESSI build scripts (`EESSI/software-layer-scripts`) to build and deploy software into a CernVM-FS repository of your own. Essentially, this means you'll build in a way that is essentially identical to how it is done for upstream EESSI - with the only major difference being the target CernVM-FS repository.

In both cases, you build 'on top' of EESSI, meaning that dependencies that are already provided by EESSI will not be reinstalled: they will simply be loaded from EESSI.

Here, we list some advantages and disadvantages to help you choose which approach best suites your requirements.

## Approach 1: using EESSI-extend on shared FS

Advantages:
- Easy to get started: no additional setup or knowledge needed
- Automatically optimizes for the host on which you run the installation, and installs in architecture-specific prefix that matches the host architecture. This means you can install optimized software for each of your CPU/GPU architectures in an organized way.

Disadvantages:
- This is a manual procedure (unless you create your own automation around it). As such, doesn't scale well to installing large amounts of software and/or installing software for many different hardware targets.
- The fact that you get optimized installations means that on a very heterogeneous system, you will have to run the installation many times - once for each architecture on which you want to offer that particular piece of software.
- Shared filesystems (and especially _parallal_ filesystems) are generally ill-suited to serve software. This means start-up time can be quite long (you can find some numbers [here](../training-events/2025/tutorial-best-practices-cvmfs-hpc/performance.md)).

## Approach 2: leveraging all of EESSI's tooling for site builds

Advantages:
- Highly automated
- Scalable to many architectures & installations
- Site builds are done based on a list of software in a GitHub repo - making it very transparent what is available / got added on your system
- Share maintenance on the automation with the EESSI community
- End-user look & feel are very similar to EESSI

Disadvantages
- More setup time
- Requires more extnesive knowledge (CVMFS, EESSI build bot, object store)
- More hardware resources (CVMFS infrastructure, bot infrastructure)
- More components (software/hardware) to maintain
