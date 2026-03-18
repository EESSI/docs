---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Flux is a flexible framework for resource management, built for\
    \ your site. The\n framework consists of a suite of projects, tools, and libraries\
    \ which may be\n used to build site-custom resource managers for High Performance\
    \ Computing\n centers. Unlike traditional resource managers, Flux can run as a\
    \ parallel job\n under most launchers that support MPI, including under Flux itself.\
    \ This not\n only makes batch scripts and workflows for Flux portable to other\
    \ resource\n managers (just launch Flux as a job), but it also means that batch\
    \ jobs have\n all the features of a full resource manager at their disposal, as\
    \ if they have\n an entire cluster to themselves.\n"
  license: Not confirmed
  name: Flux
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
  softwareVersion: '[''0.80.0'']'
  url: https://flux-framework.org/
---
# Flux



 Flux is a flexible framework for resource management, built for your site. The
 framework consists of a suite of projects, tools, and libraries which may be
 used to build site-custom resource managers for High Performance Computing
 centers. Unlike traditional resource managers, Flux can run as a parallel job
 under most launchers that support MPI, including under Flux itself. This not
 only makes batch scripts and workflows for Flux portable to other resource
 managers (just launch Flux as a job), but it also means that batch jobs have
 all the features of a full resource manager at their disposal, as if they have
 an entire cluster to themselves.


<small>homepage: </small><span class="software-link">[https://flux-framework.org/](https://flux-framework.org/)</span>

## Available installations


|Flux version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.80.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Flux/0.80.0-GCC-13.3.0`|

## Extensions

Overview of extensions included in Flux installations


### flux-core


|`flux-core` version|Flux modules that include it|
| --- | --- |
|0.80.0|`Flux/0.80.0-GCC-13.3.0`|

### flux-pmix


|`flux-pmix` version|Flux modules that include it|
| --- | --- |
|0.7.0|`Flux/0.80.0-GCC-13.3.0`|

### flux-sched


|`flux-sched` version|Flux modules that include it|
| --- | --- |
|0.48.0|`Flux/0.80.0-GCC-13.3.0`|