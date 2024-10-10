# Adding software to `dev.eessi.io`

## What is `dev.eessi.io`?

`dev.eessi.io` is the development repository of EESSI. With it, developers can build and deploy non-production ready versions of their software to a CernVM-FS repository. This way, development version can easily be tested on systems where `dev.eessi.io` is available.

## Adding software

Using `dev.eessi.io` is similar to using EESSI's production repository `software.eessi.io`. Software builds are triggered by a bot listening to pull requests in GitHub repository (at the moment https://github.com/EESSI/dev.eessi.io). This repository is organised by project, where corresponding easystack files and easyconfig files are placed.

```
dev.eessi.io
├── project1
│   ├── easyconfigs
│   └── easystacks
└── project2
    ├── easyconfigs
    └── easystacks
```

Creating a PR that adds an entry to an easystack file under on of the projects will allow authorised users to trigger 
a build with the command `bot: build` through a GitHub comment.

## Building development versions

### easyconfig files and `--software-commit`
The approach to build and install software is similar to that of `software.eessi.io`. 
It requires an easyconfig file which for `dev.eessi.io` need not be part of https://easybuilders/easybuild-easyconfigs 
as these easyconfigs can simply be placed under `project/easyconfigs`.

To allow for development builds, we leverage the `--software-commit` functionality (requires EasyBuild v4.9.3 or higher). This lets us build a given application from
a specific commit in repository. This can also be done from a fork, by changing the `github_account` field in the easyconfig file. 
We've created a template for `ESPResSo` based on the standard eaasyconfig of the most recent version. The relevant fields are:

``` python
easyblock = 'CMakeMake'

name = 'ESPResSo'
version = '4.2.2'
versionsuffix = '-%(software_commit)s'

homepage = 'https://espressomd.org/wordpress'
description = """A software package for performing and analyzing scientific Molecular Dynamics simulations."""

github_account = 'espressomd'
source_urls = ['https://github.com/%(github_account)s/%(name)s/archive/']

sources = ['%(software_commit)s.tar.gz']
```

One can also make new changes to the easyconfig file, for example, if the new functionality requires new build or 
runtime dependencies, patches, flags, etc. It's a good idea to try installing from a specific commit locally first,
to at least see if everything is parsed correctly and confirm that the right sources are being downloaded.

### Easystack files and triggering builds

After the easyconfig file has been created and added to `projectX/easyconfigs`, an easystack file that picks it up
needs to be in place. This easystack file must follow a naming convention: `software-eb-X.Y.Z-dev.yml`,
where X.Y.Z correspond to the EasyBuild version used to install the software. 
Following our example for `ESPREsSo`, it would look like: 

``` yml
easyconfigs:
  - ESPResSo-4.2.2-foss-2023a-software-commit.eb:
      options:
        software-commit: 2ba17de6096933275abec0550981d9122e4e5f28 # release 4.2.2
```

The `ESPResSo-4.2.2-foss-2023a-software-commit.eb` would be the easyconfig file added in the step above. 
Note the option passing the `software-commit` for the development version that should be built. 
For the sake of this example, the chosen commit actually corresponds to the 4.2.2 release.

To trigger a build, all one needs to do is open a PR with the changes adding the easyconfig and easystack 
files and commenting `bot: build`. This can only be done by previously authorized users. 
The current build cluster builds for the `zen2` CPU microarchitecture, but this is likely to change.

Once a build is complete and the `bot:deploy` label is added, a staging PR can be merged to deploy the
application to the `dev.eessi.io` cvmfs repository. On a system with `dev.eessi.io` mounted, then all
that is left is to `module use /cvmfs/dev.eessi.io/versions/2023.06/modules/all` and try out the software!

