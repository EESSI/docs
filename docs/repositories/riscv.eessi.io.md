# EESSI RISC-V development repository (`riscv.eessi.io`)

This repository contains development versions of an EESSI RISC-V software stack.
Note that versions may be added, modified, or deleted at any time.

## Accessing the RISC-V repository

See [Getting access](../getting_access/is_eessi_accessible.md);
by making the EESSI CVMFS domain available, you will automatically have access to `riscv.eessi.io` as well.

## Using `riscv.eessi.io`

This repository does not have any initialization scripts nor actual applications available yet.
Also, it is not clear yet which RISC-V CPUs will be supported.

The RISC-V compatibility layer is already available and can be used, as shown in the following example:

``` { .bash .copy }
$ ls /cvmfs/riscv.eessi.io/versions/20240307/compat/linux/riscv64/
bin  lib    opt     run   stage1.log  stage3.log   tmp  var
etc  lib64  reprod  sbin  stage2.log  startprefix  usr

$ /cvmfs/riscv.eessi.io/versions/20240307/compat/linux/riscv64/startprefix
Entering Gentoo Prefix /cvmfs/riscv.eessi.io/versions/20240307/compat/linux/riscv64
$ which gcc
/cvmfs/riscv.eessi.io/versions/20240307/compat/linux/riscv64/usr/bin/gcc
$ gcc --version
gcc (Gentoo 13.2.1_p20240210 p14) 13.2.1 20240210
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

## Infrastructure status

The status of the CernVM-FS infrastructure for this repository is shown at [https://status.eessi.io](https://status.eessi.io/).
