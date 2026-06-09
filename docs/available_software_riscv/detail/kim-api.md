---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Open Knowledgebase of Interatomic Models.\n\nKIM is an API and OpenKIM\
    \ is a collection of interatomic models (potentials) for\natomistic simulations.\
    \  This is a library that can be used by simulation programs\nto get access to\
    \ the models in the OpenKIM database.\n\nThis EasyBuild only installs the API,\
    \ the models can be installed with the\npackage openkim-models, or the user can\
    \ install them manually by running\n    kim-api-collections-management install\
    \ user MODELNAME\nor\n    kim-api-collections-management install user OpenKIM\n\
    to install them all.\n "
  license: Not confirmed
  name: kim-api
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
  softwareVersion: '[''2.4.1'']'
  url: https://openkim.org/
---
# kim-api


Open Knowledgebase of Interatomic Models.

KIM is an API and OpenKIM is a collection of interatomic models (potentials) for
atomistic simulations.  This is a library that can be used by simulation programs
to get access to the models in the OpenKIM database.

This EasyBuild only installs the API, the models can be installed with the
package openkim-models, or the user can install them manually by running
    kim-api-collections-management install user MODELNAME
or
    kim-api-collections-management install user OpenKIM
to install them all.
 

<small>homepage: </small><span class="software-link">[https://openkim.org/](https://openkim.org/)</span>

## Available installations


|kim-api version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.4.1|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`kim-api/2.4.1-GCC-14.3.0`|