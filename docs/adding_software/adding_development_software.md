# Adding software to `dev.eessi.io`

## What is `dev.eessi.io`?

`dev.eessi.io` is the [development repository of EESSI](repositories/dev.eessi.io.md).

## Adding software

Using `dev.eessi.io` is similar to using EESSI's production repository `software.eessi.io`. Software builds are triggered by a [bot](https://www.eessi.io/docs/bot/) listening to pull requests in [GitHub repositories](https://github.com/search?q=org%3AEESSI+dev.eessi.io&type=repositories). Each repository , where corresponding easystack files and easyconfig files are placed.

```
dev.eessi.io-example
├── easyconfigs
└── easystacks
```

Creating a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) that adds an entry to an easystack file under one of the projects will allow authorized users to trigger 
a build with the command `bot: build` through a GitHub comment.

Deploying pre-release builds of software

### easyconfig files and `--software-commit`
The approach to build and install software is similar to that of `software.eessi.io`. 
It requires an easyconfig file which for `dev.eessi.io` need not be part of https://easybuilders/easybuild-easyconfigs 
as these easyconfigs can simply be placed under `project/easyconfigs`.

To allow for development builds, we leverage the `--software-commit` functionality (requires [EasyBuild](https://easybuild.io/) v4.9.3 or higher). This lets us build a given application from
a specific commit in repository. This can also be done from a fork, by changing the `github_account` field in the easyconfig file. 
We've created a template for `ESPResSo` based on the standard eaasyconfig of the most recent version. The relevant fields are:

``` python
easyblock = 'CMakeMake'

name = 'ESPResSo'
version = 'devel'
versionsuffix = '-%(software_commit)s'

homepage = 'https://espressomd.org/wordpress'
description = """A software package for performing and analyzing scientific Molecular Dynamics simulations."""

github_account = 'espressomd'
source_urls = ['https://github.com/%(github_account)s/%(name)s/archive/']

sources = ['%(software_commit)s.tar.gz']
```

One can also make new changes to the easyconfig file, for example, if the new functionality requires new build or 
runtime dependencies, patches, configuration options, etc. It's a good idea to try installing from a specific commit locally first,
to at least see if everything is parsed correctly and confirm that the right sources are being downloaded. Note that while you can 
also build software from 


### Easystack files and triggering builds

After the easyconfig file has been created and added to the `easyconfigs` subdirectory, an [easystack file](https://docs.easybuild.io/easystack-files) that picks it up
needs to be in place. 

!!! note "Naming convention for easystack files"

    The easystack files must follow a naming convention and be named something
    like: `software-eb-X.Y.Z-dev.yml`, where X.Y.Z correspond to the EasyBuild
    version used to install the software. Following our example for 
    `ESPREsSo`, it would look like: 
    
    ``` yml
    easyconfigs:
      - ESPResSo-devel-foss-2023a-software-commit.eb:
          options:
            software-commit: 2ba17de6096933275abec0550981d9122e4e5f28 # release 4.2.2
    ```

The `ESPResSo-devel-foss-2023a-software-commit.eb` would be the easyconfig file added in the step above. 
Note the option passing the `software-commit` for the development version that should be built. 
For the sake of this example, the chosen commit actually corresponds to the 4.2.2 release.

To trigger a build, all one needs to do is open a PR with the changes adding the easyconfig and easystack 
files and commenting `bot: build`. This can only be done by previously authorized users. 
The current build cluster builds for the `zen2` CPU microarchitecture, but this is likely to change.

Once a build is complete and the `bot:deploy` label is added, a staging PR can be merged to deploy the
application to the `dev.eessi.io` cvmfs repository. On a system with `dev.eessi.io` mounted, then all
that is left is to `module use /cvmfs/dev.eessi.io/versions/2023.06/modules/all` and try out the software!

