# Leverage EESSI's build procedure for site builds
In this approach, you use the EESSI build bot (`EESSI/eessi-bot-software-layer`), together with the EESSI build scripts (`EESSI/software-layer-scripts`) to build and deploy software into a CernVM-FS repository of your own. Essentially, this means you'll build in a way that is essentially identical to how it is done for upstream EESSI - with the only major difference being the target CernVM-FS repository.

## Setup steps
What we need:
- Infrastructure for a site-specific CVMFS repository (Stratum 0, Stratum 1, proxies, client configuration)
- An instance of the EESSI build bot
- A bucket in an AWS S3-compatible object store (though you could work around this)
- A GitHub organization on which you can install GitHub Apps
- A GitHub repository within that organization which will be used to list the software you want to build
- Optionally: an automated procedure to ingest tarballs

This documentation will go through the steps to set each of these up, in order. Since many of these individual steps are documented elsewhere, we will often reference that (and only list a very short summary here).

### A site-specific CVMFS infrastructure
The recommended CVMFS setup for a site-specific CVMFS repository is:
- A Stratum 0 servers
- Two (or more) Stratum 1 servers
- Two (or more) proxies

Main reason here is:
- Having two Stratum 1's provides redundancy: if one dies, proxies seamlessly failover to the other one.
- Having two proxies provides both redundancy _and_ load balancing. If one proxy dies, clients failover to the other one. If clients are configured to use the proxies in a [proxy group](https://cvmfs.readthedocs.io/en/2.8/cpt-configure.html#proxy-lists), each client selects a proxy randomly, thus providing load balancing.

!!! note

    The recommended CVMFS setup requires a fair amount of machines. If this is more than you can afford, there are some tricks you can pull. First, you can combine each proxy with a Stratum 1 on the same machine, only use the proxies for proxy-ing upstream EESSI, and simply have your clients contact your site-specific Stratum 1's directly (without proxy). In this scenario, you can achieve load-balancing by configuring half your clients with `CVMFS_SERVER_URL="<instance_1>;<instance_2>"` and half with `CVMFS_SERVER_URL="<instance_2>;<instance_1>"`, where `instance_1` and `instance_2` are the IPs of your Stratum 1's. Finally, you can even use the Stratum 0 instead of a second Stratum 1. Note that this has security implications, as it means your Stratum 0 needs to be directly accessible to your clients. This is a potential concern: if there are vulnarebilities in the Stratum 0 software, end-users may be able to push (malicious) software in there.

An extensive [tutorial](https://cvmfs-contrib.github.io/cvmfs-tutorial-2021/) is available that teaches how to setup each of these machines, and how to configure the clients to use the relevant Stratum 1's and proxies. Below, we will summarize some of the key steps, and point out things that are specifically relevant for this setup.

#### Setting up the Stratum 0

