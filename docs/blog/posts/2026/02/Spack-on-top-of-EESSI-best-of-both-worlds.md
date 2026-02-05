---
authors: [lorisercole]
date: 2026-02-05
slug: Spack-on-top-of-EESSI-best-of-both-worlds
---

# Using Spack on Top of EESSI: Best of Both Worlds

<figure markdown="span">
![Spack + EESSI](../01/spack-plus-eessi.webp){width=75%}
</figure>

The HPC software landscape offers powerful tools for managing scientific software, such as [EasyBuild](https://easybuild.io) and [Spack](https://spack.io).

[EESSI](https://www.eessi.io) provides a ready-to-use software stack with thousands of optimized packages built with EasyBuild. 

Imagine you are working on an HPC system with EESSI already available. You have access to a wealth of optimized scientific software packages, libraries, tools, as well as compilers. But you need to install a new tool or a specific version of a package that's not in EESSI yet.

You can already extend EESSI with new software through the [EESSI-extend](https://www.eessi.io/docs/using_eessi/building_on_eessi/#building-software-on-top-of-eessi-with-easybuild) module.
This utility provides you with a pre-configured EasyBuild installation that you can use to build packages from [EasyConfig files](https://docs.easybuild.io/terminology/#easyconfig_files).

Like EasyBuild, [Spack](https://spack.io) is a flexible build tool that also offers a vast repository of build recipes maintained by a large and active community, making it a familiar tool for many HPC users.
By enabling Spack to leverage packages already available in EESSI as dependencies, we can offer users the best of both worlds: the convenience of a pre-built, optimized software stack combined with the flexibility to quickly build new packages using tools they already know.

In a previous [blog post](https://www.eessi.io/docs/blog/2026/01/09/Spack-on-top-of-EESSI-PoC/), we presented a first proof-of-concept implementation of this vision. 
We used a custom-built upstream database to make Spack aware of EESSI's software stack and managed to build a new Quantum ESPRESSO installation that reused dependencies from EESSI.

Thanks to recent updates to Spack (in particular, treating externals as concrete specs and allowing the definition of dependencies – see [this PR](https://github.com/spack/spack/pull/51118)) and an active collaboration with its developers, it is now possible to connect Spack and EESSI in a *seamless* and *Spack-native* way.

<!-- more -->


## How it works

Spack 1.1+ introduces external packages treated as concrete specs (i.e. like any other spec), with dependency support, allowing us to expose EESSI packages as externals along with their dependencies.
This is the proper, *Spack-onic* way to achieve our goal, and it does not require any* modification of Spack's source code, nor the creation of a custom database.

(*note: currently we need to add a small patch to Spack, to make sure its compiler wrapper works correctly with the unusual sysroot configuration of EESSI. This is a known [issue](https://github.com/spack/spack/issues/51582) that will be addressed in future Spack releases.)

We implement the following workflow to connect Spack to EESSI, and build a new Quantum ESPRESSO with Spack reusing EESSI packages as dependencies.


### Step 1 – EESSI software-layer builds

Declare EESSI software-layer builds as [external packages](https://spack.readthedocs.io/en/latest/packages_yaml.html#external-packages) in a `packages.yaml` configuration file with [external dependencies](https://spack.readthedocs.io/en/latest/packages_yaml.html#specifying-dependencies-among-external-packages).

![Example packages.yaml of software installations included in EESSI](spack-eessi-20260205-001.webp)

*Variants* (e.g. `~mpi+openmp`) should be specified to the best of our knowledge. By default, Spack will fill in the gaps with the package's default variants.

*Link* and *runtime dependencies* should be specified whenever possible. Pure build dependencies are not needed (the only exception being the *compiler*, Spack can reuse this information).
A dependency spec should unambiguously point to another declared external package. If an ambiguity exists, Spack will throw an error.<br>
Many packages in EESSI depends on packages of the compatibility layer (e.g. `zlib`), that were filtered out during the build process. To detect these packages, see the [next step](#step-2-optional-suggested-eessi-compat-layer).<br>
Anyway, software packages in EESSI are always RPATH-ed to their dependencies, so in most real-case scenarios linking will likely work even if you forget to declare some dependencies. 


### Step 2 – (optional, suggested) EESSI compat-layer

It is possible to detect OS packages available under the EESSI compat-layer and configure Spack to use them as externals.
In EESSI, these packages are often dependencies of software-layer packages (see previous example), so it is suggested to include them.<br>
This can be done automatically via `spack external find`:

![Detect compat-layer packages with spack external find](spack-eessi-20260205-002.webp)


### Step 3 – Show configured externals

Externals can then be listed via `spack find --show-configured-externals`.
These packages will get reused during Spack solves by default.

![Show configured externals](spack-eessi-20260205-003.webp)


### Step 4 – Build a new Quantum ESPRESSO with Spack

We can now build new packages with Spack, reusing EESSI installations as dependencies!
Let's try this out by building a new Quantum ESPRESSO with Spack.

We first check what the concretizer comes up with, using `spack spec`:

![Spack spec for quantum-espresso](spack-eessi-20260205-004.webp)

Looks good! Spack is reusing EESSI packages as external dependencies, and only needs to build the new package itself and a few (Spack-specific) ones (`compiler-wrapper`, `gcc-runtime` which is copy of runtime libraries).

Finally, we can proceed with the installation with `spack install quantum-espresso~mpi`:

![Installing Quantum ESPRESSO with Spack on top of EESSI](spack-eessi-20260205-006.webp)


### Step 5 – Verify and run Quantum ESPRESSO

Finally, we can verify that the new Quantum ESPRESSO installation works correctly by running it:

![Running Quantum ESPRESSO installed with Spack](spack-eessi-20260205-005.webp)

When we inspect the `pw.x` binary, we can see that it links to libraries provided by EESSI:

![Inspecting the list of libraries that `pw.x` binary links to](spack-eessi-20260205-007.webp)

(the only exception being `libgomp`, `libgfortran`, `libgcc_s` which come from the `gcc-runtime` package that Spack installs: this is just a local copy of the GCC runtime libraries that were provided by EESSI's `gcc@13.2.0`).


## Demo code

A demonstrated implementation of the presented approach is now available in the [EasySpack repository](https://github.com/lorisercole/easyspack).

A simple [example script](https://github.com/lorisercole/easyspack/blob/develop/quick_start.sh) showcases the workflow.
It only requires a running EESSI environment and a patched Spack installation (see instructions in the [README](https://github.com/lorisercole/easyspack/blob/develop/README.md)).

<details>
<summary>Example output of `quick_start.sh`</summary>

<figure>
	<img src="../../easyspack-demo-1.webp" alt="Output of quick_start.sh" />
</figure>
<figure>
	<img src="../../easyspack-demo-2.webp" alt="Output of quick_start.sh" />
</figure>
<figure>
	<img src="../../easyspack-demo-3.webp" alt="Output of quick_start.sh" />
</figure>

</details>


## Conclusions and outlook

The workflow we presented is a simple demonstration of how Spack can be integrated with EESSI to leverage its optimized software stack.
More complex scenarios, like building MPI-enabled packages and pre-configured toolchains, are being actively explored.

A complete integration of Spack with EESSI will require building some automation around the generation of the `packages.yaml` files to keep them in sync with EESSI updates, as well as further testing and validation of various build scenarios.

Such an integration will open powerful workflows for HPC users and administrators, allowing new software to be built quickly on top of EESSI's stable, optimized base by leveraging either Spack or EasyBuild.

The future of HPC software management is not about choosing between distributions and package managers: it is about making them work together seamlessly.

---

### Learn more and get involved

We encourage you to join the discussion on the `#spack` channel of [EESSI Slack](https://join.slack.com/t/eessi-hpc/shared_invite/zt-2wg10p26d-m_CnRB89xQq3zk9qxf1k3g) and share your experiences and suggestions!

### Acknowledgements

This work was made possible thanks to the collaboration with the Spack development team, in particular Todd Gamblin and Massimiliano Culpo, as well as EESSI team members Kenneth Hoste and Alan O'Cais.
