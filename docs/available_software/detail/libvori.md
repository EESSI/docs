---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'C++ library implementing the Voronoi integration as well as the compressed
    bqb

    file format. The present version of libvori is a very early development

    version, which is hard-coded to work with the CP2k program package.'
  license: Not confirmed
  name: libvori
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
  softwareVersion: '[''220621'']'
  url: https://brehm-research.de/libvori.php
---
# libvori


C++ library implementing the Voronoi integration as well as the compressed bqb
file format. The present version of libvori is a very early development
version, which is hard-coded to work with the CP2k program package.

<small>homepage: </small><span class="software-link">[https://brehm-research.de/libvori.php](https://brehm-research.de/libvori.php)</span>

## Available installations


|libvori version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|220621|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libvori/220621-GCCcore-12.3.0`|