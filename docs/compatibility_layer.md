# Compatibility layer

![Compatibility layer](img/compatibility_layer.png)

The middle layer of the EESSI project is the **compatibility layer**,
which ensures that our scientific software stack is compatible with
different client operating systems (different Linux distributions,
macOS and even Windows via [WSL](https://docs.microsoft.com/en-us/windows/wsl/)).

For this we rely on [Gentoo Prefix](https://wiki.gentoo.org/wiki/Project:Prefix),
by installing a limited set of Gentoo Linux packages in a non-standard location
(a "prefix"), using Gentoo's package manager [Portage](https://wiki.gentoo.org/wiki/Portage).

The compatible layer is maintained via our [https://github.com/EESSI/compatibility-layer](https://github.com/EESSI/compatibility-layer) GitHub repository.
