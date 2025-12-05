---
authors: [Crivella]
date: 2025-12-05
slug: EESSI-on-K8s-PoC
---

# EESSI on Kubernetes: A Proof of Concept

[Kubernetes](https://kubernetes.io/), also known as K8s, is an open-source container orchestration platform widely used for automating the deployment, scaling, and management of containerized applications.
Normally, deploying a specific application on Kubernetes requires preparing a container image including the target software and all its dependencies.
Furthermore, the software should be optimized depending on the target hardware architecture to achieve the best performance, which could prove particularly challenging especially on heterogeneous systems.
Implementing an integration of EESSI with Kubernetes will allow the many sites and enterprises that already use K8s to more easily get access to a wide variety of optimized software installations

In this blog post, we present a proof of concept (PoC) for deploying EESSI on a Kubernetes cluster.
A basic knowledge on running containerized applications is suggested.

## Kubernetes Cluster: an overview

While a deeper understanding of Kubernetes is beyond the scope of this post, understanding the structure of a [Kubernetes cluster](https://kubernetes.io/docs/concepts/architecture/) is essential to grasp the deployment options available for EESSI:

- Control Plane: Node running the components responsible for managing the cluster, including the API server, scheduler, controller manager and `etcd` key-value store.
  It's role is to maintain the desired state of the cluster, manage workloads, and ensure that the cluster operates smoothly.
- Worker Nodes: Nodes that run the containerized applications and services.
  Each worker node contains a container runtime (e.g., Docker, containerd), a kubelet (which communicates with the control plane), and a kube-proxy (which manages network communication).

In a minimal setup, a Kubernetes cluster can consist of a single machine acting as both the control plane and a worker node.

An important concept in Kubernetes needed for this post is that of [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).
Pods are the smallest deployable units in Kubernetes and represent a single instance of a running process in the cluster, which can contain one or more containers with shared storage and network resources.
If you are familiar with `Docker` and in particular with `Docker Compose`, you can think of a Pod as a group of containers as defined in a single `compose.yml` file.

There are several other higher-level abstractions in Kubernetes, for managing the lifecycle of Pods and for networking, storage, and configuration management, but, for the purpose of this post, knowledge of pods is sufficient.

## Minimum requirements for usage of EESSI

EESSI relies on [CernVM-FS (CVMFS)](https://cernvm.cern.ch/portal/filesystem) to provide access to the software repositories.
The main suggested way to use EESSI is to install CVMFS on the host system, and then mount the EESSI repositories, typically through [autofs](https://www.kernel.org/doc/html/latest/filesystems/autofs.html) functionalities.
Several other ways to use CVMFS are possible, and can be found by looking at how [cvmfsexec](https://github.com/cvmfs/cvmfsexec) can be used to gain access to CVMFS repositories.
The main crux behind them all is that `/dev/fuse` must be available to the process accessing CVMFS repositories, since CVMFS relies on FUSE (Filesystem in Userspace) to mount the repositories.

## Deploying EESSI on Kubernetes

Now that you have a basic understanding of Pods and the way a CVMFS filesystem (and by extension EESSI) can be accessed, we can explore the different options available to deploy EESSI on Kubernetes.

### Option 1: Installing EESSI on the host nodes

The first option is to install CVMFS directly on the worker nodes of the Kubernetes cluster.
This can be achieved by following the [official EESSI installation instructions](https://www.eessi.io/docs/getting_access/native_installation/).
Once EESSI can be accessed from the host nodes, [hostPath volumes](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) can be used to mount EESSI (eg `/cvmfs/software.eessi.io`) directly into the Pods that require it.

While this approach is relatively straightforward, it has several drawbacks:

- It requires administrative access to the worker nodes, which may not be feasible in all environments.
- Requires all nodes to have EESSI installed, or a way for the Pods to be scheduled only on nodes with EESSI.
- Introduces more complexity in managing the cluster, as the EESSI installation must be maintained and updated on each node.

### Option 2: Exporting EESSI through NFS

Another option is to set up a dedicated machine with CVMFS and EESSI installed that exports the EESSI directories through [NFS](https://en.wikipedia.org/wiki/Network_File_System).
More information on how a CVMFS filesystem can be exported through NFS can be found in the [CVMFS documentation](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#nfs-server-mode).

This is possible as Kubernetes supports the mounting of NFS shares into Pods natively through [NFS volumes](https://kubernetes.io/docs/concepts/storage/volumes/#nfs).

With respect to the previous option, this approach has the advantage of centralizing the EESSI installation, making it easier to manage and update, but it also introduces several drawbacks:

- Introduces a single point of failure, as the NFS server must be available for EESSI to be accessible.
- May introduce performance bottlenecks, especially if many Pods are accessing EESSI simultaneously.
- Could require a more complex setup to alleviate the previous points by introducing redundancy and load balancing.
- Could require the setup of multiple NFS servers or undesirable network/security configurations to allow access from all worker nodes, in particular in cloud environments (e.g., a cluster that can deploy nodes in multiple availability zones, or even on different cloud providers).

### Option 3: Mounting CVMFS directly in the Pods

As previously mentioned, CVMFS relies on FUSE to mount the filesystems.
This means that if the Pod has access to `/dev/fuse`, it can mount CVMFS filesystems directly, without requiring CVMFS to be installed on the host nodes, either by installing CVMFS inside the container or by using `cvmfsexec`.

While this approach is very flexible it also has several drawbacks:

- Natively, in order to access `/dev/fuse`, the Pod must run in privileged mode, which may not be feasible or desirable in all environments due to security concerns.
- Even though there are ways that could be used to make FUSE work without privileged mode (e.g. [smart-device-manager](https://gitlab.com/arm-research/smarter/smarter-device-manager), [fuse-device-plugin](https://github.com/kuberenetes-learning-group/fuse-device-plugin/blob/master/README_EN.md)), giving a container access to `/dev/fuse` can still be considered a security risk
- Could require re-building container images in a currently running production environment to include CVMFS.

### Option 4: Using the CVMFS-CSI plugin

The [Container Storage Interface (CSI)](https://github.com/container-storage-interface/spec?tab=readme-ov-file) is a standard for exposing storage systems to containerized workloads, which can be natively used in Kubernetes through the [CSI Volume Driver](https://kubernetes.io/docs/concepts/storage/volumes/#csi).

A plugin ([cvmfs-csi](https://github.com/cvmfs-contrib/cvmfs-csi)) for the provisioning of CVMFS filesystems through the CSI in Kubernetes has already been developed.
It works by making use of a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) that runs on each worker node.
The containers managed by the DaemonSet are responsible for mounting the CVMFS filesystems on the host nodes, and then exposing them to the Pods through the CSI and supports several mounting methods, including an `autofs` based one and a single container mode.

This option combines the best of the previous approaches as:

- Provisioning of CVMFS filesystems is centralized and managed by Kubernetes itself.
  - Can be backed up by the cluster management features (e.g., self-healing, scaling).
  - Can be updated easily by editing thee [configuration maps](https://kubernetes.io/docs/concepts/storage/volumes/#configmap) used by the DaemonSet.
- EESSI is mounted individually by every worker node, removing single points of failure and performance bottlenecks.

A demo on how to install the `cvmfs-csi` plugin already configured to mount EESSI and run examples from [eessi-demo](https://github.com/EESSI/eessi-demo) repository can be found in the [eessi-k8s](https://github.com/Crivella/eessi-k8s) github repository
