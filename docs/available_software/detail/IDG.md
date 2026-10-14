---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Image Domain Gridding (IDG) is a fast method for convolutional resampling
    (gridding/degridding)

    of radio astronomical data (visibilities). Direction dependent effects (DDEs)
    or A-tems can be applied

    in the gridding process.

    The algorithm is described in "Image Domain Gridding: a fast method for convolutional
    resampling of visibilities",

    Van der Tol (2018).

    The implementation is described in "Radio-astronomical imaging on graphics processors",
    Veenboer (2020).

    Please cite these papers in publications using IDG.

    '
  license: Not confirmed
  name: IDG
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
  softwareVersion: '[''1.2.0'']'
  url: https://idg.readthedocs.io/
---
# IDG


Image Domain Gridding (IDG) is a fast method for convolutional resampling (gridding/degridding)
of radio astronomical data (visibilities). Direction dependent effects (DDEs) or A-tems can be applied
in the gridding process.
The algorithm is described in "Image Domain Gridding: a fast method for convolutional resampling of visibilities",
Van der Tol (2018).
The implementation is described in "Radio-astronomical imaging on graphics processors", Veenboer (2020).
Please cite these papers in publications using IDG.


<small>homepage: </small><span class="software-link">[https://idg.readthedocs.io/](https://idg.readthedocs.io/)</span>

## Available installations


|IDG version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2.0|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`IDG/1.2.0-foss-2023b`|