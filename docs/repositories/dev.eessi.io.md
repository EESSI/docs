# Development repository (`dev.eessi.io`)

!!! note "Is `dev.eessi.io` a webpage?"
    If you landed on this page because you typed `dev.eessi.io` into your browser, then
    you may not know yet that this is not a URL/webpage but a [CernVM-FS repository](../filesystem_layer.md)
    that EESSI uses to distribute software.
 
    **See the [EESSI overview page](../overview.md) for a general introduction to EESSI.**

## What is `dev.eessi.io`?

`dev.eessi.io` is the development repository of EESSI. With it, developers in the [MultiXscale CoE](https://multixscale.eu) can deploy pre-release builds of their software to EESSI.
This way, development versions of software can easily be tested on systems where the `dev.eessi.io` CernVM-FS repository is available, or even added to CI workflows with little effort. 

Unlike in the [software.eessi.io](software.eessi.io.md) production repository, software installations in `dev.eessi.io` are placed in an additional `project` 
subdirectory. On a system with `dev.eessi.io` mounted, and assuming one intends to use a project named `example` access is possible with 
<pre>module use /cvmfs/dev.eessi.io/<b>example</b>/versions/$EESSI_VERSION/software/linux/$EESSI_SOFTWARE_SUBDIR/modules/all</pre>. Then, all that is left is to try out the development software!

For more information on adding software to `dev.eessi.io`, please consult the relevant [documentation](../adding_software/adding_development_software.md) page.

## Question or problems

If you have any questions regarding EESSI, or if you experience a problem in accessing or using it,
please [open a support request](../support.md). If you experience issues with the development repository, feel free to use the #dev.eessi.io channel 
of the EESSI Slack.

## Infrastructure status

The status of the CernVM-FS infrastructure for the production repository is shown at [https://status.eessi.io](https://status.eessi.io/).
