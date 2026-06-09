---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Voro++ is a software library for carrying out three-dimensional computations
    of the Voronoi

    tessellation. A distinguishing feature of the Voro++ library is that it carries
    out cell-based calculations,

    computing the Voronoi cell for each particle individually. It is particularly
    well-suited for applications that

    rely on cell-based statistics, where features of Voronoi cells (eg. volume, centroid,
    number of faces) can be used

    to analyze a system of particles.'
  license: Not confirmed
  name: Voro++
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
  softwareVersion: '[''0.4.6'']'
  url: http://math.lbl.gov/voro++/
---
# Voro++


Voro++ is a software library for carrying out three-dimensional computations of the Voronoi
tessellation. A distinguishing feature of the Voro++ library is that it carries out cell-based calculations,
computing the Voronoi cell for each particle individually. It is particularly well-suited for applications that
rely on cell-based statistics, where features of Voronoi cells (eg. volume, centroid, number of faces) can be used
to analyze a system of particles.

<small>homepage: </small><span class="software-link">[http://math.lbl.gov/voro++/](http://math.lbl.gov/voro++/)</span>

## Available installations


|Voro++ version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.4.6|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Voro++/0.4.6-GCCcore-14.3.0`|