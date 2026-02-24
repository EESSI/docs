# EESSI-extend



 The goal of the European Environment for Scientific Software Installations
 (EESSI, pronounced as "easy") is to build a common stack of scientific
 software installations for HPC systems and beyond, including laptops,
 personal workstations and cloud infrastructure.

 This module allows you to extend EESSI using the same configuration for
 EasyBuild as EESSI itself uses. A number of environment variables control the
 behaviour of the module:
 - EESSI_USER_INSTALL can be set to a location to install modules for use by
   the user only. The location must already exist on the filesystem.
 - EESSI_PROJECT_INSTALL can be set to a location to install modules for use by
   a project. The location must already exist on the filesystem and you should
   ensure that the location has the correct Linux group and the SGID permission
   is set on that directory (`chmod g+s $EESSI_PROJECT_INSTALL`) so that all
   members of the group have permission to read and write installations.
 - EESSI_SITE_INSTALL is either defined or not and cannot be used with another
   environment variable. A site installation is done in a defined location and
   any installations there are (by default) world readable.
 - EESSI_CVMFS_INSTALL is either defined or not and cannot be used with another
   environment variable. A CVMFS installation targets a defined location which
   will be ingested into CVMFS and is only useful for CVMFS administrators.
 - If none of the environment variables above are defined, an EESSI_USER_INSTALL
   is assumed with a value of $HOME/EESSI
 If both EESSI_USER_INSTALL and EESSI_PROJECT_INSTALL are defined, both sets of
 installations are exposed, but new installations are created as user
 installations.

 Strict installation path checking is enforced by EESSI for EESSI and site
 installations involving accelerators. In these cases, if you wish to create an
 accelerator installation you must set the environment variable
 EESSI_ACCELERATOR_INSTALL (and load/reload this module).


<small>homepage: </small><span class="software-link">[https://eessi.io/docs/](https://eessi.io/docs/)</span>

## Available installations


|EESSI-extend version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2023.06|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`EESSI-extend/2023.06-easybuild`|
|2025.06|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`EESSI-extend/2025.06-easybuild`|