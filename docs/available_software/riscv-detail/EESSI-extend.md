---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The goal of the European Environment for Scientific Software Installations
    (EESSI, pronounced as "easy") is to build a common stack of scientific software
    installations for HPC systems and beyond, including laptops, personal workstations
    and cloud infrastructure. This module allows you to extend EESSI using the same
    configuration for EasyBuild as EESSI itself uses. A number of environment variables
    control the behaviour of the module: - EESSI_USER_INSTALL can be set to a location
    to install modules for use by   the user only. The location must already exist
    on the filesystem. - EESSI_PROJECT_INSTALL can be set to a location to install
    modules for use by   a project. The location must already exist on the filesystem
    and you should   ensure that the location has the correct Linux group and the
    SGID permission   is set on that directory (`chmod g+s $EESSI_PROJECT_INSTALL`)
    so that all   members of the group have permission to read and write installations.
    - EESSI_SITE_INSTALL is either defined or not and cannot be used with another   environment
    variable. A site installation is done in a defined location and   any installations
    there are (by default) world readable. - EESSI_CVMFS_INSTALL is either defined
    or not and cannot be used with another   environment variable. A CVMFS installation
    targets a defined location which   will be ingested into CVMFS and is only useful
    for CVMFS administrators. - If none of the environment variables above are defined,
    an EESSI_USER_INSTALL   is assumed with a value of $HOME/EESSI If both EESSI_USER_INSTALL
    and EESSI_PROJECT_INSTALL are defined, both sets of installations are exposed,
    but new installations are created as user installations.'
  license: Not confirmed
  name: EESSI-extend
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''EESSI-extend/20240402-easybuild'']'
  url: https://eessi.io/docs/
---

EESSI-extend
============


The goal of the European Environment for Scientific Software Installations (EESSI, pronounced as "easy") is to build a common stack of scientific software installations for HPC systems and beyond, including laptops, personal workstations and cloud infrastructure. This module allows you to extend EESSI using the same configuration for EasyBuild as EESSI itself uses. A number of environment variables control the behaviour of the module: - EESSI_USER_INSTALL can be set to a location to install modules for use by   the user only. The location must already exist on the filesystem. - EESSI_PROJECT_INSTALL can be set to a location to install modules for use by   a project. The location must already exist on the filesystem and you should   ensure that the location has the correct Linux group and the SGID permission   is set on that directory (`chmod g+s $EESSI_PROJECT_INSTALL`) so that all   members of the group have permission to read and write installations. - EESSI_SITE_INSTALL is either defined or not and cannot be used with another   environment variable. A site installation is done in a defined location and   any installations there are (by default) world readable. - EESSI_CVMFS_INSTALL is either defined or not and cannot be used with another   environment variable. A CVMFS installation targets a defined location which   will be ingested into CVMFS and is only useful for CVMFS administrators. - If none of the environment variables above are defined, an EESSI_USER_INSTALL   is assumed with a value of $HOME/EESSI If both EESSI_USER_INSTALL and EESSI_PROJECT_INSTALL are defined, both sets of installations are exposed, but new installations are created as user installations.

https://eessi.io/docs/
# Available modules


The overview below shows which EESSI-extend installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using EESSI-extend, load one of these modules using a `module load` command like:

```shell
module load EESSI-extend/20240402-easybuild
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 12:19:02 CEST)*

| |scv64/generic|
| :---: | :---: |
|EESSI-extend/20240402-easybuild|x|
