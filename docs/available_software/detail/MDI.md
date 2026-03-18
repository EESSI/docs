---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The MolSSI Driver Interface (MDI) project provides a \nstandardized\
    \ API for fast, on-the-fly communication between computational \nchemistry codes.\
    \ This greatly simplifies the process of implementing \nmethods that require the\
    \ cooperation of multiple software packages and \nenables developers to write\
    \ a single implementation that works across \nmany different codes. The API is\
    \ sufficiently general to support a wide \nvariety of techniques, including QM/MM,\
    \ ab initio MD, machine learning, \nadvanced sampling, and path integral MD, while\
    \ also being straightforwardly \nextensible. Communication between codes is handled\
    \ by the MDI Library, which \nenables tight coupling between codes using either\
    \ the MPI or TCP/IP methods.\n"
  license: Not confirmed
  name: MDI
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
  softwareVersion: '[''1.4.29'', ''1.4.26'']'
  url: https://github.com/MolSSI-MDI/MDI_Library
---
# MDI


The MolSSI Driver Interface (MDI) project provides a 
standardized API for fast, on-the-fly communication between computational 
chemistry codes. This greatly simplifies the process of implementing 
methods that require the cooperation of multiple software packages and 
enables developers to write a single implementation that works across 
many different codes. The API is sufficiently general to support a wide 
variety of techniques, including QM/MM, ab initio MD, machine learning, 
advanced sampling, and path integral MD, while also being straightforwardly 
extensible. Communication between codes is handled by the MDI Library, which 
enables tight coupling between codes using either the MPI or TCP/IP methods.


<small>homepage: </small><span class="software-link">[https://github.com/MolSSI-MDI/MDI_Library](https://github.com/MolSSI-MDI/MDI_Library)</span>

## Available installations


|MDI version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.4.26|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`MDI/1.4.26-gompi-2023a`|
|1.4.29|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`MDI/1.4.29-gompi-2023b`|