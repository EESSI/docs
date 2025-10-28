# EESSI Versions

EESSI is organized in different dated versions. Each EESSI version contains a version of the [compatibility layer](compatibility_layer.md) and its' own set of software applications. In addition, a particular EESSI version will target a different set of [common toolchains](https://docs.easybuild.io/common-toolchains/) to build software with. As an example, the first production EESSI version was released in June 2023 and is named `2023.06`. It contains the production release of the compatibility layer used to build software, and contains software build using the  `foss/2022b`, `foss/2023a`, and `foss/2023b` [software toolchains](https://docs.easybuild.io/common-toolchains/#common_toolchains_overview) as defined in EasyBuild. 

The vast majority of changes are fully transparent to users. Apart from selecting a newer version when starting up EESSI, and accessing an update collection of software, the functionality remains the same, with little to no extra effort needed to use a new version compared to and older one.

Going forward, EESSI will have yearly version releases, which will target a more recent set of toolchains and an updated set of compatibility layer components.

## Current EESSI versions

| EESSI Version       | Included toolchains                    | Software list                                                                        |
| ------------------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| 2023.06 (default)   | `foss/2022b` `foss/2023a` `foss/2023b` | [2023.06](https://www.eessi.io/docs/available_software/overview/) (software count?)  |
| 2025.06             | `foss/2024a` `foss/2025a`              | PLACEHOLDER LINK                                                  (software count?)  |

The current default EESSI version is `2023.06`. Version `2025.06` is already fully available and will be made the default soon, once it contains more software. 

## Switching between EESSI versions

* The simplest way to load a specific EESSI version or to switch between them, is to load the appropriate environment module. To access version `2023.06` one can simply do `module load EESSI/2023.06` module. To switch to the 2025.06 version, `module load EESSI/2025.06`. This will automatically set up the environment and avoid conflicts between versions.